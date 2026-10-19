
**TEOREMA 3.1 (Disuguaglianza di Markov)**
Sia $X$ una v.a. che assume valori positivi. Allora, $\forall a > 0$
$$
P(X \geq a) \leq \frac{\mathbb{E}[X]}{a}
$$
**DIMOSTARAZIONE:** Consideriamo la v.a.
$$
\mathbb{1}_{X \geq a} = 
\begin{cases}
1 \iff X \geq a \\
0 \text{ altrimenti}
\end{cases}
$$
Chiaramente, $\mathbb{1}_{X \geq a} \leq \frac{X}{a}$. Infatti
- $\mathbb{1} = 0$, ma $a > 0$ e $X \geq 0$ per ipotesi $\left( \mathbb{1} \leq \frac{X}{a} \right)$.
- $\mathbb{1} = 1$ se $X \geq a,\ \implies \frac{X}{a} \geq 1 = \mathbb{1}$
Poichè $\mathbb{1}$ è una v.a. che può assumere $0/1$, allora
$$
\begin{align}
&\mathbb{E}[\mathbb{1}_{X \geq a}] = P(\mathbb{1} = 1) = P(X \geq a). \quad \text{Quindi,} \\
&P(X \geq a) = \mathbb{E}[\mathbb{1}] \leq \mathbb{E}\left[ \frac{X}{a} \right] = \frac{\mathbb{E}[X]}{a}.
\end{align}
$$

# 3.2 - Varianza e Momenti di una v.a.

**DEF 3.1:** Si definisce *momento k-esimo* di una v.a. $X$ il valore atteso della v.a. $X^k$, cioè $\mathbb{E}[X^k]$.

*Osservazione:* È possibile che $\mathbb{E}[X^k] = \pm \infty$.
Quando una v.a. ha momento secondo finito possiamo definire la varianza, una sorta di *misura* di quanto la v.a. si allontana dalla sua media.

**DEF 3.2:** La *varianza* di una v.a. $X$ è definita come
$$
VAR[X] = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - \mathbb{E}[X]^2
$$
Inoltre, definiamo la *deviazione standard* di $X$ come 
$$\sigma(X) = \sqrt{VAR[X]}$$
*Osservazione:* Se una v.a. è costante, $X \equiv c$, allora la sua varianza è 0. Consideriamo invece le due v.a.
$$
Y = 
\begin{cases}
2 \text{ con } p = \frac{1}{2} \\
0 \text{ con } p = \frac{1}{2}
\end{cases}
\qquad
Z = 
\begin{cases}
1000 &\text{ con } p = \frac{1}{1000} \\
0 &\text{ con } p = 1 - \frac{1}{1000}
\end{cases}
$$
Allora, $\mathbb{E}[Y] = \mathbb{E}[Z] = 1$. Ma,
$$
VAR[Y] = \frac{1}{2} \cdot 4 - 1 = 1, \qquad VAR[X] = \frac{1000.000}{1000} - 1 = 999 
$$
Da questo esempio si osserva come la varianza ci dica quanto una v.a. possa prendere valori lontani dalla sua media.

**ATTENZIONE!** L'aspettazione è lineare! La varianza NO!

**DEF 3.2:** La *covarianza* delle v.a. $X,\ Y$ è
$$
\begin{align}
COV[X, Y] &= \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])] \\
&=\mathbb{E}[XY] -  \mathbb{E}[X]\mathbb{E}[Y]
\end{align}
$$
**TEOREMA 3.2**
$$
VAR[X + Y] = VAR[X] + VAR[Y] - 2COV[X,Y]
$$
**DIMOSTRAZIONE:**
$$
\begin{align}
VAR[X + Y] &= \mathbb{E}[(X + Y - \mathbb{E}[X+Y])^2] = \mathbb{E}[(X + Y - \mathbb{E}[X] - \mathbb{E}[Y])^2] \\
&= \mathbb{E}[(X - \mathbb{E}[X])^2 + (Y - \mathbb{E}[Y])^2 + 2(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])] \\
&= \mathbb{E}[(X - \mathbb{E}[X])^2] + \mathbb{E}[(Y - \mathbb{E}[Y])^2] + 2\mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])] \\
&=VAR[X] + VAR[Y] - 2COV[X,Y]
\end{align}
$$
*Osservazione:* La $COV$ è simmetrica: $COV[X,Y] = COV[Y,X]$

**TEOREMA 3.3 (Generalizzato)**
Se $X_{1} \dots, X_{n}$ sono v.a. mutualmente indipendenti, allora
$$
\mathbb{E}\left[ \prod_{i=1}^n X_{i}\right] = \prod_{i=1}^n \mathbb{E}[X_{i}]
$$

*Osservazione:* se $X \perp Y$, allora $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$.

