# Esercizio 4 Esame 19.06.2024

Consideriamo la passeggiata aleatoria semplice sul grafo a papollon mostrato in figura. Supponiamo la passegiata aleatoria parta dal vertice A.

![[papillon_graph.excalidraw]]

1. Scrivere la matrice di transizione della catena.
2. La catene è irriducibile? È aperiodica?
3. Descrivere le misure stazionarie della catena.
4. La catena è reversibile?
5. Quanto vale l'aspettazione del primo tempo di ritorno in A?
6. Calcolare l'aspettazione della variabile aleatoria X che conta il numero di volte che la catena visita B prima di tornare in A.
7. Descrivere l'intera distribuzione di X.

## Soluzione

La matrice di transione $P$ è
$$ P = 
\begin{pmatrix} 
0 & 1/2 & 1/2 & 0 & 0 \\
1/2 & 0 & 1/2 & 0 & 0 \\
1/4 & 1/4 & 0 & 1/4 & 1/4  \\
0 & 0 & 1/2 & 0 & 1/2  \\
0 & 0 & 1/2 & 1/2 & 0  \\
\end{pmatrix}$$
La catena inoltre è irriducibile in quanto il grafo è uno connesso. A partire da un qualsiasi stato è possibile raggiungere tutti gli altri in tempo finito. Inoltre, catena è aperiodica in quanto ci sono cicli di lunghezze 2 e 3, di conseguenza $MCD(2, 3) = 1$.
- $A \to C \to A$, questo è un ciclo di lunghezza 2
- $A \to C \to B \to A$ è un ciclo di lunghezza 3.

Possiamo quindi concludere che la catena è *irriducibile ed ergodica*. 
Poiché stiamo considerando una passeggiata aleatoria semplice, aperiodica vale che
$$
\begin{align}
\forall v \in V, \quad \pi_{v} = \frac{\delta(v)}{2|E|}, \quad \text{ossia} \\ \\
\boxed{\bar{\pi} = \left( \frac{1}{6}, \frac{1}{6}, \frac{1}{3}, \frac{1}{6}, \frac{1}{6} \right)}
\end{align}
$$
Inoltre questa distribuzione è reversibile, infatti vale che:
$$
\begin{align}
\forall v, w \in V \setminus\{C\}: v \neq w, &\quad \pi_{v}P_{vw} = \pi_{w}P_{wv} \\ \\
&\implies \frac{1}{6} \frac{1}{2} = \frac{1}{2} \frac{1}{6} \\
\text{Mentre} \\ \\
\forall v \in V \setminus\{C\}, &\quad \pi_{v}P_{vC} = \pi_{C}P_{Cv}  \\ \\
&\implies \frac{1}{6} \frac{1}{2} = \frac{1}{3} \frac{1}{4} \\
\end{align}
$$
Concludiamo quindi che la catena è *reversibile*.

Poichè la catena è irriducibile ed ergodica valgono le ipotesi del Teorema 7.7 e di conseguenza esiste il limite $\lim_{ t \to \infty } P_{ji}^t$ che non dipende da $j$ per ogni $i \in V$, e inoltre vale che
$$
\pi_{i} = \lim_{ t \to \infty } P^t_{ji} = \frac{1}{h_{ii}} 
$$
dove $h_{ii}$ è il tempo di attesa di primo ritorno in $i$ partendo da $i$, quindi
$$
\boxed{h_{AA} = \frac{1}{\pi_{A}} = 6}
$$
Calcoliamo ora $\mathbb{E}[X]$. Definiamo $v_{i}$ come il numero atteso di visite allo stato B, partendo dallo stato $i$, prima di raggiungere A. Se raggiungiamo A ci fermiamo, quindi
$$
v_{A} = 0
$$
Se arriviamo in B, contiamo 1 più le future visite. Per gli altri stati contiamo 0.
$$
\begin{cases}
v_{B} = 1 + \frac{1}{2}v_{A} + \frac{1}{2}v_{C} = 1 + \frac{1}{2}v_{A} \\
v_{C} = 0 + \frac{1}{4}v_{B} + \frac{1}{4}v_{D} + \frac{1}{4}v_{E} \\
v_{D} = 0 + \frac{1}{2}v_{C} + \frac{1}{2}v_{E} \\
v_{E} = 0 + \frac{1}{2}v_{C} + \frac{1}{2}v_{D}
\end{cases}
$$
Da questo sistema otteniamo che
$$
v_{B} = \frac{4}{3}, \qquad v_{C} = \frac{2}{3}
$$

