1## Modello Asincrono

Nel modello asincrono non abbiamo un *clock globale* e non abbiamo un *bound* sul tempo che impiega un messaggio inviato da un nodo a raggiungere la destinazione.
Un *protocollo* nel modello asincrono è *event driven*, cioè specifica cosa fa un nodo nel momento in cui riceve un messaggio: il nodo può eseguire un numero arbitrario di operazioni locali, cambiare *stato* (lo *stato* di un nodo è costituito dai valori delle sue variabili locali, che possono dipendere dall'input e da tutti i messaggi ricevuti).

**DEF:** Una *configurazione* $C$ è una coppia $C = (S, M)$ dove 
- $S = \{s_{1}, s_{2}, \dots, s_{n}\}$ è il vettore degli stati locali dei nodi
- $M$ è la *message pool*, l'insieme dei messaggi non ancora consegnati.

**DEF:** Un *messaggio* $m$ è una coppia $m = (p, x)$ dove $p$ è il nodo destinatario del messaggio e $x$ è il contenuto del messaggio.

Se $\Pi$ è un protocollo deterministico nel modello asincrono, data una configurazione $C = (S, M)$ e un messaggio $m = (p,x)$, indichiamo con $m(C)$ la configurazione $C' = (S', M')$ che si ottiene in base al protocollo quando il messaggio $m$ viene consegnato.
L'insieme $S'$ è quello che si ottiene da $S$ aggiornando lo stato del nodo $p$ dopo l'elaborazione delle informazioni ottenute in $x$ e $M'$ è la *message pool* che si ottiene da $M$ togliendo il messaggio appena consegnato $m$ e aggiungendo tutti i messaggi inviati da $p$ a seguito della ricezione del messaggio $m$.

Formalmente, sia $C=(S, M)$ la configurazione attuale e sia $m = (p,x) \in M$ il messaggio ancora da consegnare. Quando $m$ è consegnato al nodo $p$, esso fa partire la propria funzione di transizione deterministica locale in base al suo stato corrente $s_p$ e al messaggio $x$.
- Il nuovo stato locale del nodo $p$ diventa $s_{p}'= \delta(s_{p}, x)$ mentre lo stato di tutti gli altri nodi $q \neq p$ rimane invariato.
- Il nodo $p$ genera un insieme (eventualmente vuoto) di nuovi messaggi di uscita $M_{out}(p, s_{p}, x)$.
La nuova configurazione $C'=(S', M')$ è definita da:
$$
\begin{align}
S' &= (S  \setminus \{s_{p}\}) \cup \{ s'_{p} \} \\
M' &= (M \setminus \{ m \}) \cup M_{out}(p, s_{p}, x)
\end{align}
$$

*NOTA:* Inizializzazione: $M = \{ (p_{w}, \emptyset),\ w \in [n] \}$

**Osservazione:** 
Osservare che, dato un protocollo deterministico $\Pi$, una configurazione $C = (S, M)$ e due messaggi $m_{1} = (p_{1}, x_{1})$,  $m_{2} = (p_{2}, x_{2}) \in M$,  
$$\text{se } p_{1} \neq p_{2} \implies m_{2}(m_{1}(C)) = m_{1}(m_{2}(C))$$

**Proof:** In un sistema a passaggio di messaggi, i nodi non condividono memoria: lo stato interno di ciascun nodo è accessibile e modificabile unicamente dal nodo stesso al momento della ricezione di un messaggio a lui indirizzato.

Di conseguenza:
- La ricezione di $m_1$ cambia **esclusivamente** lo stato locale di $p_1$ e aggiunge al pool i messaggi che $p_1$ decide di trasmettere.
- Lo stato di $p_2$ resta del tutto invariato, quindi quando $p_2$ riceve $m_2$ (prima o dopo $m_1$), parte dallo stesso identico stato locale ed esegue la medesima transizione deterministica, generando gli stessi identici messaggi in uscita.
- Nel _message pool_, l'effetto netto è semplicemente la rimozione di entrambi i messaggi $\{m_1, m_2\}$ e l'aggiunta di tutti i messaggi generati da entrambi i nodi, operazione che è commutativa per le proprietà dell'unione insiemistica.

