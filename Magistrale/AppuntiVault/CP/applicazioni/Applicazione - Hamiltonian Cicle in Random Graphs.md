Ci sono diversi problemi NP-HARD che si possono trattre su grafi ed un tra questi è di trovare un ciclo Hamiltoniano (cioè un cammino chiuso senza ripetizione dei vertici). Faremo vedere che il problema diventa facile su una vasta classe di grafi. Per questo motivo introduciamo i *grafi aleatori*, in cui la presenza di un arco tra due nodi viene determinata con una certa probabilità.
Introduciamo due famosi modelli di grafi aleatori (non diretti, semplici e senza archi da un nodo a se stesso).

**DEF:** Il modello di Erdos-Renyi, indicato con $G_{n,p}\ n \in \mathbb{N}, p \in (0,1)$, è un grafo aleatorio su $n$ vertici $v_{1}, \dots, v_{n}$ in cui ognuno dei possibili $\binom{n}{2}$ archi è presente indipendentemente con probabilità $p$.

*Osservazione:* La probabilità di osservare un dato grafo con esattamente $m$ archi in $G_{n,p}$ è
$$
p^m(1-p)^{\binom{n}{2} - m}
$$
*Osservazione:* In $G_{n,p}$ ci sono in media $\binom{n}{2}p$ archi ed ogni vertice ha un grado atteso di $(n-1)p$.

**DEF:** Il modello $G_{n,N}$, con $n \in \mathbb{N}$ e $N \in \mathbb{N}$, è un grafo aleatorio su $n$ vertici $v_{1}, \dots, v_{n}$ con esattamente $N$ archi. Degli $\binom{\binom{n}{2}}{N}$ tali possibili grafi, se ne sceglie ciascuno cn uguale probabilità.

*Osservazione:* I due modelli sono strettamente legati. Infatti se condizioniamo $G_{n,p}$ ad avere $N$ archi otteniamo $G_{n,N}$.
Inoltre, se prendiamo $p = \frac{N}{\binom{n}{2}}$, il numero di archi in $G_{n,p}$ si concentra fortemente intorno ad $N$. La relazione è simile a quella tra il modello con $n$ urne ed $m$ palline e quello con le $n$ Poisson indipendenti.

Ci concentriamo ora su $G_{n,p}$ e faremo vedere che con alta probabilità è facile trovare un ciclo Hamiltoniano su tale grafo se $p$ è sufficientemente grande.

*Attenzione!* Con alta probabilità si intende *sia* la probabilità legata al modello $G_{n,p}$ di selezionare un dato grafo, *sia* all'aleatorietà introdotta dall'algoritmo che utilizzeremo.

Scordiamoci un attimo $G_{n,p}$ ed introduciamo un algoritmo per trovare cicli Hamiltoniani su un grafo dato. Ricordiamo che:

**DEF:** Un *cammino Hamiltoniano* in un grafo è un cammino che attraversa ogni vertice esattamente una volta. Un *ciclo Hamiltoniano* è un cammino Hamiltorniano chiuso.

Introduciamo un'operazione su un cammino detta *rotazione*:

**DEF:** Sia $P = v_{1}, v_{2}, \dots, v_{k}$ un cammino semplice su un grafo NON-orientato $G$ e sia $(v_{k}, v_{i})$ un arco di $G$. Allora il cammino detto *rotazione di P attraverso* **$(v_{k}, v_{i})$** è il cammino semplice
$$
P' = v_{1}, v_{2}, v_{i}, v_{k}, v_{k-1}, \dots, v_{i+2}, v_{i+1}
$$
![[rotazione.png]]

Ecco un primo algoritmo per cercare un ciclo Hamiltoniano in un grafo. L'input (il grafo) è rappresentato da $n$ liste. Ogni lista corrisponde alla lista di archi che partono da ciascuno degli $n$ vertici, ordinati in maniera casuale. 
All'inizio l'algoritmo sceglie un nodo a caso, la *testa* del cammino. Ad ogni passo l'algoritmo o aggiunge un nuovo vertice al cammino, facendolo diventare la nuova testa, o effettua una rotazione. L'algoritmo si ferma quando la lista della testa diventa vuota.

### Algoritmo per trovare un Ciclo Hamiltoniano

