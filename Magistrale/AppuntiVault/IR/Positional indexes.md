1Una soluazione migliore rispetto al [[Biword Indexes]] è quello di salvare nelle posting lists, oltre che i documenti in cui un termine è presente anche le posizioni in cui esso occorre in tale documento.

```json
"to" = {
	"token": "to",
	"frequency": 993427,
	"posting": [
		{
			"docID": 1,
			"positions": [7, 18, 33, 72, 86, 231]
		},
		{
			"docID": 2,
			"positions": [1, 17, 74, 222, 225]
		},
		{
			"docID": 4,
			"positions": [8, 16, 190, 429, 433]
		},
		{
			"docID": 5,
			"positions": [363, 367]
		},
		{
			"docID": 7,
			"positions": [13, 23, 192]
		}
		...
	]
}

"be" = {
	"token": "be",
	"frequency": 178239,
	"posting": [
		{
			"docID": 1,
			"positions": [17, 25]
		},
		{
			"docID": 4,
			"positions": [17, 191, 291, 430, 434]
		},
		{
			"docID": 5,
			"positions": [14, 19, 101]
		},
		...
	]
}
...
```

Così facendo, per processare la **phrase query** `standford university palo alto` basterà trovare tutti documenti in cui appaiono tutti e 4 i termini desiderati (tramite la funzione [[Inverted Index#Intersection|intersection]] opportunamente [[Inverted Index#Optimizations of queries|ottimizzata]]) e poi cercando i documenti in cui appaiono in **posizioni consecutive**.

Ovvero i documenti che faranno parte della risposta sono tutti quei documenti per i quali esiste (almeno) un indice $k$ tale che:
- il primo termine `standford` appare in posizione $k$
- il secondo termine `university` appare in posizione $k+1$
- il terzo termine `palo` appare in posizione $k+2$
- il quarto termine `alto` appare in posizione $k+3$
$$\langle k, k+1, k+2, k+3 \rangle$$

```python
from typing import List, Tuple

class Posting:
    def __init__(self, doc_id: int, positions: List[int]):
        self.doc_id = doc_id
        self.positions = positions

def positional_intersection(L1: List[Posting], L2: List[Posting], k: int = 2) -> List[Tuple[int, int, int]]:
    """
    Algoritmo di intersezione posizionale per due posting lists L1 ed L2.
    L'algoritmo trova le posizioni in cui i due termini appaiono entro k parole di distanza
    l'una dall'altra (con il primo termine precedente al secondo).

    Ritorna una lista di triple con:
    - id del documento che rispetta la condizione
    - posizione del primo termine
    - posizione del secondo termine (postumo al primo)
    """
    result = []
    
    # In Python gli indici partono da 0
    i, j = 0, 0

    while i < len(L1) and j < len(L2):
        doc_id_1 = L1[i].doc_id
        doc_id_2 = L2[j].doc_id

        if doc_id_1 == doc_id_2:
            # Recuperiamo le posizioni relative al documento corrente
            pos1 = L1[i].positions
            pos2 = L2[j].positions

            for p1 in pos1:
                for p2 in pos2:
                    # Il secondo termine deve apparire DOPO il primo
                    if p2 <= p1:
                        continue
                    
                    distanza = p2 - p1
                    
                    if 0 < distanza <= k:
                        result.append((
                            doc_id_1, # documento
                            p1,       # posizione primo termine
                            p2        # posizione secondo termine (corretto da 'ps')
                        ))
                    elif distanza > k:
                        # Poiché le posizioni sono ordinate, se superiamo k
                        # le successive posizioni in pos2 saranno ancora più lontane
                        break

            i += 1
            j += 1

        elif doc_id_1 < doc_id_2:
            i += 1
        else:
            j += 1

    return result
```

In termini di **tempo**, nel caso di **termini frequenti**, il costo aumenta di molto per via del doppio ciclo `for` sulle position list.
Però per termini non eccessivamente frequenti, empiricamente le prestazioni non si degradano troppo.

In termini di **spazio** invece osserviamo che ora abbiamo bisogno di salvare una informazione per ogni singola occorrenza di ogni termine, mentre per l'[[Inverted Index|indice non posizionale]] ci basta salvare solamente in quali documenti apparivano.
Il supplemento di memoria aggiuntiva potrebbe risultare eccessivo, soprattutto in presenza di molti termini altamente frequenti.
Per esempio, supponiamo di avere un generico documento $D$ con dimensione $T$ (in termine di numero di termini).
Prendiamo ora un suo generico termine `t` con frequenza all'incirca dell'$1\%$.
Vediamo come cresce la memoria usata dal termine `t` per il solo documento $D$

$T$ | Expected postings | Expected entries in positional list
----|----|----
1000 | 1 | 1
10000| 1 | 10
100000 | 1 | 100
... | ... | ...


Dato però che le lingue hanno una **struttura robusta**, empiricamente un **positional index** è circa 2-4 volte più grande di uno non posizionale (*non eccessivamente grande*), e generalmente occupa il $35\%-50\%$ del volume dei testi originali (perciò può essere visto come una sorta di metodo di compressione).