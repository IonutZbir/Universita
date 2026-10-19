# Single-Pass In-Memory Indexing (SPIMI)

## 1. Motivazione

Il BSBI ha ottime proprietà di scalabilità, ma ha lo svantaggio di dover mantenere in memoria un'unica struttura dati `termine -> termID`, condivisa tra tutti i blocchi e sempre crescente.

**SPIMI** propone un'idea più semplice: **non serve un unico dizionario globale**. Ogni blocco costruisce il proprio dizionario in autonomia; quando la memoria si esaurisce, il blocco viene scritto su disco e se ne inizia uno nuovo, completamente vuoto.

```ad-important
Poiché ogni blocco ha il proprio dizionario indipendente, in fase di merge non possiamo più usare i `termID` come chiavi (sarebbero incoerenti tra blocchi diversi). Si usano direttamente i **termini** (stringhe) come chiavi.
```

Un'altra differenza fondamentale rispetto a BSBI: in SPIMI il dizionario di un blocco mappa **direttamente** `termine -> posting_list`, non più coppie `(termID, docID)` da ordinare e invertire in un secondo momento. Quando incontriamo un token, o creiamo la sua posting list, o appendiamo il docID a quella già esistente.
Infine, un altra differenza rispetto a BSBI è la dimensione dei blocchi. Non genera più blocchi di dimensione fissa, ma genera blocchi in base a quanto spazio in RAM è disponibiile.

## 2. L'algoritmo

Per ogni blocco:
1. Si processano i token del blocco in ordine.
2. Per ciascun token:
    - se il termine è già nel dizionario del blocco, si **appende** il docID corrente alla sua posting list;
    - altrimenti si crea una nuova posting list `[docID]` per quel termine.
3. Se la memoria disponibile per il blocco si esaurisce, si scrive il dizionario corrente su disco (ordinando i termini alfabeticamente prima di scrivere, in modo da rendere più semplice il merge successivo) e se ne apre uno nuovo, vuoto.
4. Al termine di tutti i documenti, si fondono (merge) i dizionari dei vari blocchi, usando i **termini** come chiave di confronto invece dei termID.

```ad-note
Come in BSBI, l'ordine delle posting list è "gratis": enumerando i documenti in ordine di arrivo, basta **appendere** un docID in coda alla posting list esistente — non serve mai riordinare.
```

## 3. Implementazione in Python

