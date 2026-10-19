---
date: 2022-10-26
draft: true
---
# Dynamic Indexing
Gli indici costruiti [[IR/Lecture 4|fin ora]] si basano su collezioni di documenti statiche.
Come possiamo fare invece nel caso di collezioni **dinamiche** che cambiano nel tempo? (*insert*, *delete* e *update* dei documenti)

## Simple approach
- Mantengo un *grande* indice costruito inizialmente
- **INSERT**: Periodicamente, creo nuovi piccoli indici con i nuovi indici aggiunti.
- A seguito di una richiesta, effetto la query su tutti gli indici, e poi *fondo* tutti i risultati ottenuti
- **DELETE**: per la rimozione invece contrassegno contrassegno il documento come **rimosso** con un flag. Così a seguito di una query, semplicemente ignoro i documenti contrassegnati come rimossi.
- **UPDATE**: per l'update, combino la rimozione e l'insert 
- Periodicamente, costruisco di nuovo un grande indice

## Svantaggi
- È troppo rischioso costruire sempre un nuovo indice.
- Troppo dispendioso fare sempre merge.
	- Sarebbe efficiente fondere se abbiamo un file per ogni posting list, basta infatti appendere righe su tale file
	- Purtroppo però un OS può tenere un numero limitato di files.


## Logarithmic Merge
Assumiamo per il momento di avere un **unico indice** in un **unico file**.
([[IR/Lecture 4|sappiamo]] che spesso non è così, perché potrei avere un indice partizionato su differenti macchine)


1. Ho un **indice principale** su disco.
2. In ram creo un **indice ausiliare** (dinamico - [[IR/Lecture 4#SPIMI: Single-Pass In-Memory Indexing|SPIMI]]), e quando la memoria è satura scrivo in memoria.
3. Quando gli indici caricati in memoria, tutti insieme, hanno una dimensione **comparabile** all'indice principale attuale, operiamo un operazione di merge.
4. Così facendo, otteniamo un **numero logaritmico** di operazione di merge, **ammartizzando** così il numero di operazioni.

### Complessità
- $T = \text{\# posting lists}$ ed $n = \text{size of auxiliary index}$.
- $T/n$ = numero di indici che creo.
- Ogni posting list è fusa **al più** $O(\log{(T/n)})$ volte.
- Dato che il merge ha costo $O(T)$, la complessità risultante sarà $O(T \log{(T/n)})$.

### Problemi
[TODO]

## Real-Time search at Twitter
In questo caso il contesto cambia, perché abbiamo una frequenza **altissima** di scrittura e lettura dei documenti (tweet).

La caratteristica importante dei tweet, non è tanto il contenuto, quanto l'autore e la data.
Infatti, non mi interessa leggere i tweet del 2010 di una celebrità, mi interessa di più quello di oggi o di ieri.

Infatti, il motore di ricerca di twitter, usa una politica **LIFO** per le posting list, trascurandone il contenuto.
Al massimo viene considerato come ulteriore indice basato sugli **hashtag**.


