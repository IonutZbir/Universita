
# 4.1 Funzione Generatrice dei Momenti

**DEF 4.1:** La funzione generatrice dei momenti (f.g.m.) di una v.a. $X$
$$
\begin{align}
M_{X}: \mathbb{R} &\to (0, \infty) \cup \{+\infty\} \\
t &\to M_{X}(t) = \mathbb{E}[e^{tX}]
\end{align}
$$
*Osservazioni:*
- $M_{X}(0) = 1\ \forall$ v.a.
- $M_{X}(t)$ può valere $+\infty$ per qualche $t$
- Se $X$ è limitata (cioè $P(a \leq X \leq b) = 1$) per qualche $a, b \in \mathbb{R}$) allora $M_{X}(t) < \infty\ \forall t \in \mathbb{R}$. Non è vero il viceversa, cioè esistono v.a. non limitate per cui $M_{X}(t) < \infty\ \forall t$ (Gaussiana)

**TEOREMA 4.1**
Sia $X$ una v.a. con $M_{X}(t)$ finita in un intorno dell'origine (cioè $\exists\ \delta > 0:\ M_{X}(t) < \infty\ \forall t \in (-\delta, \delta)$). Allora si può derivare rispetto a $t$ dentro l'aspettazione, e si ha
$$
M_{X}^{(n)}(t)\bigg|_{t=0} = \mathbb{E}[X^n]\ \forall\ n=1,2,3,\dots
$$
**DIMOSTRAZIONE:** Prendendo per buona la derivazione dentro l'aspettazione, si ha
$$
M_{X}^{(n)}(t) = \frac{d}{dt^n} \mathbb{E}[e^{tX}] = \mathbb{E}[X^n e^{tX}] \bigg|_{t=0} = \mathbb{E}[X^n]
$$

### Funzione generatrice per $Ber(p)$ e $Bin(n,p)$

Sia $X \sim Ber(p)$, allora
$$
\begin{align}
M_{X}(t) = \mathbb{E}[e^{tX}] = p + e^{t \cdot 1} + (1-p)e^{t \cdot 0} = e^tp + 1-p
\end{align}
$$

Sia ora $Y \sim Bin(n,p)$. Possiamo scrivere $Y = \sum_{i=1}^n Y_{i}$ dove $Y_{i} \sim Ber(p)$. Allora
$$
\begin{align}
M_{Y}(t) &= \mathbb{E}[e^{tY}] = \mathbb{E}\left[ e^{t\sum_{i=1}^n Y_{i}} \right] \underbrace{=}_{\text{ind.}} \prod_{i=1}^n \mathbb{E}[e^{tY_{i}}]  \\
&= \prod_{i=1}^n (e^tp + 1 - p) = (e^tp + 1 - p)^n 
\end{align}
$$

## 4.1.2 Funzione generatrice v.a. geometrica

Sia $X \sim Geom(p)$. Calcoliamo $M_{X}(t)$.
$$
\begin{align}
M_{X}(t) &= \mathbb{E}[e^{tX}] = \sum_{k=1}^{\infty} e^{tk}P(X = k)  \\
&= \sum_{k=1}^{\infty} e^{tk} (1-p)^{k-1}p  \\
&\text{moltiplico e divido per }(1-p) \\
&= \frac{p}{1-p}\sum_{k=1}^\infty(e^t(1-p))^k = 
\begin{cases}
\frac{p}{1-p} \frac{e^t(1-p)}{1 - e^t(1-p)} \iff e^t(1-p) < 1 \\
\infty \text{ altrimenti}
\end{cases}\\ \\
&= \begin{cases}
\frac{pe^t}{1-(1-p)e^t} &\iff t < -\log(1-p) \\
\infty &\iff t \geq -\log(1-p)
\end{cases}

\end{align}
$$