**COROLLARIO:** Se $X \perp Y$, allora $COV[X,Y] = 0$. In particolare 
$$
VAR[X + Y] = VAR[X] + VAR[Y]
$$

**TEOREMA 3.5**
Se $X_{1}, \dots, X_{n}$ sono v.a. mutualmente indipendenti, allora
$$
VAR\left[ \sum_{i=1}^n X_{i} \right] = \sum_{i=1}^n VAR[X_{i}]
$$
**ATTENZIONE!**
$$
X \perp Y \implies COV(X,Y) = 0.
$$
Non vale però in generale che
$$
COV[X,Y] = 0 \nRightarrow X \perp Y
$$
Infatti, osserviamo il seguente *controesempio*. Sia $X$ la v.a. tale che
$$
X = 
\begin{cases}
1 \quad p = \frac{1}{3} \\
0 \quad p = \frac{1}{3} \\
-1 \quad p = \frac{1}{3}
\end{cases}
$$
Sia ora $Y = X^2$. Allora
$\mathbb{E}[X] = 0,\ \mathbb{E}[Y] = \frac{2}{3},\ \mathbb{E}[XY] = \mathbb[X^3] = 1\cdot \frac{1}{3} + 0 \cdot \frac{1}{3} + (-1)^3 \cdot \frac{1}{3} = 0$, e quindi $COV[X, Y] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] = 0$.
Ma, $P(X = 0 \land Y = 1) = 0 \neq P(X=0)P(Y=0) = \frac{2}{9}$ e questo dimostra che $X$ e $Y$ non sono indipendente anche se la covarianza è tra loro due è nulla. 

## 3.2.1 - Varianza della Binomiale

Sia $X \sim Bin(n,p)$. Sappiamo che $\mathbb{E}[X] = np$. Calcoliamo il momento secondo.
$$
\begin{align}
\mathbb{E}[X^2] &= \sum_{k=0}^n k^2 P(X = k) = \sum_{k=0}^n k^2 \binom{n}{k}p^k(1-p)^{n-k}  \\
k^2 = k(k-1) + k&= \underbrace{\sum_{k=0}^n k(k-1) \binom{n}{k} p^k(1-p)^k}_{(\star)} + \underbrace{\sum_{k_{0}}^n k \binom{n}{k}p^k(1-p)^{n-k}}_{ \mathbb{E}[X] = np} \\
\end{align}
$$
Sviluppiamo ora la prima serie, osserviamo che fa 0 per $k=0,1$.
$$
\begin{align}
(\star) &= \sum_{k=2}^{n} k(k-1) \frac{n!}{k!(n-k)!}p^k(1-p)^{n-k} \\
&= n(n-1)p^2 \sum_{k=2}^n \frac{(n-2)!}{(k-2)!(n-k)!}p^{k-2}(1-p)^{n-k} \\
j = k-2&= n(n-1)p^2\sum_{j=0}^{n-2} \frac{(n-2)!}{j!(n-j-2)!}p^j(1-p)^{n-j-2}  \\
&= n(n-1)p^2 \underbrace{\sum_{j=0}^{n-2} P(Bin(n-2, p) = j)}_{=1} = n(n-1)p^2
\end{align}
$$
Quindi,
$$
\boxed{\mathbb{E}[X^2] = n(n-1)p^2 + np}
$$
$$
VAR[X] = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = n(n-1)p^2 + np -n^2p^2 = np(1-p) \\
$$
Alternativamente, poichè $X = \sum_{i=1}^n X_{i},\quad X_{i} \sim Ber(p)$ i.i.d. con $VAR[X_{i}] = p(1-p)$, allora
$$
VAR[X] = VAR\left[ \sum_{i=1}^n X_{i}\right] = \sum_{i=1}^n VAR[X_{i}] = np(1-p)
$$
# 3.3 - Disuguaglianza di Chebychev

**TEOREMA 3.6 (Disuguaglianza di Chebychev)**

Sia $X$ una v.a. con media finita e varianza finita, $\forall a > 0$
$$
P(|X - \mathbb{E}[X]| \geq a) \leq \frac{VAR[X]}{a^2}
$$
**DIMOSTRAZIONE:**
$$
\begin{align}
P(|X - \mathbb{E}[X]| \geq a) &= P(|X - \mathbb{E}[X]|^2 \geq a^2)  \\
\text{Markov}&\leq \frac{\mathbb{E}[|X - \mathbb{E}[X]|^2]}{a^2} = \frac{VAR[X]}{a^2}
\end{align}
$$

Riformuliamo la disuguaglianza in modo da mettere in relazione la deviazione della media di $X$ con la sua deviazione standard e con la sua media.