Siamo quindi interessati a 
$$\boxed{E_{A}[X] = P_{AB} \cdot v_{B} + P_{AC} \cdot v_{C} = \frac{1}{2} \frac{4}{3} + \frac{1}{2} \frac{2}{3} = 1}$$
Infine, rimane solo da trovare la distribuzione di $X$
$$
P(X = k)
$$
- $k = 0$, allora 
$$
\begin{align}
P(X = 0) &= P_{AC} \cdot P(\text{da C con prob. 1/2 torno in A senza passare per B})  \\
&= \frac{1}{2} \frac{1}{2} = \frac{1}{4} \\
&\implies P(X \geq 1) = 1 - P(X = 0) = \frac{3}{4}
\end{align}
$$
- $k \geq 1$, 
$$
\begin{align}
P(X = k) &= ( P_{AB} + P_{AC}P_{CB}) \cdot P_{BC}^{k-1} \cdot (P_{BA} + P_{BC}P_{CA}) \\
&=\frac{3}{4} \left( \frac{1}{2} \right)^{k-1} \cdot \frac{3}{4} = \frac{9}{16}\left( \frac{1}{2} \right)^{k-1}
\end{align}
$$
Dove $P_{AC}P_{CB} = P_{BC}P_{CA} = \frac{3}{4}$ perché andare in E e in D è solo una perdita di tempo, quindi una volta che sto in C, considero solo A e B, con prob. $\frac{1}{2}$ di andare in uno o nell'altro. Se vado in E o in D, per andare in A/B devo passare comunque per C, quindi non ha senso contarli.

In conclusione
$$
P(X = k) = \begin{cases}
\frac{1}{4} &\iff k = 0 \\
\frac{9}{16}\left( \frac{1}{2} \right)^{k-1} &\iff k \geq 1
\end{cases}
$$

# Esercizio 4 Esame 22.06.2026

Siano $X_{0}, X_{1}, \dots$ variabili aleatorie uniformi indipendenti su $\{1, \dots, 6\}$, rappresentando una sequenza di dadi a sei facce indipendenti. Sia $(Y_{i})_{i=1,2, \dots}$ il processo definito su $\{ 1, \dots, 6 \}^2$ nella maniera seguente:
$$
Y_{i} = (X_{i-1}, X_{i})
$$

1. Il processo $(Y_{i})$ è una catena di Markov?
2. Descrivere le probabilità di transizione di $(Y_{i})$.
3. Il processo è irriducibile? È aperiodico?
4. Descrivere la o le distribuzioni invarianti di $(Y_{i})$ e dire se sono misure reversibili.
5. Trovare il tempo medio di primo ritorno dello stato $(1,2)$ e quello dello stato $(6,6)$.
6. Trovare il tempo medio per andare dallo stato $(1,2)$ allo stato $(6,6)$.

## Soluzione

L'insieme di stati è $V = \{1, \dots, 6\}^2$, ossia tutte le coppie di risultati, quindi $|V| = 36$.

Vediamo il seguente esempio nella figura per capire perché questo processo è una catena di Markov.
![[catena_dadi_.excalidraw]]

