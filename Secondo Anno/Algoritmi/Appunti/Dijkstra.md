# Cammini Minimi in Grafi Pesati

**DEF**: Sia $G = (V, E)$ un grafo orientato o non orientato con pesi $w$ reali sugli archi. Il costo o la lunghezza 
di un cammino $\pi =$ {$v_{1}$, $v_{2}$, ..., $v_{k}$} è: $w(\pi) = \sum_{i = 1}^{k}w(v_{i-1}, v{i})$

**DEF**: Un cammino minimo tra una coppia di vertici $x$ e $y$ è un cammino evente costo minore o uguale a quello di ogni
altro cammino tra gli stessi vertici (non necessariamento unico).

**DEF**: La distanza $d_{g}(u, v)$ da $u$ a $v$ in $G$ è il costo di un qualsiasi cammino minimo da $u$ a $v$.

- Se non esiste un nessun cammino da $u$ a $v$ allora: $d(u, v) = +\infty$.
- Se c'è un cammino che contiene un ciclo il cui costo è negativo: $d(u, v) = -\infty$.

**Proprietà**:

1. Ogni sottocammino di un cammino minimo è un cammino minimo
2. Disuguaglianza Triangolare: Per ogni $u$, $v$, $x$, vale: $d(u,v) \leq d(u, x) + d(v, x)$. 
   Il cammino da $u$ a $v$ che passa per $x$ è un cammino nel grafo e quindi il suo costo è almeno il costo del cammino 
   minimo da $u$ a $v$.


- Dato $G = (V, E, w)$, $s\in V$, calcola le distanze di tutti i nodi da $s$, ovvero $d_{G}(s, v)$ per ogni $v\in V$.
- Dato $G = (V, E, w)$, $s\in V$, calcola l'albero dei cammini minimi di $G$ radicato in $s$.

**DEF**: $T$ è un albero dei cammini minimi (Shortest Path Tree - SPT) con sorgente $s$ di un grafo $G = (V, E, w)$, se 

- $T$ è un albero radicato in $s$.
- Per ogni nodo $v\in V$ vale: $d_{T}(s, v) = d_{G}(s, v)$. La distanza dell'unico cammino nell'albero $T$ da $s$ a $v$ 
  deve essere uguale all'cammino minimo da $s$ a $v$ nel grafo $G$.

Nel caso in cui il grafo non è pesato, SPT coincide con l'albero BFS.

## Algoritmo di Dijkstra

Calcola l'albero dei cammini minimi che le distanze da $s$.

Assunzione: tutti gli archi hanno peso non negativo, ovvero ogni arco (u, v) del grafo di peso $w(u, v) \geq 0$.

Sia `v.dist` la distanza dal nodo sorgente $s$ a $v$

```
Dijkstra(grafo G, nodo s) -> albero 
    for each(nodo u in G) do u.dist = +inf 
    T = albero con root s
    X = lista vuota
    CodaPriorita CP 
    s.dist = 0
    CP.insert(s, s.dist)

 
```




