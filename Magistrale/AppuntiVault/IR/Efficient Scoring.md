Il calcolo dello [[Scoring, term weighting & the vector space model|scoring]] è una operazione parecchio dispendiosa all'interno di un motore di IR.

Esso rappresenta il vero collo di bottiglia nel mondo dell'IR. Una volta recuperate le posting listing dei termini presenti nella query, il sistema deve calcolare quanto ogni documento sia rilevante rispetto alla query secondo una dato modello (VSM, BM25, LM...). **Questo calcolo può essere molto costoso perché le posting list che recuperiamo sono l'OR dei termini della query, quindi potenzialmente potremmo dover prendere in considerazione moltissimi documenti, se non tutti.

Generalmente abbiamo due motivazioni per voler ottimizzare questo processo:
- spesso nei motori di ricerca rivolti all'utenza si ha un tempo limitato per rispondere (circa massimo 250ms).
- per collezioni molto grandi, la CPU a disposizione non è sufficiente per calcolare lo score di tutti i documenti. ^a66320

Ci soffermeremo sul [[#^a66320|secondo punto]], vedendo come è possibile ridurre l'utilizzo della CPU senza però compromettere la qualità dello scoring.

L'idea di base si appoggia sul fatto che generalmente gli unici documenti utili sono i primi $k$, perciò se sapessimo quali sono ci basterebbe calcolare lo score su solo questi top $k$ documenti anziché sull'intera collezione.

## Selection vs Sorting
Il ranking di un risultato di una query si distingue in tre step:
1. calcolare lo **score** dei documenti.
2. **ordinarli** in senso non decrescente.
3. prelevare i primi $k$ migliori.

Supponiamo di avere $N$ documenti come risultato di una query.
L'ordinamento di questi richiederà un costo computazionale di $\Theta(N \log{N})$.
Se invece applichiamo una **struttura dati** apposita possiamo fare un po' meglio di così.

Per esempio una volta calcolati gli score potremmo usare una [coda con priorità](https://en.wikipedia.org/wiki/Priority_queue) dove usiamo i valori di score come chiavi.

Se implementiamo la coda con un [heap binomiale](https://en.wikipedia.org/wiki/Binomial_heap) o [heap di Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_heap) possiamo costruire la struttura dati con **tempo ammortizzato** $\Theta^*(N)$.

Dato che anche l'operazione di estrazione del minimo ha **costo ammortizzato** costante $\Theta^*(1)$, avremo che per individuare i top $k$ è possibile farlo in tempo $\Theta^*(k)$.

Abbiamo come miglioramento $$\Theta(N \log{N}) \to \Theta^*(N)$$

L'unica operazione dalla quale non si scappa è quindi il calcolo dello score sull'intera collezione.
Questo risulta essere il **bottleneck** (il collo di bottiglia).

## Safe vs non-safe ranking
Abbiamo appena visto che per migliorare le prestazioni del sistema di IR vogliamo trovare un metodo che non calcoli lo score su tutti i documenti, bensì su un **sottoinsieme** relativamente piccolo.

I metodi si distinguono in:
- **metodi safe**: un metodo che garantisce che i $k$ documenti restituiti siano esattamente gli stessi che avremmo ottenuto senza pruning.
- **metodi non-safe**: ovvero che non garantiscono di restituire i top $k$ con score massimo.

I metodi non safe sono però usati, in quanto a scapito della precisione garantiscono buone prestazioni.

## Non-Safe Methods
### [[Speeding Ranking Computation by Pruning]]
### [[Query-Independent Document Scores]]
### [[Cluster Pruning]]
### [[Tiered Indexes]]
### [[Impact-Ordered Postings]]

## Safe Methods
### [[Safe Scoring - WAND|WAND Scoring]]