Quindi, per ogni $p \in (0,1)$ la condizione del teorema è soddisfatta con $\delta = -\log(1-p)$. Facendo le derivate si osserva che
- $M'_{X}(t) = p(1-(1-p)e^t)^{-2}e^t$
- $M''_{X}(t) = 2p(1-p)(1-(1-p)e^t){-3}e^{2t} + p(1-(1-p)e^t)^{-2}e^t$
Prendendo $t=0$, con il teorema otteniamo che
$$
\begin{align}
\mathbb{E}[X] &= M'_{X}(t)\bigg|_{t=0} = \frac{1}{p} \\
\mathbb{E}[X^2] &= M''_{X}(t) \bigg|_{t=0} = \frac{2-p}{p^2}
\end{align}
$$

**TEOREMA 4.2:** Siano $X$ e $Y$ due v.a. tali che $M_{X}(t) = M_{Y}(t)\ \forall t \in (-\delta, \delta)$ per qualche $\delta$, allora $X \sim Y$, cioè $X$ ed $Y$ hanno la stessa distribuzione.

**TEOREMA 4.3:** Siano $X$ e $Y$ due v.a. *indipendenti*, allora
$$
M_{X+Y}(t) = M_{X}(t) \cdot M_{Y}(t)
$$
**DIMOSTRAZIONE:**
$$
\begin{align}
M_{X+Y}(t) &= \mathbb{E}[e^{(X+Y)t}] = \mathbb{E}[e^{Xt} e^{Yt}]  \\ 
&= \mathbb{E}[e^Xt]\mathbb{E}[e^Yt] = M_{X}(t) \cdot M_{Y}(t)
\end{align}
$$
**COROLLARIO 4.3:** Se $X_{1}, \dots X_{n}$ sono mutualmente indipendenti, si ha
$$
M_{\sum_{i=1}^n X_{i}}(t) = \prod_{i=1}^n M_{X_{i}}(t)
$$

Consideriamo ora $X \sim Bin(n,p)$ e $Y \sim Bin(m, p)$, e calcoliamo $M_{X + Y}$, allora
$$
\begin{align}
M_{X + Y}(t) &\underbrace{=}_{\text{Teo. } 4.3} M_{X}(t) \cdot M_{Y}(t) = (e^tp + 1 - p)^n \cdot (e^tp + 1 - p)^m \\
&= (e^tp + 1-p)^{n+m} \sim Bin(n+m, p).
\end{align}
$$
E questo verifica quanto detto nel capitolo 2.

# 4.2 Disuguaglianza di Chernoff

La disuguaglianza di Chernoff per un'unica v.a. $X$ serve a limitare la coda della v.a.

