---
date: 2022-13-12
draft: true
---

Quanto è costoso in termini computazionali calcolare il ranking dei documenti?

Purtroppo calcolare lo score su tutti i documenti restituiti da una query potrebbe risultare troppo dispendioso, in quanto potrebbero essere troppi.

1. Estrarre i documenti candidati.
2. Calcolare la funzione di similarità.
3. Ordinarli in base allo score.

Osservare che generalmente nei motori di ricerca si vogliono mostrare i soli $k$ (con $k$ **costante**) documenti più rilevanti.

Ottimizzazioni:
1. ottimizzare il calcolo dello scoring.
2. scegliere un sottoinsieme di $k$ 

Per convenzione consideriamo la sola **cosine-similarity**.

Sia $J$ il numero di documenti la cui cosine-similarity è NON ZERO.
Questo si può fare in tempo efficiente, in quanto sono i documenti che non appaiono in nessuna posting list dei termini della query.

# Use heap for selecting top k
Usiamo un **search tree** dove i documenti sono i nodi, e lo score di un nodo è maggiore dello score dei nodi figli.

Costruire tale albero costerà $2J$ operazioni.

Vorremmo individuare i $k$ top documenti in tempo $O(\log{J})$.

Un metodo di estrazione di un sottoinsieme di $k$ nodi è detta **safe** se estrare tutti e soli i $k$ documenti più rilevanti.
Invece è detto **non safe** se vado a "perdere qualcosa", ovvero manco almeno un documento tra i top $k$.

-----
# NON SAFE
## Generic Approach
Sia $A$ un sottoinsieme di documenti **candidati** tali che
- $|A| > k$
- $|A| << N$
- Non è detto che $A$ contenga TUTTI i top $k$ documenti, ma comunque una buona parte.

Quindi $A$ è NON SAFE per definizione.

Possiamo pensare ad $A$ come un **pruning** dei documenti non candidati.

Come costruire $A$ ?

Possiamo considerare i soli documenti tali che:
1. Hanno un alto **IDF**
2. Hanno il maggior numero di "dimensioni" in comune con la query.

L'idea è che i termini con basso IDF hanno posting list molto grandi, perciò non considerandoli elimino molti documenti nel retrieval.

Inoltre osserviamo che al crescere dei query term, il numero di documenti risultanti tende ed annullarsi (perché faccio troppi AND).

Perciò posso fare una **soft conjuntion**, ovvero ritorno documenti tali che contengono **almeno un numero** costante di query term (per esempio 3 termini su 4).

## Champion List Approach
Una prima idea è quella di ordinare i documenti delle posting list per **term frequency**.

Quindi per ogni termine $t$ precomputiamo i primi $r$ documenti con **TF** maggiore.
Tali documenti li chiamiamo **champion list**.

Così facendo, invece di considerare tutti i documenti delle posting list, consideriamo i soli $r$ documenti delle champion list.
Questo è un approccio più *smart* rispetto al precedente.

## Static quality scores
Un'altra idea è quella di **pre ordinare** la rilevanza dei documenti **indipendentemente** dalla query.
Per esempio su Google le pagine di wikipedia sono già più rilevanti per un utente che ricerca sul web.
Oppure una pagina più puntata risulta essere più autorevole rispetto ad altre, indipendentemente dal contenuto.

Quindi associamo una **quality score** (o **authority**) ai docuemnti, in base al numero documenti che lo puntano.
$$g(d)$$
Tale valore è **query insensitive**.

Così facendo possiamo definire lo score combinando l'authority e la cosine similarity
$$\texttt{net-score}(d,q) = g(d) + \text{cosine}(d,q)$$

## Top k by $g(d)$
Un altro approccio è quello di ordinare le posting list (in index-time) sui relativi $g(d)$.

Per i diversi query term, considero i primi $R$ documenti nelle posting list, in ordine discendente di $g(d)$.

Su questo sottoinsieme calcoliamo quindi la **cosine similarity**.

```ad-note
Non viene fatto l'AND tra le posting list.
Vengono semplicemente presi i primi $R$ docuemnti dalle posting list di tutti i termini della query $q$.
```

```ad-warning
Questo approccio non è safe.
Perché non faccio l'AND.
```


# Clustering Pruning
Idea: i documenti si rigrauppano in **cluster** simili in uno spazio geometrico.
Considero il cluster più vicino alla query come primo insieme di candidati.

Realizzazione:
prendo $\sqrt{N}$ documenti uniformemente a caso, e lo indico come **leader** del suo cluster.
Associo gli altri documenti documenti (i **follower**) più vicini al leader più vicino, e genero un cluster.
Mediamente ogni cluster è grande $O(\sqrt{N})$.

```ad-important
Tutto questo va **precomputato** in index-time.
```

Considero come pruning il cluster il cui leader è più vicino alla query $q$.


## High and low list
Per ogni termine preservo due posting list
- **high list**, come la champion list.
- **low list**, il resto delle postings.

L'importanza la posso definire come preferisco.

1. vedi [[tf-ordering]]
2. vedi [idf-ordering]

------
# SAFE

# WAND scoring
Data una posting list, abbiamo finger che punta un elemento a caso della posting list.

In ogni cella $i$ abbiamo la **maggiore** **TF** di tutti i documenti in celle $\geq i$.
I valori saranno quindi **monotoni non crescenti**.
