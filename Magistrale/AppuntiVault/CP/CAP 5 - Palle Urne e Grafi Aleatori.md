# 5.1 - Il Paradosso del Compleanno

Abbiamo 30 studenti in aula, qual è la probabilità che almeno $2$ abbiano la stessa data di compleanno?

**Soluzione Combinatorica:** Per semplicità supponiamo ciascuno abbia una data di compleanno distribuita uniformemente sui 365 giorni dell'anno. Sia
$$
E = \text{"Nessuno condivide la data di compleanno"}
$$
Allora
$$
P(E) = \frac{\binom{365}{30} \cdot 30!}{365^{30}}, \quad \text{dove}
$$
- $\binom{365}{30}$ sono i modi di scegliere 30 date diverse su 365 giorni disponibili.
- $30!$ è il numero di assegnare 30 date a 30 persone.
- $365^{30}$ è il numero di tutte le combinazioni possibili.

**Soluzione Probabilistica:** Immaginiamo che le persone entrino in aula una alla volta. La probabilità che le prime due abbiano compleanni diversi è $\left( 1 - \frac{30}{365} \right)$. La probabiltà che la terza abbia data di compleanno divesa è $\left( 1 - \frac{2}{365} \right)$ sapendo che i primi 2 l'avevano diversa.

Continuando cosi, la probabilità che la $k$-esima persona abbia una data di compleanno diversa dai primi $k-1$ sapendo che i primi $k-1$ hanno compleanno diverso è $\left( 1 - \frac{k-1}{365} \right)$. Quindi, la probabilità che 30 persone abbiano data di compleanno diversa è:
$$
P(E) = \left( 1 - \frac{1}{365} \right) \cdot \left( 1 - \frac{2}{365} \right) \cdot \dots \cdot \left( 1 - \frac{29}{365} \right) \approx 0.2937
$$
*Fun Fact:* a partire dalle 23 persone, questa probabilità diventa $< 50\%$.

In generale, se ci fossero $n$ possibili date di compleanno ed $m$ persone diverse
$$
P(E) = \prod_{j=1}^{m-1} \left( 1 - \frac{j}{m} \right)
$$
Possiamo trovare un'espressione più semplice che approssimi questa produttoria usando $1 - \frac{j}{n} \leq e^{-j/n}$ quando $j<n$, ottenendo
$$
\begin{align}
P(E) \approx \prod_{j=1}^{m-1} e^{j/n} &= \exp\left( -\frac{1}{n} \sum_{j=1}^{m-1} j \right) = \exp\left( -\frac{1}{n} \frac{m(m-1)}{2}\right)  \\
&\approx \exp\left( -\frac{m^2}{2n} \right)
\end{align}
$$
Affiché $P(E) \approx \frac{1}{2}$ dobbiamo avere $\frac{m^2}{2n} = \log(2)$, cioè $m = \sqrt{ 2n\log (2) }$.

# 5.2 - Modelli di Urne - Balls into Bins

Abbiamo $m$ palline che tiriamo a caso in $n$ urne. Qual è la distribuzione probabilistica del numero di palline in ogni urna? Siano
$$
Z_{i} = \# \text{" palline nell'}i\text{-esima urna"}
$$
Allora, $\forall\ i=1,\dots, n$ e $\forall\ r=1,\dots, m$,
$$
P(Z_{i} = r) = \binom{m}{r} \left( \frac{1}{n} \right)^r\left( 1 - \frac{1}{n} \right)^{m-r} = \Pr(m,r)
$$
- Le $Z_{i} \sim Bin\left( m, \frac{1}{n} \right)$ sono identicamente distribuite ma *NON INDIPENDENTI*, visto che la loro somma deve sempre dare $m$ ($\sum_{i=1}^n Z_{i} = m$). 