- *Coda a $+\infty$:* $\forall\ a \in \mathbb{R}$ si ha $$
P(X \geq a) \leq \frac{M_{X}(t)}{e^{ta}}\ \forall\ t>0
$$ Infatti, $$ P(X \geq a) = P(e^{tX} \geq e^{ta}) \leq \frac{\mathbb{E}[e^{tX}]}{e^{ta}} = \frac{M_{X}(t)}{e^{ta}}$$Poichè $t > 0$, la funzione $x \to e^{tx}$ è crescente. Infine, applichiamo Markov con $Y = e^{tX}$. A questo punto si può ottimizzare la disuguaglianza su $t$: $$\forall a > 0,\ P(X \geq a) \leq \min_{t>0} \frac{\mathbb{E}[e^{tX}]}{e^{ta}}$$
- *Coda a $-\infty$* $\forall\ a \in \mathbb{R}$ si ha $$P(X \leq a) \leq \min_{t < 0}\frac{M_{X}(t)}{e^{ta}}$$Infatti, $$P(X \leq a) = P(e^{Xt} \geq e^{ta}) \leq \frac{\mathbb{E}[e^{tX}]}{e^{ta}} = \frac{M_{X}(t)}{e^{ta}}$$
*NOTA:* Le disuguaglianze di Chernoff si ottengono tutte in questo modo (si prende l'esponenziale, si applica Markov e poi si ottimizza su $t$). 

## 4.2.1 Disuguaglianza di Chernoff per Somme di "Poisson Trials"

Ora vediamo un caso classico: la disuguaglianza di Chernoff per *Poisson Trials* (diverse dalle v.a. di Poisson).

**DEF 4.2:** Siano $X_{1}, \dots, X_{n}$ Bernoulliane indipendenti di parametri $p_{i} = p_{1}, \dots, p_{n}$. (Se $p_{1} = \dots = p_{n}$ sono dette anche *Bernoulli Trials* e corrispondono ad una $Bin(n,p)$). Le $X_{1}, \dots, X_{n}$ sono dette *Poisson Trials*.
Siano
$$
X = \sum_{i=1}^{n} X_{i} \qquad \mu = \mathbb{E}[X] = \sum_{i=1}^n\mathbb{E}[X_{i}] = \sum_{i=1}^{n} p_{i}
$$
**LEMMA LOWER BOUND:** La f.g.m. di $X\sim$ Poisson Trials è al più
$$
\boxed{M_{X}(t) \leq e^{\mu(e^t - 1)}}
$$
**DIMOSTRAZIONE:**
$$
\begin{align}
\mathbb{E}[e^{tX}] &= \mathbb{E}\left[ e^{t\sum_{i=1}^n X_{i}}  \right] = \mathbb{E}\left[ \prod_{i=1}^n e^{tX_{i}} \right] = \prod_{i=1}^n \mathbb{E}[e^{tX_{i}}]  \\
&= \prod_{i=1}^n(e^tp_{i} + (1 - p_{i})) = \prod_{i=1}^n (1 + p_{i}(e^t - 1))
\end{align}
$$
Usando la disuguaglianza $1 + x \leq e^x\ \forall\ x$, otteniamo,
$$
\begin{align}
M_{X}(t) &= \mathbb{E}[e^{tX}] \leq \prod_{i=1}^n \exp({p_{i}(e^t - 1))}  \\
&= \exp\left( \sum_{i=1}^n p_{i}(e^t - 1) \right) = \exp(\mu(e^t - 1))
\end{align}
$$

**TEOREMA 4.4 - Disuguglianza di Chernoff** Siano $X_{1}, \dots, X_{n}$ con $X = \sum_{i=1}^n X_{i}$ delle Poisson Trials con parametri $p_{1}, \dots, p_{n}$ e $\mathbb{E}[X] = \sum_{i=1}^n p_{i} = \mu$. Allora,
1. $$
\forall \delta > 0, \quad P(X \geq (1+\delta)\mu) \leq \left( \frac{e^\delta}{(1+\delta)^{(1+\delta)}} \right)^\mu
$$
2. $$\forall 0 < \delta \leq 1, \quad P(X \geq (1+\delta)\mu) \leq e^{-\mu \frac{\delta^2}{3}}$$
3. $$\text{Per } R \geq 6\mu,\quad P(X \geq R) \leq 2^{-R}$$
**DIMOSTRAZIONE:** La 1. è il vero Chernoff Bound mentre la 2. e la 3. sono conseguenze.

Iniziamo con la (1)
$$
\begin{align}
P(X \geq (1+\delta)\mu) &\underbrace{=}_{t > 0} P(e^{tX} \geq e^{t(1+\delta)\mu})  \\
\text{Markov}&= \frac{\mathbb{E}[e^{tX}]}{e^{t(1+\delta)\mu}} \underbrace{\leq}_{\text{Lemma LB}} \frac{e^{(e^t - 1)\mu}}{e^{t(1+\delta)\mu}}
\end{align}
$$
Qui possiamo ottimizzare per $t > 0$. Prendendo $t = \log(1+\delta) > 0$,
$$
P(X \geq (1+\delta)\mu) \leq \left( \frac{e^\delta}{(1+\delta)^{(1+\delta)}} \right)^\mu
$$
Per dimostrare la (2) dobbiamo mostrare che $\forall \delta \in (0,1]$,
$$
\frac{e^\delta}{(1+\delta)^{(1+\delta)}} \leq e^{\frac{-\delta^2}{3}}
$$
Prendendo il logaritmo, vediamo che ciò equivale a
$$
f(\delta) = \delta - (1-\delta)\log(1+\delta) + \frac{\delta^2}{3} \leq 0
$$
Notiamo che $f(0) = 0$ e studiamo le derivate.
- $f'(\delta) = \frac{1-(1+\delta)}{1+\delta} - \log(1+\delta) + \frac{2\delta}{3} = -\log(1+\delta) + \frac{2\delta}{3}$
- $f''(\delta) = - \frac{1}{1+\delta} + \frac{2}{3}$
$$
\text{Siccome }
\begin{cases}
f''(\delta) < 0 \iff \delta \in \left[ 0, \frac{1}{2} \right) \\
f''(\delta) > 0 \iff \delta > \frac{1}{2}
\end{cases}
$$
abbiamo che $f'(\delta)$ decresce tra $0$ e $\frac{1}{2}$ e poi cresce fra $\frac{1}{2}$ e $1$. Ma poiché $f'(0) = 0$ e $f'(1) < 0$, ne segue che $f'(\delta) \leq 0$ in tutto l'intervallo $[0,1]$. Quindi $f(\delta)$ è decrescente su tutto l'intervallo, e poichè $f(0) = 0$ abbiamo la disuguaglianza voluta $\forall \delta \in (0, 1]$

Per quanto riguarda la (3). Poniamo $R = (1+\delta)\mu$. Poiché $R \geq 6\mu$, si ha $\delta \geq 5$. Perciò usando il punto (1),
$$
P(X \geq (1+\delta)\mu) \leq \left( \frac{e^\delta}{(1+\delta)^{1 + \delta}} \right)^\mu \leq \left( \frac{e}{(1+\delta)} \right)^{(1+\delta)\mu} \leq \left( \frac{e}{6} \right)^R \leq 2^{-R}
$$
*Analogamente, valgono i suguenti risultati:*

**TEOREMA 4.5:** Siano $X_{1}, \dots, X_{n}$ come nel teorema 4.4. Allora, $\forall \delta \in (0,1)$
1. $$P(X \leq (1-\delta)\mu) \leq \left( \frac{e^-\delta}{(1-\delta)^{(1-\delta)}} \right)^\mu$$
2. $$P(X \leq (1-\delta)\mu) \leq e^{-\mu \frac{\delta^2}{2}}$$
**COROLLARIO 4.6:** Siano $X_{1}, \dots, X_{n}$ come nel teorema 4.4. Allora
$$
P(|X - \mu| \geq \delta \mu) \leq 2e^{-\mu \frac{\delta^2}{3}}, \quad \forall \delta \in (0,1)
$$
**DIMOSTRAZIONE:**
$$
\begin{align}
P(|X-\mu|\ge \delta\mu) &= P(X \ge (1+\delta)\mu) + P(X \le (1-\delta)\mu)  \\
&= e^{-\mu\delta^2/3} + e^{-\mu\delta^2/2} \leq 2e^{-\mu\delta^2/3}
\end{align}
$$

### Esempio: Confronto tra Markov, Chebychev e Chernoff

Qual'è la probabilità di avere almeno $\frac{3n}{4}$ volte *testa* su $n$ lanci di moneta? Siano
$$
X_{i} = 
\begin{cases}
1\ i\text{-esimo lancio è testa} \\
0\ i\text{-esimo lancio è croce}
\end{cases}
$$

Poiché $P(X_{i} = 1) = \frac{1}{2}$, segue che 
$$\mathbb{E}[X] = \frac{n}{2}, \quad VAR[X] = \frac{n}{4}$$

- *Markov:*$$P\left( X \geq \frac{3n}{4} \right) \leq \frac{\frac{n}{2}}{\frac{3n}{g}} = \frac{n}{2} \cdot \frac{4}{3n} = \frac{2}{3}$$
- *Chebychev:* $$\begin{align}
P\left( X \geq \frac{3n}{4} \right) &= P\left( X - \frac{n}{2} \geq \frac{3n}{4} - \frac{n}{2}\right) = P\left( X - \mathbb{E}[X] \geq \frac{n}{4} \right)  \\
&\leq P\left( |X - \mathbb{E}[X]| \geq \frac{n}{4} \right) \leq \frac{VAR[X]}{\frac{1}{16n^n}} = \frac{n}{4} \cdot \frac{16}{n^2} = \frac{4}{n}
\end{align}
$$Osserviamo che è una stima migliore rispetto a quella con Markov, in quanto tende a 0, per $n \to \infty$.
- *Chernoff:* $$P\left( X \geq \frac{3n}{4} \right) \leq P\left( |X - \frac{n}{2}| \geq \frac{1}{2} \frac{n}{2} \right) \leq 2e^{-\frac{-\mu}{3}} \leq 2e^{-n/24}$$Applicando il *corollario 4.6*. Osserviamo che in questo caso il decadimento è esponenziale, il che è migliore di Chebychev!

*Osservazione:* Succede spesso che la deviazione della media della somma di $n$ v.a. sia dell'ordine di $O(\sqrt{n\log n })$. Nel caso delle monete
$$
\begin{align}
P\left( |X - \mu| \geq \frac{1}{2} \sqrt{ 6n\log (n) } \right) &\leq 2\exp\left[ -\frac{\mu}{3} \frac{(\sqrt{ 6n\log(n) })^2}{n}\right]  \\
&= 2e^{-\log n} = \frac{2}{n}
\end{align}
$$

# 4.3 Disuguaglianze Migliorate per Casi Speciali

Possimo migliorare Chernoff quando 
$$
X_{i} = 
\begin{cases}
1 \quad p = \frac{1}{2} \\
-1 \quad p = \frac{1}{2}
\end{cases}
$$
sono variabili aleatori di *Rademacher*.
**TEOREMA 4.7**
Siano $X_{1}, \dots, X_{n}$ v.a. di Rademacher indipendenti. Sia $X = \sum_{i =1}^n X_{i}$. Allora, $\forall a > 0$,
$$P(X \geq a) \leq e^{\frac{-a^2}{2n}}$$
**DIMOSTRAZIONE:**
$$
P(X \geq a) = P(e^{tX} \geq e^{ta}) \leq \frac{\mathbb{E}[e^{tX}]}{e^{ta}} = \prod_{i=1}^n \frac{\mathbb{E}[e^{tX_{i}}]}{e^{ta}} \leq \exp\left( \frac{nt^2}{2} - ta \right)
$$
Dobbiamo calcolare ora $\mathbb{E}[e^{tX_{i}}]$. Abbiamo che
$$
\begin{align}
\mathbb{E}[e^{tX_{i}}] &= \frac{1}{2}e^t + \frac{1}{2}e^{-t} = \frac{1}{2}\left( \sum_{l=0}^\infty \frac{t^l}{l!} + \sum_{l=0}^\infty \frac{(-t)^l}{l!} \right) \\
\text{i termini dispari si cancellano}&= \frac{1}{2\left( 2\sum_{l=0}^\infty \frac{t^{2l}}{(2l)!}\right)}  \\
&\leq \sum_{l=0}^\infty \frac{\left( \frac{t^2}{2} \right)^l}{l!} = e^{t^2/2} 
\end{align}
$$
Ottimizzando con $t = \frac{a}{n}$ otteniamo $P(X \geq a) \leq e^{-a^2/2n}$.

**COROLLARIO 4.8:** Sotto le stesse ipotesi, vale che
$$
P(|X| \geq a) \leq 2\exp\left( -\frac{a^2}{2n} \right) \quad\ \forall a > 0
$$

**COROLLARIO 4.9:** Siano $Y_{1}, \dots, Y_{n} \sim Ber\left( \frac{1}{2} \right)$ indipendenti e sia $Y = \sum_{i=1}^n Y_{i}$ (stiamo considerando delle Bernoulli trials con $\mathbb{E}[Y] = \mu = \frac{n}{2}$). Allora,
$$
\begin{align}
&\boxed{P(Y \geq (1+\delta)\mu) \leq e^{-\delta^2\mu} \quad \forall\ \delta > 0} \\ \\
&\boxed{P(Y \geq \mu + a) \leq \exp\left( -\frac{2a^2}{n} \right) \quad \forall\ a > 0}
\end{align}
$$

*Nota:* Il punto (2) del corollario 4.9 migliora il punto (2) del teorema 4.4. La costante all'esponente è 1 invece che $\frac{1}{3}$.

**DIMOSTRAZIONE:** Usando la trasformazione $Y_{i} = \frac{X_{i}+1}{2}$ con $X_{i}$ i.i.d. Rademacher come nel teorema 4.7, si ha $Y = \frac{X}{2} + \mu$ con $X = \sum_{i=1}^n X_{i}$. Allora,
$$
P(Y \geq \mu + a) \underbrace{=}_{\frac{X}{2} + \mu \geq \mu + a} P(X \geq 2a) \underbrace{\leq}_{\text{TEO. } 4.7} \exp\left( -\frac{4a^2}{2n} \right) = \exp\left( -\frac{2a^2}{n} \right)
$$
A questo punto, ponendo $a = \delta \mu = \frac{\delta n}{2}$ otteniamo
$$
P(Y \geq (1+\delta)\mu) = P(X \geq 2\delta \mu) \leq \exp\left( -\frac{2\delta^2\mu^2}{n} \right) \underbrace{=}_{\mu = \frac{n}{2} \to n = 2\mu} e^{-\delta^2\mu}
$$
**COROLLARIO 4.10:** Siano $Y_{1} \dots, Y_{n} \sim Ber\left( \frac{1}{2} \right)$ indipendenti, allora
1. $P(Y \leq \mu - a) \leq \exp\left( -\frac{2a^2}{n} \right) \quad \forall\ a \in (0, \mu)$
2. $P(Y \leq (1+\delta)\mu) \leq e^{-\delta^2\mu} \quad \forall\ a \in (0,1)$

*Osservazione:* La (2) migliora la (2) del teorema 4.5.

# 4.5 Disuguaglianza di Hoeffding

Finora abbiamo visto disuguaglianze per (somme di) Bernoulli e Rademacher. Le disuguaglianze di Hoeffding generalizzano i risultati a v.a. a supporto limitato.

**TEOREMA 4.12 (Disuguaglianza di Hoeffding).**
Siano $X_{1}, \dots, X_{n}$ v.a. indipendenti con media comune $\mu = \mathbb{E}[X_{i}]$ tali che $P(a \leq X_{i} \leq b) = 1\ \forall X_{i} = 1, \dots, n$ e per qualche costante $a,b \in \mathbb{R}$. Allora,
$$
P\left( \bigg|\frac{1}{n} \sum_{i=1}^n X_i - \mu \bigg| \geq \epsilon \right) \leq 2\exp\left( \frac{-2n\epsilon^2}{(b-a)^2} \right)
$$
*Nota:* Anche questa è una disuguaglianza di concentrazione: ci dice  che la probabilità che la v.a. $X = \frac{1}{n}\sum_{i=1}^n X_{i}$ devii dalla sua media $\mu$ più di $\epsilon$ decade esponenzialmente veloce in $n$.

**DIMOSTRAZIONE:** La dimostrazione utilizza la solita strategia: esponenziale + Markov + ottimizzazione.

Siano $Z_{i} = X_{i} - \mathbb{E}[X_{i}]$ e $Z = \frac{1}{n} \sum_{i=1}^{n} Z_{i}$. Per ogni $\lambda > 0$,
$$
P(Z \geq \epsilon) = P(e^{\lambda Z} \geq e^{\lambda \epsilon}) \underbrace{\leq}_{\text{Markov}} \frac{\mathbb{E}[e^{\lambda Z}]}{e^{\lambda\epsilon}} = \prod_{i=1}^n \frac{\mathbb{E}\left[ \exp\left( \frac{\lambda Z_{i}}{n} \right) \right]}{e^{\lambda\epsilon}}
$$
Ora ci serve una stima della f.g.m. di una v.a. a supporto limitato.

**LEMMA 4.13 (Lemma di Hoeffding):**
Sia $Y$ una v.a tale che $\mathbb{E}[Y] = 0$ e $P(a \leq Y \leq b) = 1$. Allora
$$
\mathbb{E}[e^{tY}] \leq \exp\left( \frac{t^2(b-a)^2}{8} \right)
$$
Tornando alla dimostrazione, applichiamo il lemma con $Z_{i} = Y$ e $\frac{\lambda}{n} = t$ ottenendo
$$
\mathbb{E}\left[ e^{\frac{\lambda Z_{i}}{n}} \right] \leq \exp\left( \frac{\lambda^2}{n^2} \frac{(b - \mu - (a - \mu))^2}{8}\right) \quad \text{ dove } a-\mu \leq Z_{i} \leq b - \mu
$$
Quindi,
$$
P(Z \geq \epsilon) \leq e^{-\lambda\epsilon} \prod_{i=1}^n \exp\left( \frac{\lambda^2}{n^2} \frac{(b-a)^2}{8} \right) = \exp\left( -\lambda\epsilon + \frac{\lambda^2}{n} \frac{(b-a)^2}{8} \right)
$$
Ponendo $\lambda = \frac{4n\epsilon}{(b-a)^2}$ otteniamo
$$
P\left( \frac{1}{n} \sum_{i=1}^n X_{i} - \mu \geq \epsilon \right) = P(Z \geq \epsilon) \leq \exp\left( -\frac{2n\epsilon^2}{(b-a)^2} \right)
$$
Ripetendo l'argomento per $P(Z \leq -\epsilon)$ con $\lambda = -\frac{4n\epsilon}{(b-a)^2}$ otteniamo
$$
P\left( \frac{1}{n} \sum_{i=1}^n X_{i} - \mu \leq \epsilon\right) \leq \exp\left( -\frac{2n\epsilon^2}{(b-a)^2} \right)
$$
Combinando le due disuguaglianze ottenamo il teorema.

*Esempio:* Siano $X_{1}, \dots, X_{n}$ indipendenti uniformi su $\{0, \dots, L\}$. Si ha $\forall\ i$ che $\mathbb{E}[X_{i}] = L_{2}$. Applichiamo il teorema 4.13
$$
P\left( \bigg|\frac{1}{n} \sum_{i=1}^n X_i - \frac{L}{2} \bigg| \geq \epsilon \right) \leq 2\exp\left( -\frac{2n\epsilon^2}{L^2} \right)
$$

Infine, una generalizzazione ulteriore con v.a. non distribuite identicamente tra loro.

**TEOREMA 4.14:**
Siano $X_{1}, \dots, X_{n}$ v.a. indipendenti con $\mathbb{E}[X_{i}] = \mu_{i}$ e $P(a_{i} \leq X_{i} \leq b_{i}) = 1$ per certe costanti $a_{i}, b_{i} \in \mathbb{R}$. Allora
$$
P\left( \Bigg|\sum_{i=1}^n X_{i} - \sum_{i=1}^n \mu_{i} \Bigg| \right) \geq \epsilon) \leq 2\exp\left(-\frac{2\epsilon^2}{\sum_{i=1}^n (b_{i} - a_{i})^2} \right)
$$

*Esempio:* Siano $X_{1}, \dots, X_{n}$  indipendenti con $X_{i}$ uniformi in $\{0, \dots, i\}$. Sia $X = \sum_{i=1}^n X_{i}$. Si ha $\mathbb{E}[X_{i}] = \frac{i}{2},\ \mathbb{E}[X] = \sum_{i=1}^n \mathbb{E}[X_{i}] = \frac{n(n+1)}{4}$.
Dal teorema 4.14, 
$$
\begin{align}
P\left( \bigg| X - \frac{n(n+1)}{4} \bigg| \geq \epsilon \right) &\leq 2 \exp\left( -\frac{2\epsilon^2}{\sum_{i=1}^n i^2 } \right) \\
&= 2\exp\left(\frac{-12\epsilon^2}{n(n+1)(2n+1)} \right)
\end{align}
$$