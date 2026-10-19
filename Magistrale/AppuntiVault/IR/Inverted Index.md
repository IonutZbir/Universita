# Inverted Index e Operazioni di Merge

## Motivazione: matrici sparse

La matrice d'incidenza termine-documento, per molti **termini d'interesse** (nomi, luoghi, ecc.), è piena di zeri: è cioè **sparsa**.

> **Nota**: per termini molto frequenti (es. gli articoli) la matrice sarebbe densa di 1, ma non si fanno tipicamente query per recuperare _tutti_ i documenti contenenti `the`, dato che sarebbero praticamente tutti.

Per ottimizzare lo spazio e le query, si usa un **dizionario** (o **vocabolario**, **lexicon**) di termini, dove per ciascun termine si conserva una **lista di documenti** in cui esso occorre: la **posting list**.

> **Importante**: nella costruzione di un indice inverso si assume che sia i **termini** sia le loro **posting list** siano mantenuti **ordinati**.

> **Nota**: mantenere l'ordinamento durante inserimenti/rimozioni è costoso, ma nell'IR questi eventi sono rari, quindi il costo è accettabile.

---

## Tokenizzazione

Dato un documento (sequenza di caratteri), la **tokenizzazione** consiste nello spezzare tale sequenza in **token** (tipicamente parole), usando spazi e punteggiatura come separatori.

- **Input**: `Friends, Romans, Countrymen, lend me your ears;`
- **Output**: `Friends`, `Romans`, `Countrymen`, `lend`, `me`, `your`, `ears`

### Definizioni chiave

- **Token**: istanza di una sequenza di caratteri in un documento specifico, raggruppata come unità semantica utile. Es. `"Michael Jackson"` è meglio trattato come un **singolo token**.
- **Tipo**: classe di tutti i token che condividono la stessa sequenza di caratteri (es. `Michael Jackson`, `michael jackson`, `MICHAEL JACKSON` sono lo stesso tipo).
- **Termine**: elemento di un tipo, generalmente **normalizzato**, effettivamente usato dal motore di IR.

### Il problema della tokenizzazione

> Qual è il modo migliore di generare i token?

Esempio: `Mr. O'Neil thinks that the boys' stories about Chile's capital aren't amusing`

Come trattare `O'Neil`? Possibili scelte: `neil`, `oneil`, `o'neil`, `o' neil`, `o neil`... Come trattare `aren't`? Possibili scelte: `aren't`, `arent`, `are n't`, `aren t`...

Se si rimuovono ciecamente i punti, una parola come `U.S.A.` rischia di essere decomposta in tre token inutili: `u`, `s`, `a`.

Non esiste una risposta univoca: bisogna decidere caso per caso in base ai casi particolari che si vogliono gestire.

```python
document = "Mr. O'Neill thinks that the boys' stories about Chile's capital aren't amusing."

# tokenizzazione banale
tokens = [
    w.replace(".", "").replace("'", "").lower()
    for w in document.split()
]
```

---

## Stop words

Alcuni termini compaiono in **quasi ogni** documento (articoli, congiunzioni, preposizioni...) e non aggiungono informazione utile alla ricerca.

Esempio: cercando `"President of the United States"`, i termini realmente utili sono `President` e `United States`; la query effettiva sarà concettualmente: $$\text{president} \land \text{united states}$$

Si può quindi rimuovere dal dizionario l'insieme delle parole ad altissima frequenza e bassa utilità informativa: le **stop words**.

```python
stop_words = {"the", "that", "an", "a", "at"}
tokens = [t for t in tokens if t not in stop_words]
```

---

## Normalizzazione

La **normalizzazione** canonizza i token, raggruppando forme diverse che rappresentano lo stesso concetto in un unico termine (es. cercare `U.S.A.` o `USA` deve dare lo stesso risultato).

Il modo più comune è definire **classi di equivalenza** tra termini: se `anti-discriminatory` e `antidiscriminatory` vengono mappati entrambi su `antidiscriminatory`, ogni query con uno dei due darà lo stesso insieme di risultati.