Formalmente:
Calcoliamo $C_A = m_2(m_1(C))$. Viene consegnato il messaggio $m_{1}$ su $C$, quindi
- Lo stato di $p_1$ si aggiorna a $s'_{p_1} = \delta(s_{p_1}, x_1)$.      
- Poiché $p_2 \neq p_1$, lo stato del nodo $p_2$ *non cambia*: $s_{p_2}$ resta inalterato. 
- Il pool dei messaggi diventa:    $$M_1 = (M \setminus \{m_1\}) \cup M_{out}(p_1, s_{p_1}, x_1)$$Poiché $m_1 \neq m_2$, abbiamo ancora che $m_2 \in M_1$.
A questo punto viene consegnato $m_{2}$ su $m_{1}(C)$, quindi    
- Poiché lo stato di $p_2$ era ancora quello iniziale $s_{p_2}$, il suo stato si aggiorna a:  $s'_{p_2} = \delta(s_{p_2}, x_2)$
- Il nuovo insieme di stati locali è: $$S_A = (S \setminus \{s_{p_1}, s_{p_2}\}) \cup \{s'_{p_1}, s'_{p_2}\}$$
- I messaggi inviati da $p_2$ dipendono unicamente da $(s_{p_2}, x_2)$, quindi sono esattamente $M_{out}(p_2, s_{p_2}, x_2)$. 
Il pool finale dei messaggi è: 
$$
\begin{align}
M_A &= (M_1 \setminus \{m_2\}) \cup M_{out}(p_2, s_{p_2}, x_2)  \\
&= (M \setminus \{m_1, m_2\}) \cup M_{out}(p_1, s_{p_1}, x_1) \cup M_{out}(p_2, s_{p_2}, x_2)
\end{align}
$$
Analogamente possiamo calcolare $C_{B} = m_{1}(m_{2}(C))$ ottenendo
$$
\begin{gather*}
S_{A} = S_{B} \qquad \text{e} \qquad M_{A} = M_{B} \\
\Downarrow \\
C_{A} = C_{B}
\end{gather*}
$$

**DEF:** Uno schedule $\sigma$ è una sequenza ordinata di messaggi 
$$
\sigma = ((p_{1}, x_{1}), \dots, (p_{k}, x_{k}))
$$
Diciamo che uno schedule $\sigma$ è *applicabile*  a una configurazione $C$ se $m_{1} \in M$ e se per ogni $i = 2, \dots, k$, il messaggio $m_i$ appartiene alla *message pool* della configurazione $\sigma_{[1: i-1]}(C)$, dove con $\sigma_{[1, i-1]}$ intendiamo lo *schedule* formato dai primi $i-1$ messaggi dello *schedule* $\sigma$.
$$
\sigma_{[1: i-1]}(C) = C_{i} = (S_{i}, M_{i}) = m_{i-1}(m_{i-2}(\dots m_{1}(C) \dots))
$$
Ossia $m_i$ deve appartenere al message pool della configurazione $C_i$ risultante dalla consegna ordinata dei messaggi precedenti.

Ad esempio $m_{2}$ è applicabile o perché è un messaggio generato da $m_{1}(C)$ oppure stava già in transito ed è diventato disponibile subito dopo la consegna di $m_{1}$.

