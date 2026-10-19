Un *processo stocastico* $(X_{t})_{t\in T}$ è una collezione di v.a. indicizzate da un parametro $t$, che spesso può essere pensato come il tempo ($T$ può essere sia continuo, ad esempio $T = \mathbb{R}_{+}$, che discreto, ad esempio $T = \mathbb{N}_{0}$).
$(X_{t})$ descrive in questo caso il variare di una certa quantità col trascorrere del tempo, ad esempio
$$
X_{t} = \text{ prezzo delle azioni Microsoft al giorno } t
$$
$X_{t}$ è detto *stato* del processo al tempo $t$ e può anch'esso prendere valori nel continuo ($X_{t} \in \mathbb{R}_{+}$) o nel discreto $(X_{t} \in V$, con $V$ i vertici di un grafo).

Le *catene di Markov* sono processi stocastici a tempo discreto (spesso anche a spazio discreto) speciali: il valore al tempo $t,\ X_{t}$, dipende solo da $X_{t-1}$ e *NON* dal resto della storia.

**DEF 7.1:** Un processo stocastico a tempo discreto $(X_{t})_{t\in \mathbb{N}_{0}}$ è detto *catena di Markov* (omogeneea) se
$$
\begin{align}
P_{ij} &= P(X_{t} = j | X_{t-1} = i, X_{t-2} = i_{t-1}, \dots, X_{0} = i_{0})  \\
&= P(X_{t} = j | X_{t-1} = i) \quad \forall i, j, i_{0}, \dots, i_{t-2}
\end{align}
$$
Tale proprietà è detta *proprietà di Markov*.

*Osservazione:* La proprietà di Markov *NON* ci dice che $X_t$ è indipendente da $X_{0}, \dots, X_{t-2}$, ma che lo diventa se la si condiziona a $X_{t-1}$. Se assumiamo che $(X_{t})$ assume valori in un insieme finito $V = \{0, 1, \dots, n\}$ (o infinito numerabile $V = \{0, 1, \dots\}$) la probabilità $P_{ij}$ è la probabilità che il processo *salti* da $i$ a $j$ in un passo.

**DEF:** Possiamo raccogliere tutte queste probabilità nella matrice $P_{|V| \times |V|}$
$$
P = \begin{pmatrix}
P_{11} & P_{12} & \cdots & P_{1n} \\
P_{21} & P_{22} & \cdots & P_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
P_{n1} & P_{n2} & \cdots & P_{nn}
\end{pmatrix}
$$
detta *matrice di transizione* della catena.

*Osservazione:* Si ha che le somme sulle righe valgono 
$$\sum_{j \in V} P_{ij} = 1 \quad \forall i \in V$$
$P$ è una matrice *stocastica*.

La matrice $P$ è utile per calcolare la distribuzione della catena ad un tempo $t$. 
Sia 
$$p_{i}(t) = P(X_{t} = i)$$
la probabilità che la catena sia in $i \in V$ al tempo $t$. 
Sia
$$
\bar{p}(t) = (p_{0}(t), p_{1}(t), \dots, p_{|V| - 1}(t))
$$
il vettore riga che descrive la distribuzione di $X_t$. Allora, dalla formula delle probabilità totali
$$
\begin{align}
p_{j}(t) &= \sum_{i \in V} p_{i}(t-1)P_{ij}  \\
&\equiv \\
P(X_{t} = j) &= \sum_{i\in V} P(X_{t} = j | X_{t-1} = i)P(X_{t-1}=i)
\end{align}
$$
In forma matriciale (considerando cioè contemporaneamente tutti gli indici) si ha che 
$$
\bar{p}(t) = \bar{p}(t-1)P
$$


Possiamo anche calcolare, ad esempio, la *probabilità che si arrivi in $j$ dopo due passi partendo da $i$ al tempo $t$*.
$$
\begin{align}
P(X_{t+2}|X_{t} = i) &= \sum_{l \in V} P(X_{t+2} = j, X_{t+1} = l | X_{t} = i) \\
&= \sum_{l \in V} P(X_{t+2} = j | X_{t+1} = l, X_{t} = i)P(X_{t+1}=l|X_{t}=i) \\
&= \sum_{l \in V} P_{lj}P_{il} = (P^2)_{ij}
\end{align}
$$
Generalizzando ad $m$ passi si ha
$$
\begin{align}
&P^m_{ij} = (P^m)_{ij} = P(X_{t+m} = j | X_{t} = i) \text{ con} \\ \\
&P_{ij}^m = \sum_{l \in V}P_{il}P^{m-1}_{lj}
\end{align}
$$
La matrice di transizione ad $m$ passi
$$
P^m = \begin{pmatrix}
P^m_{11} & P^m_{12} & \cdots & P^m_{1n} \\
P^m_{21} & P^m_{22} & \cdots & P^m_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
P^m_{n1} & P^m_{n2} & \cdots & P^m_{nn}
\end{pmatrix}
$$
è tale per cui
$$
P^m = P \cdot P^{m-1} = \underbrace{P \cdots P}_{m-\text{volte}} 
$$
e $\forall t \in \mathbb{N}_{0}$ e $m \in \mathbb{N}$
$$
\bar{p}(t + m) = \bar{p}(t) P^m
$$