```python
equivalence_class = {
    "windows": ["Windows", "windows", "window"],
    "u.s.a.":  ["usa", "united states"],
    "usa":     ["usa", "united states"],
    "anti-discriminatory": ["antidiscriminatory"],
}
```

---

## Stemming e Lemmatizzazione

- **Stemming**: riduce una parola alla sua **radice**, eliminando i suffissi, per raggruppare parole con lo stesso significato ma forme grammaticali diverse (es. `authorize` e `authorization` → `authoriz`). Vantaggio: si copre un maggior numero di varianti usando meno memoria nel dizionario.
- **Lemmatizzazione**: riconduce i verbi alla forma **infinita/base** (es. `sono` → `essere`). Processo molto più complesso per lingue morfologicamente ricche come l'italiano rispetto all'inglese.

---

## Implementazione degli operatori booleani

Si assume sempre che le posting list siano **ordinate** per ID documento — assunzione essenziale per l'analisi di complessità.

```python
def is_sorted(a: list) -> bool:
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True
```

### L'idea generale del merge

Poiché **entrambe** le posting list sono ordinate, si possono confrontare con **due puntatori** che avanzano in sincronia (come nel merge sort), invece di confrontare ogni elemento di $L_1$ con ogni elemento di $L_2$ (costo $O(|L_1|\cdot|L_2|)$).

**Invariante**: ogni volta che un puntatore avanza, l'elemento superato non verrà più ricontrollato — l'ordinamento garantisce che la decisione presa (includere / scartare / rimandare) sia **definitiva**. Questo è ciò che rende il merge lineare.

---

### Intersezione: $A \cap B$

Un documento è nel risultato solo se compare in **entrambe** le liste.

```python
def intersect(L1: list, L2: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            result.append(L1[i])
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            j += 1
    return result
```

Ad ogni confronto tra $L_1[i]$ e $L_2[j]$:

1. **Uguali** → il documento è comune: lo aggiungo, avanzo **entrambi** i puntatori.
2. **$L_1[i] < L_2[j]$** → poiché $L_2$ è ordinata, tutti gli elementi successivi di $L_2$ saranno $\geq L_2[j] > L_1[i]$, quindi $L_1[i]$ non potrà mai trovare match: lo scarto, avanzo solo $i$.
3. **$L_1[i] > L_2[j]$** → simmetrico, avanzo solo $j$.

Quando una lista si esaurisce, gli elementi rimanenti dell'altra **non hanno più possibilità di match**: si scartano senza essere aggiunti.

**Complessità**: $O(\min{|A|,|B|})$ (più precisamente $\leq 2\min{|L_1|,|L_2|}$), perché ad ogni iterazione avanza almeno un puntatore, e il ciclo termina non appena una delle due liste è esaurita.

**Dimensione output**: $0 \leq |A\cap B| \leq \min{|A|,|B|}$.

---

### Unione: $A \cup B$

Un documento è nel risultato se compare in **almeno una** delle due liste.

```python
def union(L1: list, L2: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            result.append(L1[i])
            i += 1
            j += 1
        elif L1[i] > L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1

    if i >= len(L1):
        result.extend(L2[j:])
    elif j >= len(L2):
        result.extend(L1[i:])

    return result
```

Stessa struttura a tre casi, ma cambia il trattamento del caso "diverso":

1. **Uguali** → aggiungo il documento **una sola volta** (evito duplicati), avanzo entrambi.
2. **$L_1[i] < L_2[j]$** → $L_1[i]$ non avrà match futuri in $L_2$, ma va comunque **incluso** nel risultato (basta comparire in una delle due liste): lo aggiungo, avanzo solo $i$.
3. **$L_1[i] > L_2[j]$** → simmetrico, aggiungo $L_2[j]$ e avanzo solo $j$.

