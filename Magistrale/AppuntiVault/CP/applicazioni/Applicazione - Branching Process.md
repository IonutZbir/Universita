
Immaginiamo un batterio che ad ogni unità di tempo genera un numero di figli distribuito come una v.a. $Z$ e poi muore. I figli fanno altrettanto.

Siano $Y_{i}$ le v.a. che contano i batteri all'$i$-esima generazione, allora
$$
\begin{align}
Y_{0} &= 1 \\
Y_{i} &= \sum_{k=1}^{Y_{i-1}} Z_{i,k} \quad n \in \mathbb{N}
\end{align}
$$
dove $Z_{n,k}$ è il numero di figli dell'individuo $k$ alla generazione $n-1$. Inoltre le $Z_{n,k}$ sono v.a. i.i.d distribuite come $Z$.

![[branching_process.png.png|500]]

- $Z_{1,1} = 2$, numero di figli dell'unico batterio nella generazione $0$.
- $Z_{2,1} = 0$, numero di figli dell'individuo 1 nella generazione 1 (l'unica foglia a sinistra).
- $Z_{2,2} = 3, Z_{3,1} = 0, Z_{3,2} = 1, Z_{3, 3} = 1, Z_{4,1} = 0$

**Che distribuzione ha $\mathbf{Z}$?**
Consideriamo una qualunque $Z$ a valori in $\mathbb{N}$, con $\mathbb{E}[Z] = \mu < \infty$.

**Domanda:** Qual è la media degli individui alla generazione $i$ sapendo che alla generazione $i-1$ ce n'erano $Y_{i-1} = y_{i-1}$. Ossia, vogliamo calcolare 
$$
\begin{align}

\mathbb{E}[Y_{i} | Y_{i-1} = y_{i-1}] &= \mathbb{E}\left[\sum_{k = 1}^{Y_{n-1}}Z_{i,k} \mid Y_{i-1} = y_{i-1} \right] \\
\text{uso } (Y_{i-1} = y_{i-1}) &= \mathbb{E}\left[\sum_{k = 1}^{y_{n-1}}Z_{i,k} \mid Y_{i-1} = y_{i-1} \right] \\
&\text{applico la linearità, avendo sostituito no ho più una v.a.} \\
&= \sum_{k = 1}^{y_{i-1}} \mathbb{E}\left[Z_{i,k} \mid Y_{i-1} = y_{i-1}\right]  \\
&= \sum_{k = 1}^{y_{i-1}} \mathbb{E}[Z_{i,k}] = \sum_{k = 1}^{y_{i-1}} \mu = y_{i-1} \mu
\end{align}
$$
Poichè le $Z_{n,k}$ sono i.i.d, per indipendenza posso togliere la v.a. su cui sto condizionando.

A questo punto, $$\mathbb{E}[Y_{i} \mid Y_{i-1}] = Y_{i-1}\mu$$vista come v.a.
Possiamo ora calcolare la media degli individui alla generazione $n$. Usando il teorema 2.7 (*Teorema Torre*) iterativamente otteniamo,
$$
\begin{align}
\mathbb{E}[Y_{i}] &= \mathbb{E}[\mathbb{E}[Y_{i} \mid Y_{i-1}]] \\
&= \mathbb{E}[\mu Y_{i-1}] = \mu \mathbb{E}[Y_{i-1}] \\
&= \mu\mathbb{E}[\mathbb{E}[Y_{i-1} \mid Y_{i-2}]] = \mu \mathbb{E}[\mu Y_{i-2}] = \mu^2\mathbb{E}[Y_{i-2}]  \\
&= \dots = \mu^i \mathbb{E}[Y_{0}] = \mu^i 
\end{align}
$$
**Osservazione**: 
$$
\begin{align}
&\mathbb{E}[Y_{n}] \to 0 \quad \iff \mu < 1  \\
&\mathbb{E}[Y_{n}] \to \infty \quad \iff \mu > 1
\end{align}
$$
Volendo infine, possiamo calcolare la media del numero totale di batteri di tutte le generazioni:
$$
\mathbb{E}\left[ \sum_{n \ge 0} Y_{i} \right] = \sum_{i \ge 0} \mu^i =
\begin{cases}
\frac{1}{1 - \mu} \iff \mu < 1 \\
\infty \iff \mu \ge 1
\end{cases}
$$

### Calcolo della Varianza

Calcoliamo la varianza di $Y_{n}$. Useremo la formula
$$
VAR[Y_{i}] = \mathbb{E}[VAR[Y_{i} | Y_{i-1}]] + VAR[\mathbb{E}[Y_{i} | Y_{i-1}]]
$$
Sia $\sigma^2 = VAR[Z_{i,k}]$ e $\mu = \mathbb{E}[Z_{i,k}]$, allora abbiamo che
$$
\begin{align}
\boxed{VAR[Y_{i}]} &= \mathbb{E}\left[ VAR\left[ \sum_{k = 1}^{Y_{i-1}} Z_{i,k} \Bigg| Y_{i-1}=y_{i-1} \right] \right] + VAR[\mu Y_{i-1}]  \\
&=\mathbb{E}\left[ VAR\left[ \sum_{k = 1}^{Y_{i-1}=y_{i-1}} Z_{i,k} \Bigg| Y_{i-1}=y_{i-1} \right] \right] + \mu^2 VAR[Y_{i-1}] \\
&= \mathbb{E}\left[\sum_{k = 1}^{y_{i-1}} VAR[Z_{i,k}] \Bigg| Y_{i-1}=y_{i-1} \right] + \mu^2 VAR[Y_{i-1}] \\
&= \mathbb{E}\left[\sum_{k = 1}^{y_{i-1}} VAR[Z_{i,k}] \right] + \mu^2 VAR[Y_{i-1}]  \\
&= \mathbb{E}[(y_{i-1})\sigma^2] + \mu^2 VAR[Y_{i-1}] \\
&= \mathbb{E}[(Y_{i-1})\sigma^2] + \mu^2 VAR[Y_{i-1}] \\ \\
&= \boxed{\mu^{i-1}\sigma^2 + \mu^2VAR[Y_{i-1}]}
\end{align}
$$


