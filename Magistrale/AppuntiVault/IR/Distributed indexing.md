In molti contesti, come per esempio il World Wide Web, una sola macchina non è sufficiente per poter costruire e mantenere un indice di tutta la collezione di documenti.
Si fa quindi utilizzo di un grande cluster di computer interconnessi, e di **algoritmi distribuiti** per l'indicizzazione.
Non solo l'indice viene costruito in maniera distribuita, ma viene anche partizionato e distribuito su svariate macchine.
Perciò anche gli algoritmi di retriveal dei documenti saranno distribuiti.
Per il momento discutiamo però solo la costruizione dell'indice.

```ad-info
title: Massive Data Center
Supponiamo di avere un sistema distribuito non-fault-tollerant (si blocca se una macchina si rompe) con 1000 nodi, ognuno con una garanzia di funzionamento del 99.9\%.

A prima vista, questo ci può sembrare un sistema estramamente stabile.
Però, per quanto tempo in realtà il sistema è funzionante?

La probabilità che il sistema sia funzionante è pari alla probabilità che tutti nodi funzionino, ovvero $p = 0.999^n \approx 37\%$.
Invece la probabilità che non funzioni è pari alla probabilità che almeno una macchina non funzioni, o in altri termini $1 - p \approx 63\%$.

In poche parole, per circa $2/3$ del tempo il sistema sarà non funzionante!
```


La costruizione di un indice distribuito è una semplice applicazione del paradigma **MAP-REDUCE**.

Abbiamo una macchina **Master** considerata <b><u>stabile</u></b>, divide il processo di costruizione in **task paralleli**, e li assegna alle altre macchine coordinandone il lavoro.

```ad-important
title: Vantaggi
- Il primo vantaggio di questo metodo è che quando una macchina è "libera", le si può sempre assegnare un nuovo task, ottimizzando così i tempi.

- Il secondo vantaggio è che il sistema diventa **fault-tollerant**. Se una macchina si rompe mentre sta processando un task basterà semplicemente riassegnare il suo task ad un'altra macchina in funzione.
```

È importante osservare che se la macchina che si rompe è il **master**, si rompe tutto il sistema, a meno che non ci siano più **master**. Inoltre, **parser** e **inverter** lavorano in **parallelo**.

Più precisamente il processo segue i seguenti passaggi:
1. Il **master** partiziona i documenti in $n$ sottoinsiemi detti **splits**.
2. Il **master** assegna man mano gli splits a macchine (libere) dette **Parser**.
3. I **parser** leggono i documenti e generano un insieme di coppie **term-docID**, tutte partizionate in $j$ **segmenti**. Per esempio per $j=3$ si possono partizionare i termini per range di lettere, del tipo `a-f`, `g-p` e `q-z`.
4. Infine, delle macchine dette **Inverter** prendono tutte le postings di un **segmento** e creano delle posting list per i termini di tale segmento, salvandolo **localmente** sul proprio disco.

In tale processo la fase di **Map** è data in mano ai **parser**, i quali **trasformano** gli splits in segmenti.
La fase di **Reduce** è invece incaricata agli **inverter**, i quali **fondono** i segmenti in indici (parziali).

Quello appena descritto è il **term-partinioned index**, dove ogni partizione contiene un range di termini, e per ogni termne è presente la sua posting list completa.

![](./img/IR_distributed_index_1.png)

### Document-partioned distributed index
Quello che abbiamo precedentemente descritto è la costruzione di un indice distribuito **term-partitioned**, ovvero nel quale ogni macchina mantiene un indice per un sottointervallo di termini.

Purtroppo però tale approccio potrebbe avere una distribuzione degli indici parecchio sbilanciata.
Infatti quasi sempre campita che ci sono range con termini molto più frequenti di altri.

Una tecnica per bilanciare meglio il carico, è quella di partizionare i **segmenti** per range di **documenti**, e non per termini.
Questa tecnica è più scalabile e bilanciata, ed è quella generalmente usata per i search engine sul web. Un'altro vantaggio di tale metodo è un miglioramento del **fault tolerance**, infatti con un term-partitioned index, se una macchina si rompe allora si perde *tutta* la posting list relativa ad un termine, mentre con document-partitioned index, si perde l'accesso solo alla posting list parziale.

### Map Reduce

L'algoritmo visto è un esempio di **MapReduce**, un framework per fare calcoli distribuiti senza dover gestire la comunicazione tra macchine, fault tolerance e parallelismo. L'utente scrive solo le due funzioni chiave, **Map** e **Reduce**, e il framework si occupa di tutto il resto. In generale:

- **Map**: dall'input produce una lista di coppie `k, v`. Nel nostro caso produce la lista di coppie `term, docId`.
- **Reduce**: in input prende una lista di valori associati ad una chiave, Nel nostro caso prende in input una lista di `docId` per un termine e produce l'inverted index di quel termine.