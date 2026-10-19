Abbiamo un album con $n$ figurine. Ogni pacchetto contiene solo *una* figurina (a caso tra le $n$ possibili). 

**Domanda:** Quanti pacchetti devo comprare per completare la collezione?

Sia 
$$X = \text{\# di pacchetti per completare la collezione}$$
Vogliamo calcolare $\mathbb{E}[X]$. Siano
$X_j$ = \# di pacchetti comprati avendo $j-1$ figurine diverse nella collezione per trovare la $j$-esima figurina diversa.

Osserviamo che le $X_j$ sono delle v.a. geometriche indipendenti. Di che *paramentro*? Se ho $j-1$ figurine diverse nella collezione, ad ogni nuovo pacchetto avrò una probabilità 
$$1 - \frac{j-1}{n} = \frac{n-j+1}{n}$$di trovare una nuova figurina. Infatti, $\frac{j-1}{n}$ è la probabilità di trovare una delle $j-1$ figurine diverse già presenti nella collezione. Quindi
$$
X_{j} \sim Geom(p_{j}), \quad p_{j} = 1 - \frac{j-1}{n}, \quad \mathbb{E}[X_{j}] = \frac{1}{p_{j}} = \frac{n}{n-j + 1} 
$$
A questo punto ci possiamo calcolare il valore atteso di $X$ come
$$\mathbb{E}[X] = \mathbb{E}\left[ \sum_{j=1}^n X_{j} \right] = \sum_{j=1}^n \mathbb{E}[X_{j}] = \sum_{j=1}^n \frac{n}{n -j+1}$$
Osserviamo che 
$$
\begin{align}
\sum_{j = 1}^n \frac{1}{n-j+1} &= \frac{1}{n} + \frac{1}{n-1} + \dots + \frac{1}{2} + 1 \\
&= 1 + \frac{1}{2} + \dots + \frac{1}{n-1} + \frac{1}{n}  \\
&= \sum_{j = 1}^n \frac{1}{j} = H(n) = \log(n) + \Theta(1) \\
&H(n) \text{ è il numero armonico}
\end{align}
$$
Concludendo, otteniamo che
$$\mathbb{E}[X] = n \sum_{j = 1}^n \frac{1}{j} = nH(n) \approx n\log (n)$$
## Varianza

Poichè $X_{i} \sim Geom(p_{i}),\quad \mathbb{E}[X] = \frac{1}{p_{i}},\quad Var[X_{i}] = \frac{1-p_{i}}{p_{i}^2}$, dove 
$$
p_{i} = 1 - \frac{j-1}{n} = \frac{n - j + 1}{n}
$$

$$
\begin{align}
VAR[X_{i}] = \frac{1-p_{i}}{p_{i}^2} = \frac{1-\frac{n - j + 1}{n}}{\left(\frac{n - j + 1}{n}\right)^2} = \frac{\frac{j-1}{n}}{\left(\frac{n - j + 1}{n}\right)^2} = \frac{n(j-1)}{(n - j + 1)^2}
\end{align}
$$
Sostituiamo $k = n-j+1$, di conseguenza $j-1 = n-k$ e otteniamo
$$
VAR[X_{i}] = \frac{n(n-k)}{k^2}
$$
Poichè le $X_{i}$ sono indipendenti, la varianza della somma è uguale alla somma delle varianze
$$
\begin{align}
VAR[X] &= VAR\left[ \sum_{i=1}^n X_{i} \right] = \sum_{i = 1}^n VAR[X_{i}] = \sum_{k = 1}^n \frac{n(n-k)}{k^2}  \\
&= n^2 \sum_{k = 1}^2 \frac{1}{k^2} - n \sum_{k = 1}^n \frac{1}{k} \\
&= n^2 H^{(2)}_{n} - nH_{n}
\end{align}
$$
Dove,
- $H_{n} = \sum_{k=1}^{n} \frac{1}{k}$ è il numero *armonico*;
- $H_{n}^{(2)} = \sum_{k=1}^n \frac{1}{k^2}$ è il numero *armonico generalizzato di ordine 2*

## Chebychev \& Markov

Applichiamo ora le disuguaglianze di Chebychev e Markov per dare un bound alla probabilità
$$
P(X \geq 2nH_{n}) = P(X \geq 2\mathbb{E}[X]) \leq \frac{\mathbb{E}[X]}{2\mathbb{E}[X]} = \frac{1}{2} \quad \text{per Markov ineq.}
$$

Per applicare Chebyshev, diamo un bound alla varianza. Abbiamo che
$$
VAR[X] = n^2 \sum_{k = 1}^n \frac{1}{k^2} - n \sum_{k = 1}^n \frac{1}{k} \leq n^2 \sum_{k = 1}^n \frac{1}{k^2} \leq\frac{n^2\pi^2}{6}
$$
Usando la disuguaglianza
$$
\boxed{\sum_{k = 1}^\infty \frac{1}{k^2} \leq \frac{\pi^2}{6}}
$$
Ora, applicando Chebyshev, si ha
$$
\begin{align}
P(X \geq 2nH_{n}) &= P(|X - nH_{n}| \geq nH_{n})  \\
&\leq \frac{\frac{n^2\pi^2}{6}}{(nH_{n})^2} = \frac{\pi^2}{6(H_{n})^2}  = O\left( \frac{1}{\ln^2 n} \right)
\end{align}
$$
Questo bound è migliore di Markov! Ma comunque ancora non buonissimo. Facciamo un'altra stima. Sia
$$
E_{i} = \text{non ho ancora trovato la figurina } i \text{ all'}N\text{-esimo pacchetto} 
$$
con $N \in \mathbb{N}$. Allora
$$
P(E_{i}) = \left( 1 - \frac{1}{n} \right)^N
$$
Prendendo $N = n(\log n + c)$ con $c>0$
$$
P(E_{i}) = \left( 1 -\frac{1}{n} \right)^{n(\log n + c)} \leq e^{-\log n - c} = \frac{1}{e^c \cdot n}
$$
Se poi prendo $c = \log n$ ottengo
$$
P(E_{i}) \leq \frac{1}{n^2}
$$
Allora
$$
P(X \geq 2nH_{n}) \approx P(X \geq \underbrace{2n\log n}_{N  \text{ con } c = \log n}) = P\left( \bigcup_{j=1}^n E_{j} \right) \leq nP(E_{j}) \leq \frac{1}{n}
$$
che è un bound molto migliore di quello di Chebychev.