$$
\begin{align}
P(Z_{i} = r) &= \binom{m}{r} \left( \frac{1}{n} \right)^r \left( 1 - \frac{1}{n} \right)^{m-r}  \\
&= \frac{1}{r!} \frac{m(m-1)(m-2)\cdots(m-r+1)}{n^r} \left( 1-\frac{1}{n} \right)^{m-r}
\end{align}
$$
Se $m \gg r$ e $n \gg r$ possiamo approssimare il secondo termine con $\left( \frac{m}{n} \right)^r$ e il terzo termine con $e^{-m/n}$, ottenendo
$$
\Pr(m, n) \approx \frac{e^{-m/n}\left( \frac{m}{n} \right)^r}{r!}
$$
Per essepre più precisi, si ha che $\frac{m}{n} \to \mu$ per qualche $\mu > 0$, allora
$$
\lim_{ n,m \to \infty ,\ \frac{m}{r}\to \mu } \Pr(m,n) = e^{-\mu} \frac{\mu^r}{r!} 
$$
*Osservazione:* Il paradosso del compleanno mostrava che 
$$
P(\exists i \in \{1, \dots, n\}:\ Z_{i} \geq 2) \geq \frac{1}{2} \iff m \geq \sqrt{ 2n\log 2 }
$$

*Esempio:* Possiamo chiederci: qual è il numero medio di urne rimaste vuote? Sia
$$
X_{i} = 
\begin{cases}
1 \iff \text{ l'urna }i\text{-esima è rimasta vuota}  \\
0 \text{ altrimenti}
\end{cases}
$$
Allora
$$
P(X_{i} = 1) = \left( 1 - \frac{1}{n} \right)^m \approx e^{-m/n}
$$
$m$ palline finiscono in una delle $n-1$ urne *sbagliate*. Quindi
$$
\mathbb{E}[\text{\# urne rimaste vuote}] = \mathbb{E}\left[ \sum_{i=1}^n X_{i} \right] = n\left( 1 - \frac{1}{n} \right)^m \approx n e^{-m/n}
$$
*Osservazione:* L'approssimazione $1-x \approx e^{-x}$ è molto buona se $x$ è piccolo. In generale, $\forall x \in (0,1),\ 1-x \leq e^{-x} \leq 1 - \frac{x}{2}$.

**DEF 5.1.** Una v.a. è detta di Poisson di parametro $\mu$, $X \sim Poi(\mu)$
, se
$$
P(X = k) = e^{-\mu} \frac{\mu^k}{k!} \quad \forall\ k = 0,1,2,\dots
$$

*Interpretazione:* $X$ è il numero di telefonate che arrivano ad un centralino in un arco di tempo. Oppure, $X$ è il numero di terremoti che si verificano in una data regione in un certo arco di tempo. Oppure, $X$ è il numero di palline che vanno a finire in una determinata urna. (**Legge degli eventi rari**)

*NOTA:* Espansione dell'esponenziale:
Vale che, $\forall x \in \mathbb{R}$
$$
\boxed{\sum_{n=0}^\infty \frac{x^n}{n!} = e^x}
$$

**VALOR ATTESO**
$$
\begin{align}

\mathbb{E}[X] &= \sum_{k=0}^{\infty} k \frac{e^{-\mu}\mu^k}{k!} = e^{-\mu}\mu \sum_{k=0}^{\infty} \frac{\mu^{k-1}}{(k-1)!} \\ &\underbrace{=}_{j=k-1} e^{-\mu}\mu\underbrace{\sum_{j=0}^{\infty} \frac{\mu^j}{j!}}_{e^\mu \text{ espansione esponenziale}} = \mu
\end{align}
$$

**FUNZIONE GENERATRICE DEI MOMENTI**
$$
\begin{align}
M_{X}(t) &= \mathbb{E}[e^{tX}] = \sum_{k=0}^{\infty} e^{tk} e^{-\mu} \frac{\mu^k}{k!} = e^{-\mu} \sum_{k=0}^{\infty}\frac{(e^t\mu)^k}{k!} \\
&= e^{-\mu}e^{e^t\mu} = e^{\mu(e^t - 1)} \quad \forall t \in \mathbb{R}
\end{align}
$$
**MOMENTO SECONDO**
$$
\begin{align}
\mathbb{E}[X^2] &= M_{X}''(t)\bigg|_{t=0} = \frac{d^2}{dt^2} e^{u(e^t - 1)}\bigg|_{t=0} = \frac{d}{dt} \mu e^te^{\mu(e^t - 1)}\bigg|_{t=0} \\
&= \mu e^t e^{\mu(e^t - 1)} + (\mu e^t)^2 e^{\mu(e^t - 1)}\bigg|_{t=0} = \mu + \mu^2
\end{align}
$$
**VARIANZA**
$$
VAR[X] = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \mu + \mu^2 - \mu^2 = \mu
$$

**LEMMA 5.2 (Diverso dal libro)**
Siano $X_{1}, \dots, X_{n}$ v.a. di Poisson di parametri $\mu_{1}, \dots, \mu_{n}$ rispettivamente, che siano indipendenti tra loro, allora
$$
Y = \sum_{i=1}^{n} X_{i} \sim Poi(\mu_{1} + \dots + \mu_{n})
$$
**DIMOSTRAZIONE:**
Calcoliamo la f.g.m. di $Y$.
$$
\begin{align}
M_{Y}(t) &= \mathbb{E}[e^{Yt}] = \mathbb{E}\left[ e^{t \sum_{t=1}^n X_{i}} \right] = \prod_{i=1}^n \mathbb{E}[e^{tX_{i}}]  \\
\text{f.g.m.}&= \prod_{i=1}^n e^{\mu_{i}(e^t - 1)} = e^{\left(\sum_{i=1}^n \mu_{i}\right)(e^t - 1)} 
\end{align}
$$
che è la f.g.m di una $Poi\left( \sum_{i=1}^n \mu_{i} \right)$.

**TEOREMA 5.4 (Disuguaglianza di Chernioff per una singola v.a. di Poisson):**
Sia $X \sim Poi(\mu)$, allora
1. Se $x > \mu$, $P(X \geq x) \leq \frac{(e\mu)^xe^\mu}{x^x}$
2. Se $x < \mu$, $P(X \leq x) \leq \frac{(e\mu)^xe^\mu}{x^x}$

**DIMOSTRAZIONE:** Applichiamo la solita strategia: esponenziale + 
Markov + ottimizzazione.
1. Per $t > 0,$ $$P(X \geq x) = P(e^{tX} \geq e^{tx}) \leq \frac{\mathbb{E}[e^{tX}]}{e^{tx}} = e^{\mu(e^t - 1) - tx}$$Il minimo si ottiene per $t = \log\left( \frac{x}{\mu} \right) > 0$, e quindi $$P(X \geq x) \leq e^{\mu(x/\mu - 1) - x\log(x/\mu)} = (e\mu)^x \frac{e^{-\mu}}{x^x}$$
2. Per $t < 0$, $$P(X \leq x) = P(e^{tX} \geq e^{tx}) \leq \frac{\mathbb{E}[e^{tX}]}{e^{tx}} = e^{\mu(e^t - 1) - tx}$$SI conclude come sopra, prendendo $t = \log\left( \frac{x}{\mu} \right) < 0$, che ora è negativo poiché $x < \mu$.

**COROLLARIO (punti 3 e 4 del teorema 5.4 sul libro):**
Sia $X \sim Poi(\mu)$, allora
1. $P(X \geq (1 + \delta) \mu) \leq \left( \frac{e^\delta}{(1+\delta)^{(1+\delta)}} \right)^\mu, \quad \delta > 0$
2. $P(X \leq (1 + \delta) \mu) \leq \left( \frac{e^{-\delta}}{(1+\delta)^{(1+\delta)}} \right)^\mu, \quad \delta \in (0,1)$

## 5.3.1 Poisson come limite della Binomiale

Consideriamo una $Bin(n,p)$ con $n$ molto grande, ma $p$ molto piccolo, in modo che $np = \mu$ per qualche $\mu \in (0, \infty)$. Il seguente teorema mostra che questa binomiale è ben approssimata da una $Poi(\mu)$.

**TEOREMA 5.5**
Sia $X_{n} \sim Bin(n, p_{n})$ (sarebbe meglio parlare di una seq. di v.a.) tale che $\lim_{ n \to \infty } n \cdot p_{n} = \mu$ con $\mu \in (0, \infty)$. Allora
$$
\lim_{ n \to \infty } P(X_{n} = k) = \frac{e^{-\mu}\mu^k}{k!} \quad \forall\ k = 0,1,2,\dots
$$
ed inoltre
$$
\lim_{ n \to \infty } M_{X_{n}}(t) = e^{\mu(e^t - 1)} \quad \forall\ t \in \mathbb{R}
$$
**DIMOSTRAZIONE:** Fissiamo mentalmente un $k \in \{0, 1, 2, \dots\}$ e calcoliamo $P(X_{n} = k)$ (per $n> k$)
$$
\begin{align}
P(X_{n} = k) &= \binom{n}{k}p_{n}^k(1-p_{n})^{n-k}  \\
\left(p_{n} = \frac{np_{n}}{n} \right)&= \frac{n(n-1) \cdots n - (k-1)}{k!} \frac{(np_{n})^k}{n^k} \left( 1 - \frac{np_{n}}{n} \right)^{n-k} \\
&= \frac{(n p_{n})^k}{k!} \frac{n}{n} \frac{n-1}{n} \cdots \frac{n-(k-1)}{n} \left( 1 - \frac{np_{n}}{n} \right)^{n-k} \\
&= \frac{(n p_{n})^k}{k!} \left( 1 - \frac{1}{n} \right) \cdots\left( 1 - \frac{k-1}{n} \right)\left( 1 - \frac{np_{n}}{n} \right)^n\left( 1-\frac{np_{n}}{n} \right)^{k}
\end{align}
$$
Abbiamo che:
- Per ipotesi $\frac{(np_{n})^k}{k!} \to \frac{\mu^k}{k!}$;
- $\left( 1 -\frac{1}{n} \right) \cdots \left( 1 - \frac{k-1}{n} \right)$ tendono tutti a $1$ quand $n \to \infty$;
- $\left(1- \frac{p_{n}n}{n} \right)^n \xrightarrow{n \to \infty} e^{-\mu}$, poiché in generale si ha il limite notevole $\lim_{ n \to \infty } \left( 1 - \frac{z_{n}}{n} \right)^n = e^{z}$ per $z_{n} \xrightarrow{n \to \infty} z$.
- $\left( 1 - \frac{np_{n}}{n} \right)^{-k} \xrightarrow{n \to \infty} 1$

Perciò $P(X_{n} = k) \xrightarrow{n \to \infty} \frac{\mu^k}{k!} e^{-\mu}$.

Passiamo ora alla f.g.m. $\forall t \in \mathbb{R}$
$$
\begin{align}
M_{X_{n}}(t) &= \mathbb{E}[e^{tX_{n}}] = \mathbb{E}[e^{tY_{n}}]^n \\
&= (p_{n}e^t + (1 - p_{n}))^n = \left( 1 + \frac{np_{n}(e^t - 1)}{n} \right)^n
\end{align}
$$
dove, $X_{n} = \sum_{i=1}^n Y_{i}$ con $Y_{i} \sim Ber(p)$ i.i.d.
Usando di nuovo il limite notevole con
$Z_{n} = np_{n}(e^t - 1) \to z = \mu(e^t - 1)$ otteniamo
$$
M_{X_{n}}(t) \xrightarrow{n \to \infty} e^{\mu(e^t - 1)}
$$

# 5.4 - Approssimazione di Poisson

Torniamo al problema delle $m$ palline tirate a caso in $n$ urne. Sia di nuovo, per $i = 1, 2, \dots, n$
$$
X_{i}^{(m)} = \text{"\# palline nell'}i\text{-esima urna"}
$$
Nella sezione 5.2 avevamo notato che le $X_{i}^{(m)}$ *NON* sono indipendenti. Questo è il problema principale del modello delle urne, perché ad esempio *NON* ci permette di usare disuguaglianze di Chernoff.

*Domanda:* Perché le $X_{i}^{(m)}$ non sono indipendenti? Se lanciamo $m$ palline in $n$ urne e scopriamo che l'urna 1 è vuota, allora è meno probabile che la 2 sia vuota, poiché le $m$ palline devono ora essere distribuite in $n-1$ urne.

Avevamo notato che la distribuzione di $X_{i}^{(m)}$ era *quasi* quella di una Poisson di parametro $\frac{m}{n}$. Quello che vogliamo dimostrare ora è che la *distribuzione congiunta* di *tutte* le $X_{i}^{(m)}$ contemporaneamente è *quasi* quella di $n$ variabili di Poisson $Y_{1}^{(m)}, \dots, Y_{n}^{(m)}$. Faremo vedere che questa approssimazione vale a meno di un errore di $e \sqrt{ m }$ (che è trascurabile per eventi rari). *Che ci avremo guadagnato?* Saremo passati da un modello con dipendenze $(X_{1}^{(m)}, \dots, X_{n}^{(m)})$ ad uno più semplice da trattare, cioè quello di v.a. di Poisson indipendenti $(Y_{1}^{(m)}, \dots, Y_{n}^{(m)})$.

**TEOREMA 5.6:**
La distribuzione congiunta delle $Y_{1}^{(m)}, \dots, Y_{n}^{(m)}$ condizionata all'evento $\sum_{i=1}^n Y_{i} = k$ è la stessa di quella di $X_{1}^{(m)}, \dots, X_{n}^{(m)}$, indipendentemente dal valore di $m$. Cioè,
$\forall\ m,\ \forall k_{1},\dots,k_{m} \in \{0, 1, \dots\}$ tali che $\sum_{i=1}^n k_{i} = k$ si ha che
$$
P(X_{1}^{(k)} = k_{1}, \dots, X_{n}^{(k)} = k_{n}) = P\left( Y_{1}^{(m)} = k_{1}, \dots, Y_{n}^{(m)} = k_{n} \Bigg| \sum_{i = 1}^n Y_{i} = k\right)
$$
**DIMOSTRAZIONE:**
Tirando $k$ palline in $n$ urne, la probabilità che $X_{1}^{(k)} = k_{1}, \dots, X_{n}^{(k)}= k_{n}$ tale che $\sum_{i=1}^n k_{i} = k$ è
$$
P(X_{1}^{(k)} = k_{1}, \dots, X_{n}^{(k)}= k_{n}) = \frac{\binom{k}{k_{1}, k_{2}, \dots, k_{n}}}{n^k} = \frac{k!}{k_{1}!, \dots, k_{n}!} \frac{1}{n^k}
$$
Invece, usando la definizione di probabilità condizionata, abbiamo
$$
\begin{align}
P\left( Y_{1}^{(m)} = k_{1}, \dots, Y_{n}^{(m)} = k_{n} \bigg| \sum_{i=1}^{n} Y_{i}^{(m)} = k \right) &= \frac{P\left(\bigcap_{i=1}^n Y_{i}^{(m)} = k_{i}\right)}{P\left( \sum_{i=1}^n Y_{i}^{(n)} = k \right)}  \\
&= \frac{\prod_{i=1}^n P(Y_{i}^{(m)} = k_{i})}{P\left( \sum_{i=1}^n Y_{i}^{(m)} = k \right)}
\end{align}
$$
Per ogni $Y_{i}^{(m)}$ si ha $P(Y_{i}^{(m)} = k_{i}) = \frac{e^{-m/n}\left( \frac{m}{n} \right)^{k_{i}}}{k_{i}!}$. Inoltre, sappiamo che $\sum_{i=1}^{n} Y_{i}^{(m)} \sim Poi\left( \frac{m}{n} \cdot n\right)$, poiché somma di $n$ Poisson indipendenti di paramentro $\frac{m}{n}$. Mettendo tutto insieme
$$
\begin{align}
&P\left( Y_{1}^{(m)} = k_{1}, \dots, Y_{n}^{(m)} = k_{n} \bigg| \sum_{i=1}^{n} Y_{i}^{(m)} = k \right) = \frac{\prod_{i=1}^n \frac{e^{-m/n}\left( \frac{m}{n} \right)^{k_{i}}}{k_{i}!}}{\frac{e^{-m}m^k}{k!}} \\
&= \frac{\exp\left( -\sum_{i=1}^n\left( \frac{m}{n} \right) \right)}{e^{-m}} \cdot \frac{\left( \frac{m}{n} \right)^{\sum_{i=1}^n k_{i}}}{m^k} \cdot \frac{k!}{k_{1}! \cdots k_{n}!}  \\
&= \frac{e^{-m}}{e^{-m}} \cdot \frac{m^k}{n^km^k} \cdot \frac{k!}{k_{1}! \cdots k_{n}!} \\
&= \frac{1}{n^k} \frac{k!}{k_{1}! \cdots k_{n}!} = P\left(X_{1}^{(k)} = k_{1}, \dots, X_{n}^{(k)} = k_{n}\right)
\end{align}
$$

Conoscendo ora questa relazione tra le distribuzioni, possiamo provare risultati su qualsiasi funzione delle variabili aleatorie.

**TEOREMA 5.7:**
Sia $f$ una funzione *NON* negativa $f: \mathbb{N}_{0}^n \to \mathbb{R}$. Si ha che
$$
\mathbb{E}[f(X_{1}^{(m)}, \dots, X_{n}^{(m)})] \leq e\sqrt{ m }\ \mathbb{E}[f(Y_{1}^{(m)}, \dots, Y_{n}^{(m)})]
$$
**DIMOSTRAZIONE:**
Dal *Lemma 2.5* si ha
$$
\begin{align}
&\mathbb{E}[f(Y_{1}^{(m)}, \dots, Y_{n}^{(m)})] = \\
&=  \sum_{k=0}^{\infty}\mathbb{E}\left[ f(Y_{1}^{(m)}, \dots, Y_{n}^{(m)}) \bigg| \sum_{i=1}^{n}Y_{i}^{(m)} = m \right]P\left( \sum_{i=1}^n Y_{i}^{(m)} = m \right) \\
&\geq \mathbb{E}\left[ f(Y_{1}^{(m)}, \dots, Y_{n}^{(m)}) \bigg| \sum_{i=1}^{n}Y_{i}^{(m)} = m \right]P\left( \sum_{i=1}^n Y_{i}^{(m)} = m \right)  \\
&f\text{ non negativa, ogni addenso è non- negativo} \\
(\text{Teo 5.6)}&= \mathbb{E}[f(X_{1}^{(m)}, \dots, X_{n}^{(m)})]P\left( \sum_{i=1}^n Y_{i}^{(m)} = m \right) \\
&\text{poiché}\sum_{i=1}^{n} Y_{i}^{(m)} \sim Poi(m) \\
&= \mathbb{E}[f(X_{1}^{(m)}, \dots, X_{n}^{(m)})] e^{-m} \frac{m^m}{m!}  \\
&\geq \mathbb{E}[f(X_{1}^{(m)}, \dots, X_{n}^{(m)})]e^{-m} m^m \frac{1}{e\sqrt{ m }}\left( \frac{e}{m} \right)^m  \\
&=\mathbb{E}[f(X_{1}^{(m)}, \dots, X_{n}^{(m)})]\frac{1}{e\sqrt{ m }} \\
\end{align}
$$
Quindi, per concludere, abbiamo ottenuto che:
$$
\mathbb{E}[f(Y_{1}^{(m)}, \dots, Y_{n}^{(m)})] \geq \frac{1}{e\sqrt{ m }}\mathbb{E}[f(X_{1}^{(m)}, \dots, X_{n}^{(m)})]
$$
Ossia,
$$
\mathbb{E}[f(X_{1}^{(m)}, \dots, X_{n}^{(m)})] \leq e\sqrt{ m }\ \mathbb{E}[f(Y_{1}^{(m)}, \dots, Y_{n}^{(m)})]
$$

**COROLLARIO 5.9:**
Ogni evento di probabilità $p$ per le variabili di Poisson $Y_{1}^{(m)}, \dots, Y_{n}^{(m)}$ ha probabilità al più $pe\sqrt{ m }$ nel caso *esatto* delle urne $X_{1}^{(m)}, \dots, X_{n}^{(m)}$
**DIMOSTRAZIONE:** Basta prendere $d = \mathbb{1}_{\{\dots\}}$ nel teorema precedente, cioè la funzione dell'evento in questione. Allora $\mathbb{E}[\mathbb{1}_{\{\dots\}}]$ diventa la probabilità dell'evento stesso.