**Differenza chiave rispetto all'intersezione**: quando il ciclo termina, tutti gli elementi **rimasti** nella lista non esaurita vanno appesi in blocco al risultato, perché per definizione di unione appartengono comunque all'insieme finale.

**Complessità**: $O(|A|+|B|)$. **Dimensione output**: $\max{|A|,|B|} \leq |A\cup B| \leq |A|+|B|$.

---

### Differenza: $A \setminus B$

Un documento è nel risultato se appartiene ad $A$ ma **non** a $B$.

```python
def difference(L1: list, L2: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            j += 1
        else:
            i += 1
            j += 1

    if j >= len(L2):
        result.extend(L1[i:])

    return result
```

1. **$L_1[i] < L_2[j]$** → per l'ordinamento, $L_1[i]$ non troverà mai un match in $L_2$: è quindi _sicuramente_ assente da $B$ → lo aggiungo al risultato, avanzo $i$.
2. **$L_1[i] > L_2[j]$** → $L_2[j]$ non è più utile a nessun confronto futuro con $L_1$ → lo scarto (non aggiungo nulla), avanzo solo $j$.
3. **Uguali** → il documento è anche in $B$, va **escluso** dal risultato → avanzo entrambi senza aggiungere nulla.

Se $L_2$ si esaurisce, tutto ciò che resta in $L_1$ non ha più modo di essere escluso: va appeso in blocco. Se invece si esaurisce $L_1$, non resta nulla da valutare.

**Complessità**: $O(|A|+|B|)$. **Dimensione output**: $0 \leq |A\setminus B| \leq |A|$.

---

### Tabella riassuntiva del merge

|Operazione|$L_1[i]=L_2[j]$|$L_1[i]<L_2[j]$|$L_1[i]>L_2[j]$|coda residua|
|---|---|---|---|---|
|$\cap$|aggiungi, avanza entrambi|avanza $i$|avanza $j$|scartata|
|$\cup$|aggiungi (una volta), avanza entrambi|aggiungi, avanza $i$|aggiungi, avanza $j$|appesa (di qualunque lista resti)|
|$\setminus$|avanza entrambi (nessuna aggiunta)|aggiungi, avanza $i$|avanza $j$|appesa solo se resta $L_1$|

**Idea unificante**: il confronto tra $L_1[i]$ e $L_2[j]$ individua sempre l'elemento "più piccolo non ancora deciso"; l'ordinamento garantisce che la decisione presa su di esso sia definitiva, senza dover mai rivedere elementi già superati.

---

## Ottimizzazione di query con più termini AND

Consideriamo la query: $$\text{Brutus} \land \text{Calpurnia} \land \text{Caesar}$$

Siano $n, m, \ell$ le lunghezze delle rispettive posting list, con $n < m < \ell$.

**Implementazione 1**: (Brutus AND Calpurnia) AND Caesar

- Prima intersezione: $O(\min{n,m}) = O(n)$, risultato di lunghezza $\leq n$
- Seconda intersezione: $O(\min{n,\ell}) = O(n)$
- **Totale**: $O(n)$

**Implementazione 2**: Brutus AND (Calpurnia AND Caesar)

- Prima intersezione (Calpurnia, Caesar): $O(m)$
- Seconda intersezione: $O(n)$
- **Totale**: $O(n+m) \in O(m)$ — potenzialmente molto peggio della prima!

**Regola generale**: per intersecare più posting list conviene sempre **partire dalla lista più corta** e procedere in ordine crescente di lunghezza.

```python
def intersect_many(L: list[list]) -> list:
    # ordino le liste per lunghezza crescente
    L_sorted = sorted(L, key=len)
    result = L_sorted[0]
    for lst in L_sorted[1:]:
        result = intersect(result, lst)
    return result
```

Per questo motivo conviene salvare, per ogni termine, la sua **frequenza** (= lunghezza della posting list = numero di documenti in cui compare).

---

## Esercizi

### Esercizio 1 — Ordine ottimale con OR e AND

