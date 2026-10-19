Fin ora abbiamo visto una serie di tecniche per la [[Index construction|costruzione]], [[Index Compression|compressione]] e [[Scoring, term weighting & the vector space model|scoring]] di un motore di IR.

Una domanda lecita è:

> Quale combinazione di tecniche è meglio usare, possibilmente rispetto alle mie esigenze?
> Quale modello usare? 
> Il mio motore di IR è **buono**?

Per rispondere a queste domande abbiamo bisogno di **misurare** la qualità del modello.
Per fare ciò abbiamo bisogno di:
1. Un **sottoinsieme** di documenti significativi per il mio **information need** su cui fare test. ^79484d
2. Un insieme di **query** significative per il mio **information need**.
3. Per valutare la qualità delle risposte alle query, abbiamo bisogno di **precomputare** (tramite degli annotatori *umani*) la **rilevanza** dei documenti nel punto [[#^79484d|(1)]] in base all'**user need**. ^e22ebc

L'etichettamento accennato nel punto [[#^e22ebc|(3)]] è anche noto come **gold standard**.
Costruire un **gold standard** risulta dispendioso, in quano abbiamo bisogno dell'intervento umano.
Per costruire un *gold standard* in genere si procede nel seguente modo: ^f2d730
1. Si defisce una serie di query che soddisfano determinati **information needs**. Se voglio cercare come pulire una piscina una possibile query è `clear pool`.
2. Utilizzando un sistema di IR basilare, si recuperano tutti i documenti potenzialmente rilevanti.
3. Un gruppo di persone valuta, per ogni coppia `query-document` risultante se effettivamente tale documento è rilevante o meno rispetto alla query (**true** o **false**).

Definire quindi un **Gold Standard** è dispendioso in termini di risorse, in quanto necessità di elevato lavoro umano.

Una volta ottenuto quello di cui abbiamo bisogno, possiamo valutare la qualità di un motore di IR tramite una serie di **banchmark**.

```ad-example
title: Esempio
1. Prendo il mio **user need**: "*la mia piscina è sporca e la voglio pulire*".
2. Costruisco una query sulla base del mio user need "*clear pool*".
3. Pongo la query al mio motore di IR sulla collezione composta dal solo **sottoinsieme di documenti** rappresentativi.
4. Confronto il risultato con le **annotazioni** pre-computate a priori.
5. Come faccio a valutare la qualità della risposta? Il mio risultato è abbastanza "*azzeccato*"?
```

-----
- [[Set Based Measures]] (Precision, Recall, Accuracy, Error, F-Measure)
- [[Rank-Based Measures]]
- [[Beyond Binary Relevance]]