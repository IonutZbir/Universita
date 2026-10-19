**DEF 2.1:** Una variabile aleatoria è un'applicazione $X: \Omega \to \mathbb{R}$. Si dice discreta se può assumere un numero finito o numerabile di valori.

*Osservazione:* Se $\Omega$ è finito o numerabile, si ha che $\forall a \in \mathbb{R}$
$$
\begin{align}
\{X = a\} = \{\omega \in \Omega: X(\omega) = a\} \text{ cosi che} \\ \\
P(\{X = a \}) = \sum_{\omega \in \Omega\ \land\ X(\omega) = a} P(\{\omega\})
\end{align}
$$

*NOTA:* Quando studiamo eventi random, siamo spesso interessati in un qualsiasi valore associato all'evento random che all'evento stesso.

*Esempio:* Lancio due dadi equi: $\Omega = \{ (1,1), (1,2), (2,1), \dots, (6,6) = \omega \}$. Sia $X$ la somma dei due dadi. Allora
$$
P(\{X = 4\}) = P(\{1,3\}) + P(\{2,2\}) + P(\{3,1\}) = \frac{1}{12}
$$

**DEF 2.2:** Due v.a. discrete $X$ e $Y$ si dicono *indipendenti* se e solo se 
$$
P(\{X = x\}) \cap P(\{Y = y\}) = P(\{X = x\})P(\{Y = y\}) \quad \forall x,y \in R
$$
Analogamente, $X_{1}, \dots, X_{k}$ sono *mutualmente indipendenti* se e solo se, $\forall$ sottoinsieme $I \subseteq\{1, \dots, k \}$ e $\forall\ x_{i} \in \mathbb{R}$,
$$
P\left(\bigcap_{i \in I} \{X_{i} = x_{i}\} \right) = \prod_{i\in I} P(\{X_{i} = x_{i}\})
$$

**DEF 2.3:** Una v.a. discreta $X$ ha valore atteso finito se
$$
\sum_{x_{k}} |x_{k}| P(X = x_{k}) < \infty 
$$
In pratica stiamo sommando su tutti i possibili valori che può assumere $X$. In tal caso, il *valor atteso* (o *media*, o *speranza matematica*) è
$$
\mathbb{E}[X] = \sum_{x_{k}} |x_{k}| P(X = x_{k}) 
$$

*NOTA:* Il valor atteso di una v.a. è una media pesata di tutti i possibili valori che può assumere, ognuno pesato con la probabilità che assuma quel valore.

*Esempio:* Sia $X$ la v.a. tale che $P(X = i) = \frac{1}{i}\ \forall i \in \mathbb{N}$, allora
$$
\mathbb{E}[X] = \sum_{i \in \mathbb{N}} i \left( \frac{1}{i} \right) = \infty
$$

