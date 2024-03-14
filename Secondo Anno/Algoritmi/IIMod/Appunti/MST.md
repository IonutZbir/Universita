# Minimum Spanning Tree

- Input
Un grafo $G = (V, E)$ pesato e connesso non orientato, con valori reali dei pesi $c_{e}$

- Soluzione ammisibile
Un `Spanning Tree` di $G$ è un albero $T = (V, F)$ con $T \subseteq E$ tale che i vertici raggiungono tutti i nodi del grafo.

- Misura (da minimizzare)
Il costo totale dei pesi dell'albero T, ovvero $c(T) = \sum_{e\in T}c_{e}$

> [!IMPORTANT]
> Se $G$ ha pesi diversi per ciascun arco, l' MST è unico. In generale, se i pesi sono anche uguali, ci sono $n^(n-2)$ MST di un 
> grafo con $n$ nodi (Teorema di Cayley).

## Cicli
Un **ciclo** è un cammino chiuso nel grafo del tipo `a-b, b-c, ...., y-z, z-a`.

<img src="img/mst/ciclo.png" width="300" />

> [!IMPORTANT]
> Cycle property: Sia $C$ un ciclo, e sia $f$ l'arco di costo massimo appartenente a $C$. Allora esiste un MST $T^{\star}$ che non contiene $f$.
> Dim.  
> - Supponiamo che $f$ appartiene a $T^{\star}$.
> - Cancellando $f$ da $T^{\star}$, si crea un cut $S$ in $T^{\star}$.
> - L'arco $f$ sta sia nel ciclo $C$ e sia nel cutset $D$ corrsipondente a $S$. Allora esiste un altro arco, $e$ che sta sia in $C$ che in $D$.
> - $T^{'} = T^{\star} \cup \left\{ e \right\} - \left\{ f \right\}$ è ancora uno spanning tree.
> - Siccome $c_{e} \leq c_{f} => cost(T^{'}) \leq cost(T^{\star})$.
> - Allora $T^{'}$ è un MST che non contiene $f$.

<img src="img/mst/ciclop.png" width="200" />

## Cut
Il **cut** è un sottoinsieme di nodi $S$. (Definito anche come una partizione di $V$: $S$ e $V - S$).
Il **cutset** $D$ di un cut $S$ è un sottoinsieme di archi con un nodo in $S$ e un nodo in $V - S$.

<img src="img/mst/cut.png" width="300" />

> [!IMPORTANT]
> Cut property: Sia $S$ un sottoinsieme di nodi, e sia $e$ l'arco di costo minimo con un nodo in $S$ e un nodo in $V - S$. Allora 
> esiste un MST $T^{\star}$ contenente $e$.
> Dim.  
> - Supponiamo che $e$ non appartiene a $T^{\star}$.
> - Aggiungendo $e$ a $T^{\star}$ crea un ciclo $C$ in $T^{\star}$.
> - L'arco $e$ appartiene sia a $C$ che al cutset $D$ corrsipondente a $S$, allora esiste un altro arco, $f$ che appartiene sia a $C$ che a $D$.
> - $T^{'} = T^{\star} \cup \left\{ e \right\} - \left\{ f \right\}$ è ancora uno spanning tree.
> - Siccome $c_{e} \leq c_{f} => cost(T^{'}) \leq cost(T^{\star})$.
> - Allora $T^{'}$ è un MST contenente $e$.

<img src="img/mst/cutp.png" width="200" />

> [!IMPORTANT]
> L'intersezione tra un ciclo e un cutset contiene un numero pari di vertici.

<img src="img/mst/intersezione.png" width="300" />

Partendo da una nodo in S, esiste un arco per passare da $S$ a $V - S$. Avendo un ciclo C, allora esiste un arco per 
passare da $V - S$ a $S$. Di conseguenza, ci sono almeno 2 archi nell'intersezione. In generale ci sono $2\cdot k$ archi nell'intersezione.

## Algoritmo di Kruskal

Considera gli archi ordinati in modo crescente in base al costo. Aggiungi a $T$, che inizialmente è un albero vuoto, gli archi 
finchè non si crea un ciclo.

Per implementare in modo efficiente l'algoritmo di Kruskal, si usa la struttra dati `Union-Find`, perché:
- Per mantenere le componenti connessi delle soluzioni correnti-
- Per controllare se l'arco corrente forma un ciclo (con la soluzione corrente).

```
Kruskal(graph G=(V, E, c))
    UnionFind UF 
    Sia T un albero vuoto
    ordina gli archi in modo crescente in base ai costi
    for each vertex v do UF.makeset(v)
    for each edge (x, y) do 
        set_x = UF.find(x)
        set_y = UF.find(y)
        if set_x != set_y then 
            UF.union(set_x, set_y)
            aggiungi l'arco (x, y) a T
    return T
```

**Correttezza**: 

<img src="img/mst/kruskal.png" width="300" />

- Prendiamo in considerazione il cut $S$ di vertici appartenenti alla stessa componente connessa di $y$. 
- Dato che l'algoritmo guarda i vertici in ordine crescente, per collegare $S$ a $V - S$, l'algoritmo andrà a prendere l'arco (x,y) di costo minimo che attraversa il cut (`cut property`). 

**Complessità Temporale**:

- Ordinare gli archi costa: $O(m log m) = O(m log n)$
- Operazioni sulla Union-Find: 
    - $n$ `makeset`
    - $n - 1$ `union`
    - $m$ `find`
- Usando QuickFind con l'euristica *union by size*: $O(m log n + m + n log n) = O(m log n)$
- Usando QuickUnion con l'euristica *union by size*: $O(m log n + m log n + n) = O(m log n)$