Dato un protocollo $\Pi$, una configurazione $C$ e uno schedule $\sigma$, indichiamo con $\sigma(C)$ la configurazione che si ottiene partendo da $C$ in base al protocollo $\Pi$ dopo la consegna di tutti i messaggi in $\sigma$ (nell'ordine stabilito della sequenza.)

**Osservazione:**
Osservare che, dato un protocollo deterministico $\Pi$, una configurazione $C = (S, M)$ e due schedule $\sigma_{1} = (p_{1}, x_{1}), \dots , (p_{k}, x_{k})$ e$\sigma_{2} = (q_{1}, y_{1}), \dots , (q_{h}, y_{h})$ applicabili a C, se gli insiemi di nodi destinatari nei due schedule sono disgiunti, $\{p_{1}, \dots , p_{k}\} \cap \{q_{1}, \dots, q_{h}\} = \emptyset$, allora $\sigma_{2}(\sigma_{1}(C)) = \sigma_{1}(\sigma_{2}(C))$.

## Byzantine Agreement

Nel problema del Byzantine Agreement abbiamo $n$ nodi di cui $f$ corrotti. A ogni nodi $u$ viene affidato in input un messaggio $b_u$. Vogliamo progettare un protocollo, che termini in un tempo finito, in cui ogni nodo onesto $i$ dia in output un valore $y_{i}$ tale che:
- *Consistency:* Se $i$ e $j$ sono due nodi onesti, allora $y_{i} = y_{j}$;
- *Validity*: Se tutti i nodi onesti hanno in input lo stesso bit $b$, allora $y_{i} = b$ per ogni nodo onesto $i$.

TODO: da fare gli esercizi 1,2,3

## Teorema Impossibilità

**TEOREMA - FLP Impossibility:** Nel modello asincrono nessun protocollo deterministico per Byzantine Agreement che termina in un tempo finito può soddisfare consistency e validity, se c'è almeno un nodo corrotto.

**DEF:** Dato $\Pi_{BA}$ un protocollo per Byzantine Agreement che soddisfa validity e consistency e un configurazione $C = (S, M)$, diremo che $C$ è:
- *0-VALENTE* per $\Pi_{BA}$ se, qualunque cosa faccia l'avversario, a partire dalla configurazione $C$ il protocollo fa in modo che tutti i nodi onesti danno in output 0.
- *1-VALENTE* per $\Pi_{BA}$ se, qualunque cosa faccia l'avversario, a partire dalla configurazione $C$ il protocollo fa in modo in modo che tutti i nodi onesti danno in output 1.
- *BI-VALENTE* per $\Pi_{BA}$ se sistono due strategie diverse dell'avversario (due diversi schedule $\sigma_0$ e $\sigma_1$) tali che in una esecuzione tutti i nodi onesti decidono $0$, mentre nell'altra tutti i nodi onesti decidono $1$.
Formalmente, sia $V(C)$ l'insieme dei valori $v \in \{0, 1\}$ tali che esiste almeno una configurazione decidibile raggiungibile da $C$ in cui i nodi onesti decidono $v$.
- Se $V(C) = \{0\}$, allora $\vert{}V\vert{} = 1$ ed è *0-valente.
- Se $V(C) = \{1\}$, allora $\vert{}V\vert{} = 1$ ed è *1-valente*.
- Se $V(C) = \{0, 1\}$, allora $\vert{}V\vert{} = 2$ ed è *bivalente*.

*Sketch of Proof:* La dimostrazione procede dimostrando che se $\Pi$ è un protocollo deterministico per Byzantine Agreement che soddisfa validity e consistency allora esiste una strategia dell'avversario che fa in modo che il protocollo non termini mai.
Informalmente, la dimostrazione procede come segue:
1. Si dimostra che esiste un'assegnazione degli input ai nodi tale che la configurazione iniziale $C_{0}$ è bivalente;
2. Si dimostra che se $C$ è una configurazione bivalente, allora l'avversario può fare in modo che, partendo da $C$, il protocollo raggiunga una nuova configurazione bivalente $C'$.

Dai punti 1 e 2 segue che l’avversario può fare in modo che il protocollo $\Pi_{BA}$ non termini mai, dimostrando quindi il teorema.

**Lemma 1:** Se $\Pi_{BA}$ è un protocollo deterministico per Byzantine Agreement che termina e soddisfa validity e consistency allora esiste un’assegnazione degli input ai nodi tale che la configurazione
iniziale è bivalente.

**Proof:** Per $i = 0,1, \dots, n$, sia $X_{i}$ la configurazione iniziale in cui gli input dei nodi minori o uguali a $i$ sono $1$ e gli input dei nodi maggiori sono $0$.
$$
\begin{align}
X_{0} &= [0, 0, 0, \dots, 0] \qquad \text{0-valente} \\
X_{1} &= [1, 0, 0, \dots, 0] \\
X_{2} &= [1, 1, 0, \dots, 0]  \\
&\vdots \\
X_{i-1} &= [1, \dots, 1, 0, \dots, 0] \qquad \text{0-valente} \\
X_{i} &= [1, \dots, 1, 1, 0, \dots, 0] \qquad \text{?-valente} \\
&\vdots \\
X_{n-1} &= [1, 1, 1, \dots, 1, 0] \\
X_{n} &= [1, 1, 1, \dots, 1] \qquad \text{1-valente} \\
\end{align}
$$
Siccome per ipotesi $\Pi_{{BA}}$ soddisfa validity la configurazione $X_{0}$ (in cui tutti gli input sono 0) deve essere 0-valente e la configurazione
$X_{n}$ (in cui tutti gli input sono 1) deve essere 1-valente.

Sia $i$ il più piccolo indice tale che $X_{i-1}$ è 0-valente e $X_{i}$ non è 0-valente.

*GOAL:* Vogliamo dimostrare che $X_i$ non è 1-valente, e di conseguenza è bi-valente.

Osserviamo che tra $X_{i-1}$ e $X_{i}$ cambia l'input di un solo nodo: il nodo $i$ (che in $X_{i-1}$ riceve 0 e in $X_{i}$ riceve 1). Tutti gli altri $n-1$ nodi hanno lo stesso input in entrambe le configurazioni.

Poiché per ipotesi il protocollo $\Pi_{BA}$ termina in tempo finito anche in presenza di un nodo corrotto ($f \geq 1$), deve funzionare anche se il nodo $i$ smette di funzionare o non risponde a nessun messaggio.

Formalmente: a partire da $X_{i-1}$, deve esistere uno schedule $\sigma$ tale che:
1. Non consegna nessun messaggio al nodo $i$;
2. Porta tutti gli altri $n-1$ nodi a decidere in tempo finito.
 Se uno schedule del genere non esistesse, l' avversario potrebbe semplicemente bloccare il nodo $i$, e gli altri nodi rimarebbero bloccati all'infinito senza mai terminare (quindi questo schedule deve esistere dato che $\Pi_{BA}$ termina in tempo finito).

Applicando ora questo schedule $\sigma$ su $X_{i-1}$ e $X_{i}$ osserviamo che:
- $\sigma(X_{i-1})$: poiché $X_{i-1}$ è 0-valente per definizione, applicando $\sigma$ a tutti i nodi diversi da $i$ devono per forza dare in output 0.
- $\sigma(X_{i})$: poichè $\sigma$ non consegna nessun messaggio al nodo $i$, il nodo $i$ non esegue nessuna operazione e non invia alcun messaggio a nessuno. Gli $n-1$ nodi diversi da $i$ hanno lo stesso input che avevano in $X_{i-1}$, di conseguenza, per tutti i nodi diversi da $i$, l'esecuzione è *identica e indistinguibile* rispetto a quella partita da $X_{i-1}$. Dunque, anche partendo da $X_{i}$ e applicando lo schedule $\sigma$ tutti i nodi decidono 0.

Abbiamo quindi trovato uno schedule valido $\sigma$ che applicato a $X_{i}$ porta tutti i nodi a decidere 0 anche se $X_{i}$ non è 0-valente. Ovviamente $X_{i}$ non può essere neanche 1-valente quindi in conclusione $X_{i}$ deve essere *bi-valente*.

**Lemma 2:** Se $\Pi_{BA}$ è un protocollo deterministico per Byzantine Agreement che termina e soddisfa validity e consistency, $C = (S, M)$ è una configurazione bi-valente per $\Pi_{BA}$ e $m = (p, x)$ è un messaggio in $M$, allora esiste uno schedule $\sigma = (m_{1} = (p_{1}, x_{1}), \dots , m_{k} = (p_{k}, x_{k}))$ applicabile a $C$ tale che
1. $m_k = m$;
2. $\sigma(C)$ è una configurazione bi-valente per $\Pi_{BA}$.

**Proof:** Se $m(C)$ è bi-valente, il lemma è dimostrato in quanto basta porre $\sigma = m(C)$.

Altrimenti $m(C)$ è 0-valente o 1-valente. Supponiamo senza perdità di generalità che $m(C)$ sia 0-valente; il caso in cui $m(C)$ è 1-valente è speculare.

**DEF:** Data una configurazione bi-valente $\hat{C}$ per $\Pi_{BA}$ diciamo che $\hat{C}$ è:
- di tipo $0^*$ per il nostro messaggio $m$ se $m(\hat{C})$ è 0-valente;
- di tipo $1^*$ per il nostro messaggio $m$ se $m(\hat{C})$ è 1-valente;
$$
\begin{align}
\underbrace{C}_{0^*} \longrightarrow \underbrace{m(C)}_{0-\text{valente}} \\
\underbrace{C}_{1^*} \longrightarrow \underbrace{m(C)}_{1-\text{valente}}
\end{align}
$$

Siccome ci siamo posti, senza perdità di generalità, nel caso in cui $m(C)$ è 0-valente, con la definizione appena data, possiamo dire che $C$ è una configurazione bi-valente di tipo $0^*$.

**Esistenza di una configurazione non $0^*$:**
Consideriamo ora tutte le configurazioni raggiungibili da $C$ mediante schedule che **non contengono mai il messaggio $m$**. Tra questa configurazioni raggiungibili senza mai consegnare $m$, **deve esistere almeno una configurazione che non è di tipo $0^*$**.
- *Perché?* Se tutte le configurazioni raggiungibili da $C$ senza consegnare $m$ fossero di tipo $0^*$, allora qualunque esecuzione da $C$ (in cui $m$ viene eventualemente consegnato) porterebbe invariabilmente alla decisione 0. Ma questo significherebbe che $C$ stessa è 0-valente, contraddicendo l'ipotesi che $C$ è bi-valente.
Dunque lungo il cammino esiste un punto in cui si passa da uno stato $0^*$ a uno non-$0^*$.
- Sia $X$ l'ultima configurazione di tipo $0^*$.
- Sia $Y$ la prima configurazione **non $0^*$** raggiungible applicando a $C$ uno schedule che non contiene il messaggio $m$.
- Sia $m' = (p', x')$ il messaggio che fa compiere il passo da $X$ a $Y$, cioè $Y = m'(X)$

![[flp1.png]]

Il nostro messaggio $m = (p, x)$ è applicabile alla configurazione Y , perché stava nella message pool della configurazione C e non è mai stato consegnato, quindi sta anche nella message pool di $Y$ . 
Sia allora $Z = m(Y)$ la configurazione che si ottiene applicando $m$ a $Y$.
$$Z = m(Y) = m(m'(X))$$
L'obiettivo diventa dimostrare che **$Z$ è bivalente**.

**$Z$ non può essere 0-valente.** Per definizione, $Y$ non è di tipo $0^*$, di conseguenza la configurazione ottenuta applicando $m$ a $Y$ non può essere 0-valente.

**I destinatari coincidono $p = p'$.**
Ricordiamo che dato un protocollo deterministico $\Pi$ e data una configurazione $C = (S, M)$ e due messaggi $m_{1} = (p_{1}, x_{1})$,  $m_{2} = (p_{2}, x_{2}) \in M$,  se $\boxed{p_{1} \neq p_{2}}$ allora $m_{2}(m_{1}(C)) = m_{1}(m_{2}(C))$.

$$
\begin{gather*}
Y = m'(X) \qquad \land \qquad Z = m(Y) \\
\Downarrow \\
Z = m(m'(X)) \underbrace{\equiv}_{p \neq p'} Z = m'(m(X))
\end{gather*}
$$
Ma questo implicherebbe che $m(X)$ è 0-valente in quanto $X$ è di tipo $0^*$, il che implicherebbe che $Z$ è 0-valente, ma questo è un assurdo per quanto detto prima.
Quindi $\boxed{p' = p}$.

**Schedule $\sigma$ con nodo $p$ non funzionante.**
Dato che il protocollo $\Pi_{BA}$ *termina* in tempo finito anche con un nodo corrotto/guasto ($f \ge 1$), deve poter terminare anche nel caso in cui il nodo $p$ smetta di rispondere.

Esiste quindi uno schedule $\sigma$ applicabile a $X$ tale che:
1. Non consegna alcun messaggio al nodo $p$.
2. Porta tutti gli altri $n-1$ nodi a decidere il valore di output, raggiungendo una configurazione $X' = \sigma(X)$.
Infatti, se un tale schedule non ci fosse, nel caso in cui $p$ è un nodo corrotto che non fa nulla ogni volta che riceve un messaggio, nessuno schedule consentirebbe agli altri $n − 1$ nodi di terminare.

Lo schedule $\sigma$ non contiene messaggi per il nodo $p$, quindi è applicabile anche alla configurazione $m(X)$ e, poichè $p' = p$, anche alla configurazione $Z$:

![[flp2.png]]

- *Applicato a $m(X)$:* $$\sigma(m(X)) = m(\sigma(X)) = m(X')$$Ma poiché $X$ è $0^*$, $m(X)$ è 0-valente, la decisione presa quindi dai nodi in $X'$ deve essere per forza 0.
- *Applicato a $Z$:* $$\sigma(Z) = \sigma(m(m'(X))) = m(m'(\sigma(X))) = m(m'(X'))$$Tuttavia, nella configurazione $X'$ tutti i nodi diversi da $p$ hanno già deciso 0. L'arrivo successivo di $m'$ e $m$ al solo nodo $p$ non può alterare la decisione già assunta dal resto dei nodi.

In conclusione abbiamo esibito uno schedule valido $\sigma$ che, applicato a $Z$, porta i nodi a decidere 0. Quindi
- $Z$ non è 0-valente (per costruzione di $Y$);
- $Z$ non può essere 1-valente
Pertanto $Z$ è *necessariamente bi-valente*.

**Lemma 1 + Lemma 2:**
Supponiamo per assurdo che esista un protocollo deterministico $\Pi_{BA}$ che termina e soddisfa validity e consistency nel modello asincrono anche in presenza di un nodo corrotto. Per il Lemma 2 deve esistere una configurazione iniziale bivalente $C_{0} = (S_{0}, M_{0})$ per $\Pi_{BA}$.
Per ogni $i \geq 1$, sia $m_{i}$ il messaggio "più vecchio" presente in $M_{i-1}$ (rompendo la simmeria arbitrariamente in caso di più messaggi), sia $\sigma_{i}$ lo schedule che termina con $m_{i}$ la cui esistenza è garanita dal Lemma 2 e sia $C_{i} = \sigma_{i}(C_{i−1})$ la configurazione bi-valente risultante.
Lo schedule $(\sigma_{1}, \sigma_{2}, \dots)$ è quindi uno schedule infinito che garantisce che ogni messaggio inserito nella message pool viene prima o poi consegnato e fa in modo che il protocollo rimanga sempre in configurazioni bivalenti.

## Protocollo Probabilistico per Byzantine Agreement

Mostriamo ora un protocollo probabilistico per BA che termina in tempo finito con probabilità 1 e soddisfa validity e consistency se il numero di nodi corrotti è $f < \frac{n-2}{10}$.

![[benor.png]]

Ogni nodo $u \in [n]$ parte con un bit $b \in \{0,1\}$ al round/fase $t = 1$ e trasmette $(b,1)$ a tutti i nodi. Il protocollo procede per fasi asincrone guidate dagli eventi di ricezione dei messaggi.

1. Ogni nodo accetta al più un messaggio da ciascun mittente $v$ per ogni fase.
2. Il nodo aspetta poi di ragiungere un quorum, $|M_{t}| \geq n-f$ messggi relativi alla fase $t$ prima di procedere.
3. Una volta raggiunto il quorum, calcola il numero di zeri $v_{0}$ e uni $v_{1}$ e impone `decided = TRUE` $\iff \max\{v_0, v_1\} \ge \frac{n}{2} + 3f + 1$. Quindi se vede moltissimi zeri o uni, non solo decide il proprio bit in base alla maggioranza ma decide anche di terminare l'esecuzione.
4. Infine, aggiorna la proposta in base alla maggioranza, in questo caso una maggioranza più debole e invia il bit scelto a tutti passando alla prossima fase.

**Teorema:** Se il numero di nodi corrotti è $f < \frac{n − 2}{10}$ allora il protocollo asincrono di Ben-Or termina con probabilità 1 e soddisfa validity e consistency.

La dimostrazione del teorema segue dai seguenti lemmi.

**Lemma 1:** Se esistono un $t \in \mathbb{N}$ e un $b \in \{ 0,1 \}$ tali che tutti i nodi onesti inviano $(b,t)$, allora tutti i nodi onesti danno in output $b$.

**Proof:** Osserviamo che questo lemma implica che Ben-Or soddisfa validity.
- $n$ nodi, di cui $\leq f$ sono corrotti, ossia i nodi onesti sono $\geq n-f$.
- Un nodo onesto $u$ sblocca la fase $t$ solo quando ha raccolto un insieme $M_{t}$ di almeno $n-f$ messaggi.
- Nel peggiore dei casi, di questi $n-f$ messaggi, $f$ sono arrivati da nodi corrotti e potrebbero contenere il bit $1-b$. Quindi il numero di messaggi validi raccolti dal nodo $u$ è almeno $$v_{b} \geq (n-f) - f = n - 2f$$
Confrontiamo ora questa quantità con la soglia di decisione forte:
$$
n - 2f \geq \frac{n}{2} + 3f + 1 \iff \frac{n}{2}-5f - 1\geq 0 \iff f \leq \frac{n-2}{10}
$$
Quindi la disuguaglianza è strettamente verificata dall'ipotesi.
Di conseguenza,
$$
v_{b} \geq n-2f \geq \frac{n}{2} + 3f + 1
$$
quindi scatta la regola deterministica e impone $y_{u}(t) = b$, imponendo anche `decided = true`.
La proprietà di validity è una diretta conseguenza di questo lemma, infatti se tutti i nodi onesti al round $t=1$ partono con lo stesso bit $b$, tutti inviano $(b,1)$. Per il lemma appena dimostrato, tutti i nodi onesti terminano decidendo $b$.

Dato un nodo $u$, indichiamo con $y_{u}(t)$ e $\texttt{decided}_u(t)$ le variabili locali $y$ e `decided` al tempo $t$ del nodo $u$.

---

**Lemma 2:** Sia $t \in \mathbb{N}$. Se un nodo onesto $u$ imposta la sua variabile $y_{u}(t)$ in modo deterministico, allora per ogni altro nodo onesto $v$ che imposta la sua variabile $y_{v}(t)$ in modo deterministico deve essere $y_{u}(t) = y_{v}(t)$.

**Proof:** Supponiamo per assurdo che $\exists\ u,v$ onesti tale che nello stesso round $t$:
- $y_{u}(t) = 0$ impostato deterministicamente da $u$;
- $y_{v}(t) = 1$ impostato deterministicamente da $v$;

Ma se $u$ ha impostato deterministicamente $y_{u}(t)$ deve aver ricevuto almeno $\frac{n}{2} + f + 1$ messaggi $(0, t)$.

Poichè i nodi scartano i duplicati dello stesso mittente nel round $t$, in qualsiasi esecuzione, al più $f$ nodi corrotti possono aver inviato messaggi ambigui o discordanti. Quindi, dei messaggi ricevuti da $u$ con valore 0, almeno $v_{0}^{(u)} - f$ provengono da nodi onesti.
I nodi onesti tramettono un solo bit per round, quindi l'insieme dei nodi onesti che hanno inviato 0 e l'insieme di quelli che hanno inviato 1 sono disgiunti. La loro somma non può superare il numero totale di nodi onesti, a maggior ragione il numero totale di nodi.
$$
(v_{0}^{(u)} - f) + (v_{1}^{(v)} - f) \leq n-f < n
 $$
 Da cui
 $$
 \begin{align}
\left( \frac{n}{2} + f + 1 - f \right) + \left( \frac{n}{2} + f + 1 - f \right) &= \left( \frac{n}{2} + 1 \right) + \left( \frac{n}{2} + 1 \right) \\
&= n + 2 \underbrace{\leq}_{!!!}n 
 \end{align}
 $$
Dunque è impossibile che $u$ e $v$ impostino deterministicamente valori discordanti.

Il Lemma 2 implica che, data una fase $t \in \mathbb{N}$, se per due nodi onesti $u$ e $v$ si ha che $y_{u}(t) \neq y_{v}(t)$ allora almeno uno dei due nella fase $t$ ha impostato la sua variabile locale $y$ in modo aleatorio.

Inoltre, segue anche che se due nodi onesti $u$ e $v$ impostano $\texttt{decided}_{u}(t) = \texttt{decided}_{v}(t) = \texttt{TRUE}$, allora $y_{u}(t) = y_{v}(t)$.

---

**Lemma 3:**
Siano $t \in \mathbb{N}$ e $b \in \{ 0,1 \}$. Se un nodo onesto $u$ imposta $\text{decided}_u(t) = \text{TRUE}$ e $y_u(t) = b$, allora ogni altro nodo onesto $v$ invierà il messaggio $(b, t+1)$.

**Proof:** Sia $u \in [n]$ il nodo onesto che ha deciso definitivamente $\texttt{decided}_u(t) = \texttt{TRUE}$ e $y_u(t) = b$. Ma allora $u$ deve aver ricevuto almeno $\frac{n}{2} + 3f + 1$ messaggi $(b, t)$. Di questi, almeno $\left(\frac{n}{2} + 3f + 1\right) - f = \frac{n}{2} + 2f + 1$ messaggi $(b, t)$ erano da parte di nodi onesti.

Sia $w$ un altro nodo onesto. Gli almeno $\frac{n}{2} + 2f + 1$ messaggi $(b, t)$ inviati da nodi onesti verso $u$ devono essere stati inviati anche verso $w$ perché i nodi onesti seguono il protocollo inviando a tutti. Ma $w$ procede nella fase non appena riceve un quorum di almeno $n-f$ messaggi, quindi nel suo insieme $M_t$ omette al più $n - (n - f) = f$ nodi dell'intera rete.

Nel caso peggiore in cui tutti i messaggi omessi provengano da quei nodi onesti, $w$ include comunque nel suo insieme $M_t$ almeno:
$$\left(\frac{n}{2} + 2f + 1\right) - f = \frac{n}{2} + f + 1$$
messaggi $(b, t)$.
Si ha quindi che:
$$v_b \ge \frac{n}{2} + f + 1 \implies y_w(t) = b$$
in modo deterministico. Di conseguenza, $w$ invia il messaggio $(b, t+1)$.
E questo avviene per ogni nodo onesto.

---

**Lemma 4:** Per ogni $t \in \mathbb{N}$ tale che $\texttt{decided} = \texttt{FALSE}$ per tutti i nodi onesti, esiste un $b \in \{0, 1\}$ tale che la probabilità che tutti i nodi onesti inviino $(b, t + 1)$ è almeno $2^{-n}$.

**Proof:** Sia $t$ una fase fissata in cui nessun nodo onesto ha ancora deciso. Alla fase $t$ possono verificarsi le seguenti situazioni:
1. **Almeno un nodo onesto imposta $y$ in modo deterministico:** Per l'Esercizio 2, tutti gli altri nodi onesti che impostano la loro variabile $y$ in modo deterministico devono fissare lo stesso bit, chiamiamolo $b$. Sia $k$ il numero di nodi onesti che impostano $y$ in modo aleatorio (linea 20). Ciascuno di essi sceglie indipendentemente il valore $b$ con probabilità $\frac{1}{2}$. Poiché le scelte locali sono mutuamente indipendenti, la probabilità che tutti i $k$ nodi scelgano proprio il bit $b$ è: $$\left(\frac{1}{2}\right)^k = \frac{1}{2^k}$$Dato che il numero totale di nodi nella rete è $n$, abbiamo $k \le n$, da cui segue: $$\frac{1}{2^k} \ge \frac{1}{2^n}$$In questo modo tutti i nodi onesti impostano $y = b$ e inviano $(b, t+1)$.
2. **Nessun nodo onesto imposta $y$ in modo deterministico:** Tutti i nodi onesti (che sono al più $n$) impostano $y$ in modo aleatorio. Fissato arbitrariamente un bit $b \in \{0, 1\}$, la probabilità che tutti i nodi onesti estraggono proprio $b$ è pari a: $$\left(\frac{1}{2}\right)^{\text{nodi onesti}} \ge \left(\frac{1}{2}\right)^n = 2^{-n}$$
In entrambi i casi esiste quindi un valore $b \in \{0, 1\}$ tale che la probabilità che tutti i nodi onesti trasmettano il messaggio $(b, t+1)$ è almeno $2^{-n}$.

---

**Dimostrazione Teorema:**
*Validity* e *Consistency* seguono direttamente dai Lemmi 1, 3 e 4.
Vediamo ora che il protocollo termina con probabilità 1. Sia
$$
\tau = \inf\{ t \in \mathbb{N}: \texttt{decided}_{u}(t) = \texttt{TRUE} \text{ per qualche nodo onesto } u \}
$$
Ossa, la v.a. $\tau$ è il primo round in cui almeno un nodo onesto decide.
Dal Lemma 4, ad ogni round $t$, la probabilità condizionata che tutti i nodi concordino al round successivo è almeno $2^{-n}$. 
La probabilità che il protocollo non abbia deciso dopo $t$ passi decade esponenzialmente:
$$
P(\tau > t) \leq (1 - 2^{-n})^t
$$
Per $t \to \infty$, si ha che
$$
\lim_{ t \to \infty } P(\tau > t) \leq \lim_{ t \to \infty } (1 - 2^{-n})^t = 0
$$
Ne segue che $P(\tau < +\infty) = 1$.
Dal Lemma 3, una volta che il primo nodo decide a tempo $\tau$, tutti i nodi decidono entro la fase $\tau + 1$. Il protocollo termina quindi con probabilità 1 in tempo finito.