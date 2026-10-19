### 1. Uniforme Discreta
Modella la scelta equiprobabile tra $n$ valori interi consecutivi, tipicamente $\{1, 2, \dots, n\}$.
* **Parametri:** $n$ (numero di esiti possibili)
* **Probabilità:** $\mathbb{P}(X = k) = \frac{1}{n}$
* **Valore Atteso:** $\mathbb{E}[X] = \frac{n+1}{2}$
* **Varianza:** $\text{Var}(X) = \frac{n^2-1}{12}$

### 2. Bernoulli
Modella un singolo esperimento con due esiti: successo ($1$) o fallimento ($0$).
* **Parametri:** $p \in [0,1]$ (probabilità di successo)
* **Probabilità:** $\mathbb{P}(X = 1) = p$, $\mathbb{P}(X = 0) = 1-p$
* **Valore Atteso:** $\mathbb{E}[X] = p$
* **Varianza:** $\text{Var}(X) = p(1-p)$
* **F.g.m:** $M_X(t) = 1 - p + pe^t$
* **Trick utile:** Poiché $X$ assume solo valori $0$ e $1$, vale l'identità $X^k = X$ per qualsiasi intero $k \ge 1$. Di conseguenza, tutti i momenti non centrati sono uguali: $\mathbb{E}[X^k] = p$.

### 3. Binomiale
Modella il numero di successi in $n$ prove di Bernoulli indipendenti.
* **Parametri:** $n \in \mathbb{N}$ (prove), $p \in [0,1]$ (probabilità)
* **Probabilità:** $\mathbb{P}(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
* **Valore Atteso:** $\mathbb{E}[X] = np$
* **Varianza:** $\text{Var}(X) = np(1-p)$
* **F.g.m:** $M_X(t) = (1 - p + pe^t)^n$
* **Trick utile (Riproducibilità):** La somma di due binomiali indipendenti $X \sim \text{Bin}(n_1, p)$ e $Y \sim \text{Bin}(n_2, p)$ con lo *stesso* parametro $p$ è ancora una binomiale: $X+Y \sim \text{Bin}(n_1+n_2, p)$.
* **Trick utile (Approssimazione):** Se $n \to \infty$ e $p \to 0$ in modo che $np \to \lambda$, la Binomiale si approssima con una Poisson di parametro $\lambda$.

### 4. Geometrica (Numero di prove)
Modella il numero di prove necessarie per ottenere il **primo successo** (supporto $k \in \{1, 2, 3, \dots\}$).
* **Parametri:** $p \in (0,1]$
* **Probabilità:** $\mathbb{P}(X = k) = p(1-p)^{k-1}$
* **Valore Atteso:** $\mathbb{E}[X] = \frac{1}{p}$
* **Momento Secondo:** $\mathbb{E}[X^2] = \frac{2-p}{^2}$
* **Varianza:** $\text{Var}(X) = \frac{1-p}{p^2}$
* **F.g.m:** $M_X(t) = \frac{pe^t}{1 - (1-p)e^t}$ per $t < -\ln(1-p)$
* **Trick utile (Assenza di memoria):** Unica distribuzione discreta senza memoria. Sapere che hai già fallito $n$ volte non cambia la probabilità di successo ai tentativi futuri: $\mathbb{P}(X > n + m \mid X > n) = \mathbb{P}(X > m)$.

*(Nota: Esiste una versione alternativa che conta il numero di "fallimenti" prima del successo, con supporto $k \in \{0, 1, 2, \dots\}$. In quel caso, $\mathbb{E}[X] = \frac{1-p}{p}$).*

### 5. Poisson
Modella il numero di eventi rari che si verificano in un intervallo di tempo o spazio fissato.
* **Parametri:** $\lambda > 0$ (tasso medio di accadimento)
* **Probabilità:** $\mathbb{P}(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$
* **Valore Atteso:** $\mathbb{E}[X] = \lambda$
* **Varianza:** $\text{Var}(X) = \lambda$
* **F.g.m:** $M_X(t) = \exp(\lambda(e^t - 1))$
* **Trick utile (Riproducibilità):** La somma di Poisson indipendenti è sempre una Poisson con parametro pari alla somma dei parametri: se $X \sim \text{Po}(\lambda_1)$ e $Y \sim \text{Po}(\lambda_2)$, allora $X+Y \sim \text{Po}(\lambda_1 + \lambda_2)$. Valore atteso e varianza coincidono.