**TEOREMA 2.1 (Linearità del Valor Atteso)**
Siano $X_{1}, \dots, X_{n}$ v.a. con aspettazione finita, allora
$$
\mathbb{E}\left[\sum_{i=1}^n X_{i}\right] = \sum_{i=1}^n\mathbb{E}[X_{i}]
$$
**DIMOSTRAZIONE:**
Sia $X$ e $Y$ v.a.
$$
\begin{align}
\mathbb{E}[X + Y] &= \sum_{i}\sum_{j}(i+j)P(\{X = i\} \cap \{Y = j\}) \\
&= \sum_{i}\sum_{j} iP(\{X = i\} \cap \{Y = j\} + \sum_{i}\sum_{j}j P(\{X = i\} \cap \{Y = j\} \\
&= \sum_{i} i P(\{X = i\}) + \sum_{j} jP(\{Y = j\}) = \mathbb{E}[X] + \mathbb{E}[Y]
\end{align}
$$

**LEMMA 2.2:**
$\forall$ costante $c \in \mathbb{R}$ e $\forall$ v.a. $X$, vale che 
$$
\mathbb{E}[cX] = c\mathbb{E}[X]
$$
**DIMOSTRAZIONE:** Per $c = 0$ è banale. Sia $c \neq 0$, allora
$$
\begin{align}
\mathbb{E}[cX] &= \sum_{j}j P(cX = j) = c\sum_{j} \left( \frac{j}{c} \right) P\left( X = \frac{j}{c} \right)  \\
&= c \sum_{k} k P(X = k) = c\mathbb{E}[X]
\end{align}
$$

*Osservazione:* La linearità del valor atteso può essere applicata sempre. Le v.a. non devono necessariamente essere indipendenti.

*Esempio:* Abbiamo due dadi. Sia $X_{1}$ il risultato del primo dado e $X_2$ il risultato del secondo dado. Sia $X=X_1 + X_2$, allora
$$
\begin{align}
\mathbb{E}[X_{1}] = \sum_{i = 1}^6 i P(X_{1} = i) = \frac{7}{2}, \qquad \mathbb{E}[X_{2}] = \frac{7}{2} \\
\mathbb{E}[X] = \mathbb{E}[X_{1} + X_{2}] = \mathbb{E}[X_{1}] + \mathbb{E}[X_{2}] = 7.
\end{align}
$$
## 2.1.2 - Disuguaglianza di Jensen

In generale 
$$
\mathbb{E}[X^k] \neq \mathbb{E}[X]^k \quad \forall k \in \mathbb{N}
$$
Consideriamo ora la varianza di una v.a.
$$
VAR[X] = \mathbb{E}[(X - \mathbb{E}[X])^2)] \geq 0
$$
Allora
$$
\begin{align}
0 &\leq \mathbb{E}[X^2 - 2\mathbb{E}[X]X + \mathbb{E}[X]^2] \\
&=\mathbb{E}[X^2] - 2\mathbb{E}[X]^2 + \mathbb{E}[X]^2 \\
&=\mathbb{E}[X^2] - \mathbb{E}[X]^2 \\
& \implies \mathbb{E}[X^2] \geq \mathbb{E}[X]^2
\end{align}
$$

**DEF 2.4:** Una funzione $f: \mathbb{R} \to \mathbb{R}$ è *convessa (concava)* se $\forall x_{1}, x_{2} \in \mathbb{R}$ si ha $\forall \lambda \in (0,1)$
$$
f(\lambda x_{1} + (1-\lambda)x_{2}) \underbrace{\geq}_{\leq} \lambda f(x_{1}) + (1 - \lambda)f(x_{2})
$$
![[f_convessa.png|500]]

**TEOREMA 2.4 (Disuguaglianza di Jensen)**
Sia $X$ v.a. e $f: \mathbb{R} \to \mathbb{R}$ una funzione convessa. Allora
$$
\mathbb{E}[f(X)] \geq f(\mathbb{E}[X])
$$
**DIMOSTRAZIONE:** Dimostrazione solo nel caso in cui $f$ ammette sviluppo di Taylor di secondo ordine.
$$
f(x) = f(y) + f'(y)(x - y) + \frac{f''(\xi)}{2}(x-y)^2 \text{ per qualche } \xi \in [x,y]
$$
Applichiamo la formula con $y = \mathbb{E}[X]$
$$
\begin{align}
f(x) &= f(\mathbb{E}[X]) + f'(\mathbb{E}[X])(x - \mathbb{E}[X]) + \underbrace{\frac{f''(\xi)}{2}(x - \mathbb{E}[X])^2}_{f''(\xi) > 0 \text{ perchè convessa}}  \\
&\geq f(\mathbb{E}[X]) + f'(\mathbb{E}[X])(x - \mathbb{E}[X]) \quad \forall x \in \mathbb{R}

\end{align}
$$

Sostituendo $x$ con $X$ v.a. e applicando il valor atteso a entrambi i membri, otteniamo
$$
\begin{align}
\mathbb{E}[f(X)] &\geq \mathbb{E}[f(\mathbb{E}[X]) + f'(\mathbb{E}[X])(X - \mathbb{E}[X])]  \\
&= f(\mathbb{E}[X]) + f'(\mathbb{E}[X])\underbrace{(\mathbb{E}[X] - \mathbb{E}[X])}_{= 0} \\
&\implies \mathbb{E}[f(X)] \geq f(\mathbb{E}[X])
\end{align}
$$

*Osservazione:* Un'altra scelta possibile per $f$ è $f(x) = x^k$ con $k$ intero pari.

*Osservazione:* Se $f(x)$ è concava, vale da disuguaglianza di Jensen nel senso inverso.

# 2.2 Variabile Aleatoria di Bernoulli e Binomiale

**DEF:** Una v.a. si dice di *Bernoulli* di parametro $p \in [0,1]$ se
$$
X = 
\begin{cases}
1 \text{ con probabilità } p \\ 
0 \text{ con probabilità } 1-p 
\end{cases}
$$
e scriviamo $X \sim Ber(p)$.

**Valor Atteso**
$$\mathbb{E}[X] = P(X = 1) = 1\cdot p + 0 \cdot(1-p) = p$$

**DEF:** Una v.a. $X$ è detta *Binomiale* di parametri $n$ e $p$, $X \sim Bin(n,p)$ se può assumere i valori $\{0, 1, \dots, n\}$ con probabilità
$$
P(X = j) = \binom{n}{j} p^j (1-p)^{n-j}
$$
dove $\binom{n}{j}$ è il numero di sequenze con $j$ successi e $n-j$ insuccessi (numero di configurazioni per la prob. di una configurazione).

*Osservazione:* Se $X_{1}, \dots, X_{n} \sim Ber(p)$ *indipendenti*, allora
$$
Y = \sum_{i=1}^n X_{i} \sim Bin(n, p)
$$
**Valor Atteso**
$$
\mathbb{E}[Y] = \mathbb{E}\left[ \sum_{j=1}^n X_{j} \right] = \sum_{j=1}^n \mathbb{E}[X_{j}] = np
$$

*Osservazione:* Se $X_{1}, \dots, X_{n} \sim Bin(n_{i}, p)$ *indipendenti*, allora
$$
\sum_{j=1}^n X_{j} \sim Bin\left( \sum_{j=1}^n n_{i} , p\right)
$$

# 2.3 Valore Atteso Condizionato

**DEF 2.6:**
$$
\mathbb{E}[X|E] = \sum_{x_{k}} x_{k}P(X = x_{k}|E)
$$
dove $x_{k}$ sono tutti i possibili valori che può assumere $X$.

*Esempio:* Siano
$$
\begin{align}
X_{1} &= \text{risultato dado rosso} \\
X_{2} &= \text{risultato dado blu} \\
X &= X_{1} + X_{2} \text{ la loro somma} \\
\end{align}
$$
Calcoliamo $\mathbb{E}[X| X_{1} = 2]$.
$$
\begin{align}
\mathbb{E}[X|X_{1} = 2] &= \sum_{k = 3}^{12} kP(X=k|X_{1} = 2)  \\
&k=3 \text{, perchè se } X_{1} = 3 \text{ allora } X \geq 3 \\
&= \sum_{k=3}^{12} k \frac{P(X = k \cap X_{1} = 2)}{P(X_{1} = 2)} \\
&X\text{ dipende da } X_{1} \text{, non sono quindi ind. ma posso riscrivere}\\
& \text{l'evento in modo che diventino ind.} \\
&= \sum_{k=3}^{12} k \frac{P(X_{2} = k-2 \cap X_{1} = 2)}{P(X_{1} = 2)} \\
&\text{Ho riscritto la prob. come intersezione di due eventi ind.} \\
&X = X_{1} + X_{2}\text{. Sapendo che } X_{1}=2 \text{ allora } X_{2} = k-2. \\
&=\sum_{k=3}^{12} k \frac{P(X_{2} = k-2)P(X_{1} = 2)}{P(X_{1} = 2)} = \underbrace{\sum_{k=3}^{8} k P(X_{2} = k-2)}_{\text{fino a } 8,\ X_{2} \in [1,6]}  \\
&= \frac{1}{6}\sum_{k=3}^{8} k = \frac{33}{6} = \frac{11}{2}

\end{align}
$$

Vediamo ora una soluzione *smart* usando la linearità del valore atteso.
$$
\begin{align}
\mathbb{E}[X| X_{1} = 2] &= \mathbb{E}[X_{1} + X_{2} | X_{1} = 2] = \mathbb{E}[X_{1}|X_{1} = 2] + \mathbb{E}[X_{2} | X_{1} = 2] \\
&= 2 + \mathbb{E}[X_{2}] = 2 + \frac{7}{2} = \frac{11}{2}
\end{align}
$$
$\mathbb{E}[X_{2} | X_{1} = 2] = \mathbb{E}[X_{2}]$ perché il lancio del secondo dado non è influenzato dal risultato del primo (per indipendenza).

Calcoliamo adesso $\mathbb{E}[X_{1} | X=5]$. In questo caso dobbiamo applicare la formula generica del valore atteso condizionato. Non possimo applicare la linearità del valore atteso in quanto stiamo condizionando a $X=5$.
$$
\begin{align}
\mathbb{E}[X_{1} | X=5] &= \sum_{k=1}^{6} k P(X_{1} = k|X = 5) = \sum_{k=1}^{6} k \frac{P(X_{1} = k \cap X = 5)}{P(X = 5)} \\
\text{eventi ind. }&= \sum_{k=1}^6 k \frac{P(X_{1} = k \cap X_{2} = 5-k)}{P(X = 5)} \\
&=\sum_{k=1}^4 k \frac{P(X_{1} = k)P(X_{2} = 5-k)}{P(X = 5)} = \sum_{k=1}^4 \frac{k \frac{1}{6} \frac{1}{6}}{\frac{1}{9}} = \frac{5}{2}
\end{align}
$$
Più velocemente, possiamo applicare la simmetria, ovvero, poiché $X_{1}$ e $X_{2}$ hanno la stessa distribuzione deve valere che
$$
\mathbb{E}[X_{1} | X=5] = \mathbb{E}[X_{2} | X = 5]
$$
Quindi,
$$
\begin{align}
\mathbb{E}[X | X=5] &= \mathbb{E}[X_{1} + X_{2} | X = 5] = \mathbb{E}[X_{1} | X=5] + \mathbb{E}[X_{2}|X=5]  \\
&= 2\mathbb{E}[X_{1}|X = 5] \\
&\implies 5 = 2\mathbb[E][X_{1} | X = 5]  \\
&\implies = \mathbb{E}[X_{1} | X = 5] = \frac{5}{2}
\end{align}
$$

**LEMMA 2.5:** Se $X$ e $Y$ sono due v.a. con $\mathbb{E}[X]$ finito, allora
$$
\mathbb{E}[X] = \sum_{y_{k},\ P(Y=y_{k})>0} y_{k} \mathbb{E}[X | Y = y_{k}]P(Y = y_{k})
$$

*Osservazione:* È una formula simile a quella delle prob. totali, ma con le medie al posto delle probabilità.

**DIMOSTRAZIONE:** Partendo dal membro di destra
$$
\begin{align}
\sum_{y_{k,\ P(Y=y_{k} > 0)}} \mathbb{E}[X | Y=y_{k}]P(Y = y_{k}) &= \sum_{y_{k}} \left( \sum_{x_{l}} x_{l} P(X = x_{l}|Y=y_{k}) \right)P(Y=y_{l}) \\
&= \sum_{x_{l}} x_{l} \sum_{y_{k}} P(X = x_{l} | Y=y_{l})P(Y = y_{k}) \\
&= \sum_{x_{l}} x_{l}\sum_{y_{k}} P(X=x_{l} \cap Y=y_{k}) \\
&= \sum_{x_{l}} x_{l}\sum_{y_{k}} P(X=x_{l}) P(Y=y_{k}) \\
\sum_{y_{k}} P(Y=y_{k})=1\qquad &= \sum_{x_{l}} x_{l} P(X = x_{l}) = \mathbb{E}[X]
\end{align}
$$

*Spiegazione Lemma 2.5:* Ci dice che il valore atteso globale di una v.a. $X$ può essere calcolato come la *media delle medie condizionate*. Ad esempio, se vogliamo calcolare l'altezza media di tutta la popolazione ($X$), possiamo dividere la popolazione in gruppi in base alla regione di provenienza ($Y$), calcolare l'altezza media in ciascuna regione ($\mathbb{E}[X | Y = y]$), e poi fare la media di questi valori pesandoli in base a quante persone vivono in ciascuna regione ($P(Y = y)$).

**LEMMA 2.6:** Siano $X_{1}, \dots, X_{n}$ v.a. con valor atteso finito, allora $\forall Y$ v.a.
$$
\mathbb{E}\left[ \sum_{i=1}^n  X_{i} | Y=y\right] = \sum_{i=1}^n \mathbb{E}[X_{i} | Y = y]
$$

*ATTENZIONE!* Se non specifichiamo il valore della v.a. su cui stiamo condizionando, la quantità $\mathbb{E}[X|Y]$ è a sua volta una v.a. Quindi, da non confondere
- $\mathbb{E}[X|Y]$ che è una v.a. con
- $\mathbb{E}[X|Y=y]$ è un valore deterministico.

**DEF 2.7:** L'espressione $\mathbb{E}[X|Y]$ è una v.a. $f(Y)$ che assume il valore $\mathbb{E}[X|Y=y]$ quando $Y = y$.

*Esempio:* Sempre dadi. Sia $X = X_{1} + X_{2}$ la somma dei due dadi. Avevamo calcolato $\mathbb{E}[X | X_{1} = 2] = \frac{11}{2}$.
Vogliamo ora calcolare la distribuzione $f(X_{1}) = \mathbb{E}[X|X_{1}]$. $f(X_1)$ è una v.a. che può prendere certi valori con certe probabilità.
$$
\begin{align}
&\forall x_{1} \in \{1, \dots, 6\} \\
&\mathbb{E}[X|X_{1}=x_{1}] = \mathbb{E}[X_{1} + X_{2} | X_{1} = x_{1}] = x_{1} + \mathbb{E}[X_{2}] = x_{1} + \frac{7}{2}
\end{align}
$$
Quindi in generale, $f(X_{1}) = \mathbb{E}[X|X_{1}] = X_{1} + \frac{7}{2}$. La sua dist. è
$$
f(X_{1}) = 
\begin{cases}
1 + \frac{7}{2} \text{ con prob. } \frac{1}{6} \\
2 + \frac{7}{2} \text{ con prob. } \frac{1}{6} \\
\vdots \\
6 + \frac{7}{2} \text{ con prob. } \frac{1}{6} \\
\end{cases}
$$
Siccome $f(X_{1})$ è una v.a., posso calcolare l'aspettazione
$$
\mathbb{E}[f(X_{1})] = \mathbb{E}[\mathbb{E}[X|X_{1}]] = \mathbb{E}\left[ X_{1} + \frac{7}{2} \right] = \mathbb{E}[X_{1}] + \frac{7}{2} = 7
$$
In particolare, $\mathbb{E}[f(X_{1})] = \mathbb{E}[\mathbb{E}[X|X_{1}]] = \mathbb{E}[X]$.

**TEOREMA 2.7 (Proprietà della Torre)**
$$
\mathbb{E}[\mathbb{E}[X|Y]] = \mathbb{E}[X] 
$$
**DIMOSTRAZIONE:** Conseguenza del Lemma 2.5
$$
\mathbb{E}[\mathbb{E}[X|Y]] \underbrace{=}_{\text{Def. media condizionata}} \sum_{y_{k}} y_{k} \mathbb{E}[X | Y=y_{k}]P(Y=y_{k}) \underbrace{=}_{\text{Lemma } 2.5} \mathbb{E}[X]
$$

# 2.4 Distribuzione Geometrica

*Interpretazione:* Supponiamo di lanciare una moneta finché non esce *TESTA*. Qual è la distribuzione del numero di lanci? Questo è un esempio di *distribuzione geometrica*, ossia: eseguiamo una sequenza di prove indipendenti finché non otteniamo il *primo successo*, ciascuna prova con probabilità $p$.

**DEF 2.8:** $X$ è detta geometrica di parametro $p \in (0,1)$ ($X \sim Geom(p)$) se
$$
P(X = k) = (1-p)^k p \quad \forall\ k=1,2,3, \dots 
$$
- $k-1$ insucessi con probabilità $1-p = q$
- Successo alla $k$-esima prova con prob. $p$.

*Esercizio:* Verificare che $\sum_{k=1}^\infty P(X = k) = 1$.
$$
\sum_{k=1}^\infty P(X = k) = \sum_{k=1}^\infty (1-p)^k p = p \sum_{k=1}^\infty (1-p)^k = p \frac{1}{1 - (1-p)} = 1
$$

### Ripasso Serie Geometrica

**DEF:** Definiamo serie geometrica la seguente sommatoria:
$$
\sum_{k=m}^n q^k = 
\begin{cases} 
\frac{q^m}{1-q} &\iff |q| < 1 \\
+\infty &\iff q \geq 1  \\
\text{non esiste} &\iff q \leq -1
\end{cases}
$$
1. Per $n$ fissato vale che $\sum_{k=0}^n x^k = \frac{1-x^{n+1}}{1-x}$
2. Se la serie non parte da 0, ma da $k= m$, allora $$\sum_{k=m}^n x^k = \frac{x^m - x^{n-1}}{1 - x}$$
3. Per $|x| < 1$ (nel nostro caso $p \in (0,1)$, quindi vale sempre) 

$$\begin{align}
\sum_{k=0}^\infty x^k = \lim_{ n \to \infty } \sum_{k=0}^\infty x^k = \lim_{ n \to \infty } \frac{1- x^{n+1}}{1-x} = \frac{1}{1-x}
  \\ \\
   \boxed{\sum_{k=0}^\infty x^k = \frac{1}{1-x}} \quad
   \boxed{\sum_{k=1}^\infty x^k = \frac{x}{1-x}} \quad
   \boxed{\sum_{k=m}^\infty x^k = \frac{x^m}{1-x}}
\end{align}
$$
*Osservazione:* Si dice che la v.a. Geometrica *non abbia memoria*. Sapendo di aver fallito nelle prime $k$ prove, la probabilità di avere successo dopo altre $n$ prove è la stessa che si avrebbe all'inizio del processo.

**LEMMA 2.8 (perdità memoria della geometrica)**
Sia $X \sim Geom(p)$, allora
$$
P(X = n+k | X > k) = P(X = n) \quad \forall k,n \in \{1,2, \dots \}
$$
**DIMOSTRAZIONE:** 
$$
\begin{align}
P(X = n+k | X > k) &= \frac{P(\{X = n+k \cap X > k\})}{P(X > k)} \\
\{X = n+k\} \implies \{X > k\}&= \frac{P(X = n+k)}{P(X > k)} = \frac{(1 - p)^{n+k-1} p}{(1-p)^k}  \\
&= (1-p)^{n-1}p = P(X = n)
\end{align}
$$
Notiamo che $P(X > k) = (1-p)^k$. Qual è la prob. che il primo successo avvenga dopo il tentativo $k$? Significa che i primi $k$ tentativi devono essere tutti fallimenti ($P(X \geq k) = (1-p)^{k-1}$).
$$
P(X > k) = \sum_{i=k+1}^\infty p(1-p)^{i-1} = p \sum_{i=k}^\infty (1-p)^i = \frac{p (1-p)^k}{1 - (1 - p)} = (1 - p)^k
$$

A questo punto possiamo dare una formula alternativa per calcolare l'aspettazione di un v.a. positiva.

**LEMMA 2.9:** Sia $X$ una v.a. a valori interi positivi, si ha
$$
\mathbb{E}[X] = \sum_{n=1}^\infty P(X \geq n)
$$
**DIMOSTRAZIONE:**
$$
\sum_{n=1}^\infty P(X \geq n) = \sum_{n=1}^\infty \sum_{k=n}^\infty P(X = k)
$$
Infatti, $P(X \geq n) = \sum_{k = n}^\infty P(X = k) = P(X = n) + P(X = n+1) + \dots$
$$
= \sum_{k=1}^\infty \sum_{n=1}^k P(X=k) = \sum_{k=1}^\infty k P(X = k) = \mathbb{E}[X]
$$
**VALOR ATTESO**

###### 1. MODO 1
Usiamo il Lemma 2.9 per calcolare il valore atteso di $X \sim Geom(p)$.

Abbiamo che $P(X \geq n) = P(X > n-1) = (1-p)^{n-1}$, quindi
$$
\begin{align}
\mathbb{E}[X] = \sum_{n=1}^\infty P(X \geq n) = \sum_{n=1}^\infty (1-p)^{n-1} &\underbrace{=}_{k = n-1} \sum_{k=0}^{\infty} (1-p)^k \\
&= \frac{1}{1-(1-p)} =\frac{1}{p}
\end{align}
$$

###### 2. MODO 2
Usiamo la media condizionata. Sia $X \sim Geom(p)$ e sia
$$
Y = 
\begin{cases}
1 \text{ il primo lancio è T} \\
0 \text{ altrimenti}
\end{cases}
$$
Condizionando sul primo lancio della moneta, abbiamo
$$
\begin{align}
\mathbb{E}[X] &= \mathbb{E}[X | Y = 0]P(Y = 0) + \mathbb{E}[X|Y=1]P(Y=1) \\
&= \mathbb{E}[X|Y=0](1-p) + \underbrace{\mathbb{E}[X|Y]}_{= 1 \text{ se ho T al primo lancio}}p \\
&=\mathbb{E}[X | Y=0](1-p) + p
\end{align}
$$
Ora, $\mathbb{E}[X|Y=0] = 1 + \mathbb{E}[X]$. Infatti, se $Y = 0$ allora il numero di tentativi deve essere $X > 1$.
$$
\begin{align}
\mathbb{E}[X | Y = 0] - 1 &= \mathbb{E}[X - 1 | X > 1] = \sum_{n \geq 1}^\infty n P(X - 1 = n | X > 1) \\
\text{Lemma 2.8}&=\sum_{n\geq_{1}}^\infty n P(X = n) = \mathbb{E}[X]
\end{align}
$$
Quindi, 
$$
\begin{align}
\mathbb{E}[X] &= (1 + \mathbb{E}[X])(1-p) + p  \\
&\implies \mathbb{E}[X] = 1 + \mathbb{E}[X] - p - p\mathbb{E}[X] + p \\
&\implies \mathbb{E}[X] = \frac{1}{p}
\end{align}
$$

### Esempi di Calcolo

#### Es.1
Siano $X \sim Geom(p)$ e $Y \sim Geom(q)$, allora

$$
\begin{align}
\boxed{P(X > Y) = \frac{q(1-p)}{q + p - pq}} \\ \\
\boxed{P(X < Y) = \frac{p(1-q)}{q + p - pq}} \\ \\
\boxed{P(X = Y) = \frac{pq}{q + p - pq}}
\end{align}
$$

TODO: Fare i calcoli.

#### Es.2
In generale vale la seguente relazione algebrica: Siano $X$ e $Y$ due v.a. avente la stessa distribuzione
$$
X + Y = \min(X, Y) + \max(X, Y)
$$
Applicando l'aspettazione ad entrambi i membri, otteniamo che
$$
\mathbb{E}[X + Y] = \mathbb{E}[\min(X, Y)] + \mathbb{E}[\max(X, Y)]
$$
Se $X \sim Geom(p)$ e $Y \sim Geom(q)$, allora

$$
\begin{align}
&\boxed{\mathbb{E}[X + Y] = \frac{1}{p} + \frac{1}{q}} \\ \\
&\boxed{\mathbb{E}[\min(X, Y)] = \frac{1}{r} = \frac{1}{p + q - pq}} \\ \\
&\boxed{\mathbb{E}[\max(X,Y)] = \frac{1}{p} + \frac{1}{q} - \frac{1}{r}}
\end{align}
$$

Se $X \sim Bin(n,p)$ e $Y \sim Bin(m,q)$, allora...