## Disuguaglianza di Chernoff (base)

- Coda superiore: $\forall a \in \mathbb{R}$ $$P(X\ge a) \le \min_{t>0} \frac{M_X(t)}{e^{ta}}$$
- Coda inferiore: $\forall a \in \mathbb{R}$ $$P(X\le a) \le \min_{t<0} \frac{M_X(t)}{e^{ta}}$$

## Teorema 4.4

Siano $X_1,\dots,X_n$ Poisson Trials, $X=\sum_i X_i$, $\mu = \mathbb{E}[X]$.

1. $$\forall \delta>0,\quad P(X \ge (1+\delta)\mu) \le \left(\frac{e^\delta}{(1+\delta)^{1+\delta}}\right)^\mu$$
2. $$\forall\ 0<\delta\le 1,\quad P(X \ge (1+\delta)\mu) \le e^{-\mu\delta^2/3}$$
3. $$\text{Per } R\ge 6\mu,\quad P(X\ge R) \le 2^{-R}$$

## Teorema 4.5

Siano $X_1,\dots,X_n$ Poisson Trials, $X=\sum_i X_i$, $\mu = \mathbb{E}[X]$.
$\forall \delta \in (0,1)$:

1. $$P(X \le (1-\delta)\mu) \le \left(\frac{e^{-\delta}}{(1-\delta)^{1-\delta}}\right)^\mu$$
2. $$P(X \le (1-\delta)\mu) \le e^{-\mu\delta^2/2}$$

## Corollario 4.6

Siano $X_1,\dots,X_n$ Poisson Trials, $X=\sum_i X_i$, $\mu = \mathbb{E}[X]$.
$$P(|X-\mu|\ge \delta\mu) \le 2e^{-\mu\delta^2/3}, \quad \forall \delta \in (0,1)$$

## Corollario 4.9

Siano $Y_1,\dots,Y_n \sim Ber(1/2)$, $Y=\sum_i Y_i$, $\mu=n/2$: $$P(Y \ge (1+\delta)\mu) \le e^{-\delta^2\mu}, \quad \forall \delta>0$$ $$P(Y \ge \mu+a) \le \exp\left(-\frac{2a^2}{n}\right), \quad \forall a>0$$

## Corollario 4.10
Siano $Y_1,\dots,Y_n \sim Ber(1/2)$, $Y=\sum_i Y_i$, $\mu=n/2$:
1. $$P(Y \le \mu-a) \le \exp\left(-\frac{2a^2}{n}\right), \quad \forall a \in (0,\mu)$$
2. $$P(Y \le (1-\delta)\mu) \le e^{-\delta^2\mu}, \quad \forall \delta \in (0,1)$$

## Teorema 4.12 (Disuguaglianza di Hoeffding)

Siano $X_1,\dots,X_n$ indipendenti con media comune $\mu$, $P(a\le X_i\le b)=1$: $$P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \mu\right| \ge \epsilon\right) \le 2\exp\left(\frac{-2n\epsilon^2}{(b-a)^2}\right)$$

## Lemma 4.13 (Lemma di Hoeffding)

Sia $Y$ con $\mathbb{E}[Y]=0$, $P(a\le Y\le b)=1$: $$\mathbb{E}[e^{tY}] \le \exp\left(\frac{t^2(b-a)^2}{8}\right)$$

## Teorema 4.14

Siano $X_1,\dots,X_n$ indipendenti con $\mathbb{E}[X_i]=\mu_i$, $P(a_i\le X_i\le b_i)=1$: $$P\left(\left|\sum_{i=1}^n X_i - \sum_{i=1}^n \mu_i\right| \ge \epsilon\right) \le 2\exp\left(-\frac{2\epsilon^2}{\sum_{i=1}^n(b_i-a_i)^2}\right)$$