Un altro utile modo di pensare una catena di Markov è vederla come un grafo diretto pesato $G = (V, E, w)$. I suoi vertici $V$ sono gli stati della catena. L'arco diretto $(i,j)$ è presente se e solo se $P_{ij} > 0$, nel tal caso gli si associa il peso $w_{ij} = P_{ij}$. Sono permessi self-loops (quando $P_{ii} > 0$). 
Per definizione i pesi soddisfano $\sum_{j \in V} w_{ij} = 1\quad \forall i \in V$.

Una sequenza di stati visitati dal processo è rappresentata da un cammino diretto sul grafo. La probabilità che il processo segua un dato cammino è il prodotto dei pesi degli archi utilizzati dal cammino.

*Esempio:* La seguente matrice ed il seguente grafo rappresentano la stessa catena di Markov.
![[catena_grafo_matrice_esempio.png|500]]
Calcoliamo con le due rappresentazioni la probabilità di andare da 0 a 3 in esattamente 3 passi.

- $0 \to 1 \to 0 \to 3 \implies P = \frac{1}{4} \cdot \frac{1}{2} \cdot \frac{3}{4} = \frac{3}{32}$
- $0 \to 1 \to 3 \to 3 \implies P = \frac{1}{4} \cdot \frac{1}{6} \cdot \frac{1}{4} = \frac{1}{96}$
- $0 \to 3 \to 1 \to 3 \implies P = \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{1}{6} = \frac{1}{16}$
- $0 \to 3 \to 3 \to 3 \implies P = \frac{3}{4} \cdot \frac{1}{4} \cdot \frac{1}{4} = \frac{3}{64}$
Sommando, $P^3_{03} = \frac{41}{192}$.
Per la matrice calcoliamo la terza potenza
$$
P^3 = \begin{pmatrix}
\frac{3}{16} & \frac{7}{48} & \frac{29}{64} & \boxed{\frac{41}{192}} \\
\frac{5}{48} & \frac{5}{24} & \frac{79}{144} & \frac{5}{36} \\
0 & 0 & 1 & 0 \\
\frac{1}{16} & \frac{13}{96} & \frac{107}{192} & \frac{47}{192}
\end{pmatrix}
$$

*Osservazione:* La matrice ci dice anche, ad esempio, la probabilità di essere in 3 dopo tre passi se cominciamo da un vertice a caso: essa varrà $\frac{43}{288}$ poiché
$$
\left( \frac{1}{4}, \frac{1}{4}, \frac{1}{4}, \frac{1}{4} \right)P^3 = \left( \frac{17}{192}, \frac{47}{384}, \frac{737}{1152}, \frac{42}{288} \right)
$$

# 7.2 - Classificazione degli Stati

**DEF 7.2:** Lo stato $j \in V$ è detto *accessibile* da un altro stato $i \in V$ se $\exists n \in \mathbb{N}_{0}:\ P^n_{ij} > 0$ (cioè esiste un cammino nel grafo da $i$ a $j$ di lunghezza $n$). Se due stati $i$ e $j$ sono accessibili l'uno dall'alto, diciamo che sono *comunicanti* e scriviamo $i \leftrightarrow j$.

*Osservazione:* La relazione *essere comunicanti* è una relazione di equivalente, cioè:
1. **Riflessiva:** ($i \leftrightarrow j\ \forall i \in V$)
2. **Simmetrica:** ($i \leftrightarrow j \iff j \leftrightarrow\ i\  \forall i,j \in V$)
3. **Transitiva:** ($i \leftrightarrow j$ e $j \leftrightarrow l \implies i \leftrightarrow l\ \forall i,j,l \in V$)

*Osservazione:* La relazione di comunicazione "$\leftrightarrow$" partiziona perciò $V$ in classi di equivalenza disgiunte. È possibile che la catena possa spostarsi da una classe all'altra, ma in questo caso *NON* potrà mai più tornare alla classe precedente.

**DEF 7.3:** Una catena di Markov è detta *irriducibile* se tutti gli stati di $V$ appartengono alla stessa classe d'equivalenza rispetto a "$\leftrightarrow$" (ovvero se è possibile andare in un numero finito di passi con probabilità positiva da un qualsiasi stato $i \in V$ ad un altro stato $j \in V$).

**DEF ALTERNATIVA (RIGOROSA):**
Una catena di Markov su uno spazio degli stati $V$ è **irriducibile** se per **ogni** coppia di stati $i,j \in V$ esiste (almeno) un intero $n \geq 1$ tale che
$$
\boxed{P^n_{ij} > 0}
$$

