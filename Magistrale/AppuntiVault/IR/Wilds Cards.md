
Le wild cards rappresentano un carattere jolly che può essere utilizzato per rappresentare uno o più caratteri in una stringa.

Vediamo alcuni esempi:

- **mon**\*: trova tutti i documenti che iniziano con `mon`. 
- \***mon**: trova tutti documenti che finiscono con `mon`.

Nel primo caso, risolvere una query di questo tipo risulta abbastanza facile se il dizionario è implementato come **B-Tree**, in quanto i termini sono ordinati in modo lessico-grafico, quindi è sufficiente prendere tutte le parole nel range
$$\text{mon} \leq \text{w} \leq \text{moo}$$
Nel secondo caso invece, la query risulta più complessa poiché il dizionario è ordinato per suffissi e non per prefissi. Una soluzione semplice è quella di mantenere un secondo dizionario con le parole scritte al contrario.

- `demon` $\to$ `nomed`,
- `common` $\to$ `nommoc` ...

È banale osservare che una tale soluzione porta ad un enorme overhead in termini di spazio in quanto è **necessario mantere un secondo B-Tree**.

Tuttavia, anche se siamo riusciti a enumerare tutti i termini del dizionario che soddisfano le wildcard, c'è un costo significativo da pagare per recuperare le posting di ciascun termine enumerato dal momento che è necessario fare l'unione delle posting list, e quindi restituisce moltissimi documenti. Sapendo che gli utenti tendono a digitare query più complesse (es. `de* AND *mon`) ciò può portare all'esecuzione di operazioni molto costose.

Supponimo adesso di voler rispondere a query del tipo: `co*tion`? Un'idea naive potrebbe essere: recupera `co*, *tion` e poi effettua l'intersezione tra le due posting list. Tuttavia ciò è estremamente costoso, di conseguenza si usa un approccio più efficiente: i [[Permuterm Index]].