```python
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator
import json
import sys

# --- Lettura documenti a blocchi ----------------------------------------

@dataclass
class Document:
    path: Path
    doc_id: int

    def read_blocks(self, block_size: int = 1024) -> Iterator[str]:
        with open(self.path, "r", encoding="utf-8") as f:
            while True:
                chunk = f.read(block_size)
                if not chunk:
                    break
                yield chunk


# --- Controllo memoria ---------------------------------------------------

def is_memory_full(dictionary: dict, max_terms: int) -> bool:
    """
    Versione semplificata: in un sistema reale si controllerebbe
    l'uso effettivo di RAM (es. con sys.getsizeof o resource.getrusage).
    Qui usiamo un limite sul numero di termini distinti per blocco,
    solo a scopo didattico.
    """
    return len(dictionary) >= max_terms


# --- SPIMI-Invert: costruzione del dizionario di UN blocco ---------------

def spimi_invert(text: str, doc_id: int, max_terms: int, out_dir: Path,
                  block_counter: list[int]) -> list[Path]:
    """
    Processa i token di un blocco di testo, costruendo un dizionario
    term -> posting_list. Quando la memoria si esaurisce, scrive il
    dizionario corrente su disco e ne apre uno nuovo.

    Restituisce la lista dei file scritti per questo blocco di testo.
    """
    # La differenza rispetto a BISBI e che non è necessario l'ordinamento dei token
    # tokens = sorted(text.lower().split())
    tokens = text.lower().split()

    dictionary: dict[str, list[int]] = {}
    output_files: list[Path] = []

    for token in tokens:
        if token in dictionary:
            dictionary[token].append(doc_id)
        else:
            dictionary[token] = [doc_id]

        if is_memory_full(dictionary, max_terms):
            path = write_block_to_disk(dictionary, out_dir, block_counter[0])
            output_files.append(path)
            block_counter[0] += 1
            dictionary = {}

    # scriviamo su disco anche l'ultimo dizionario, non ancora pieno
    if dictionary:
        path = write_block_to_disk(dictionary, out_dir, block_counter[0])
        output_files.append(path)
        block_counter[0] += 1

    return output_files


def write_block_to_disk(dictionary: dict[str, list[int]], out_dir: Path, index: int) -> Path:
    """Scrive il dizionario ordinando i termini alfabeticamente (facilita il merge)."""
    path = out_dir / f"spimi_block_{index}.json"
    sorted_dict = dict(sorted(dictionary.items()))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sorted_dict, f)
    return path


# --- Costruzione indice completa ----------------------------------------

def spimi_index_construction(documents: list[Document], out_dir: Path,
                              block_size: int = 1024, max_terms_per_block: int = 5000) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    files: list[Path] = []
    block_counter = [0]  # contatore condiviso e mutabile tra le chiamate

    for document in documents:
        for chunk in document.read_blocks(block_size):
            output_files = spimi_invert(chunk, document.doc_id, max_terms_per_block,
                                         out_dir, block_counter)
            files.extend(output_files)

    return merge_blocks(files, out_dir)


# --- Merge dei blocchi, per TERMINE invece che per termID ----------------

def load_block(path: Path) -> dict[str, list[int]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def merge_two_blocks(a: dict[str, list[int]], b: dict[str, list[int]]) -> dict[str, list[int]]:
    """
    Merge lineare di due dizionari term -> posting_list, ordinati per termine.
    Le posting list condivise vengono concatenate e deduplicate,
    sfruttando il fatto che i docID sono già in ordine crescente.
    """
    terms_a = sorted(a.keys())
    terms_b = sorted(b.keys())

    i = j = 0
    merged: dict[str, list[int]] = {}

    while i < len(terms_a) and j < len(terms_b):
        ta, tb = terms_a[i], terms_b[j]
        if ta == tb:
            merged[ta] = _dedup(a[ta] + b[tb])
            i += 1
            j += 1
        elif ta < tb:
            merged[ta] = a[ta]
            i += 1
        else:
            merged[tb] = b[tb]
            j += 1

    while i < len(terms_a):
        merged[terms_a[i]] = a[terms_a[i]]
        i += 1
    while j < len(terms_b):
        merged[terms_b[j]] = b[terms_b[j]]
        j += 1

    return dict(sorted(merged.items()))


def _dedup(sorted_list: list[int]) -> list[int]:
    result = []
    for x in sorted_list:
        if not result or result[-1] != x:
            result.append(x)
    return result


def merge_blocks(block_files: list[Path], out_dir: Path) -> Path:
    """Merge iterativo a coppie, come in BSBI, ma confrontando termini invece che termID."""
    files = list(block_files)
    round_num = 0

    while len(files) > 1:
        next_round: list[Path] = []
        for k in range(0, len(files), 2):
            if k + 1 < len(files):
                a = load_block(files[k])
                b = load_block(files[k + 1])
                merged = merge_two_blocks(a, b)
            else:
                merged = load_block(files[k])

            path = out_dir / f"spimi_merged_r{round_num}_{k // 2}.json"
            with open(path, "w", encoding="utf-8") as f:
                json.dump(merged, f)
            next_round.append(path)

        files = next_round
        round_num += 1

    return files[0]
```

## 4. Vantaggi rispetto a BSBI

**Tempo**: non serve alcuna fase di _sorting_ delle coppie `(termID, docID)`, dato che le posting list si costruiscono incrementalmente man mano che si leggono i token. Il costo di ordinamento $O(T \log T)$ di BSBI sparisce.

**Spazio**:

1. Non serve mantenere la mappa `termine -> termID`: si ha un riferimento diretto alla posting list per ogni termine.
2. Per i termini molto frequenti, BSBI scriveva una coppia `(termID, docID)` per ogni singola occorrenza — per un termine come `"the"`, presente in quasi ogni documento, prima del merge esistevano tantissime coppie ridondanti. SPIMI invece mantiene direttamente **un'unica posting list** per `"the"`, aggiornata in place.

```ad-note
Anche in SPIMI l'ordine delle posting list è "gratis": enumerando i documenti in ordine di arrivo, ogni nuovo docID viene semplicemente **appeso** in coda — non serve mai un riordinamento esplicito.
```

## 5. Confronto rapido con BSBI

|Aspetto|BSBI|SPIMI|
|---|---|---|
|Dizionario `termine -> termID`|Unico, globale, condiviso tra blocchi|Non serve: si lavora direttamente sui termini|
|Rappresentazione intermedia|Coppie `(termID, docID)`, una per occorrenza|`termine -> posting_list`, aggiornata incrementalmente|
|Fase di sort|Necessaria, $O(T\log T)$|Non necessaria|
|Chiave usata nel merge|termID|termine (stringa)|
|Costo spaziale per termini frequenti|Alto (una coppia per occorrenza)|Basso (un'unica posting list aggiornata)|