**LEMMA 7.4:** Sia $V$ finito, allora una catena di Markov su $V$ è *irriducibile* se e solo se la sua rappresentazione come grafo è un grafo *fortemente connesso (grafo orientato)*.

*Notazione:* 
$$
\boxed{r_{ij}^t = P(X_{t} = j \land X_{s} \neq j\ \forall s \in \{1, \dots, t-1\} | X_{0} = i)}
$$
- $i \neq j$: Probabilità di visitare $j$ per la prima volta al tempo $t$ (*tempo di prima visita*).
- $i = j$: Probabilità di tornare in $j$ al tempo $t$ (*tempo di primo ritorno*).

**DEF 7.4:** Uno stato $i \in V$ è detto
- *Ricorrente* se $\tilde{p} = \sum_{t\geq 1} r^t_{ii} = 1$. Ossia uno stato $i$ è ricorrente se la catena arriva in quel stato, poi ci ritorna con probabilità $1$ (e quindi ritornerà un numero infinito di volte).
- *Transiente* se $\tilde{p} = \sum_{t \geq 1} r^t_{ii} < 1$. Ossia uno stato $i$ è transiente, se non è detto che la catena ci torni. Tornerà con probabilità $\tilde{p} = \sum_{t\geq_{1}} r^t_{ii}$. Quindi con probabilità $1 - \tilde{p}$ si verificherà l'evento *non ritorno*. Per questo motivo il numero totale di ritorni successivi $N_{i}$ segue una distribuzione geometrica $Geom(1 - \tilde{p})$. $$P(N_{i} = k) = \tilde{p}^{k-1}(1-\tilde{p})$$Poiché $1- \tilde{p} > 0$, il numero di visite a uno stato transiente è **finito** con prob. 1, e il valore atteso di ritorno è: $$\mathbb{E}[N_{i}] = \frac{1}{1- \tilde{p}} < \infty$$
*Osservazione:* Se uno stato di una classe d'equivalenza rispetto a "$\leftrightarrow$" è transiente (ricorrente), allora tutti gli altri stati della classe lo saranno.

*Notazione:* Chiamiamo $h_{ij}$ il valor atteso del tempo per arrivare a $j$ partendo da $i$, cioè
$$
\boxed{h_{ij} = \sum_{t=1}^\infty t r^t_{ij}}
$$
chiamato anche *hitting time expected*. Per $j=i$ parliamo di *tempo atteso di primo ritorno* ($h_{ii}$).

*Osservazione:* Si potrebbe pensare che se $i \in V$ è uno stato ricorrente allora $h_{ii}$ dovrebbe essere finito. Ciò *NON* è sempre vero (lo è se $|V| < \infty$), ma *NON* necessariamente se $|V| = \infty$).

**DEF 7.5:** Uno stato ricorrente $i \in V$ è detto *ricorrente positivo* se $h_{ii} < \infty$. *Ricorrente nullo* se $h_{ii} = \infty$.

*Esempio: (Stato ricorrente nullo).* Sia $V = \mathbb{N} = \{1,2,3, \dots\}$ e consideriamo la catena di Markov data dalle seguenti probabilità di transizione:
$$
P_{ij} = 
\begin{cases}
\frac{i}{i+1} &\iff j = i+1 \\
\frac{1}{i+1} &\iff j = 1 \\
0 &\text{altrimenti}
\end{cases}
$$
![[esempio_stati_ricorrenti.png|500]]
La catena è irriducibile (ad ogni passo si torna in 1 con probabilità positiva e da li si può raggiungere qualsiasi altro punto con probabilità positiva in un numero finito di passi). Partendo da $1$, la probabilità che la catena non sia ritornata in 1 dopo $t$ passi è:
$$
\prod_{j=1}^t \frac{j}{j+1} = \frac{1}{t+1} \quad \text{sono sempre andato a destra}
$$
Quindi lo stato 1 è *ricorrente* (la probabilità di non tornare mai più in 1 è $\lim_{ t \to \infty } \frac{1}{t+1} = 0$).
Quindi,
$$
\begin{align}
r^t_{11} &= P(\text{non tornare in 1 per }t-1\text{ e poi torno al tempo t} | X_{0}=1)  \\
&= \frac{1}{t} \frac{1}{t+1} \quad \text{prob. di tornare indietro dopo } t-1 \text{ passi}
\end{align}
$$
Dove:
- $\frac{1}{t} = \prod_{j=1}^{t-1} \frac{j}{j+1}$, quindi sono andato avanti per $t-1$ passi.
- $\frac{1}{t+1}$: Dopo $t-1$ passi in avanti mi ritrovo nello stato $t$, quindi ho probabilità $P_{t1}$ di tornare in 1.
Infatti, $\sum_{t\geq 1} \frac{1}{t} \frac{1}{t+1} = 1$.

