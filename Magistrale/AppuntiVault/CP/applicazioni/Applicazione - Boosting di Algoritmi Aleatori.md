Supponimo di avere un algoritmo per un problema di decisione (ad esempio: il numero $p$ è primo?) che dà la risposta esatta con probabilità $\frac{1}{2} + \delta$ per qualche $\delta > 0$ piccolino. Ripetiamo l'algoritmo $N$ volte e prendiamo per buona la riposta che è stata data dall'algoritmo più volte.

**Problema:** Dato $\epsilon > 0$, supponiamo di voler dare la risposta esatta con probabilità $1 - \epsilon$. Quanto grande dobbiamo prendere $N$?

Siano $X_{1}, \dots, X_{N}$ i.i.d. tali che
$$
X_{i} = 
\begin{cases}
1 \text{ Algo(i) = Wrong} \\
0 \text{ Algo(i) = Right}
\end{cases}
$$
La risposta finale sarà sbagliata se 
$$
\sum_{i = 1}^N X_{i} \ge \frac{N}{2}
$$

Notiamo che $X_{i} \sim Ber\left( \frac{1}{2} - \delta \right)$ e quindi $\mathbb{E}[X_{i}] = \frac{1}{2} - \delta$. Allora,
$$
\begin{align}
P\left( \sum_{i=1}^N X_{i} \geq \frac{N}{2} \right) &= P\left( \sum_{i=1}^N X_{i} - \left(\frac{1}{2} - \delta\right) \geq \frac{N}{2} - \left(\frac{1}{2} - \delta\right) \right)  \\
&= P\left( \frac{1}{N}\sum_{i=1}^N(X_{i} - \mathbb{E}[X_{i}]) \geq \delta \right) \\
&= \frac{1}{2}P\left(\left| \frac{1}{N}\sum_{i=1}^N(X_{i} - \mathbb{E}[X_{i}]) \right| \geq \delta \right)  \\
& \leq \frac{1}{2} \cdot 2\exp(-2N\delta^2) = \exp(-2N\delta^2) 
\end{align}
$$
Come bound abbiamo applicato il *Teorema 4.12* con $b=1$ e $a = 0$.

**Teorema 4.12**: Siano $X_{1}, \dots, X_{n}$ v.a. indipendenti con media comune $\mu = \mathbb{E}[X_{i}]$ e tali che $P(a \leq X_{i} \leq b) = 1,\ \forall i = 1, \dots, n$ e per qualche costante $a, b \in \mathbb{R}$. Allora, 
$$P\left( \left| \frac{1}{n} \sum_{i=1}^n X_{i} - \mu \geq \epsilon \right| \right) \leq 2\exp\left(\frac{-2n \epsilon^2}{(b-a)^2}\right)$$
A questo punto, vogliamo che questa quantità sia $\leq \epsilon$.
$$
\begin{align}
\exp\left( -2N\delta^2 \right) \leq \epsilon &\iff -2N\delta^2 \leq \log(\epsilon) \\
& N \geq \frac{1}{2\delta^2}\log\left( \frac{1}{\epsilon} \right)
\end{align}
$$
Quindi ripetendo l'algoritmo $N \geq \frac{1}{2\delta^2}\log\left( \frac{1}{\epsilon} \right)$ volte e prendiamo la risposta uscita più volte, sapremo che essa è corretta con probabilità $\geq 1 - \epsilon$.
