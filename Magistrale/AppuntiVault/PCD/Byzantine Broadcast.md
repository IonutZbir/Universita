Consideriamo un sistema distribuito con $[n] = \{1, 2, \dots, n\}$ nodi (entità). Ogni nodo può eseguire computazioni arbitrarie (CPU, RAM, 
DISCO) e inviare messaggi di lunghezza arbitraria a ogni altro nodo.
Diremo che:
- $f$ nodi sono *corrotti* (possono scegliere se eseguire correttamente il protocollo oppure prendere delle decisioni diverse rispetto al protocollo). Assumeremo che, *worst-case* tutti i nodi corrotti si coalizzeranno per far fallire il protocollo. Inoltre non sapiammo quali sono i nodi corrotti. 
- $n-f$ nodi sono *onesti* (seguono il protocollo così come è definito).
- $\exists!\ s \in V$ detto nodo *sorgente* avente un messaggio $b \in \{0,1\}$.

Vogliamo quindi progettare un *protocollo* al termine del quale ogni nodo onesto $i$ dia in output un valore $y_{i}$ tale che

- **Consistency:** Se $i$ e $j$ sono due onesti, allora $y_{i} = y_{j}$;
- **Validity:** Se $s$ sorgente è un nodo onesto, allora $y_{i} = b$ per ogni nodo onesto $i$.

## Modelli di Calcolo Distribuito e Assunzioni

La modalità di progettazione del protocollo dipende da quale modello di calcolo distribuito consideriamo e quali assunzioni.

- **Synchronous / Asynchronous.** Diremo che il sistema è sincrono se, all'invio di un messaggio da parte di un nodo, possiamo assumere un upper bound al tempo che impiega per arrivare a destinazione. Altrimenti diremo che il sistema è asincrono.
- **Authenticated / Non Authenticated.** Diremo che il sistema è autenticato se nel modello c'è una PKI (Public Key Infrastructure). In questo modo ogni nodo è in grado di verificare l'autenticità del messaggio appena ricevuto (il messaggio che ho ricevuto è stato veramente inviato dal nodo $k$?). Se non c'è una PKI allora il sistema è non autenticato.
- **Permissioned / Permissionless.** Diremo che il sistema è permissioned se il numero di nodi (entità) all'interno della rete è fissato ($n$) e non cambia durante l'esecuzione del protocollo. Una rete è permissionless se invece il numero di nodi nella rete può variare, ad esempio la rete Bitcoin.

## Modello Sincrono, Permissioned, Authenticated

Consideriamo un sistema *sincrono*, ossia
- C'è un *global clock* noto a tutti i nodi che scandisce il tempo in *round* discreti: $0, 1, 2, \dots$;
- Ogni messaggio inviato in un round $t$ arriva a destinazione prima dell'inizio del round $t+1$.

Assumiamo che ci sia un PKI setup:
- Ogni nodo $i$ ha una coppia di chiavi *pubblica/privata* $(pk_{i}, sk_{i})$;
- L'insieme delle chiavi pubbliche $\{pk_{1}, \dots, pk_{n}\}$ è *common knowledge* fra i nodi (tutti i nodi conoscono l'insieme delle chiavi e inoltre ogni nodo è a conoscenza del fatto che ogni nodo conosce l'insieme delle chiavi.)
- Dato un messaggio $m$, indichiamo con $<m>_{i}$ il messaggio $m$ con l'aggiunta della firma valida del nodo $i$ eseguita con la sua $sk_i$.

## Protocollo Dolev-Strong

![[dolevstrong.png]]

Perchè questo protocollo funziona? Perchè sono sufficienti $f + 1$ round?

### Intuizione