Dall'altra parte il numero atteso di passi per tornare in 1 è
$$
h_{11} = \sum_{t=1}^\infty r^t_{11}t = \infty
$$
Quindi, *1 è uno stato ricorrente nullo*.
*Nota:* La passeggiata aleatoria semplice è ricorrente (nulla) in dimensione 1 e 2 e diventa transiente per dimensione $\geq 3$.

**LEMMA 7.5:** Sia $V$ finito, allora
1. Almeno uno stato è ricorrente.
2. Tutti gli stati ricorrenti sono ricorrenti positivi.

**DEF 7.6:** Uno stato $j \in V$ è detto *periodico* se esiste $\Delta > 1$ intero tale che
$$
P(X_{t+s} = j | X_{t} = j) = 0
$$
a meno che $s$ sia divisibile per $\Delta$. Allora si dice che la catena di Markov è *periodica* se esiste almeno uno stato periodico. Uno stato o una catena sono detti *aperiodici* se non sono periodici.

*Esempio:* Sia $(X_{t})_{t \in \mathbb{N}_{0}}$ la passeggiata aleatoria sugli interi positivi $V = \mathbb{N}_{0}$: quando si trova in $i$, la catena si muove di un passo a destra con probabilità $\frac{1}{2}$ andando a $i+1$ o a sinistra con probabilità $\frac{1}{2}$ andando in $i-1$ (quando è in 0 va a destra con prob. 1).

![[esempio_catena_periodica.png|500]]

La catena è periodica: se parte da 0, la catena sarà sempre in stati pari in tempi pari e in stati dispari in tempi dispari. Rifacendosi alla definizione, $P(X_{t+s} = j | X_{t}=0)$ a meno che $s$ sia divisibile per $2$.

**DEF 7.7:** Uno stato aperiodico e ricorrente positivo è detto stato *ergodico*. Una catena di Markov è detta *ergodica* se tutti i suoi stati sono ergodici.

**COROLLARIO 7.6:** Ogni catena di Markov con spazio degli stati $V$ finito che sia irriducibile ed aperiodica è una catena ergodica.

**DIMOSTRAZIONE:** Una catena con $V$ finito ha almeno uno stato ricorrente dal Lemma 7.5 e se la catena è irriducibile, allora tutti gli stati sono ricorrenti. Siccome $V$ è finito, allora tutti gli stati ricorrenti sono ricorrenti positivi (Lemma 7.5). Quindi tutti gli stati sono ricorrenti positivi ed aperiodici. La catena è perciò ergodica.

# 7.3 Distribuzioni Stazionarie

**DEF 7.8:** Una distribuzione di probabiltà $\bar{\pi} = (\pi_{i})_{i \in \mathbb{N}}$ su $V$, vista come un vettore-riga, è detta *distribuzione stazionaria* se
$$
\boxed{\bar{\pi} = \bar{\pi}P}
$$

*Osservazione:* Dalla definizione notiamo quindi che se una catena di Markov raggiunge una sua distribuzione stazionaria $\bar{\pi}$, allora continuerà ad essere distribuita secondo $\bar{\pi}$ per sempre.

Il seguente fondamentale teorema ci dice che, sotto certe condizioni, una catena di Markov *converge in distribuzione* alla propria misura stazionaria (indipendentemente dal suo punto iniziale!)

**TEOREMA 7.7 (Teorema Fondamentale delle Catene di Markov)**
Sia *$V$ finito* e consideriamo una catena di Markov su $V$ che sia *irriducibile ed ergodica*. Allora
1. La catena ha un'*unica* distribuzione stazionaria $$\bar{\pi} = (\pi_{i})_{i \in V}$$
2. $\forall i,j \in V$, esiste il limite $\lim_{ t \to \infty } P^t_{ji}$ ed è *indipendente* da $j$.
3. $$\pi_{i} = \lim_{ t \to \infty } P^t_{ji} = \frac{1}{h_{ii}}$$ dove $h_{ii}$ è il *tempo atteso di primo ritorno*.

*Osservazione:* Se sto sotto le condizioni del teorema e conosco $\pi_{i}$, allora riesco a calcolare immediatamente il tempo di primo ritorno $h_{ii} = \frac{1}{\pi_{i}}$.

*Osservazione:* Se la matrice di transizione $P$ è doppiamente stocastica, allora la distribuzione uniforme è la distribuzione stazionaria per la catena.

*Osservazione:* Il teorema ci dice che, indipendentemente dalla distribuzione iniziale, la probabilità che la catena si trovi in $i \in V$ per tempi *grandi* è vicina al valore $\pi_{i}$.
Inoltre, ci dice anche che $\pi_{i}$ è l'inverso di $h_{ii} = \sum_{t \geq 1} t r^t_{ii}$, il numero atteso di passi che la catena ritorni per la prima volta in $i$ partendo da $i$. Dunque, se in media il tempo atteso di primo ritorno in $i$ è $h_{ii}$, allora ci aspettiamo di tornare in $i$ per $\frac{1}{h_{ii}}$ volte e quindi nel limite dobbiamo avere $\pi_{i} = \frac{1}{h_{ii}}$.

