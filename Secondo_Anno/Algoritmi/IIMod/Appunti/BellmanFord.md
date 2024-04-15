# Cammini minimi in un grafo con pesi negativi

> [!IMPORTANT]
>
>**Shortest Path Problem**: Dato un grafo diretto $G=(V, E)$ con lunghezze degli archi $l_{vw}$, trovare il cammino minimo dal nodo sorgente $s$ al nodo destinazione $t$.

<img src="img/bellmanford/esempio_grafo_SP.png" width="400" />

La lunghezza di dell'cammino minimo sa $s -> t$ è : $9 - 3 - 6 + 11 = 11$.

L'algoritmo di Dijkstra non funziona con un grafo in cui ci sono pesi negativi. Si potrebbe pensare di aggiungere una costante $c > 0$ a ciascun peso per ottenere solo pesi positivi, ma anche così facendo, non otteremo il risultato corretto.

<img src="img/bellmanford/dijkstra_fail.png" width="400" />

>[!IMPORTANT]
>
>**DEF**: Un ciclo negativo è un ciclo diretto tale che la somma dei pesi degli archi è negativa.
$$l(W) = \sum_{e\in W} l_{e} < 0$$

>[!IMPORTANT]
>
> - **Lemma 1**: Se un qualsiasi cammino da $v$ a $t$ contiene un ciclo negativo, allora non esiste un cammino minimo da $v$ a $t$.
> - **Dim**: Se esiste un tale ciclo $W$, allora è possibile costruire un cammino da $v$ a $t$ di lunghezza negativa, passando un numero arbitrario di volte per $W$ accorciando ogni volta la lunghezza del cammino. In questo caso si dice che la distanza da $v$ a $t$ è $-\infty$.

<img src="img/bellmanford/negcycle.png" width="300" />

>[!IMPORTANT]
>
> - **Lemma 2**: Se $G$ non ha cicli negativi, allora esiste un cammino minimo da $v$ a $t$ che è semplice (no ha cicli), avente $\leq n - 1$ archi.
> - **Dim**: Tra tutti i cammini minimi da $v$ a $t$, consideriamo quello che usa il minimo numero di archi. Questo cammino può avere solo cicli di lunghezza 0, perchè per il lemma sopra, se esiste il cammino minimo, allora non ci sono cicli negativi, inoltre, avendo preso il cammino di lunghezza minima, siamo sicuri che non ci sono cicli di lunghezza positivi. Gli unici cicli ammissibili sono i cicli di linghezza 0, che si possono semplicemente ignorare.

**Single-destination shortest-paths problem**
- Dato un grafo diretto $G=(V, E)$ con lunghezza degli archi $l_{vw}$, senza cicli negativi e un nodo distinto $t$, trovare il cammino minimo da $v$ a $t$ per ogni nodo $v$.

E' un problema del tutto equivalente del problema dei cammini minimi a singola sorgente, a singola sorgente, o a singola destinazione, il problema algoritmicamente è identico. Avendo l'algoritmo per uno dei due problemi, basta solamente invertire gli archi e scambiare il ruole della destinazione con la sorgente.

**Negative-cycle problem**
- Dato un grafo diretto $G = (V, E)$, con lunghezza degli archi $l_{vw}$, trovare un ciclo negativo (se esiste). 

Vedremo che questo è un problema relazionato al problema dei cammini minimi, in qualche modo con l'algoritmo di Bellman-Ford, riusciremo a rispondere anche a questo quesito.

### Algoritmo di programmazione dinamica

>[!IMPORTANT]
> - **DEF**: $OPT(i, v)$: lunghezza del cammino minimo da $v$ a $t$ che utilizza $\leq$ $i$ archi.
> - **GOAL**: $OPT(n - 1, v)$ per ogni vertice $v$. Per il Lemma 2, se non ci sono cicli negativi, allora esiste un cammino minimo da $v$ a $t$ che è minimo. Quindi vogliamo trovare il cammino minimo che va da $v$ a $t$ che usa al più un arco, il cammino minimo che va da $v$ a $t$ che usa al più 2 archi è cosi via, fino a $n - 1$ archi.
> - **Caso 1**: Il cammino minimo da $v$ a $t$ usa $\leq$ $i - 1$ archi, allora $OPT(i, v) = OPT(i - 1, v)$.
> - **Caso 2**: Il cammino minimo da $v$ a $t$ usa esattamente $i$ archi. Se $(v, w)$ è il primo arco nel cammino minimo da $v$ a $t$, con costo $l_{vw}$. Allora seleziona il cammino minimo da $w$ a $t$ utilizzando $\leq$ $i - 1$ archi.

**Equazione di Bellman**
- $OPT(i, v) = 0$ se $i = 0$ e $v = t$
- $OPT(i, v) = \infty$ se $i = 0$ e $v \neq t$
- $OPT(i, v) = \min${ $OPT(i - 1)$,  $\min_{(v,w)\in E}${ $OPT(i - 1) + l_{vw}$ }} se $i > 0$

```
Shortest-paths(V, E, l, t)
    for each node v:
        OPT[0, v] = inf
    OPT[0, t] = 0
    for i = 1 to n - 1 do:
        for each node v:
            OPT[i, v] = OPT[i - 1, v]
            for each edge(v, w):
                OPT[i, v] = min{OPT[i, v], OPT[i - 1, w] + l_vw}
```

> [!IMPORTANT]
>
> - **Teorema**: Dato un grafo diretto $G = (V, E)$ senza cicli negativi, l'algoritmo calcola la lunghezza del cammino minimo da $v$ a $t$ per ogni nodo $v$ in tempo $\theta(n\cdot m)$ e spazio $\theta(n^2)$.
> - **Dimostrazione**: La tabella $OPT$ occupa spazio $\theta(n^2)$. Ogni iterazione costa $\theta(m)$ dato che esaminiamo ciascun nodo una volta sola.

Adesso, rimane solo da trovare i nodi che formano il cammino minimo. Ci sono due approcci:
1. Mantenere `successor[i, v]`, un puntatore che punta al prossimo nodo del cammino minimo da $v$ a $t$ che usa al più $i$ archi. 
2. Calcolare `OPT[i, v]`, poi andare a considerare solo gli archi per cui vale $OPT[i, v] = OPT[i - 1, w] + l_{vw}$. Ciascun cammino diretto in questo sottografo è un cammino minimo.