Supponiamo che tutti i nodi debbano termina al round $f$ dando in output $y_{i}\ \forall i \in [n]$ invece che al round $f + 1$. Consideriamo il seguente attacco:
- La sorgente $s$ è corrotta e invia $<1>_{1}$ a tutti i nodi onesti.
- Tutti i nodi onesti aggiungeranno $<1>$ all'interno del proprio insieme $\mathcal{E}$.
- Ora, poichè ci sono $f$ nodi corrotti (sorgente inclusa), all'inizio del round $f$, i nodi corrotti creano un messaggio $$<0>_{1, \sigma_{2}, \dots, \sigma_{f-1}}$$che lo inviano solo ad un nodo onesto $v$ inserendo $0$ in $\mathcal{E}$.
- Alla fine del round $f$, $v$ è l'unico nodo ad aver ricevuto 2 bit diversi, ossia $\mathcal{E}_{v} = \{0,1\}$ mentre $\mathcal{E}_{k} = \{1\}\ \forall k \in [n] \setminus \{v\}$. Quindi $$y_{v} = 0\ (|\mathcal{E}_{v}| = 2) \qquad \land \qquad y_{k} = 1\ \forall k \neq v$$violando così la proprietà di *consistency*.

Se invece il numero di round è $f + 1$, l'attacco appena descritto non è possibile, infatti, un bit con $f+1$ firme deve essere per forza stato firmato da almeno un nodo onesto, sia questo $i$. Quando il nodo $i$ ha firmato il bit $b$ di prima nel round $r < f+1$ avrà sicuramente propagato $b$ firmato da una sequenza di $r+1$ firme (inclusa la sua) a tutti gli altri nodi onesti, di conseguenza i nodi onesti che ricevono $b$ lo dovranno aggiungere nel loro $\mathcal{E}$. Dunque, per ogni nodo $k$ onesto
$$
|\mathcal{E}_{k}| = 2 \implies y_{k} = 0
$$
verificando così la proprietà di consistency.
### Analisi

**Lemma 1:** Sia $r \leq f$. Se alla fine del round $r$, esiste un nodo onesto $i$ tale che $\hat{b} \in \mathcal{E}_{i}$, allora entro la fine del round $r+1$ ogni nodo onesto $j$ avrà $\hat{b} \in \mathcal{E}_{j}$.
**Proof:** Per ipotesi, $\hat{b} \in \mathcal{E_{i}}$ alla fine del round $r$. Sia $t \leq r \leq f$ il round in cui il nodo $i$ ha aggiunto per la prima volta $\hat{b}$ a $\mathcal{E}$.

Secondo le specifiche del protocollo, all'inizio del round $t$ il nodo $i$ ha ricevuto $<\hat{b}>_{1, \sigma_{1}, \dots, \sigma_{t-1}}$ valido con $t$ firme distinte (inclusa quella della sorgente). Tra queste firme non può comparire quella del nodo $i$, poiché se fosse già presente significherebbe che $i$ aveva già firmato e inserito $\hat{b}$ in un round precedente a $t$.