**DIMOSTRAZIONE:** Prendiamo per buono il seguente risultato:

**LEMMA 7.8:** Sotto le ipotesi del teorema, si ha che
$$
\lim_{ t \to \infty } P^t_{ii} = \frac{1}{h_{ii}} \quad \forall i \in V
$$
Euristicamente il lemma si spiega notando che $h_{ii}$ è il tempo medio di primo ritorno in $i$, quindi lo stato $i$ viene visitato $\frac{1}{h_{ii}}$ delle volte. Quindi $\lim_{ t \to \infty } P^t_{ii}$, che rappresenta la probabilità di trovarsi in $i$ partendo da $i$ in un tempo molto lontano nel futuro, deve essere proprio $\frac{1}{h_{ii}}$.

###### Dimostriamo la 2. (LB + UB)
Ricordiamo che 
$$
r^t_{ji} = P(\text{partendo da }j\text{, visito }i\text{ per la prima volta al tempo } t)
$$
Poiché la catena è irriducibile, si ha $\sum_{t=1}^\infty r^t_{ji} = 1$ (poichè irriducibile, ad ogni istante di tempo posso raggiungere $i$ partendo da $j$), quindi $\forall \epsilon > 0, \exists\ t_{1}(\epsilon)$ tale che 
$$
\sum_{t=1}^{t_{1}(\epsilon)} r^t_{ji} \geq 1 -\epsilon
$$
ossia, da un certo istante $t_{1}(\epsilon)$ la probabilità di arrivare in $i$ partendo da $j$ è molto grande. Inoltre, per $j \neq i$, si ha
$$
P_{ji}^t = \sum_{k=1}^t r_{ji}^k P_{ii}^{t-k}
$$
dove:
- $r_{ji}^k$: visito $i$ per la prima volta dopo $k$ passi partendo da $j$;
- $P_{ii}^{t-k}$: ritorno in $i$ dopo i successivi $t-k$ passi.

Usando che $\lim_{ t \to \infty } P_{ii}^t$ esiste (dal Lemma 7.8) e che $t_{1}$ è finito, si ha
$$
\begin{align}
\lim_{ t \to \infty } P_{ji}^t &= \lim_{ t \to \infty } \left( \sum_{k=1}^{t_{1}(\epsilon)} r_{ji}^k P_{ii}^{t-k} + \sum_{k=t_{1}(\epsilon) + 1}^{t} r^k_{ji}P_{ii}^{t-k}\right) \\
&\geq \lim_{ t \to \infty } \sum_{k=1}^{t_{1}(\epsilon)} r^k_{ji}P_{ii}^{t-k} \underbrace{=}_{\lim_{ t \to \infty }x^{t-k} = \lim_{ t \to \infty } x^t } \sum_{k=1}^{t_{1}(\epsilon)} r_{ji}^k \lim_{ t \to \infty } P_{ii}^{t}  \\
&= \lim_{ t \to \infty } P_{ii}^t \underbrace{\sum_{k=1}^{t_{1}(\epsilon)} r_{ji}^k}_{\geq 1 - \epsilon} \geq (1-\epsilon)\lim_{ t \to \infty } P_{ii}^t = (1-\epsilon) \frac{1}{h_{ii}} 
\end{align}
$$
Abbiamo quindi trovato il *lower bound*:
$$
\lim_{ t \to \infty } P_{ji}^t \geq (1-\epsilon) \frac{1}{h_{ii}}
$$
Analogamente,
$$
\begin{align}
\lim_{ t \to \infty } P^t_{ji} &= \lim_{ t \to \infty } \sum_{k=1}^{t_{1}(\epsilon)} r_{ji}^kP_{ii}^{t-k} + \underbrace{\sum_{k=t_{1}(\epsilon) + 1}^{t} r_{ji}^kP_{ii}^{t-k}}_{\leq\ \sum_{k=t_{1}(\epsilon)}^\infty r_{ji}^k \leq \epsilon } \\
&\leq \lim_{ t \to \infty } \sum_{k=1}^{t_{1}(\epsilon)} r_{ji}^tP_{ii}^{t-k} + \epsilon \leq \lim_{ t \to \infty } P_{ii}^t + \epsilon = \frac{1}{h_{ii}} + \epsilon
\end{align}
$$
Abbiamo perciò mostrato che $\forall \epsilon > 0$
$$
\frac{1-\epsilon}{h_{ii}} \leq \lim_{ t \to \infty } P_{ji}^t \leq \frac{1}{h_{ii}} + \epsilon
$$
scegliendo arbitrariamente $\epsilon$.