**Input:** Un grafo $G = (V,E)$ con $n$ nodi
**Output:** Un ciclo Hamiltoniano o fallimento.
1. Selezionare un vertice a caso, la testa del cammino.
2. Ripetere i seguenti passi fino a che l'arco della rotazione non chiude un ciclo Hamiltoniano o fino a che la lista di archi inutilizzati della testa si svuota:
	1. Sia $P = v_{1}, \dots, v_{k}$ il cammino attuale con $v_k$ la testa. Sia $(v_{k}, u)$ il primo arco della lista della testa.
	2. Cancellare $(v_{k}, u)$ dalle liste di $v_{k}$ e di $u$.
	3. Se $u \neq v_{i}$ per qualche $i = 1, 2, \dots, k-1$, aggiungere $u = v_{k+1}$ al cammino e fallo diventare la nuova testa.
	4. Se invece $\exists i \in \{ 1, \dots, k-1 \}$ tale che $u = v_{i}$, ruotare il cammino corrente $P$ attraverso $(v_{k}, v_{i})$ e porre $v_{i+1}$ come la nuova testa. (*Osservazione:* questo passo chiude un ciclo Hamiltoniano se $k = n$ e se si sceglie l'arco $(v_{n}, v_{1})$).
3. Restituire il ciclo Hamiltoniano se è stato trovato, oppure fallimento.

Questo semplice algoritmo è putroppo difficile da analizzare a causa delle dipendenze che si creano: una volta che gli degli archi sono stati esplorati, la distribuzione degli archi ancora da esplorare dipende da essi. Modifichiamo ora l'algoritmo per evitare questo problema, aggiungendo dell'aleatorietà.

*NOTA:* L'algoritmo precedente, una volta scelto l'ordine delle liste di ogni nodo e la testa iniziale, procedeva in maniera del tutto deterministica.
Il nuovo algoritmo è un po meno efficiente, ma più facile da analizzare. Ora ogni vertice $v$ avrà due liste: 
- `ARCHI-USATI(v)` che contiene archi adiacenti $v$ usati dall'algoritmo mentre $v$ era la testa 
- `ARCHI-NON-USATI(v)` contenente quelli mai ancora utilizzati

### Algoritmo modificato per trovare un Ciclo Hamiltoniano

**INPUT:** Un grafo $G = (V,E)$ con $n$ nodi.
**OUTPUT:** Un ciclo Hamiltoniano o un fallimento.
1. Selezionare un vertice a caso, la testa del cammino.
2. Ripetere i seguenti passi fino a che l'arco della rotazione non chiude un ciclo Hamiltoniano o fino a che la lista `ARCHI-NON-USATI(testa)` è vuota:
	1. Sia $P = v_{1}, \dots, v_{k}$ il cammino attuale con $v_{k}$ la testa.
	2. Eseguire $$\begin{align}
	&[i] \text{ con probabilità } \quad \frac{1}{n} \\
	&[ii] \text{ con probabilità } \quad \frac{\texttt{|ARCHI-USATI(v)|}}{n} \\
	&[iii] \text{ con probabilità } \quad 1 - \frac{1}{n} - \frac{\texttt{|ARCHI-USATI}(v_{k})|}{n}
	\end{align}$$
		- $[i]$ Invertire il cammino e rendere $v_{1}$ la nuova testa.
		- $[ii]$ Scegliere uniformemente a caso un arco della lista `ARCHI-USATI`$(v_{k})$: se l'arco è $(v_{k}, v_{i})$ per qualche $i = 1, \dots, k-1$, ruotare l'attuale cammino $P$ attraverso $(v_{k}, v_{i)}$ e rendere $v_{i+1}$ la nuova testa (altrimenti non fare nulla).
		- $[iii]$ Scegliere il primo arco della lista `ARCHI-NON-USATI`$(v_{k})$, sia $(v_{k}, u)$. Se $u \neq v_{i}\ \forall i = 1, \dots, k$, aggiungere $u = v_{k+1}$ al cammino e rendere $v_{k+1}$ la nuova testa. Se invece $\exists i:\ u = v_{i}$, ruotare il cammino corrente $P$ attraverso $(v_{k}, v_{i})$ e rendere $v_{i+1}$ la nuova testa. (*Osservazione:* questo passo chiude un ciclo Hamiltoniano e $k=n$ e se si sceglie l'arco $(v_{n}, v_{1})$)
3. Restituire il ciclo Hamiltoniano se è stato trovato, oppure fallimento.


**GOAL:** Vogliamo dimostrare che questo algoritmo trova un ciclo Hamiltoniano in un grafo campionato secondo il modello Erdos-Renyi $G_{n,p}$ quando $p$ è sufficientemente grande con alta probabilità.
Prima di trattare $G_{n,p}$ analizziamo l'algoritmo assumendo una particolare distribuzione iniziale degli `ARCHI-NON-USATI`.

Assumiamo che $\forall v$, ciascuno dei prossibili $n-1$ archi che connettono $v$ ad un altro vertice sia nella lista `ARCHI-NON-USATI(v)` all'inizio con probabilità $q \in (0,1)$. Assumiamo inoltre che in ogni lista l'ordine sia casuale.

*Osservazione:* In questo modello, se $v$ è la testa e l'arco $(u,v)$ viene selezionato per la prima volta, allora $(u,v)$ viene rimosso da `ARCHI-NON-USATI(v)` ma NON da `ARCHI-NON-USATI(u)` (se era anche li presente).

*NOTA:* Cosa abbiamo guadagnato aggiungendo aleatorietà nel passo 2. dell'algoritmo? Faremo vedere che in questo modo ad ogni passo la nuova testa del cammino sarà scelta in maniera uniforme tra gli $n$ vertici, facilitando moltissimo l'analisi dell'algoritmo (che si riduce sostanzialmente ad un problema di collezionatore di figurine).

**LEMMA 5.16:**
Utilizzando l'algoritmo modificato su questo nuovo modello si verifica la cosa seguente: Sia $V_{t}$ la testa del camino al $t$-esimo passo dell'algoritmo. Allora, per ogni vertice $u$, se al $t$-esimo passo `ARCHI-NON-USATI`$(V_{t})$ è NON vuoto, si ha che
$$
P(V_{t+1} = u \Big| V_{t} = u_{t}, V_{t-1} = u_{t-1}, \dots, V_{0} = u_{0}) = \frac{1}{n}
$$
Cioè, la testa del cammino può essere considerata come presa a caso ad ogni passo, indipendentemente da quanto successo fino a quel punto.
**DIMOSTRAZIONE:**
Consideriamo tutte le possibilità se $P = v_{1}, v_{2}, \dots, v_{k}$.
- $P(V_{t+1} = v_{1} \Big| \text{ al tempo } t \text{ ho } P) = \frac{1}{n}$, poiché l'unico modo in cui $v_{1}$ possa diventare la nuova testa è che il cammino $P$ venga invertito (caso $(b)[i]$)
- Per ogni $i = 1, \dots, k-1$ $$\begin{align}
&P(V_{t+1} = v_{i+1} \Big| \text{ al tempo } t \text{ ho } P) = \\
&= P(V_{t+1} = v_{i+1} \cap (v_{k}, v_{i}) \in \texttt{ARCHI-USATI}(v_{k}) \Big| \text{ al tempo } t \text{ ho } P)  \\
&+ P(V_{t+1} = v_{t+1} \cap (v_{k}, v_{i}) \not\in \texttt{ARCHI-USATI}(v_{k}) \Big | \text{ al tempo } t \text{ ho } P)
\end{align}
$$La prima delle probabilità vale (caso $(b)[ii]$) $$\frac{|\texttt{ARCHI-USATI}(v_{k})|}{n} \cdot \frac{1}{|\texttt{ARCHI-USATI}(v_{k})|} = \frac{1}{n}$$moltiplicato per la probabilità che $(v_{k}, v_{i}) \in \texttt{ARCHI-USATI}(v_{k})$. La seconda probabilità vale (caso $(b)[iii]$) $$\left(1 - \frac{1}{n} - \frac{|\texttt{ARCHI-USATI}(v_{k})|}{n}\right)\left( \frac{1}{n - |\texttt{ARCHI-USATI}(v_{k})| - 1} \right) = \frac{1}{n}$$moltiplicata per la probabilità che $(v_{k}, v_{i}) \notin \texttt{ARCHI-USATI}(v_{k})$. La prima parentesi è la probabilità che l'algoritmo decida di fare $[iii]$. La seconda parentesi viene da fatto che gli archi in $\texttt{ARCHI-USATI}(v_{k})$ sono stati scelti indipendentemente dalle liste degli altri vertici e sono stati messi in ordine casuale: possiamo pensare che ogni volta che l'algoritmo sceglie $[iii]$ un nuovo arco della lista $\texttt{ARCHI-NON-USATI}(v_{k})$ viene *rivelato* (nel senso che la lista NON era conosciuta a priori), e siccome ogni arco $(v_{k}, v)$ che non è stato usato fino a quel momento ha uguale probabilità di essere in cima alla lista $\texttt{ARCHI-NON-USATI}(v_{k})$ tra gli $n - |\texttt{ARCHI-USATI}(v_{k})| - 1$ disponibili, si ha che la probabilità che esso venga scelto è proprio $$\frac{1}{n - |\texttt{ARCHI-USATI}(v_{k})| - 1}$$Abbiamo quindi, $\forall i=1, \dots k-1$ $$P(V_{t+1} = v_{t+1} \Big | \text{ al tempo } t \text{ ho } P) = \frac{1}{n}$$
- Infine, se $\not\exists i:\ u = v_{i}$ si ha $$P(V_{t+1} = u \Big | \text{ al tempo } t \text{ ho } P ) = \frac{1}{n}$$poiché questa è la probabilità che $(v_{k}, u)$ venga *rivelato* come prossimo elemento della lista $\texttt{ARCHI-NON-USATI}(v_{k})$, e si ragiona come prima.

*NOTA:*  Grazie a questo Lemma abbiamo ridotto il problema ad uno del tipo *urne e palline* o *collezionatore di figurine*. Infatti, quando il cammino è lungo $n-k$, la probabilità di allungarlo di un vertice è $\frac{k}{n}$, cioè la probabilità che l'algoritmo scelga uno dei $k$ vertici rimanenti. Una volta che il cammino è lungo $n$, la probabilità di chiuderlo in un ciclo Hamiltoniano è $\frac{1}{n}$. Perciò avremo bisogno di:
- $O(n \log n)$ passi per formare un cammino Hamiltoniano.
- $O(n \log n)$ ulteriori passi (rotazioni) per chiuderlo in un ciclo Hamiltoniano (fermo restando che la lista $\texttt{ARCHI-NON-USATI}$(testa) non si sia mai svuotata).

**TEOREMA 5.17:**
Supponiamo di avere come input dell'algoritmo modificato per trovare un ciclo Hamiltoniano liste di $\texttt{ARCHI-NON-USATI}$ in cui ogni arco $(u,v)$ con $u \neq v$, si trova in $\texttt{ARCHI-NON-USATI}(v)$ indipendentemente con probabilità $q \geq 20 \frac{\log n}{n}$. Allora l'algoritmo trova un ciclo Hamiltoniano in $O(n \log n)$ passi con probabilità $1 - O\left( \frac{1}{n} \right)$.
**DIMOSTRAZIONE:**
Consideriamo i due venti
$$
\begin{align}
\mathcal{E}_{1} = &\text{ In } 3n\log n \text{ passi nessuna lista di} \texttt{ ARCHI-NON-USATI }  \\
&\text{ si svuota e l'algoritmo trova un ciclo Hamiltoniano} \\ \\
\mathcal{E}_{2} = &\text{ Almeno una lista di} \texttt{ ARCHI-NON-USATI } \text{si svuota in } 3n\log n \text{ passi}
\end{align}
$$
Si ha che l'algoritmo fallisce $\iff$ $\mathcal{E}_{1} \lor \mathcal{E}_{2}$ si realizzano. Ci basta far vedere che sia $\mathcal{E}_{1}$ che $\mathcal{E}_{2}$ hanno probabilità bassa.
- $\mathcal{E}_{1}:$ Dal Lemma 5.16 sappiamo che se le liste di $\texttt{ARCHI-NON-USATI}$ NON sono vuote, ad ogni passo l'algoritmo sceglie una nuova testa in modo uniforme tra gli $n$ vertici. Condizionatamente a liste NON vuote si ha allora $$\begin{align}
&P(\text{ In } 2n\log n \text{ passi NON trovo un cammino Hamiltoniano}) \\
&=P(\text{ collezionare figurine necessita più di } 2n\log n  \\
&\qquad \text{pacchetti per trovare le } n \text{ figurine diverse}) \\
&\leq \sum_{i=1}^{n} P(i-\text{esima figurina NON-trovata in } 2n\log n \text{ pacchetti}) \\
&\leq \sum_{i=1}^n \left( 1 - \frac{1}{n} \right)^{2n\log n} \leq n \cdot \exp\left( -\frac{1}{n}(2n\log n) \right) = \frac{1}{n}
\end{align}$$Una volta ottenuto un cammino Hamiltoniano, la probabilità di non chiuderlo in un ciclo in ulteriori $n\log n$ passi è $$\left( 1 - \frac{1}{n} \right)^{n\log n} \leq \frac{1}{n}$$Abbiamo quindi mostrato che $$P(\mathcal{E}_{1}) \leq \frac{2}{n}$$
- $\mathcal{E}_{2}$: Si ha $$P(\mathcal{E}_{2}) \leq P(\mathcal{E}_{2a}) + P(\mathcal{E}_{2b})$$ dove $$\begin{align}
\mathcal{E_{2a}} &= \text{ In } 3n\log n \text{ passi almeno } 9\log n \text{ archi sono stati rimossi da } \\
&\qquad \texttt{ARCHI-NON-USATI}(v) \text{ per qualche } v  \\ \\
\mathcal{E}_{2b} &= \exists v: |\texttt{ARCHI-NON-USATI}(v)| \leq 10\log n \text{ all'inizio}
\end{align}$$Per $\mathcal{E}_{2a}$ notiamo che il vertice $v$ deve essere stato selezionato come testa $9\log n$ volte nei primi $3n\log n$ passi. Se $$X = \# \text{ volte che } v \text{ viene selezionato come testa nei primi } 3n\log n \text{ passi}$$si ha che $X \sim Bin\left( 3n\log n, \frac{1}{n} \right)$ dal Lemma 5.16. Usando un CB ( Teo. 4.4, 1. con $\delta = 2,\ \mu = 3\log n$) $$P(X \geq 9 \log n) \leq \left( \frac{e^2}{27} \right)^{3\log n} \leq \frac{1}{n^2}$$Allora, prendendo uno Union Bound, si ha che $$P(\mathcal{E}_{2a}) \leq \sum_{v} P(X \geq 9 \log n) \leq \frac{1}{n}$$Per quanto riguarda $\mathcal{E}_{2b}$, sia $Y = |\texttt{ARCHI-NON-USATI}(v)|$ all'inizio. $$\mathbb{E}[Y] = q(n-1) \geq \frac{20 \log n}{n}(n-1) \geq 19 \log n$$Per CB (Teo. 4.5, 2.) $$P(Y \leq 10 \log n) \leq \exp\left( (19\log n )\left( \frac{9}{19} \right)^2 \frac{1}{2} \right) \leq \frac{1}{n^2}$$Di nuovo con uno Union Bound $$P(\mathcal{E}_{2b}) \leq \frac{1}{n}$$Mettendo insieme le due disuguaglianze abbiamo ottenuto $$P(\mathcal{E}_2) \leq P(\mathcal{E}_{2a}) + P(\mathcal{E}_{2b}) \leq \frac{2}{n}$$
Concludiamo quindi che la probabilità che l'algoritmo NON trovi un ciclo Hamiltoniano in $3n\log n$ passi è $\leq P(\mathcal{E}_{1}) + P(\mathcal{E}_{2}) \leq \frac{4}{n}$.

Rircordiamo che il nostro obiettivo era quello di provare lo stesso teorema ma per il modello di Erdos-Renyi.

**COROLLARIO 5.18:**
L'algoritmo modificato per trovare un ciclo Hamiltoniano con in input un grafo campionato con il modello di Erdos-Renyi $G_{n,p}$ con $p \geq \frac{40\log n}{n}$ trova un cilo Hamiltoniano con probabilità $1 - O\left( \frac{1}{n} \right)$.
**DIMOSTRAZIONE:**
Partizioniamo gli archi di $G_{n,p}$ nel modo seguente. Sia $q \in [0,1]$ tale che $p = 2q - q^2$. Consideriamo un qualsiasi arco $(u,v)$ dal grafo in input. Allora
- Con probabilità $\frac{q(1-q)}{2q - q^2}$ mettiamo $(u,v)$ in $\texttt{ARCHI-NON-USATI}(u)$ ma non in $\texttt{ARCHI-NON-USATI}(v)$.
- Con probabilità $\frac{q(1-q)}{2q - q^2}$ facciamo il contrario.
- Con probabilità rimanente $\frac{q^2}{2q - q^2}$ mettiamo $(u,v)$ in entrambe le liste.
Notiamo che $\forall (u,v)$
$$
\begin{align}
P((u,v) \in \texttt{ARCHI-NON-USATI}(v) \text{ all'inizio}) &= p\left( \frac{q(1-q)}{2q-q^2} + \frac{q^2}{2q-q^2} \right)  \\
&= q
\end{align}
$$
e che
$$
\begin{align}
P((u,v) \in \texttt{ARCHI-NON-USATI}(v) \cap \texttt{ARCHI-NON-USATI}(u) \text{ all'inizio})  \\
= p\left( \frac{q^2}{2q-q^2} \right) = q^2
\end{align}
$$

Quindi questi due eventi sono indipendenti. Poichè ogni $(u,v)$ è trattato in maniera indipendente, questo partizionamento soddisfa le ipotesi del Teorema 5.17 se $q \geq \frac{20\log n}{n}$. Ma poiché $p \geq \frac{40 \log n}{n}$ abbiamo in effetti
$$
q \geq \frac{p}{2} \geq \frac{20\log n}{n}
$$