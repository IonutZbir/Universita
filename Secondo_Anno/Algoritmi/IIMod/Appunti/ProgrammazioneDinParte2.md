# Weighted interval scheduling 

Questo problema è una generalizzazione dell'interval scheduling, problema che abbiamo risolto mediante un algoritmo greedy. Osserveremo che il problema 
che abbiamo risolto con l'algoritmo greedy è un istanza di questo problema generale.

> [!IMPORTANT]
> - Il $j-esimo$ job inizia a $s_{j}$ e termina a $f_{j}$, avendo un peso $w_{j} > 0$, che potrebbe rappresentare il profitto guadagnato se eseguito quel job.
> - Due job $i$ e $j$ con $s_{i} \leq s_{j}$ si dicono **incompatibili** se non si sovrappongono, ovvero se $f_{j} \geq s_{i}$.
> - **GOAL**: L'obbiettivo è di trovare il sottoinsieme di peso massimo di job mutualmente compatibili.

<img src="img/progdin/wis.png" width="300" />

Come detto prima, l'algoritmo `earliest finish-time first`, ovvero l'algoritmo greedy progettato in precedenza funziona solo con un determinata istanza di questo problema generale, ovvero se il peso di tutti i job è 1.

Per convenzione, ordiniamo i job in ordine crescente per finish-time, come nell'algoritmo greedy, quindi: $f_{1} \leq f_{2} \leq$...$\leq f_{n}$.

> [!IMPORTANT]
> **DEF**: $p(j)$ è il più grande indice $i < j$ tale che l' $i-esimo$ job è compatibile con il $j-esimo$ job. Ovvero $i$ è l'intervallo più a destra che finisce prima che inizi $j$.

<img src="img/progdin/def.png" width="300" />

**Per esempio:** $p(8) = 1$, $p(7) = 3$, $p(2) = 0$. Osserviamo che se il job $i$ compatibile con $j$ non esiste, allora $p(j) = 0$.

Adesso, abbiamo tutto il necessario per progettare l'algoritmo di programmazione dinamica che risolve questo problema.

> [!IMPORTANT]
> **DEF**: $OPT(j)$ è il peso massimo di un qualunque sottoinsieme di job mutualmente compatibili per i sottoproblemi costituiti dai soli job da $1$ a $j$. 
> **GOAL**: $OPT(n)$ è il peso massimo di un qualunque sottoinsieme di job mutualmente compatibili