###### Dimostriamo la 3.
Occorre far vedere che 
$$
\pi_{i} = \lim_{ t \to \infty } P_{ji}^t = \frac{1}{h_{ii}}
$$
e in effetti è una distribuzione stazionaria. Ovviamente $\pi_{i} \geq 0\ \forall i \in V$. Inoltre
$$
\sum_{i\in V} \pi_{i} = \sum_{i\in V} \lim_{ t \to \infty } P_{ji}^t = \lim_{ t \to \infty } \underbrace{\sum_{i\in V}P_{ji}^t}_{=1} = 1
$$
Poiché $P$ è stocastica, la somma sulle righe fa 1, quindi $\bar{\pi}$ è effettivamente un vettore di probabilità (una distribuzione).
Infine, visto che $P_{ji}^{t+1}= \sum_{k \in V} P_{jk}^t P_{ki}$, prendendo il limite per $t \to \infty$ ad ambo i membri
$$
\begin{align}
&\lim_{ t \to \infty } P_{ji}^{t+1} = \lim_{ t \to \infty } \sum_{k\in V} P_{jk}^tP_{ki}\quad \forall i \\
&\iff \pi_{i} = \sum_{k\in V} (\lim_{ t \to \infty } P_{jk}^t ) P_{ki} = \sum_{k \in V} \pi_{k} P_{ki} = (\bar{\pi}P)_{i}
\end{align}
$$
Ovvero in forma matriciale $\bar{\pi} = \pi P$ che è la proprietà di stazionarità.

###### Dimostriamo la 1.
Dimostriamo ora l'unicità del limite. Supponiamo esista un'altra distribuzione strazionaria $\Phi$. Dalla definizione di stazionarità, sappiamo che
$$
\Phi = \Phi P = \Phi P P = \dots = \Phi P^t \quad t \in \mathbb{N}_{0}
$$
Scrivendo l'uguaglinza per componenti si ha
$$
\Phi_{i} = \sum_{k \in V} \Phi_{k} P_{ki}^t \quad \forall i \in V
$$
Prendendo il limite per $t \to \infty$ vediamo che
$$
\Phi_{i} = \lim_{ t \to \infty } \sum_{k \in V} \Phi_{k}P_{ki}^t = \sum_{k \in V} \Phi_{k} \underbrace{(\lim_{ t \to \infty } P_{ki}^t)}_{= \frac{1}{h_{ii}}} = \frac{1}{h_{ii}}\sum_{k \in V} \Phi_{k} = \frac{1}{h_{ii}} = \pi_{i}\ \forall i \in V
$$

**NOTE (Al Teorema 7.7) - IMPORTANTE!**
- L'enunciato richiede ergodicità ed irriducibilità, il che equivale (poiché $V$ è finito) a chiedere l'aperiodicità.
- Se $V$ è finito, una distribuzione stazionaria esiste sempre (ma magari più di una!) 
- Se la catena è *periodica* il limite $\lim_{ t \to \infty } P^t_{ji}$ *NON* esiste! Però (Se $V$ è finito e la catena è irriducibile) *esiste sempre un'unica distribuzione stazionaria $\bar{\pi}$* e si ha $$\boxed{\pi_{i} = \lim_{ t \to \infty } \frac{\#\{k \in \{1, 2, \dots, t\}: X_{k} = i\}}{t} \quad \forall i \in V}$$
- Ogni catena di Markov con spazio degli stati $V$ finito ha almeno una classe d'equivalenza (rispetto a "$\leftrightarrow$") costituita da stati tutti ricorrenti. Se la catena raggiunge una di queste classi, vi rimane per sempre. Quindi ognuna di queste classi determina una sottocatena irriducibile e con stati riccorrenti: il Teorema 7.7 si può applicare a ciascuna di queste sottocatene (se c'è aperiodicità).

**DOMANDA:** Come si può calcolare la (o le) distribuzione stazionaria di una catena di Markov.
- La via diretta è quella di risolvere il sistema di equazioni ottenuto da $$\begin{cases}
\bar{\pi} = \bar{\pi} P \\
\sum_{i\in V} \pi_{i} = 1
\end{cases}$$
- Per alcune catene è molto semplice verificare se $\bar{\pi}$ è una distribuzione stazionaria.

**DEF:** Sia $\bar{\pi}$ una distribuzione su $V$. $\bar{\pi}$ è detta *reversibile* se
$$
\pi_{i} P_{ij} = \pi_{j}P_{ji} \quad \forall\ i,j \in V
$$

**TEOREMA 7.10:** Se $\bar{\pi}$ è una distribuzione reversibile per una catena di Markov con matrice di transizione $P$, allora è anche una sua distribuzione stazionaria.

**DIMOSTRAZIONE:** Si tratta di verificare che $\bar{\pi} = \bar{\pi}P$. Si ha, componente per componente
$$
(\bar{\pi}P)_{i} = \sum_{j \in V} \pi_{j}P_{ji} \underbrace{=}_{\text{reversibilità}} \sum_{j\in V} \pi_{j}P_{ji} = \pi_{i}\sum_{j\in V}P_{ij} = \pi_{i} \quad \forall i \in V
$$

