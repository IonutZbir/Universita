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
1.  Dijkstra(G, s)
2.  Dijkstra(G, t)
3.  z = arg(min{const(x)})
4.  return const(z)
```
**Corretteza**: L'algoritmo è corretto poiché l'algoritmo di Dijkstra è corretto. Inoltre per ogni nodo $x$, calcolo il cammino minimo, quindi provo tutti i cammini possibili, e 
sceglo quello ottimale.

**Complessità Temporale**: $T(n) = O(m + nlogn)$.

## Esercizio 3 del 04/07/2023

Sia $G = (V, E)$ un grafo diretto con $n$ nodi ed $m$ archi. Ci sono Alice e Bob che vogliono incontrarsi in un nodo di $G$.
Inizialmente, Alice si trova sul nodo $S_{A}$ ed ha a disposizione $\Delta(A)$ monete di tipo $A$, mentre Bob si trova sul nodo $S_{B}$ ed ha a disposizione $\Delta(B)$ monete di tipo $B$.
Ad ogni arco $e\in E$, sono associati due interi, $c^{A}_{e}$ e $c^{B}_{e}$, che rappresentano rispettivamente il numero di monete di tipo $A$ che Alice deve pagare per attraversare $e$,
e il numero di monete di tipo $B$ che Bob deve pagare per poter attraversare $e$.
Progettate un algoritmo di complessità $O(m + n log n)$ che calcola, se esiste, un modo per far incontrare Alice e Bob.

<div align="center" style="margin-bottom: 20px">
    <img src="Alice_Bob.png" width=400 />
</div>

L'idea è quella di andare a calcolare attraverso l'algoritmo di Dijkstra l'SPT radicato in $S_{A}$ e l'SPT radicato in $S_{B}$. Cosi ottieniamo le distanze dalle 2 sorgenti verso tutti i
nodi $x\in V$. 

- $cost_{A}(x) = d(S_{A, x}) = \sum_{e\in E}^{x} w_{A}(e) = c_{e}^{A}$
- $cost_{B}(x) = d(S_{B, x}) = \sum_{e\in E}^{x} w_{B}(e) = c_{e}^{B}$

Per ogni nodo $x$, trovo il cammino minimo, e vado a confrontare $\Delta(A)$ e $\Delta(B)$ con $cost_{A}(x)$ e $cost_{B}(x)$. Se Il costo è superiore per tutti i nodi $x$, allora non esiste 
uno nodo in cui Alice e Bob si possono incontrare.

```
1.  Dijkstra(G, SA) // SPT radicato in SA 
2.  Dijkstra(G, SB) // SPT radicato in SB 
3.  for each x do
4.      A = costA(x)
5.      B = costB(x)
6.      if A <= DeltaA and B <= DeltaB then
7.          return A, B, x
8.  return -1
```
**Complessità Temporale**: $T(n) = O(m + nlog(n))$

**Corretteza**: L'algoritmo è corretto poiche l'algoritmo di Dijkstra è corretto. Inoltre provo tutti i nodi $x$ per cui ho calcolato la distanza e trovo il nodo in comune $x$ se esiste 
nel quale Alice e Bob si possono incontrare spendendo meno monete di quante ne hanno a disposizione.


## Esercizio 3 del 07/25/2023

Nell’ultimo gioco rilasciato dalla Mintendo, Super Ciano Bross si trova su un nodo $s$ di un grafo orientato $G = (V, E)$ con $n$ nodi ed $m$ archi, e deve raggiungere il nodo $t$ 
per vincere il livello. Ogni arco $e$ è associato inizialmente uno stato $\sigma(e)\in$ {on, off}. Super Ciano può attraversare solo gli archi che sono nello stato on. 
C'è inoltre un insieme di nodi $B\subseteq V$ che contengono un bottone speciale. Se Ciano è su un nodo $b\in B$ può decidere di schiacciare il bottone e tutti gli archi
invertono il proprio stato, quelli che erano nello stato on passano allo stato off e quelli che erano nello stato off passano nello stato on.
Progettate un algoritmo di complessità $O(m + n)$ che calcola, se esiste, una strategia per Super Ciano che lo porta a vincere il livello nel nodo $t$.

**Idea**

L'idea è quella di creare un grafo ausiliario $G'$ a livelli, più precisamente con 2 livelli. Appena Ciano incontra un nodo con un bottone può decidere se premere il bottone e andare 
nel secondo livello oppure continuare sel primo livello se possibile (se l'arco successivo è on). Nel secondo livello, si invertono on e off, quindi se Ciano preme il bottone perchè 
davanti a se l'arco è off e non può procedere, premendo il bottone andrà nel secondo livello dove potrà procedere.

<div style="margin-bottom: 300px">
    <img src="CianoOn.png" width=400 style="float: left;" />
    <img src="CianoOnL.png" width=300 style="float: right;"/>
</div>

Come viene creato il grafo $G'$?

**Nodi**: 

- per ogni $v\in V$ ho $2\cdot v$.
- un nodo finale $T$ 

**Archi**:

- per ogni nodo $u\in G$ bottone aggiungo un nuovo arco $(u, u')$ dove $u'\in G'$ con $w(u, u') =$ On.
- Per ogni arco $(u, v)\in G$ con peso $w$ ho l'arco $(u', v')\in G'$ con peso $w'$. 
    - Se $w =$ On $=> w' =$ off
    - Se $w =$ Off $=> w' =$ On.
- due archi $(T, T')$ e $(T_{0}, T')$ con peso On

**Proprietà**: Esiste un cammino da $S$ a $T$ in $G$ se e soltanto se esiste un cammino da $S$ a $T'$ in $G'$. Per trovare questo cammino si può effettuare una visita BFS o DFS, entrambe 
con costo $O(n + m)$, poiché il numero di livelli è costante ovvero 2.

La costruzione del grafo $G'$ costa $O(n + m)$.


## Esercizio 2 del 27/09/2023

Un labirinto è modellato come un grafo non diretto $G = (V, E)$. Voi siete nel nodo $s$ e l’uscita si trova nel nodo $t$. Potete percorrere gli archi, spendendo un minuto per ogni arco. 
Nel labirinto inoltre c'è un nodo speciale $p$ che è un teletrasporto, e un insieme di nodi $U\in V$ che sono uscite del teletrasporto. 
Se siete su $p$ potete teletrasportarvi in un qualsiasi nodo $q\in U$ a vostra scelta. Il tempo del teletrasporto è di 3 minuti.
Progettate un algoritmo efficiente che calcoli la strategia più veloce, se esiste, per uscire dal labirinto.

**Idea**

L'idea è quella di andare a confrontare la distanza da $s$ a $t$ con la minima distanza $const(u_{i})$ dove   
$const(u_{i}) = d(s, p) + 3 + d(u_{i}, t)$.  
Essendo un grafo pesato, con pesi tutti 1, possiamo usare una BFS per calcolare le distanze. Per calcolare $d(u_{i}, t)$ invertiamo gli archi del grafo è facciamo una BFS con sorgente $t$.

Di conseguenza abbiamo due casi:

<div style="margin-bottom: 300px">
    <img src="Lab1.png" width=300 style="float: left;" />
    <img src="Lab2.png" width=300 style="float: right;"/>
</div>

```
1.  BFS(G, s)
2.  BFS(G, t)
3.  z = arg(min(const(x))) // dove x è uno dei nodi uscita u
4.  d = d(s, t)
5.  if const(z) > d then
6.      return d
7.  else
8.      return const(z)
```

**Complessità Temporale**: Costo della BFS ovvero $O(n + m)$, lineare nella dimensione del grafo.

## Esercizio 2 del 18/07/2022

Si consideri il seguente gioco giocato su un grafo diretto $G = (V, E)$ con $n$ nodi ed $m$ archi. Una pedina è posizionata inizialmente su un nodo $s$. 
E' possibile spostare la pedina dalla posizione corrente, diciamo $u$, su un nodo $v$, se esiste un arco diretto $(u, v)\in E$ in $G$. Inoltre, c'è un insieme di nodi speciali $X\in V$. 
Se la pedina si trova su un nodo speciale $x\in X$ è possibile muovere la pedina anche lungo archi entranti in $x$, oltre quelli uscenti da $x$,
ovvero è possibile muovere la pedina da $x$ a $v$ se e solo se $(v, x)\in E$ o $(x, v)\in E$, o entrambi.
Progettare una algoritmo che in tempo $O(m + n)$ decide se, indipendentemente dalla posizione iniziale $s$, è sempre possibile spostare la pedina da $s$ a ogni altro nodo $t$ del grafo
con un'opportuna sequenza di mosse.

**Idea**:

L'idea è quella di creare un drafo ausiliario $G'$ dove per ogni nodo $x\in E$, se esiste l'arco $(u, x)$ (entrante) allora esiste anche l'arco $(x, u)$ (uscente).


<div style="margin-bottom: 200px">
    <img src="Inverti.png" width=300 style="float: left;" />
    <img src="Inverti1.png" width=300 style="float: right;"/>
</div>

In questo caso il nodo $u$ nel grafo $G$ non è raggiungibile da $s$, ma lo è nel grafo $G'$, poiche viene aggiunto l'arco $(x, u)$.

**Proprietà**: Esiste una sequenza di mosse (cammino) che pemette di spostare la pedina da $s$ a ogni altro nodo in $G$ se e soltanto se esiste un cammino da $s$ a tutti gli altri 
nodi in $G'$.

**Complessità Temporale**: Costo di una visita BFS, O(n + m), lineare nella dimensione del grafo.

