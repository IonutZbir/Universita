# Raccolta di esercizi sui grafi

## Esercizio 3 del 20/02/2023

La vostra città è modellata come un grafo diretto e pesato $G = (V, E, w)$. Voi siete nel nodo $s$ e dovete raggiungere il nodo $t$ dove si svolgerà l’esonero del corso di ASD.
Ma siete in ritardo. Dovete fare in fretta. Per fortuna avete una bicicletta. Con la vostra bicicletta, attraversare un arco $e\in E$ richiede tempo $w(e)$.

La bicicletta non è il solo mezzo che potete usare. Sapete che ci sono dei nodi del grafo, i nodi nell’insieme $X\subseteq V$,
in cui potete affittare scooter, monopattini e altra roba.
Avete soldi per affittare un solo mezzo. Per ogni nodo $x\in X$, conoscete due cose:

- il tempo $\tau_{x}$ che vi richiede lo scambio fra la bicicletta e il mezzo che si trova in $x$,
- il fattore di speed-up $\sigma_{x} \leq 1$ del mezzo: con il mezzo preso nel nodo $x$ il tempo di attraversamento di un arco e scende da $w(e)$ a $\sigma_{x}\cdot w(e)$.

Progettate un algoritmo che in tempo $O(m + n log n)$, calcola la strategia che vi porta a $t$ nel minor tempo possibile.

$const(x) = d(s, x) + \tau_{x} + \sigma_{x} \cdot d(x, t)$.

La distanza $d(s, x)$ si può calcolare in tempo $O(m + nlogn)$ usando Dijkstra. Mentre per trovare $d(x, t)$, l'idea è quella di invertire gli archi del grafo $G$ e far partire 
l'algoritmo di Dijkstra con sorgente $t$. In tempo costante possiamo accedere alle distanze calcolate.

Per ogni nodo $x$, in tempo costante accedo alla distanza $d(s, x)$ e alla distanza $d(x, t)$ e calcolo $const(x)$, ovvero il costo del cammino passando per il nodo $x$. Di tutti
questi costi, vado a scegliere il cammino avente costo minimo.
```
1. Dijkstra(G, s)
2. Dijkstra(G, t)
3. z = arg(min{const(x)})
4. return const(z)
```
**Corretteza**: L'algoritmo è corretto poiché l'algoritmo di Dijkstra è corretto. Inoltre per ogni nodo $x$, calcolo il cammino minimo, quindi provo tutti i cammini possibili, e 
sceglo quello ottimale.

**Complessità Temporale**: $T(n) = O(m + nlogn)$.