Query: $$(\text{tangerine} \lor \text{trees}) \land (\text{marmalade} \lor \text{skies}) \land (\text{kaleidoscope} \lor \text{eyes})$$

|Termine|Frequenza|
|---|---|
|eyes|213312|
|kaleidoscope|87009|
|marmalade|107913|
|skies|271658|
|tangerine|46653|
|trees|316812|

**Soluzione**: le dimensioni delle unioni risultanti sono limitate da:

- $316812 \leq |\text{tangerine} \lor \text{trees}| \leq 363465$
- $271658 \leq |\text{marmalade} \lor \text{skies}| \leq 379571$
- $213312 \leq |\text{kaleidoscope} \lor \text{eyes}| \leq 300321$

La strategia migliore è calcolare prima l'intersezione tra le due unioni più piccole, quindi: $$(\text{tangerine} \lor \text{trees}) \land \big((\text{marmalade} \lor \text{skies}) \land (\text{kaleidoscope} \lor \text{eyes})\big)$$

---

### Esercizio 2 — AND NOT e OR NOT

**a) Brutus AND NOT Caesar**

Equivale semplicemente alla differenza tra insiemi: $$\text{Brutus} \land \lnot\text{Caesar} \equiv \text{Brutus} \setminus \text{Caesar}$$

Si usa direttamente `difference`, mantenendo complessità $O(L_1+L_2)$.

**b) Brutus OR NOT Caesar**

Qui non si può fare altrettanto agevolmente: bisognerebbe unire tutti i documenti di $\lnot\text{Caesar}$ (che nel caso peggiore sono quasi tutti i documenti della collezione) con quelli di Brutus.

Applicando De Morgan: $$\text{Brutus} \lor \lnot\text{Caesar} \equiv \lnot(\lnot\text{Brutus} \land \text{Caesar}) \equiv \lnot(\text{Caesar} \land \lnot\text{Brutus})$$

ci si riconduce al caso (a), calcolando prima $\text{Caesar}\setminus\text{Brutus}$ e poi complementando rispetto all'insieme di tutti i documenti:

```python
def or_not(L1: list, L2: list, num_documents: int = 1000) -> list:
    # complessità: len(L1) + len(L2) + num_documents
    # output size: 0 <= len(result) <= num_documents
    a = difference(L1, L2)
    all_docs = list(range(1, num_documents + 1))
    return difference(all_docs, a)
```

---

### Esercizio 3 — Formula arbitraria

Query: $$(\text{Brutus} \lor \text{Caesar}) \land \lnot(\text{Antony} \lor \text{Cleopatra})$$

Siano $L_1,L_2,L_3,L_4$ le lunghezze delle posting list di Brutus, Caesar, Antony, Cleopatra.

Definendo:

- $E_1 = \text{Brutus} \lor \text{Caesar}$
- $E_2 = \text{Antony} \lor \text{Cleopatra}$

la query diventa: $$E_1 \land \lnot E_2 \equiv E_1 \setminus E_2$$

```python
E1 = union(brutus, caesar)
E2 = union(antony, cleopatra)
result = difference(E1, E2)
```

**Analisi dei costi**:

- $E_1$: tempo $O(L_1+L_2)$, dimensione al più $O(L_1+L_2)$
- $E_2$: tempo $O(L_3+L_4)$, dimensione al più $O(L_3+L_4)$
- $E_1 \setminus E_2$: tempo $O(|E_1|+|E_2|) \in O(L_1+L_2+L_3+L_4)$, dimensione al più $O(|E_1|) \in O(L_1+L_2)$

**Conclusione generale**: qualunque formula booleana può essere valutata in tempo lineare rispetto alla **somma delle lunghezze di tutte le posting list coinvolte**, componendo ricorsivamente `union`, `intersect` e `difference` — a patto di scegliere con attenzione l'ordine di valutazione delle sotto-espressioni (v. Esercizio 1) per minimizzare le dimensioni intermedie.