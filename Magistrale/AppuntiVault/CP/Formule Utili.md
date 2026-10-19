# Grafo Erdos Renyi

Consideriamo un grafo di Erdos Renyi $G_{n,p}$ di $n$ nodi, dove $p$ rappresenta la probabilità che un arco $(i,j) \in E$. Ossia, la probabilità di generare un grafo di $m$ archi è
$$
\boxed{P(|E| = m) = \binom{\binom{n}{2}}{m}p^m (1-p)^{\binom{n}{2} - m}}
$$
Calcoliamo ora $\mathbb{E}[|E|]$. Sia
$$
E_{ij} = \begin{cases}
1 \iff (i,j) \in E \text{ con prob. } p \\
0 \text{ altrimenti}
\end{cases}
$$
Allora, $|E| = \sum_{i<j} E_{ij}$.
$$
\mathbb{E}[|E|] = \mathbb{E}\left[ \sum_{i,j \in V} E_{ij} \right] = \sum_{i,j \in V} \mathbb{E}[E_{ij}] = \binom{n}{2}p
$$
*Osservazione:* $|E| \sim Bin\left(\binom{n}{2}, p\right)$.
$$
\begin{align}
&\boxed{\mathbb{E}[|E|] = \binom{n}{2}p} \\ \\
&\boxed{VAR[|E|] = \binom{n}{2}p(1-p)}
\end{align}
$$

Fissiamo ora un nodo $v \in V$ e calcoliamo il valor atteso del grado di $v$, ossia $\mathbb{E}[\delta(v)]$.
$$
\mathbb{E}[\delta(v)] = \mathbb{E}\left[ \sum_{i=1}^{n-1} E_{v,i} \right] = \sum_{i=1}^{n-1}\mathbb{E}[E_{v,i}] = (n-1)p
$$

*Osservazione:* $\delta(v) \sim Bin(n-1, p)$.
$$
\begin{align}
&\boxed{\mathbb{E}[\delta(v)] = (n-1)p} \\ \\
&\boxed{VAR[\delta(v)] = (n-1)p(1-p)}
\end{align}
$$

---

## 1. Serie e Sommatorie Note

### Progressione Aritmetica (Somma di Gauss)
Somma dei primi $n$ numeri interi:
$$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$$

### Somma dei Quadrati
Somma dei quadrati dei primi $n$ numeri interi:
$$\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$$

### Serie Geometrica (Finita)
Ragione $q \neq 1$:
$$\sum_{k=0}^{n} q^k = \frac{1 - q^{n+1}}{1 - q}$$
$$\sum_{k=m}^n q^k = \frac{q^m - q^{n-1}}{1 - q}$$

### Serie Geometrica (Infinita)
Converge solo se $|q| < 1$:
$$\sum_{k=0}^{\infty} q^k = \frac{1}{1 - q}$$
$$\sum_{k=0}^\infty q^k = \frac{1}{1-q} \quad
   \sum_{k=1}^\infty q^k = \frac{q}{1-q} \quad
   \sum_{k=m}^\infty q^k = \frac{q^m}{1-q}$$

### Serie Aritmetico-Geometrica (Infinita)
Fondamentale per calcolare il valore atteso di distribuzioni come la Geometrica. Converge per $|q| < 1$:
$$\sum_{k=1}^{\infty} k q^{k-1} = \frac{1}{(1 - q)^2}$$

---

## 2. Limiti Notevoli e Approssimazioni

### Il limite di Nepero (Esponenziale)
Fondamentale per passare dalla Binomiale a Poisson:
$$\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = e^x$$
$$\lim_{n \to \infty} \left(1 - p\right)^n = e^{-np} \quad (\text{se } p \to 0)$$

### Approssimazione di Poisson per la Binomiale (Eventi Rari)
Se $X \sim \text{Bin}(n, p)$ con $n$ grande e $p$ piccolo, ponendo $\lambda = np$:
$$\mathbb{P}(X = k) \approx \frac{\lambda^k e^{-\lambda}}{k!}$$
Da cui la probabilità di zero successi:
$$\mathbb{P}(X = 0) \approx e^{-np}$$

---

## 3. Disuguaglianze di Concentrazione

### Disuguaglianza di Markov
Per una variabile aleatoria $X \ge 0$ e $a > 0$:
$$\mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a}$$

### Disuguaglianza di Chebyshev
Per una variabile con media $\mu$ e varianza $\sigma^2$:
$$\mathbb{P}(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

### Disuguaglianza di Chernoff (Coda Bilatera per Bernoulli)
Sia $X$ la somma di variabili di Bernoulli indipendenti con media $\mu$ e $0 < \delta < 1$:
$$\mathbb{P}(|X - \mu| \ge \delta\mu) \le 2 \exp\left(-\frac{\delta^2\mu}{3}\right)$$

---

## 4. Catene di Markov e Grafi

### Misura Stazionaria su Grafi Non Orientati
Per una passeggiata aleatoria semplice su un grafo connesso non orientato $G = (V, E)$, la distribuzione stazionaria $\pi$ è proporzionale al grado dei nodi:
$$\pi_i = \frac{\text{deg}(i)}{\sum_{j \in V} \text{deg}(j)} = \frac{\text{deg}(i)}{2|E|}$$

### Equazioni di Bilancio Dettagliato (Reversibilità)
Una catena è reversibile rispetto a $\pi$ se e solo se per ogni coppia di stati $i, j$:
$$\pi_i P_{ij} = \pi_j P_{ji}$$

### Tempo Medio di Primo Ritorno (Teorema Ergodico)
Per una catena irriducibile e ricorrente positiva, il tempo atteso per tornare allo stato $i$ partendo da $i$ è l'inverso della sua probabilità stazionaria:
$$\mathbb{E}_i[T_i] = \frac{1}{\pi_i}$$

### Numero Atteso di Visite in un'Escursione
In un ciclo che parte da $i$ e si chiude al primo ritorno in $i$, il numero medio di visite a un generico stato $j$ è:
$$\mathbb{E}_i[\text{Visite a } j] = \frac{\pi_j}{\pi_i}$$

---

## 5. Sistemi Lineari per l'Analisi al Primo Passo

Sia $T_A$ il tempo di primo arrivo all'insieme di stati $A$.

### Calcolo delle Probabilità di Assorbimento ($h_k$)
Probabilità di raggiungere $A$ partendo da $k$:
* $h_k = 1$ per $k \in A$
* $h_k = 0$ per $k$ in altri stati assorbenti non in $A$
* $h_k = \sum_j P_{kj} h_j$ per gli stati transitori.

### Calcolo dei Tempi Medi di Assorbimento ($v_k$)
Tempo atteso per raggiungere $A$ partendo da $k$:
* $v_k = 0$ per $k \in A$
* $v_k = 1 + \sum_j P_{kj} v_j$ per gli stati transitori.