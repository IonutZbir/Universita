Un'altra **euristica** ragionevole è quella di considerare i soli documenti nei quali i *query-term* appaiono **molte volte**.

Possiamo quindi ordinare in senso non crescente le **posting list** rispetto alla **term frequency** $\text{tf}_{t,d}$.

Data quna query $q$, per identificare quali sono i $k$ documenti su cui calcolare il ranking esistono due approcci:

### 1 - Early Termination
Quando attraversiamo una posting list di un query-term $t$ ci fermiamo quando:
- abbiamo osservato un numero fissato $r$ di documenti, oppure
- quando la term frequency $\text{tf}_{t,d}$ scende sotto una **soglia critica** prestabilita

Una volta prelevati questi (al più) $r$ documenti per ogni query-term, facciamo l'**unione** di essi e calcoliamo il **ranking**.

### 2 - IDF-Ordered Terms
Consideriamo i *query-terms* in ordine non crescente dei rispettivi [[TF-IDF weight#^3ca620|IDF]].
Preleviamo in ordine le relative posting list, fermandoci quando avremo recuperato almeno $k$ documenti.
Dopodiché calcoliamo il **ranking** sull'insieme risultante.

L'idea è che considerando prima i query-term più informativi, otterremo documenti più rilevanti.