Affinché il processo sia una catena di Markov, deve soddisfare la proprietà di Markov. Infatti
$$
\begin{align}
&P(Y_{i+1} = (X_{i}, X_{i+1}) = ((b,c) \big| Y_{i} = (X_{i-1}, X_{i}) = ((a,b), Y_{i-1}, \dots, Y_{1})  \\
&= P(X_{i+1} = c) = \frac{1}{6}  \\
&= P(Y_{i+1} = (X_{i}, X_{i+1}) \big | Y_{i} = (X_{i-1}, X_{i}))
\end{align}
$$
Le probabilità di transizione sono:
$$
P(Y_{i}, Y_{i+1}) = P((a,b), (b', c)) = 
\begin{cases}
\frac{1}{6} &\iff b = b',\ \forall c \in \{ 1,\dots,6 \} \\
0 &\iff b \neq b'
\end{cases}
$$
Cioè dallo stato $(a,b)$ si va con probabilità $\frac{1}{6}$ a ciascuno dei 6 stati $(b,1), (b,2), \dots, (b,6)$.

È *irriducibile* perchè a partire da un qualunque stato è possibile visitare tutti gli altri. Formalmente, per verificare che sia irriducibile dobbiamo mostrare che $\exists n>0: P^n_{ij} > 0,\ \forall i,j \in V$. Calcoliamo $P^{2}$:
$$
\begin{align}
P^2((a,b), (x,y)) &= \sum_{z=1}^6 P((a,b),(b,z))P((b,z),(x,y)) \\ &= \underbrace{\frac{1}{6}}_{z = x} \cdot \frac{1}{6} = \frac{1}{36} > 0
\end{align}
$$
**per ogni** $(a,b)$ e $(x,y)$: in due passi si può raggiungere qualsiasi stato, indipendentemente da dove si parte. Quindi tutti gli stati comunicano fra loro $\Rightarrow$ **catena irriducibile**.

È *aperiodica* in quanto per gli stati $(a,a)$ è presente un self loop. Infatti 
$$
P((a,a), (a,a)) = \frac{1}{6} \forall a \in \{ 1, \dots, 6 \}
$$
$\Rightarrow$ **catena aperiodica**.
Possiamo quindi concludere che la catena è **irriducibile ed ergodica**.

Esiste dunque un'unica distribuzione invariante, data da
$$
\boxed{\pi_{(a,b)} = \frac{1}{36} \quad \forall (a,b) \in V}
$$
È invariante perchè soddisfa la relazione $\pi = \pi P$, infatti
$$
\begin{align}
(\pi P)_{(b', c)} &= \sum_{(a,b)} \pi_{(a,b)}P((b',c), (a,b))  \\
&= \sum_{a=1}^6 \underbrace{\pi_{(a,b')}}_{\text{ solo } b = b' \text{ soppravvive}} \cdot P((a, b'), (b', c)) \\
&= \frac{6}{36} \cdot \frac{1}{6} = \frac{1}{36}
\end{align}
$$
Ricordiamo la probabilità di transizione. Vale $\frac{1}{6}$ solo quando $b=b'$, altrimenti vale 0. Su tutti i possibili 36 stati su cui stiamo sommando, soppravvivono solo i 6 nei quali possiamo andare con probabilità $\frac{1}{6}$.

La catena non è reversibile, basta verificare $\pi(x)P(x,y) = \pi(y)P(y,x)$ su $x = (a,b),\ y=(b,c)$ con $a \neq c$.
$$
\begin{align}
\pi(x)P(x,y) &= \frac{1}{36} \frac{1}{6} > 0 \\
&\neq \\
\pi(y)P(y,x) &= \frac{1}{36} P((b,c), P(a,b)) = 0 \quad (c \neq a)
\end{align}
$$
$\Rightarrow$ **misura non reversibile**.

Poiché la catena è irriducibile ed aperiodica, ossia è ergodica, esiste 
$$
\lim_{ t \to \infty } P^t_{ji} > 0
$$
indipendentemente da $j$, e inoltre vale che
$$
\pi(x) = \lim_{ t \to \infty } P^t_{jx} = \frac{1}{h_{xx}}
$$
dove $h_{xx}$ è il *tempo medio di primo ritorno* in $x$. Quindi, per ogni $x \in V$, vale che
$$
\boxed{h_{xx} = \frac{1}{\pi(x)} = 36}
$$
Infine, calcoliamo il tempo medio per andare dallo stato $(1,2)$ allo stato $(6,6)$.

Sia 
$$
h(a,b) = \text{tempo medio per andare in } (6,6) \text{ partendo da } (a,b)
$$
Allora,
$$
h(a,b) = 1 + \frac{1}{6} \sum_{c=1}^6 h(b, c)
$$
Ora abbiamo due casi:
- Quando $b = 6$ si ha $$h(a,6) = 1 + \frac{1}{6}h(6,6) + \frac{1}{6} \sum_{c=1}^5 h(6,c) = \frac{1}{6} \sum_{c=1}^5 h(6,c)$$
- Quando $b \neq 6$ si ha $$h(a,b) = 1 + \frac{1}{6}\sum_{c = 1}^5 h(b,c) + \frac{1}{6}h(a,6)$$
Notiamo che $h(a,b)$ dipende solo da $b$ e non da $a$, quindi
$$
h(b) = h(a,b) \qquad \land \qquad h(6) = h(a,6)
$$
Riscrivendo le due equazioni abbiamo che
$$
\begin{cases}
h(6) = 1 + \frac{1}{6} \sum_{c=1}^5 h(c) \\ \\
h(b) = 1 + \frac{1}{6} \sum_{c=1}^c h(c) + \frac{1}{6}h(6)
\end{cases}
$$

*Osservazione:* $h(1) = h(2), \dots, h(5) = h$. Infatti
$$
\begin{cases}
h(1) = 1 + \frac{1}{6}\sum_{c=1}^5 h(c) \\
h(2) = 1 + \frac{1}{6}\sum_{c=1}^5 h(c) \\
h(3) = 1 + \frac{1}{6}\sum_{c=1}^5 h(c) \\
h(4) = 1 + \frac{1}{6}\sum_{c=1}^5 h(c) \\
h(5) = 1 + \frac{1}{6}\sum_{c=1}^5 h(c) \\
\end{cases}
$$
Quindi, riscrivendo il sistema, otteniamo
$$
\begin{cases}
h(6) = 1 + \frac{5}{6}h \\ \\
h = 1 + \frac{5}{6} h + \frac{1}{6}h(6)
\end{cases}
$$
Sostituendo, si ha
$$
\begin{align}
&h = 1 +\frac{5}{6}h + \frac{1}{6}\left( 1 + \frac{5}{6}h \right) \\
&\iff \left( 1-\frac{5}{6} - \frac{5}{36} \right)h = 1 + \frac{1}{6} \\
&\iff h = 42
\end{align}
$$
In conclusione
$$
\boxed{h(1,2) = h(2) = h = 42}
$$

# Esercizio 3 Esame 24.02.2025

A mezzanotte l'orologio di Palazzo Senatorio al Campidoglio si è rotto. Adesso, ad ogni ora, invece di girare in senso orario la lancetta delle ore salta in maniera casuale (cioè, con uguale probabilità) su uno dei due numeri ad essa adiacenti.

1. Introdurre una catena di Markov che descriva la posizione della lancetta ad ogni ora ed esibire la sua matrice di transizione.
2. La catena è irriducibile? È aperiodica?
3. Trovare la distribuzione invariante della catena. La catena è reversibile rispetto a questa distribuzione?
4. Supponiamo ora invece che ad ogni ora le lancette restino ferme con probabilità $1/2$ e che saltino su uno dei due numeri adiacenti a caso con probailità $1/4$ e $1/4$. Introdurre una nuova catena che descriva il moto delle lancette in questo nuovo scenario e spiegare cosa cambia ripetto alle domande in (b) e (c).
5. Quante ore si deve aspettare in media prima che le lancette tornino alle ore 12?
6. Qual è la probabilità che prima di ritornare alle ore 12 le lancette abbiano visitato almeno una volta tutti gli altri numeri?

**Punto (1)**
Lo spazio degli stati rappresenta le $12$ ore del quadrante dell'orologio:
$$S = \{1, 2, \dots, 12\} \cong \mathbb{Z}_{12}$$

Sia $X_t \in S$ la posizione della lancetta all'ora $t$. Il processo $(X_t)_{t \ge 0}$ è una catena di Markov a tempo discreto e spazio degli stati finito. A ogni passo la lancetta salta con uguale probabilità $1/2$ su uno dei due numeri adiacenti:

$$
P_{ij} = 
\begin{cases}
\frac{1}{2} \iff j = i \pm 1 \\
0 \text{ altrimenti }
\end{cases}
$$

La matrice di transizione $P$ di dimensione $12 \times 12$ è una matrice circolante:
$$P = \begin{pmatrix} 0 & 1/2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1/2 \\ 1/2 & 0 & 1/2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 1/2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1/2 & 0 & 1/2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1/2 & 0 & 1/2 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1/2 & 0 & 1/2 \\ 1/2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1/2 & 0 \end{pmatrix}$$

Notiamo che $P$ è una matrice simmetrica.

**Punto (2)**
- **Irriducibilità:** La catena è **irriducibile**. Il grafo associato è un ciclo semplice non orientato di lunghezza 12 ($C_{12}$), quindi è connesso: per ogni coppia di stati $i, j \in S$ esiste un cammino di lunghezza al più 6 tale che $P^n(i, j) > 0$.
- **Aperiodicità:** La catena **non è aperiodica**, ha periodo $d = 2$. Il grafo $C_{12}$ è bipartito (ore pari e ore dispari): partendo da uno stato $i$, si può ritornare in $i$ solo compiendo un numero pari di passi, dunque: $$d(i) = \gcd\{n \ge 1 : P^n(i, i) > 0\} = \gcd\{2, 4, 6, \dots\} = 2$$
**Punto (3)**
- **Distribuzione invariante:** La matrice $P$ è simmetrica ($P_{ij} = P_{ji}$), quindi è doppiamente stocastica:$$\sum_{i=1}^{12} P_{ij} = 1 \quad \forall j \in S$$Di conseguenza, la distribuzione invariante è la **distribuzione uniforme** su $S$:    $$\pi = \left(\frac{1}{12}, \frac{1}{12}, \dots, \frac{1}{12}\right)$$Verifica: $(\pi P)_j = \sum_{i=1}^{12} \pi_i P_{ij} = \frac{1}{12} \sum_{i=1}^{12} P_{ij} = \frac{1}{12} = \pi_j$. Se vediamo la catena di Markov come una passeggiata aleatoria semplice, per un teorema noto vale che: $$\pi_{i} = \frac{\delta_{i}}{2|E|} = \frac{2}{24} = \frac{1}{12}$$
- **Reversibilità:** La catena è **reversibile** rispetto a $\pi$. Verifichiamo la condizione di bilancio dettagliato: $$\pi_i P_{ij} = \pi_j P_{ji} \quad \forall i, j \in S$$Essendo $\pi_i = \pi_j = \frac{1}{12}$ per ogni $i, j$, l'uguaglianza si riduce a $P_{ij} = P_{ji}$, che è verificata per la simmetria di $P$.

**Punto (4)**
Nel nuovo scenario le probabilità di transizione diventano:
$$\widetilde{P}_{i, i} = \frac{1}{2}, \quad \widetilde{P}_{i, i+1} = \frac{1}{4}, \quad \widetilde{P}_{i, i-1} = \frac{1}{4}$$
La matrice di transizione è $\widetilde{P} = \frac{1}{2} I + \frac{1}{2} P$.
- **Cosa cambia rispetto a (2):**
	- **Irriducibilità:** Resta **irriducibile** (tutti gli stati continuano a comunicare).
    - **Aperiodicità:** La catena diventa **aperiodica**. La catena è lazy, di conseguenza esistono cicli di lunghezza pari e di lunghezza dispari: $$d(i) = \gcd\{1, 2, 3, \dots\} = 1$$
- **Cosa cambia rispetto a (3):**
    - **Distribuzione invariante:** Non cambia. $\widetilde{P}$ resta simmetrica e doppiamente stocastica, quindi $\pi$ rimane la distribuzione uniforme $\pi_i = 1/12$. Oppure $$\pi_{i} = \frac{\delta_{i}}{2|E|} = \frac{4}{48} = \frac{1}{12}$$Il grado di ciascun nodo è 4 perche quello del cappio lo considero due volte, una volta entrante e una volta uscente.
    - **Reversibilità:** Resta reversibile, poiché $\widetilde{P}_{ij} = \widetilde{P}_{ji}$ per ogni $i, j$.

**Punto (5)**
Si richiede il tempo medio di primo ritorno allo stato 12, partendo da 12, per la catena originaria:
$$\mathbb{E}_{12}[T_{12}] = \mu_{12}$$
Per il teorema fondamentale delle catene di Markov irriducibili (e ricorrenti positive), il tempo medio di ricorrenza di uno stato $i$ è l'inverso della sua probabilità stazionaria:
$$\mathbb{E}_i[T_i] = \frac{1}{\pi_i}$$
Poiché $\pi_{12} = \frac{1}{12}$:
$$\mathbb{E}_{12}[T_{12}] = \frac{1}{1/12} = 12 \text{ ore}$$
**Punto (6)**

Sia 
$$q_{i} = P(\text{raggiungere l'estremo 11 prima di toccare 0 } | \text{ partendo da }k)$$
in pratica è un'applicazione della **rovina del giocatore**.
$$
\begin{cases}
q_{i} = \frac{1}{2}q_{i+1} + \frac{1}{2}q_{i-1} \\
q_{12}=q_{0} = 0 &\text{tocco 12 troppo presto} \\
q_{11} = 1 &\text{ raggiunto l'ultimo nodo troppo presto}
\end{cases}
$$
Senza svolgere di nuovo tutti i calcolo, abbiamo che
$$q_{i} = \frac{i}{11}$$
Quindi
$$
q_{1} = \frac{1}{11}
$$