**COROLLARIO 3.7:** $\forall t \geq 1$
- $P(|X - \mathbb{E}[X]| \geq t\sigma(X)) \leq \frac{1}{t^2}$
- $P(|X - \mathbb{E}[X]| \geq t\mathbb{E}[X]) \leq \frac{VAR[X]}{t^2\mathbb{E}[X]^2}$

**LEMMA 3.8**
Sia $X \sim Geom(p)$. Allora
$$
\boxed{VAR[X] = \frac{1-p}{p^2} = \frac{q}{p^2}}
$$
**DIMOSTRAZIONE:** Sappiamo che $\mathbb{E}[X] = \frac{1}{p}$ e perciò
$$
VAR[X] = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \underbrace {\sum_{k=1}^{\infty}k^2(1-p)^{k-1}p}_{(\star)} - \frac{1}{p^2}
$$
Vediamo ora quanto fa la sommatoria $(\star)$.

$$
\begin{align}
(\star) &= \sum_{k \geq 1} k^2 (1-p)^{k-1}p = \\
k^2 = (k^2 - k) + k&= \sum_{k \geq 1} (k^2-k)(1-p)^{k-1}p + \underbrace{\sum_{k \geq 1} k(1-p)^{k-1}p}_{\mathbb{E}[X] = \frac{1}{p}}
\end{align}
$$

Sia $F(p) = p(1-p) \sum_{k \geq 2} k(k-1) (1-p)^{k-2}$. Usiamo ora che, per $|x| < 1$, $$\frac{1}{1-x} = \sum_{k\geq 0} x^k,$$
derivando due volte, otteniamo
$$
\begin{align}
&D''\left( \frac{1}{1-x} \right) = D'\left( \frac{1}{(1-x)^2}\right) = \sum_{k \geq 1}{k x^{k-1}} \\
&D'\left( \frac{1}{(1-x)^2} \right) = \frac{2}{(1-x)^3} = \sum_{k \geq 2} k(k-1)x^{k-2}
\end{align}
$$
Usiamo questa formula all'interno di $F(p)$ con $x = 1-p$, otteniamo
$$
F(p) = p(1-p) \frac{2}{p^3} = \frac{2(1-p)}{p^2}
$$
e quindi, $\mathbb{E}[X^2] = D(p) + \frac{1}{p} = \frac{1-p}{p^2}$.
In conclusione,
$$
VAR[X] = \frac{2-p}{p^2} - \frac{1}{p^2} = \frac{1-p}{p^2}
$$

##### Metodo alternativo per calcolare $VAR[X],\ X \sim Geom(p)$.

Sappiamo che 
$$
VAR[X] = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \mathbb{E}[X^2] - \frac{1}{p^2}
$$

Calcoliamo ora $\mathbb{E}[X^2]$ come abbiamo fatto per $\mathbb{E}[X]$, applicando la perdità di memoria della geometrica e il valor medio condizionato.
Sia
$$
Y = \begin{cases}
1 \iff \text{ il primo lancio è T} \\
0 \text{ altrimenti}
\end{cases}
$$
Calcoliamo $\mathbb{E}[X^2]$ condizionando al fatto che il primo lancio è testa o croce.
$$
\begin{align}
\mathbb{E}[X^2] &= P(Y = 0)\mathbb{E}[X^2|Y = 0] + P(Y = 1)\mathbb{E}[X^2 | Y = 1]  \\
&= (1-p)\mathbb{E}[X^2 | Y = 0] + p\mathbb{E}[X^2 | Y = 1]
\end{align}
$$
Se $Y = 1$, allora anche $X = 1$ e quindi $\mathbb{E}[X^2|Y=1] = 1$. Se $Y = 0$, allora $X > 1$. In questo caso, sia $Z$ il numero di lanci rimanenti prima che esca $T$. Allora
$$
\begin{align}
\mathbb{E}[X^2] &= (1-p)\mathbb{E}[(Z + 1)^2] + p \\
&= (1-p)\mathbb{E}[Z^2] + 2(1-p)\mathbb{E}[Z] + 1 - p + p \\
&= (1-p)\mathbb{E}[Z^2] + 2(1-p)\mathbb{E}[Z] + 1
\end{align}
$$
Applicando la perdità di memoria della geoemetrica, anche $Z$ a sua volta è una v.a. geometrica di parametro $p$. Sapendo quindi che $\mathbb{E}[Z] = \frac{1}{p}$ e $\mathbb{E}[X^2] = \mathbb{E}[Z^2]$, otteniamo l'equazione
$$
\begin{align}
\mathbb{E}[X^2] &= (1-p)\mathbb{E}[X^2] + \frac{2(1-p)}{p} + 1 \\
&= (1-p)\mathbb{E}[X^2] + \frac{2-p}{p} \\
&\implies \mathbb{E}[X] = \frac{2-p}{p^2}
\end{align}
$$