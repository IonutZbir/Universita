La **Query Expansion** è un altro metodo per aumentare la recall di un sistema di IR.

L'idea è quella di **modificare** la query fatta dall'utente utilizzando dei **[[Relevance feedback & Query expansion#^dcdf9e|tesauri]]** per migliorare la recall.

Un tesauro può essere visto come un **database** che per ogni termine associa una collezione di altri termini (**quasi-**)**sinonimi** rispetto al dominio applicativo.

Più precisamente, per ogni *query-term* $t$ **espandiamo** la query con tutti quei termini che secondo il nostro tesauro sono **semanticamente** correlati a $t$.

Generalmente questo metodo aumenta la recall, in quanto si prendono in considerazione tutti quei termini non esplicitamente presenti nella query.
Purtroppo però c'è sempre il rischio di **diminuire la precision**, soprattutto nel caso in cui si utilizzano **termini ambigui**.

## Manual Thesaurus

Un **Manual Thesaurus** è una risorsa costruira a *mano* a partire dalla collezione tramite esperti. Essa contiene relazioni tra termini, per esempio, dato un termine, gli vengono associati sinonimi, quasi-sinonimi, termini più generici o più specifici, termini correlati etc...

Un contesto molto usato è nei sistemi di dominio specialistico (pubmed). Un utente potrebbe cercare *heart attack*, ma i documenti scientifici tipicamente fanno riferimentoa questo concetto usando termini più tecnici tipo *myocardial infarction*. 

Un thesaurus costruito a mano da esperti del dominio può aiutare ad aumentare la recall. Tuttavia risulta molto costoso.

### Come Funziona?

Quando un utente scrive una query, il thesaurus (una specie di dizionario) viene consultato per ogni *term-query*, e i termini correlati vengono aggiunti alla query originale con un peso minore rispetto a quello dei termini orginali.

```python
thesaurus = {
	"aircraft": ["plane", "aviation", "flight"],
	"safety": ["security"]
}

query = "aircraft safety"

expanded_query = consult_thesaurus(query)

print(expandend_query)
```
```shell
Ouput: (0.5aircraft OR 0.2plane OR 0.2aviation OR 0.1flight) AND (0.8safety OR 0.2security)
```

Questo metodo chiaramente aumenta la recall poiché permette di recuperare documenti che non contengono esattamente i termini della query orginale, ma che sono comunque rilevanti. Tuttavia può anche abbassare la precision se vengono aggiunti termini sbagliati o troppo generali che portano a recuperare documenti non rilevanti (rischio di **query drift**)

```python
thesaurus = {
	"jaguar": ["animal", "feline", "car"],
	"lion": ["animal", "feline", "candy bar"]
}
```


## Automatic thesaurus generation

Invece di costruire manualmente il tesauro (troppo costoso), l'idea è generarlo automaticamente a partire dalla collezione, osservando la distribuzione nei documenti.

Esistono generalmente due definizione di **similitudine** tra due parole:
1. **Due parole sono simili quando co-occorrono con parole simili.** Infatti le parole `macchina` e `moto` sono simili perché appaiono spesso insieme alle parole `strada`, `benzina`, `patente`, ecc.. perciò devono essere simili.
2. **Due parole sono simili quando sono grammaticalmente correlate con parole simili**. Infatti una persona può `raccogliere`, `pelare`, `mangiare` sia una `mela` che una `pera`, perciò esse devono essere simili.

## Query log

Un altro metodo per espandere le query è quello di tenere traccia delle azioni fatte dall'utente a seguito di una query.

Per esempio, se un utente $X$ a seguito della query $\text{"piante"}$ cerca spesso la query $\text{"rimedi naturali"}$ si potrebbe inferire che `rimedi naturali` è una potenziale espansione del termine `piante` per l'utente $X$.

Un altro esempio è se a seguito di due query $q_1,q_2$ un utente $X$ clicca molto spesso sullo **stesso url**, possiamo ben pensare che $q_1$ e $q_2$ sono due potenziali reciproche espansioni per l'utente $X$.

**Importante differenza tra tesauro e query log**: mentre i tesauri sono costruiti a partire dai documenti e si basano sulla distribuzione/semantica dei termini nei documenti, i query logs si basano invece sul comportamento degli utenti e sulle loro interazioni con il motore di ricerca.

Quali di questi 3 approcci devo usare? Dipende dall'applicazione e dalla collezione.

## Possibile Domanda d'Esame

Data una query $q$, come devo applicare *query expansion*? Come fa il sistema a decidere quali termini aggiungere, con quale peso e come fa ad evitare i termini che abbassano troppo la precision?

In questo caso, la questione dei **pesi** è di fondamentale importanza. Se si da troppo peso ai termini aggiunti si rischia di ottenere una query troppo distante da quella orginale, abbassando di molto la *usability* del sistema.

Bisogna quindi dare un peso ai termini della query originale ed un peso ai termini della query espansa. Infatti, possiamo pensarla come una formula del tipo $$\textbf{expanded}\_\mathbf{q} = \alpha \mathbf{q} + \bar{\beta} \mathbf{e}^T$$
Dove $\mathbf{q}$ è la query originale, $\mathbf{e}$ è il vettore dei termini aggiuntivi, $\alpha$ è un peso che controlla l'iportanza della query originale mentre $\bar{\beta}$ è un vettore di pesi che controlla l'importanza dei termini aggiunti. 
- $\bar{\beta} = \langle \beta, \dots \beta\rangle$, ossia è un fattore unico per tutti i termini aggiunti, oppure
- $\bar{\beta} = \langle \beta_{1}, \dots \beta_{n}\rangle$, possono essere tutte delle costanti diverse in base al tipo di *thesaurus* che sto considerando. Se considero un thesaurus manuale, allora posso dare pesi alti per i sinonimi stretti e più bassi per le altre categorie. Nel caso di tesauri automatici (LSI - dimensione latente) posso considerare la similità tra i termini (*cosine*).

Nel caso di query log si può pensare l'espansione in base alla frequenza con cui gli utenti si comportano in un certo modo.

Ricapitolando:

1. L'utente scrive una query $q$, applichiamo le solite trasformazioni per poi trasformarla in un vettore pesato (*tf-idf*). È necessario che sia un vettore in quanto per fare query expansion dobbiamo assegnare dei pesi ai termini aggiunti.
2. Per ogni query-term, si cercano possibili espansioni in una risorsa globale (manual thesaurus, automatic thesaurus, query log, LSI, etc...)
3. In base ai ragionamenti visti sopra, assegno un peso a ciascun termine aggiunto, e costruisco la query espansa.
4. Eseguo il sistema di retrieval con la query espansa, ottenendo una lista di documenti ordinati per rilevanza rispetto alla query espansa.