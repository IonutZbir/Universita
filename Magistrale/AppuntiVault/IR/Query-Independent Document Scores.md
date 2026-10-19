Fin'ora abbiamo calcolato il ranking rispetto a una **misura di rilevanza** di un documento rispetto a una query.
Un altro aspetto che si potrebbe tenere i considerazione è l'**autorevolezza** di un documento rispetto alla collezzione.
Per esempio:
- le pagine di Wikipedia sono generalmente molto autorevoli sul web.
- gli articoli scientifici molto citati sono in genere molto autorevoli.
- i post su un social che hanno molti like e condivisioni.

Infatti in un motore di ricerca generalmente l'utente non vuole solo i documenti più rilevanti, ma anche quelli più autorevoli.

Osservare che l'autorevolezza è una misura totalmente **indipendente** dalla query.

## Net-Score
Assegnamo a priori a ogni documento $d$ un **quality-score** $g(d)$ in maniera **indipendente** dalla query $q$.
Per semplicità assumiamo che tale quantità è normalizzata in $\left[ 0,1 \right]$.

Possiamo quindi **combinare** la $g(d)$ per una qualsiasi funzione di score (per esempio la [[Vector Space Model#^eef545|cosine similarity]]) per definire una misura che tiene in considerazione la rilevanza e l'autorità.

Se li combiniamo in maniera **additiva** otteniamo una quantità nota come **net-score** $$\text{net-score}(d,q) = g(d) + \cos(\alpha(d,q))$$
Possiamo tranquillamente usare qualsiasi **combinazione lineare** per definire il net-score, in base anche allo *user need*. ^1f3930

Si potrebbe usare il **net-score** per uno scoring più preciso, però il problema di doverlo calcolare per troppi documenti persiste.

## Fast method - $g(d)$ posting list ordering
Una ottimizzazione consiste nel pre-ordinare le posting list rispetto a $g(d)$ e non rispetto alla loro occorrenza in fase di indicizzazione.
Dopodiché possiamo usare [[#^1f3930|net-score]] oppure una qualsiasi misura di rilevanza per ritornare i top $k$ più importanti.

Tale metodo è buono in contesti di tipo **time-bound**, in cui si vogliono i primi $k$ risultati in tempi brevissimi (come per esempio sul web).
In tal caso infatti possiamo restituire i primi $k$ documenti all'utente, e se lui dovesse richiederlo calcolare e restituire i secondi top $k$, e così via...

```python
def score(query, k=10):
	terms = get_terms(query)
	posting_lists = [get_posting_list(t) for t in set(terms)]

	min_len = min([len(pl) for pl in posting_lists])
	for i in range(1, min_len/k):
		docs = set()
		for pl in posting_lists:
			docs.union(set(pl))
		docs = list(docs)
		yield sorted(docs, key=lambda d: cosine(d,query))
```

## Combine $g(d)$-ordering and [[Speeding Ranking Computation by Pruning#Champion lists|Champion list]]
Possiamo **combinare** l'ordinamento per $g(d)$ con le [[Speeding Ranking Computation by Pruning#Champion lists|champion list]].
Ovvero per ogni termine $t$ conserviamo una **champion list** degli $r$ documenti con valore $g(d) + \text{tf-idf}_{t,d}$ massimo.
Possiamo quindi riddure lo scoring a questa champion list, anziché a tutti i documenti delle posting list.