Un **approccio generico** è quello di identificare un sottoinsieme $A$ di documenti **contenders**, di dimensione ragionevolmente piccola $k < \vert A \vert \ll N$, sui quali poi calcolare la funzione di [[Scoring, term weighting & the vector space model|scoring]] e restituire i primi $k$.

Se $A$ contiene tutti i top $k$ documenti con score massimo, allora avremo che questo metodo è [[Efficient Scoring#Safe vs non-safe ranking|safe]].
Ciò però non è detto che sia garantito, dipende dal metodo usato per computare $A$.

Possiamo pensare all'insieme $A$ come un **pruning** di documento *non-contenders*.

## Index Elimination
Un primo approccio per identificare l'insieme $A$ è noto come **Index Elimination**.
Questo metodo è molto semplice e consiste nel inserire in $A$ i soli documenti che presentano **almeno** un *query term*.

```ad-warning
Questo metodo non tiene affatto in considerazione il **significato** dei documenti.
Infatti potrei avere un documento che non presenta alcun query term, ma che però utilizza molti sinonimi dei termini della query.
Perciò avremo un documento potenzialmente molto rilevante che non sarà presente in $A$.
```

Questo è un filtro banale e safe in quanto i documenti che non contengono alcun temine della query, avranno score zero. Index Elimination però è il punto di partenza per due tecniche più selettive:

### High-IDF query terms only
Una prima ottimizzazione di questo metodo consiste nel tenere in considerazioni i soli termini con valore informati maggiore, ovvero quei termini $t$ della query con alto [[TF-IDF weight#^3ca620|IDF]].
Perciò se ho la query $q = \text{"the kaleidoscope"}$ considererò i soli documenti che hanno presente il termine `kaleidoscope`, in quanto il termine `the` ha un basso idf.

Il vantaggio di questo approccio è che verranno scartati parecchi documenti dall'insieme $A$.
Infatti i termini con basso IDF sono quelli che hanno posting list molto grandi.

Quindi teniamo in considerazione solo quei documenti per cui i termini hanno un $idf$ sopra una certa soglia. Questo è un metodo non-safe, perchè potremmo perdere documenti che contengono solo termini a basso $idf$ ma che sono comunque rilevanti per la query.

### Many query terms
Un'altra ottimizzazione consiste nell'includere in $A$ solo documenti che hanno **molti** query term.

Prendo solo quei documenti che hanno almeno $n$ termini nella query.

Per *"molti"* si intende una frazione tale che:
- non sia troppo grande, altrimenti l'insieme $A$ diventa troppo piccolo. Più $A$ è piccolo, minore è la probabilità che contengra i top $k$ documenti.
- non sia troppo piccola, altrimenti $A$ tende a crescere molto.

L'importante è scegliere una quantità in modo tale che $A$ non sia troppo grande, ma comunque rimanga significativo rispetto all'insieme dei documenti rilevanti.

Tale intersezione *"morbida"* è anche nota come **soft conjuction**.


## Champion lists
L'idea di questo metodo è quella di precalcolare per ogni entry $t$ dell'indice i primi $r$ documenti con peso maggiore.
Tali $r$ elementi sono anche noti come **champion list**.

- Questa tecnica è non-safe perchè ogni champion list contiene  solo $r$ documenti. Puo capitare che un documento non presente nella champion list di nessun termine della query sia molto buono complessivamente nel calcolo dello score.
- Può capitare che $r < K$, in quel caso potremmo non avere abbastanza documenti per la top-$K$.
- Se un documento non compare in nessuna champion list di nessun termine, e il motore di ricerca utilizza solo le champion list, allora quel documento non sarà mai indicizzato e per esempio potrà finire nel deep web, quella parte del web non indizzata dai motori di ricerca, i cui documenti sono raggiungibili solo tramite link diretto.

**Come Implementare la Champion List?** A partire dall'inverted index, ogni termine possiede la propria posting list, la quale include coppie (docID, weight), dove `weight` rappresenta il peso del termine all'interno del documento (nel caso VSM, $tf-idf$). Basta poi ordinare la posting list in ordine decrescete per il peso e considerare i primi $r$ documenti.

**Utilizzo:** Per quanto riguardo l'utilizzo delle champion list, si possono usare al posto delle posting, oppure per evitare il problema $r < K$, iniziare scorrendo le champion list per poi continuare con le posting list.

