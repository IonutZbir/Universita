---
date: 2022-11-08
draft: true
---
# Ranked Retrieval
Abbiamo visto fin ora:
- delle strutture dati che ci consentano di rispondere a delle [[IR/Lecture 3|query booleane]] semplici su un insieme enorme di documenti
- come tali strutture dati possono essere [[IR/Lecture 6|comprimere]] al minimo.

Una seconda parte del problema è che dei sistemi di IR è che:
- i documenti restituiti da una query sono generalmente tantissimi, e una persona non può processarli in maniera efficiente per trovare quello che gli serve
- usando male gli **operatori** di ricerca booleana potrebbe indurre in un risultato vuoto.

Infatti consideriamo la query `world climate change merkle`, espressa in **linguaggio naturale**.
Possiamo processarla come:
	- `world climate change` AND `merkle` -> $\emptyset$
	- `world climate change` OR `merkle` -> **very big result**

Però capire come usare gli operatori booleani in maniera autmatica è computazionalmente difficile.

Generalmente, possiamo definire le proprietà che si voglia che un motore di IR abbia:
1. Deve mostrare solo un **piccolo sottoinsieme** di pagine più rilevante (per esempio 10). ^b46390
2. L'utente non dovrebbe esprimere le query in maniera troppo complessa, è preferibile che usi il **linguaggio naturale**.

Per il [[#^b46390|punto 1]] vogliamo che il motore dia uno **score** *di rilevanza* ai documenti, generalmente **normalizzato** in $\left[ 0,1 \right]$, in modo così da ordinarli in modo **non crescente**.

Tale *score* deve essere un **indice di rilevanza** del documento rispetto alla query.

Per esempio, se cerco un termine `X` mi aspetto che più in documento esso appare più il documento è rilevante ai fini della query. 

## Jaccard Coefficient
Siano $A,B$ due **insiemi**.
Il **coefficente di Jaccard** è definito come $$J(A,B) = \frac{\vert A \cap B \vert}{\vert A \cup B \vert}$$

- $J(A,B) = 0 \implies$ sono totalmente differenti.
- $J(A,B) = 1 \implies$ sono uguali.

```ad-important
La misura di *Jaccard* non è una metrica, in quanto non vale che:
- $J(A,A) = 0$
- $J(A,B) = J(A,X) + J(X,B)$ (**disugagliaza triangolare**)

Abbiamo come proprietà solo la **simmetria**.
```


Se poniamo $A = \text{query}$ e $B = \text{document}$, possiamo misurare la "*rilevanza*" del documento $B$ rispetto alla query $A$.


Possiamo quindi usare il coefficiente di Jaccard come **funzione di ordinamento** per il risultato della nostra query.

### Problema
Questo coefficiente purtroppo non tiene conto della **frequenza** in cui i termini appaiono in un documento: tiene solo conto di quali termini della query appaiono nel documento.

Esempio: ho due documenti $D_1$ e $D_2$.
La mia query è $B = \{ \texttt{ termaX } \}$.
Supponiamo che il termine `termX` in entrambi i documenti, con frequenze relativamente $3$ volte e $88$ volte.
Se la dimensione è lastessa, allora avremo che $$J(B,D_1) = J(B,D_2)$$ anche se in teoria il documento $D_2$ è più significativo.

Un altro problema è la **dimensione** del documento.
Più un documento è grande, più esso verrà **penalizato** nello scoring.

Un accorgimento è quindi quello di normalizzare per la **radice** dell'unione degli insiemi.

$$J'(A,B) = \frac{\vert A \cap B \vert}{\sqrt{\vert A \cup B \vert}}$$

## Count matrix - Bag of Word Model
Per dare maggiore enfasi ai documenti con maggiore frequnza dei termini della query, usiamo una rappresentazione di tipo **bag of words**.

Abbiamo una matrice `term x doc`, dove nella cella $i,j$ ho il numero di volte in cui il termine $i$ appare nel documenti $j$.

```ad-attention
Questo metodo è **naive**, in quanto non tiene conto della **semantica** della query.

Infatti se cerco:
- `il gatto morde il cane`
- `il cane morde il gatto`

tale modello restituisce lo stesso risultato, attribuendo lo stesso voto agli stessi documenti.
```


Indichiamo con $\text{tf}_{t,d}$ il numero di volte in cui il termine $t$ occorre nel documento $d$.

Pensiamo che se due termini hanno frequenze 300,000 o 300,012 volte in due documenti, è una informazione che non ci interessa molto.

Pericò applichiamo una **scalatura non lineare** nelle sequenze, così da misurare le frequenze solamente tra **scale di risoluzione significative**.

$$w_{t,d} = \begin{cases}
1 + \log_{10}{(\text{tf}_{t,d})} &\text{if } \text{tf}_{t,d} > 0\\
0 &\text{otherwise}
\end{cases}$$

[FAI ESERCIZIO]

### Problema
Se cerco `il cane`, e cerco `il` riavrò tutti i documenti che hanno il termine `il`, anche se non hanno `cane`!

Un primo approccio che abbiamo visto per rimuovere i termini *"rumore"* è **rimuovere le stopword**.

Un altro modo è quello di stimare la **distribuzione** dei termini nella mia intera collezione, basandomi sull'osservazione che

> un termine che occorre più volte sarà **meno informativo** di un termine **più raro**

Possiamo quindi anche **pesare** i termini in base alla loro **rarità**.
(Sfruttiamo di nuovo la **document frequency**).

- vogliamo dare un **peso alto ai termini rari**.
- vogliamo dare un **preso basso a termini frequenti**.
- vogliamo dare un **peso infitesimale ai termini alle stop word.

Definiamo quindi la **informativeness** di un termine come
$$\text{idf}_t = \log_{10}{\frac{N}{\text{df}_t}}$$
dove $\text{df}_t$ è la **document frequency** del termine $t$ nella mia collezione, ed $N$ è il numero di documenti.

![](./img/IR_td-idf_1.png)

![](./img/IR_td-idf_2.png)

## TD-IDF weight
Possiamo quindi definire il **peso** di un termine $t$ rispetto a un documento $d$
$$w_{t,d} = (1 + \log{(\text{tf}_{t,d}})) \cdot \log{ \left( \frac{N}{\text{df}_t} \right)} = \text{tf-weight} \times \text{idf-weight}$$

Possiamo quindi definire una **score matrix** dove le entri saranno $w_{i,j}$, dove $i$ è un termine e $j$ è un docuemnto.

## Vector representation of documents
Con questa rappresentazione possiamo vedere i documenti come dei **vettori**.
I termini sono le **dimensioni** del nostro spazio.
La [[#TD-IDF weight|td-idf frequency]] sono le coordinate del nostro vettore.
Quindi ogni documento diventa un punto.

Così abbiamo rappresentato la nostra collezione come uno **spazio metrico**, sul quale possiamo quindi fare **classificazione**.

Possiamo rappresentare in maniera analoga (vettoriale) anche i termini, usando i **documenti** come dimensione (coordinate) per i itermini.
Infatti, i termini `calciatore` e `calcio`, appariranno più o meno negli stessi documenti con la stessa frequenza.
Quindi possiamo dire che i due termini sono **simili**, nel senso che appartengono allo stesso argomento.