*Osservazione:* Consideriamo un cammino $x_{0}, x_{1}, \dots, x_{n} \in V$. Iterando la definizione di misura reversibile si può vedere che
$$
\underbrace{\pi_{x_{0}}P_{x_{0},x_{1}}}_{P_{x_{1}x_{0}}\pi_{x_{1}}}P_{x_{1}x_{2}} \cdots P_{x_{n-1}x_{n}} = \pi_{x_{n-1}}P_{x_{n}x_{n-1}}P_{x_{n-1}x_{n-2}} \dots P_{x_{1}, x_{0}}
$$
Quindi un interpretazione di una distribuzione reversibile è: partendo da $\bar{\pi}$, non riusciamo a distinguere se il tempo stia fluendo in avanti o all'indietro. Le catene con questa proprietà sono dette *reversibili*.

Vediamo ora l'equivalente del Teorema 7.7 quando $V$ non è finito.

**TEOREMA 7.11**
Consideriamo una catena di Markov irriducibile ed aperiodica. Allora vale una delle due seguenti affermazioni (nel caso in cui $V$ sia finito vale sicuramente la prima, se $V$ è infinito non necessariamente).
1. La catena è ergodica, $\forall\ i,j \in V$ esiste $\lim_{ n \to \infty} P_{ij}^t$ e *NON* dipende da $i$, si ha un'unica distribuzione stazionaria $$\bar{\pi} = (\pi_{j})_{j\in V},\ \forall\ i,j \quad \lim_{ t \to \infty } P_{ij}^t > 0$$
2. Non esistono stati ricorrenti positivi, $\forall\ i,j \in V$ si ha $\lim_{ t \to \infty } P_{ij}^t = 0$ e *NON* esistono distribuzioni stazionarie.

# 7.4 - Passeggiate Aletorie su Grafi Non Diretti

Sia $G=(V,E)$ un grafo finito, *NON*-diretto e connesso.

**DEF 7.9:** Una passeggiata aleatoria su $G$ è una catena di Markov rappresentata da una particella che si muove sui vertici $V$. La posizione della particella al tempo $t$ rappresenta lo stato della catena. Quando la particella è nello stato $i$ ed il vertice $i$ ha $\delta(i)$ archi che partono da esso, la particella segue l'arco $(i,j)$ con probabilità $\frac{1}{\delta(i)}$ e si trova su $j$ al passo successivo.

*Osservazione:* In principio stiamo considerando anche grafi con self loop e archi multipli (*multigrafi*).

*Osservazione:* Poiché il grafo che consideriamo è connesso, la passegiata aleatoria su $G$ è automaticamente irriducibile.

**LEMMA 7.12:** La passeggiata aleatoria su $G$ è aperiodica se e solo se $G$ *NON*  è *bipartito*.
**DIMOSTRAZIONE:** Un grafo è bipartito se e solo se *NON* ha cicli con un numero dispari di archi. In un grafo *NON*-diretto c'è sempre un ciclo di lunghezza 2 da un vertice a se stesso. Se il grafo è bipartito la passeggiata aleatoria è periodica di periodo 2. Se *NON* è bipartito allora ha sia un ciclo di lunghezza dispari che un ciclo di lunghezza 2.
$$
\implies MCD(3,2) = 1 \implies \text{ catena aperiodica}
$$

Da ora in poi assumeremo $G$ *NON* bipartito (oltre che finito, *NON*-diretto, connesso). Tale $G$ soddisfa le condizioni del Teorema 7.7 e si ha:

**TEOREMA 7.13:**
La passeggiata aleatoria su $G$ (con le caratteristiche sopra menzionate) converge alla distribuzione stazionaria $\bar{\pi}$ data da
$$
\boxed{\pi_{v} = \frac{\delta(v)}{2|E|} \quad \forall\ v \in V}
$$

*Osservazione:* Il teorema parla di convergenza. Ricordando le note al teorema 7.7, la distribuzione stazionaria esiste sempre anche se $G$ è bipartito.

**DIMOSTRAZIONE:** Poiché $\sum_{v \in V} \delta_{v} = 2|E|$, si ha immediatamente $\sum_{v \in V} \pi_{v} = \sum_{v\in V} \frac{\delta(v)}{2|E|} = 1$, cioè $\bar{\pi}$ è una distribuzione di probabilità. Sia ora $P$ la matrice di transizione della catena e chiamiamo $N(v)$ l'insieme dei vicini del vertice $v \in V$ in $G$. Allora la relazione $\bar{\pi} = \bar{\pi}P$ è equivalente
$$
\pi_{v} = \sum_{u \in N(v)} \underbrace{\frac{\delta(u)}{2|E|}}_{{\pi_{u}}} \quad \underbrace{\frac{1}{\delta(u)}}_{P_{uv}} = \underbrace{\delta(v)}_{\sum_{u \in N(v)} 1 = \delta(v)}  \frac{1}{2|E|} \quad \forall\ v\in V
$$
*Osservazione:* $\bar{\pi}$ appena descritta è anche reversibile. Infatti
$$
\pi_u P_{uv} = \frac{\delta(u)}{2\vert{}E\vert{}} \frac{1}{\delta(u)} = \frac{1}{2\vert{}E\vert{}} = \frac{\delta(v)}{2\vert{}E\vert{}} \frac{1}{\delta(v)} = \pi_v P_{vu} \quad \forall \{u,v\} \in E
$$