Srotolando l'equazione di ricorrenza, si ha che
$$
VAR[Y_{i}] = \mu^{i-1}\sigma^2 \left( \frac{\mu^i - 1}{\mu - 1} \right)
$$
---
*Ossevazione:* Se $Z_{i,k} \sim Bin(n,p)$, allora
$$
\begin{align}
\mathbb{E}[Y_{i}] &= (np)^i \\ \\
VAR[Y_{i}] &= (np)^{i-1}np(1-p) + (np)^2VAR[Y_{i-1}]  \\
&= (np)^{i-1}np(1-p) \left( \frac{(np)^i - 1}{np-1} \right)
\end{align}
$$
## Modellazione come catena di Markov

È possibile mostrare che il processo $(Y_{i})$ è una catena di Markov a valori in $\mathbb{N}$. Determiniano esplicitamente le probabilità di transizione
$$
\begin{align}
P(x,y) &= P(Y_{i+1} = y | Y_{i} = x) \\
&= P\left( \sum_{k=1}^{Y_{i}} Z_{i,k} = y \Bigg | Y_{i} = x\right) \\
&= P\left( \sum_{k=1}^{Y_{i} = x} Z_{i,k} = y \Bigg | Y_{i} = x\right) \\
&= P(Bin(x \cdot n, p) = y)  \\
&= \binom{xn}{y}p^y(1-p)^{xn - y}
\end{align}
$$
Che è esattamente ciò che ci aspettavamo in quanto la distribuzione delle $Z_{i,k} \sim Bin(n,p)$.

Vediamo ora quali e come sono i stati di questa catena di Markov. L'insieme degli stati $V = \mathbb{N}$, quindi stiamo considerando una catena infinita.
![[branching_process_chain]]

### Classificazion degli stati

Dobbiamo suddividere lo spazio degli stati $V = \mathbb{N} = \{0, 1, 2, \dots\}$ in classi di equivalenza (stati che comunicano tra loro) e stabilirne la natura.

**Lo stato $x = 0$:**
La probabilità di transizione da 0 a 0 è certa: $P(0,0) = 1$.
Una volta che la popolazione si estingue, rimane estinta per sempre.
$\{0\}$ forma una classe di equivalenza chiusa da sola ed essendo uno stato assorbente che si visita infinite volte con probabilità 1, lo stato 0 è **ricorrente positivo**.

**Gli stati $x \ge 1$:**
Prendiamo un qualsiasi stato $x > 0$. Qual è la probabilità che l'intera popolazione si estingua improvvisamente al passo successivo? Corrisponde al caso in cui tutte le estrazioni binomiali diano fallimento (zero figli generati da $nx$ "tentativi").

$$P(x, 0) = \binom{nx}{0} p^0 (1-p)^{nx} = (1-p)^{nx}$$

Poiché $p \in (0,1)$, questa probabilità è strettamente maggiore di zero.

Questo significa che da _qualsiasi_ stato $x$ è possibile finire nello stato $0$. Tuttavia, poiché $0$ è assorbente, una volta finiti in $0$ è **impossibile** tornare allo stato $x$. Di conseguenza, la probabilità di ritornare allo stato di partenza $x$ è strettamente minore di 1.
Tutti gli stati $x \ge 1$ sono **transienti**. A seconda del valore di $n$, possono formare un'unica grande classe comunicante o più classi, ma la loro natura non cambia: sono tutti transienti, perché inevitabilmente "perdono probabilità" verso lo stato assorbente 0 o, se $np > 1$, divergono verso l'infinito.  

### Distribuzioni invarianti

Una distribuzione invariante (o stazionaria) è un vettore di probabilità $\pi = (\pi_0, \pi_1, \pi_2, \dots)$ tale che $\pi P = \pi$, dove $P$ è la matrice di transizione, e $\sum \pi_i = 1$.

Per un noto teorema sulle catene di Markov, **tutti gli stati transienti hanno probabilità invariante nulla**. Poiché la catena non trascorre una frazione di tempo positiva in questi stati sul lungo periodo, la massa di probabilità non può accumularsi su di essi.

Quindi, per ogni $x \ge 1$, si ha:

$$\pi_x = 0$$

$$\pi = (1, 0, 0, 0, \dots)$$

Questo ha perfettamente senso dal punto di vista fisico del problema: sul lunghissimo periodo, il sistema stazionario è quello in cui la coltura batterica è completamente morta.