Di conseguenza, durante il round $t$, il nodo $i$ aggiunge la prorpia firma $\sigma_{i}$ e invia $<\hat{b}>_{1, \sigma_{1}, \dots, \sigma_{t-1}, \sigma_{i}}$ a tutti gli altri nodi.
Poiché il sistema è sincrono, tutti i nodi onesti $j$ riceveranno questo messaggio con $t+1$ firme distinte alla fine del round $t$ (quindi all'inizio del round $t+1$). 
Infine. se $\hat{b} \not\in \mathcal{E}_{j}$, il nodo $j$ lo aggiunge al proprio insieme durante il round $t+1$.
In conclusione, poiché $t \leq r$ , abbiamo $t+1 \leq r+1 \leq f+1$ il che implica che alla fine del round $r+1$ ogni nodo onesto $j$ avrà $\hat{b} \in \mathcal{E}_{j}$.

**Lemma 2:** Se alla fine del round $f+1$, esiste un nodo onesto $i$ tale che $\hat{b} \in \mathcal{E}_{i}$, allora entro la fine del round $f+1$ ogni nodo onesto $j$ avrà $\hat{b} \in \mathcal{E}_{j}$.

**Proof:** Consideriamo i seguenti due casi:
1. *Il nodo $i$ ha aggiunto $\hat{b}$ in $\mathcal{E}_{i}$ al round $r < f + 1$:* Per il Lemma 1, una volta che $\hat{b} \in \mathcal{E}_{i}$ alla fine del round $r$, ogni nodo onesto $j$ avrà $\hat{b}$ all'interno di $\mathcal{E}_{j}$ alla fine del round $r+1 \leq f+1$.
2. *Il nodo $i$ ha aggiunto $\hat{b}$ in $\mathcal{E}_{i}$ al round $f+1$:* Affinché ciò possa accadere, il nodo $i$ deve aver ricevuto $<\hat{b}>_{1, \sigma_{1}, \dots, \sigma_{f}}$ con $f+1$ firme distinte all'inizio del round $f+1$. Poiché ci sono $\leq f$ nodi corrotti, almeno un nodo onesto deve aver firmato $\hat{b}$ in un round precedente $r < f+1$. Quindi, per il Lemma 1, ogni nodo onesto $j$ avrà $\hat{b}$ all'interno di $\mathcal{E}_{j}$ alla fine del round $r+1 \leq f+1$.

**Teorema:** Il protocollo Dolev-Strong risolve il problema del Byzantine Broadcast se il numero di nodi corrotti è al più $f$.

**Proof:**
- *Consistency:* Per il Lemma 2, al termine del round $f+1$, tutti i nodi onesti $j$ hanno lo stesso valore all'interno del proprio insieme $\mathcal{E}_j$, verificando la Consistency.
- *Validity:* Se la sorgente (nodo 1) è onesta con input $b$, al round 0 invia $<b>_{1}$ a tutti i nodi. All'inizio del Round 1, ogni nodo onesto $u$ riceve $<b>_{1}$ con una firma valida e aggiunge $b$ al proprio insieme $\mathcal{E}_u$. Poiché lo schema di firma digitale è sicuro e la sorgente è onesta, nessun nodo (neppure corrotto) è in grado di produrre una firma valida della sorgente su un messaggio differente $b' \neq b$. Poiché ogni messaggio accettato deve contenere la firma della sorgente alla base della catena, nessun altro valore potrà mai essere inserito in $\mathcal{E}_u$. Al termine del round $f+1$, ogni nodo onesto ha $\mathcal{E}_u = \{b\}$ e restituisce in output $b$, verificando la Validity.


## Protocollo Probabilistico per BB

Abbiamo dimostrato che per $f \geq \frac{n}{3}$ nodi corrotti non esiste un protocollo che risolvi BB ([[Lower Bound Per Byzantine Broadcast senza PKI |LB BB]]). Vediamo ora un protocollo probabilistico che garantisce *validity* con probabilità 1 e *consistency* w.h.p. se ci sono $f < \frac{n}{3}$ nodi corrotti.

*NOTA:* Diremo che un evento $E_n$ avviene con altà probabilità (w.h.p.) se per ogni costante $c \geq 1$ fissata arbitrariamente esiste $n_{0}(c) \in \mathbb{N}$ tale per cui, $\forall n \geq n_{0}(c)$
$$
P(E_{n}) \geq 1 - \frac{1}{n^c} = 1 - O(n^{-c})
$$

Sia $H: \mathbb{N} \cup \{0\} \to [n]$ una funzione tale che $H(0) = 1$ e $\forall t = 1, 2, \dots$ si comporta come un random oracle. Possiamo pensare ad $H$ come una funzione hash (anche crittografica, per es. SHA256).

![[probBB.png]]

Il protocollo procede per votazioni. 
Ciascun nodo $i \in [n]$ mantiene localmente una variabile interna $sb_i \in \{0, 1, \perp\}$ (detta _sticky bit_), che rappresenta la scelta corrente del nodo.

All'inizio (Round 0), tutti i nodi inizializzano $sb_i = \perp$, tranne la sorgente designata (il nodo 1) che riceve in input $b$ e imposta $sb_1 = b$.
Il protocollo si articola in $k$ iterazioni successive ($t = 0, \dots, k-1$), ciascuna composta da 3 round sincroni:

1. **Proposta del Leader (Round $3t$):** Viene eletto il leader dell'iterazione $\ell_t$: per $t = 0$ è la sorgente stessa ($\ell_0 = 1$), mentre per $t \ge 1$ viene scelto tramite una funzione oracolo casuale $\ell_t := H(t)$.
	- Se $sb_{\ell_t} \ne \perp$, il leader invia a tutti il proprio $sb_{\ell_t}$;
	- Altrimenti, sceglie un bit in $\{0, 1\}$ in modo uniforme a caso (u.a.r.) e lo invia a tutti.
2. **Votazione (Round $3t+1$):** Ciascun nodo $i$ invia un bit in broadcast a tutti gli altri:
	- Se ha $sb_i \ne \perp$, invia il proprio $sb_i$;
	- Se ha $sb_i = \perp$, invia il bit ricevuto da $\ell_t$ (se non ha ricevuto nulla o ha ricevuto informazioni discordanti, sceglie un bit arbitrario).        
3. **Aggiornamento dello stato (Round $3t+2$):**   Ogni nodo $i$ conta i voti ricevuti nel round precedente:
	- Se riceve lo stesso bit $\hat{b}$ da almeno $\frac{2n}{3}$ nodi distinti, imposta $sb_i = \hat{b}$;       
	- Altrimenti, imposta $sb_i = \perp$.         
Al termine delle $k$ iterazioni (Round $3k$), ogni nodo onesto produce in output il valore del proprio sticky bit $sb_i$.

### Analisi

**Lemma 1:** Sia $t$ un'iterazione qualsiasi, e siano $u,w$ due nodi onesti. Non è possibile che alla fine dell'iterazione $t$ si abbia
$$
sb_{u} = 0 \qquad \text{ e } \qquad sb_{w} = 1
$$
Il Lemma non ci dice ovviamente che tutti i nodi onesti hanno lo stesso bit. È pero possibile che $sb_{u} = 0$ e $sb_{w} = \perp$ e viceversa.

**Proof:** Supponiamo per assurdo che $sb_{u} = 0$ e $sb_{w} = 1$ e che $u,w$ siano nodi onesti. Se $u$ è onesto, allora, per come è imposto il protocollo, al round $3t+1$ deve aver ricevuto $b=0$ da almeno $\frac{2n}{3}$ nodi. Lo stesso vale per $sb_{w}$.
Sia $S_{u}$ l'insieme costituito dai nodi che hanno inviato $0$ a $u$ e sia $S_{w}$ l'insieme dei nodi cha hanno inviato $1$ a $w$. Allora
$$
|S_{u}| \geq \frac{2n}{3} \qquad \text{ e } \qquad |S_{w}| \geq \frac{2n}{3}
$$
Ma questo implica che $\geq \frac{n}{3}$ nodi hanno inviato sia 1 che 0, ossia che $f \geq \frac{n}{3}$.
$$
\begin{gather*}
|S_{u} \cup S_{w}| = |S_{u}| + |S_{w}| - |S_{u} \cap S_{w}|  \\
\implies \\
|S_{u} \cap S_{w}| = |S_{u}| + |S_{w}| - |S_{u} \cup S_{w}|  \\
\implies \\
|S_{u} \cap S_{w}| \geq \frac{2n}{3} + \frac{2n}{3} - n = \frac{n}{3} 
\end{gather*}
$$

**Def:** Diremo che un'iterazione $t$ è *lucky* se:
1. Il leader scelto $\ell_{t}$ è onesto;
2. Il bit ricevuto dal leader è lo stesso di ogni nodo onesto $i$ che in quel iterazione ha $sb_{i} \neq \perp$.

**Lemma 2:** Se c'è un'iterazione *lucky*, allora tutti i nodi onesti danno in output lo stesso bit.

**Proof:** Sia $t$ la prima iterazione _lucky_ del protocollo.

Per definizione di iterazione _lucky_, il leader $\ell_t$ è un nodo onesto e propone un bit $b$ che coincide con lo sticky bit di qualunque eventuale nodo onesto che abbia $sb \ne \perp$ all'inizio dell'iterazione.

1. **Round $3t$:** Il leader onesto $\ell_t$ invia lo stesso bit $b$ a tutti i nodi.    
2. **Round $3t+1$:**
    - I nodi onesti $u$ con $sb_u \ne \perp$ inviano il proprio sticky bit, che per definizione di iterazione _lucky_ è proprio $b$.
    - I nodi onesti $w$ con $sb_w = \perp$ inviano il bit ricevuto dal leader onesto, ovvero $b$. Quindi, **ogni singolo nodo onesto** invia il bit $b$ in broadcast.
3. **Round $3t+2$:**
    Poiché il numero di nodi corrotti è $f < n/3$, il numero di nodi onesti è almeno $n - f \geq \frac{2n}{3}$. Data la sincronia della rete, ogni nodo onesto riceve il bit $b$ da tutti i nodi onesti, ossia da più di $\frac{2n}{3}$ nodi distinti. Di conseguenza, **ogni nodo onesto $u$ imposta $sb_u = b$** entro la fine dell'iterazione $t$.

Infine, per induzione dimostriamo che tutti i nodi onesti mantengono $sb_u = b$ fino al Round finale $3k$, terminando tutti con lo stesso output $y_u = b$.
- Supponiamo per induzione che all'inizio di un'iterazione $t' > t$ tutti i nodi onesti abbiano $sb_u = b$.
- Nel Round $3t'+1$, poiché nessun nodo onesto ha $sb = \perp$, tutti i nodi onesti trasmettono $b$, ignorando qualsiasi proposta del leader.
- Nel Round $3t'+2$, ogni nodo onesto riceve nuovamente $\geq \frac{2n}{3}$ voti per $b$, riconfermando $sb_u = b$.

Questo teorema ci dimostra la consistency del protocollo se si verifica un'iterazione lucky.

**DOMANDA:** Quanto deve essere $k$ affinchè w.h.p. si verifica un'iterazione lucky?

**Lemma 3:** La probabilità che vi sia almeno un'iterazione lucky è 
$$
1 - \left( \frac{2}{3} \right)^k
$$

**Proof:** Sia $t$ un'iterazione.
Abbiamo che
$$
\begin{align}
P(\text{honest leader}) &= P(H(t) = \ell_{t}) \cdot P(\ell_{t} \text{ is honest}) \\
\frac{1}{n} \cdot \frac{2n}{3} = \frac{2}{3}
\end{align}
$$
Sia ora 
$$
\mathcal{E}_{t} = \text{"iteration } t \text{ i lucky"}
$$
allora,
$$
P(\mathcal{E}_{t}) = P(\text{honest leader}) \cdot P(\text{bit leader = bit nodi onesti} ) = \frac{2}{3} \cdot \frac{1}{2} = \frac{1}{3}
$$
La probabilità che in $k$ round non vi sia nessuna iterazione lucky è
$$
P\left( \bigcap_{t=0}^{k-1} \bar{\mathcal{E}_{t}} \right) \leq \left( 1 - \frac{1}{3} \right)^k = \left( \frac{2}{3} \right)^k
$$
(Le iterazioni sono mutualmente indipendenti grazie al random oracle).
Quindi la probabilità che vi sia almeno un'iterazione lucky è
$$
1 - \left( \frac{2}{3} \right)^k
$$

**Teorema:** Il protocollo soddisfa *consistency* w.h.p. se 
$$k = \Theta(\log(n))$$
e soddisfa *validity* con probabilità 1.

**Proof:**
*Consistency:* Per il Lemma 3 sappiamo che 
$$
\begin{align}
1 - \left( \frac{2}{3} \right)^k \geq 1 - \frac{1}{n^c}
&\equiv
-\left( \frac{2}{3} \right)^k \geq -\frac{1}{n^c} \\
\left( \frac{2}{3} \right)^k \leq \frac{1}{n^c} &\iff e^{k \log(2/3)} \leq e^{\log(1/n^c)} \\
k\log\left( \frac{2}{3} \right) \leq \log\left( \frac{1}{n^c} \right) &\iff -k\log\left( \frac{3}{2} \right) \leq -\log(n^c) \\
k\log\left( \frac{3}{2} \right) \geq c\log(n) &\iff k \geq \frac{c\log(n)}{\log\left( \frac{3}{2} \right)} \\ \\
&\implies k = \Theta(\log n)
\end{align}
$$
*Validity:* Se il leader scelto è onesto, allora tutti i nodi onesti daranno in output il bit del leader. La dimostrazione segue dal Lemma 2 e dalla definizione del protocollo.