Ricordiamo la definizione 
$$
h_{u,v} = \mathbb{E}[\# \text{ passi per andare da $u$ a $v$}]
$$
Chiameremo $h_{u,v}$ lo *hitting time medio* da $u$ a $v$. Il *commute time medio* tra $u$ e $v$ è definito come $h_{u,v} + h_{v,u}$ (è simmetrico al contrario dell'hitting time).

**DEF 7.10:**
Il *tempo di ricoprimento* di un grafo $G = (V,E)$ è il massimo su tutti i $v \in V$ dell'aspettazione del tempo necessario per visitare tutti i nodi di $G$ partendo da $v$.

**LEMMA 7.14:**
Sia $G = (V,E)$ finito, *NON*-diretto, connesso. Se $(u,v) \in E$, il commute time $$h_{u,v} + h_{v,u} \leq 2|E|$$
**DIMOSTRAZIONE:**
Consideriamo $D$, l'insieme degli archi *diretti* ottenuti sdoppiando ogni arco *NON*-diretto di $E$ (se $(u,v) \in E$, si ottengono due archi diretti $u \to v$ e $v \to u$). Pensiamo alla passeggiata aleatoria su $G$ come ad una nuova catena di Markov con spazio degli stati $D$, sia $(Y_{t})_{t\in\mathbb{N}}$; si ha che $Y_{t} = u \to v$ se la passeggiata aleatoria originale passava da $u$ a $v$ al passo $t$-esimo. Questa catena $(Y_{t})$ ha esattamente $2|E|$ stati e si può dimostrare che  ha misura stazionaria uniforme.

Quindi, $\forall$ arco diretto $u\to v$ si ha $\pi_{u \to v} = \frac{1}{2|E|}$ e perciò 
$$h_{\{u \to v\}, \{u\to v\}} = 2|E| \text{ (tempo atteso per riattraversare l'arco $u,v$)}$$
Dalla proprietà di assenza di memoria delle catene di Markov, una volta che RW originale raggiunge $v$, possiamo *dimenticare* che lo abbia fatto attraverso l'arco $u \to v$.
Quindi il tempo atteso, partendo da $v$, per raggiungere $u$ e poi attraversare l'arco $u \to v$ raggiungendo di nuovo $v$ e limitato da sopra da $2|E|$. Siccome questa è solo uno dei possibili modi da $v$ ad $u$ e poi di nuovo a $v$, abbiamo mostrato che $h_{u,v} + h_{v,u} \leq 2|E|$.

**LEMMA 7.15:**
Il tempo di ricoprimento di $G = (V,E)$ è limitato da sopra da $2|E|(|V| - 1)$.

**DIMOSTRAZIONE:**
Scegliamo un albero di ricoprimento $T$ di $G$, ovvero un sottografo di $G$ senza cicli in cui tutti i vertici sono comunque connessi. Partendo da un qualsiasi vertice $v$, esiste un ciclo (Euleriano) su $T$ in cui ogni arco è attraversato una sola volta in ogni direzione (ciclo ottenuto attraverso una DFS).

Il massimo del tempo atteso per passare da ogni vertice del ciclo (massimo preso sul vertice iniziale) è un upper bound del tempo di ricoprimento. Sia $v_{0}, v_{1}, \dots, v_{2|V|-2}$ la sequenza di vertici del ciclo iniziato da $v_{0} = v$. Il tempo atteso per attraversare tutti i vertici in ordine sequenziale è
$$
\sum_{i=0}^{2|V| - 3} h_{v_{i}, v_{(i+1)}} = \sum_{(x,y) \in T} (h_{x,y} + h_{y,x}) \leq 2|E|(|V|-1)
$$
A parole, il commute time per ogni coppia di vertici adiacenti su $T$ è limitato da sopra da $2|E|$, e ci sono $|V|-1$ di queste coppie.

Il seguente risultato mette in relazione tempo di ricoprimento e hitting time di un grafo.

**LEMMA 7.16 (Teorema di Matthews)**
Il tempo di ricoprimento $C_{G}$ di un grafo $G=(V,E)$ con $n$ vertici è limitato da
$$
C_{G} \leq H(n-1) \max_{u,v\in V,\ u\neq v} h_{u,v}
$$








