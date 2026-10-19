
Esercizi Proposti dal libro Probability and Computing - Michael Mitzenmacher Eli Upfal.

1. 1.4, 1.6, 1.13, 1.14, 1.19, 1.20, 1.22
2. 2.1, 2.6, 2.7, 2.8, 2.9, 2.12, 2.16, 2.24, 2.25
3. 3.2, 3.3, 3.4, 3.7, 3.13, 3.17, 3.20 (II ed. 3.22, 3.23, 3.26)
4. 4.1, 4.2, 4.3, 4.4, 4.5, 4.10, 4.12
5. 5.10
6. 7.2, 7.7, 7.11, 7.17 (solo stazionaria)



# Esercizio 2.24

Lanciamo un dado equo (a sei facce) ripetutamente. Qual è il numero atteso di lanci fino alla comparsa della prima coppia di 6 consecutivi?

Possiamo risolvere questo esercizio in due modi diversi. Uno standard definendo due v.a. aleatorie oppure definendo una catena di Markov.

Generalizzare poi il problema ad $n$ facce ed $r$ 6 consecutivi.
## Soluzione Standard:

Siano
$$
\begin{align}
&X: \text{\# di lanci prima di vedere un 6}  \\
&Y: \text{\# di lanci prima di vedere due 6 consecutivi}
\end{align}
$$
---
# Esercizio 2.20, 3.22 (Esame 24.02.2025)

Un punto fisso di una permutazione $\pi: [1, n] \to [1, n]$ è un valore per il quale $\pi(x) = x$. 

- Descrivere la legge di $\pi$
- Trova il valore atteso del numero di punti fissi di una permutazione scelta uniformemente a caso tra tutte le permutazioni
- Trova la varianza del numero di punti fissi di una permutazione scelta uniformemente a caso tra tutte le permutazioni.

(Suggerimento: Sia $X_i$ uguale a $1$ se $\pi(i) = i$, in modo che $\sum_{i=1}^n X_i$ sia il numero di punti fissi. Non puoi usare la linearità per trovare $Var[\sum_{i=1}^n X_i]$, ma puoi calcolarla direttamente.)

## Soluzione

Sia $\pi$ una permutazione scelta uniformemente a caso tra le $n!$ 

$$P(\pi = \sigma) = \frac{1}{n!}$$

permutazioni di $[1,n]$. Per $i=1,\dots,n$ definiamo le variabili indicatrici: $$ X_i = \mathbb{1}[\pi(i)=i], \qquad X = \sum_{i=1}^n X_i \quad (\text{numero totale di punti fissi}) $$
#### Valore atteso

Per simmetria, ogni immagine $\pi(i)$ è uniforme su ${1,\dots,n}$, quindi: 
$$ \mathbb{E}[X_i] = \Pr(\pi(i)=i) = \frac{(n-1)!}{n!} = \frac{(n-1)(n-2)!}{n(n-1)(n-2)!} = \frac1n $$

Per **linearità dell'aspettativa** (valida anche con $X_i$ dipendenti tra loro): $$ \mathbb{E}[X] = \sum_{i=1}^n \mathbb{E}[X_i] = n\cdot\frac1n = 1 $$
$$ \boxed{\mathbb{E}[X] = 1} $$

---

#### Varianza

Usiamo $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \mathbb{E}[X^2] - 1$.

*Osservazione:* Non possiamo usare la formula $VAR[X] = \sum_{i=1}^n VAR[X_{i}]$ perchè le $X_{i}$ sono dipendenti tra loro. Dato un punto fisso $\pi(i) = i$, i restanti elementi della permutazione dipendono dal punto fisso.
##### Calcolo di $\mathbb{E}[X^2]$

Scriviamo $X^2 = \left(\sum_i X_i\right)^2 = \sum_i X_i^2 + \sum_{i\ne j} X_i X_j$, quindi: $$ \mathbb{E}[X^2] = \sum_{i=1}^n \mathbb{E}[X_i^2] + \sum_{i\ne j} \mathbb{E}[X_iX_j] $$
**Termine 1 — $\mathbb{E}[X_i^2]$.** Poiché $X_i$ è un indicatore (vale $0$ o $1$), $X_i^2=X_i$: $$ \mathbb{E}[X_i^2] = \mathbb{E}[X_i] = \frac1n $$ Sommando sugli $n$ indici: $$ \sum_{i=1}^n \mathbb{E}[X_i^2] = n\cdot\frac1n = 1 $$

**Termine 2 — $\mathbb{E}[X_iX_j]$ per $i\ne j$.** Questo vale $\Pr(\pi(i)=i,\ \pi(j)=j)$, cioè la probabilità che **due** punti specifici siano fissi simultaneamente. Fissati $\pi(i)=i$ e $\pi(j)=j$, restano da permutare liberamente gli altri $n-2$ elementi: 
$$
\begin{align}
\Pr(X_{i}X_{j} = 1) &= \Pr(\pi(i)=i,,\pi(j)=j) = \frac{(n-2)!}{n!}  \\
&= \frac{(n-2)(n-3)!}{n(n-1)(n-2)(n-3)!}  =  \frac{1}{n(n-1)}
\end{align}
$$

Il numero di coppie ordinate $(i,j)$ con $i\ne j$ è $n(n-1)$. 
Quando espandiamo il quadrato di una somma di nn n termini, otteniamo una **doppia somma** su tutte le coppie ordinate $(i,j)$ con $i,j \in \{1,\dots,n\}$, cioè una somma con $n \times n= n^2$ termini in totale. 
- I termini con $i = j$ sono esattamente $n$.
- I termin $i \neq j$ sono $n(n-1)$.
Quindi: $$ \sum_{i\ne j} \mathbb{E}[X_iX_j] = n(n-1)\cdot\frac{1}{n(n-1)} = 1 $$
In conclusione

$$ \mathbb{E}[X^2] = \underbrace{1}_{\text{termine 1}} + \underbrace{1}_{\text{termine 2}} = 2 $$

$$ \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = 2 - 1^2 = 1 $$

$$ \boxed{\text{Var}(X) = 1} $$

---

*Osservazione:* Sia il valore atteso ($=1$) sia la varianza ($=1$) sono **indipendenti da $n$** (per $n\ge 2$) — risultato sorprendente, dato che il numero di punti fissi è una variabile su un dominio che cresce con $n$ ma la sua distribuzione si "stabilizza".

---
# Esercizio 4.10

Un casinò sta testando una nuova categoria di slot machine semplici. Ad ogni partita, il giocatore inserisce 1$ e la slot machine dovrebbe restituire al giocatore 3$ con probabilità $\frac{4}{25}$, 100$ con probabilità $\frac{1}{200}$ oppure nulla con la probabilità residua.
Ogni partita è considerata indipendente dalle altre.
Il casinò è rimasto sorpreso nello scoprire, durante i test, che le macchine hanno perso 10.000$ nel corso del primo milione di partite. Derivare un Chernoff Boound per la probabilità di questo evento.

## Soluzione

Sia $N = 10^6$. Definiamo la v.a. 
$$
X_{i} = \begin{cases}
2 &\text{ con prob. } p = \frac{4}{25} \\
99 &\text{ con prob. } p = \frac{1}{200} \\
-1 &\text{ con prob. } p = \frac{167}{200} 
\end{cases}
$$
e sia 
$$
X = \sum_{i=1}^N X_{i}
$$
A questo punto, siamo interessati a stimare la probabilità
$$
P(X \geq 10^4)
$$

Andremo a definire il CB da 0, calcolando la f.g.m + esponenziale + Markov + ottimizzazione su $t$.

$$
\begin{align}
&\mathbb{E}[X_{i}] = 2 \cdot \frac{4}{25} + 99 \cdot \frac{1}{200} + (-1)\cdot \frac{167}{200} = -\frac{1}{50}  \\
&\mathbb{E}[X] = -\frac{10^6}{50} = -2 \cdot 10^4
\end{align}
$$
Dove $\mathbb{E}[X_{i}]$ è la perdità media per ogni giocata. Calcoliamo ora
$$
\begin{align}
M_{X}(t) &= \mathbb{E}[e^{tX}] = \mathbb{E}\left[ e^{t\sum_{i=1}^N X_{i}} \right] = \prod_{i=1}^N \mathbb{E}[e^{tX_{i}}]  \\
&= \prod_{i=1}^N \left( e^{2t} \frac{32}{200} + e^{99t}\frac{1}{200} + e^{-t} \frac{167}{200} \right)  \\
&= \frac{1}{200^N}\left( e^{2t} 32 + e^{99t} + e^{-t} 167 \right)^N
\end{align}
$$
A questo punto siamo pronti a calcolare il CB
$$
\begin{align}
P(X \geq 10^4) &\underbrace{=}_{t \geq 0} P(e^{tX} \geq e^{t10^4}) \underbrace{\leq}_{\text{Markov}} \frac{\mathbb{E}[e^{tX}]}{e^{t10^4}} \\
f(t)&= e^{10^4t} \cdot 200^{-10^6}\left( e^{2t} 32 + e^{99t} + e^{-t} 167 \right)^{-10^6}
\end{align}
$$
Questa disuguaglianza vale $\forall t \geq 0$. Possiamo prendere il $t$ che minimizza $f(t)$, ottenendo 
$$
t^* \approx 0.0001577, \quad f(t^*) \approx 0.0001586
$$

---
# Esercizio 1 (Esame 19.06.2024)

TODO: DA FARE

---
# Esercizio 1 (Esame 22.06.2026)

Sia $X \sim Geom(p),\ p\in(0,1)$. Dimostrare che la probabilità dell'evento $\{ X = 2 \}$ diventa più del doppio se condizioniamo all'evento $\{ X \text{ è pari} \}$ rispetto alla probabilità dello stesso evento senza condizionamento.

## Soluzione

Si ha che 
$$
P(X = 2) = p(1-p)
$$
Calcoliamo ora 
$$
P(X = 2 | X \text{ è pari}) = \frac{P(X = 2 \cap X \text{ è pari})}{P(X \text{ è pari})} = \frac{P(X = 2)}{P(X = 2k)}
$$

$$
\begin{align}
P(X = 2k) &= \sum_{k=1}^\infty p (1-p)^{2k-1} \underbrace{=}_{q = 1-p} p\sum_{k=1}^\infty q^{2k-1} = \frac{p}{q}\sum_{k=1}^\infty q^{2k} = \frac{p}{q}\sum_{k=1}^\infty (q^2)^k \\
&\text{è una geometrica di ragione } q^2 \\
&= \frac{p}{q} \cdot \frac{q^2}{1 - q^2} = \frac{pq}{1-q^2} \\
&= \frac{p(1-p)}{1-(1-p)^2} = \frac{p(1-p)}{2p - p^2} \\
&=\frac{p(1-p)}{p(2-p)} = \frac{1-p}{2-p}
\end{align}
$$
Quindi
$$
\begin{align}
&\boxed{P(X = 2) = p(1-p)} \\ \\
&\boxed{P(X = 2 | X \text{ è pari}) = p(1-p) \cdot \frac{2-p}{1-p} = p(2-p)}
\end{align}
$$
L'esercizio chiede di dimostrare che
$$
\begin{align}
P(X = 2 | X \text{ è pari}) &\overbrace{>}^{?} 2P(X = 2) &\iff \\
p(2-p) &> 2p(1-p) &\iff \\
2p - p^2 &> 2p - 2p^2 &\iff \\
2p^2 + p^2 &> 0 &\iff \\
p^2 &> 0 \qquad \forall\ p \in(0,1)
\end{align}
$$

---
# Esercizio 1 Esame 16.07.2024

##### (a) Siano $X$ e $Y$ due v.a. i.i.d a media finita. Calcolare $\mathbb{E}[X|X+Y]$
Risolviamo l'esercizio completo, punto per punto.

Poiché $X$ e $Y$ sono i.i.d. (in particolare hanno la stessa distribuzione), per un **argomento di simmetria**: $$\mathbb{E}[X \mid X+Y] = \mathbb{E}[Y \mid X+Y]$$
Infatti la coppia $(X,Y)$ ha la stessa legge congiunta di $(Y,X)$ essendo i.i.d., quindi condizionare rispetto alla somma (che è simmetrica in $X,Y$) dà lo stesso risultato scambiando i ruoli.

D'altra parte, per **linearità dell'attesa condizionata**: $$\mathbb{E}[X \mid X+Y] + \mathbb{E}[Y \mid X+Y] = \mathbb{E}[X+Y \mid X+Y] = X+Y$$
Combinando le due relazioni: $$2\mathbb{E}[X \mid X+Y] = X+Y \quad \Longrightarrow \quad \boxed{\mathbb{E}[X \mid X+Y] = \frac{X+Y}{2}}$$
##### (b) Siano $X_{1}, \dots, X_{n}$ varibiali i.i.d di media finita $\mu$ e sia $S = \sum_{i=1}^n X_{i}$. Calcolare $\mathbb{E}[X_{1}|S]$ e $\mathbb{E}[S|X_{1}]$

Stesso argomento di simmetria del punto (a), esteso a $n$ variabili: poiché $X_1, \dots, X_n$ sono i.i.d., per ogni $i,j$: $$\mathbb{E}[X_i \mid S] = \mathbb{E}[X_j \mid S]$$
Sommando su tutti gli indici $i = 1, \dots, n$: $$\sum_{i=1}^n \mathbb{E}[X_i \mid S] = \mathbb{E}\left[\sum_{i=1}^n X_i \Big| S\right] = \mathbb{E}[S \mid S] = S$$
Ma per simmetria ogni termine della somma a sinistra vale $\mathbb{E}[X_1 \mid S]$, quindi: $$n \cdot \mathbb{E}[X_1 \mid S] = S \quad \Longrightarrow \quad \boxed{\mathbb{E}[X_1 \mid S] = \frac{S}{n}}$$
Scriviamo $S = X_1 + \sum_{i=2}^n X_i$. Per linearità: $$\mathbb{E}[S \mid X_1] = \mathbb{E}[X_1 \mid X_1] + \mathbb{E}\left[\sum_{i=2}^n X_i \Big| X_1\right]$$
Il primo termine è semplicemente $X_1$ (è nota, condizionandoci su se stessa). Il secondo termine: poiché $X_2, \dots, X_n$ sono **indipendenti** da $X_1$, condizionare su $X_1$ non cambia la loro attesa: $$\mathbb{E}\left[\sum_{i=2}^n X_i \Big| X_1\right] = \sum_{i=2}^n \mathbb{E}[X_i] = (n-1)\mu$$

Quindi: $$\boxed{\mathbb{E}[S \mid X_1] = X_1 + (n-1)\mu}$$
##### (c) Siano ora $X$ e $Y$ due variabili indipendenti di Poisson di parametri $\lambda_{1}$ e $\lambda_{2}$ e sia $Z = X + Y$

###### (i) Calcolo di $\mathbb{P}(X=k \mid Z=n)$

Prima ricordiamo che, per la proprietà di somma di Poisson indipendenti, $Z \sim \text{Poisson}(\lambda_1+\lambda_2)$.

Per $k = 0, 1, \dots, n$ (altrimenti la probabilità è $0$, dato che $Y \geq 0$):

$$\mathbb{P}(X=k \mid Z=n) = \frac{\mathbb{P}(X=k, Z=n)}{\mathbb{P}(Z=n)} = \frac{\mathbb{P}(X=k, Y=n-k)}{\mathbb{P}(Z=n)}$$

Per l'**indipendenza** di $X$ e $Y$: $\mathbb{P}(X=k, Y=n-k) = \mathbb{P}(X=k),\mathbb{P}(Y=n-k)$.

Sostituendo le densità di Poisson: $$\mathbb{P}(X=k \mid Z=n) = \frac{e^{-\lambda_1}\dfrac{\lambda_1^k}{k!} \cdot e^{-\lambda_2}\dfrac{\lambda_2^{n-k}}{(n-k)!}}{e^{-(\lambda_1+\lambda_2)}\dfrac{(\lambda_1+\lambda_2)^n}{n!}}$$
Gli esponenziali si semplificano ($e^{-\lambda_1-\lambda_2}$ compare sia sopra che sotto): $$= \frac{n!}{k!(n-k)!} \cdot \frac{\lambda_1^k \lambda_2^{n-k}}{(\lambda_1+\lambda_2)^n}$$
Riscriviamo separando le potenze di $(\lambda_1+\lambda_2)$: $$= \binom{n}{k} \left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^{k} \left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k}$$
$$\boxed{\mathbb{P}(X=k \mid Z=n) = \binom{n}{k} \left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^{k} \left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k}, \quad k=0,\dots,n}$$

###### (ii) Identificazione della distribuzione

L'espressione trovata è esattamente la funzione di massa di probabilità di una **distribuzione Binomiale** con parametri: $$n \quad \text{(numero di prove)}, \qquad p = \frac{\lambda_1}{\lambda_1+\lambda_2} \quad \text{(probabilità di successo)}$$

Infatti ponendo $p = \frac{\lambda_1}{\lambda_1+\lambda_2}$, si ha $1-p = \frac{\lambda_2}{\lambda_1+\lambda_2}$, e la formula diventa proprio $\binom{n}{k}p^k(1-p)^{n-k}$.

$$\boxed{X \mid {Z=n} ;\sim; \text{Binomiale}\left(n,; p=\frac{\lambda_1}{\lambda_1+\lambda_2}\right)}$$

###### (iii) Calcolare $\mathbb{E}[X|Z]$

Sapendo che la definizione formale di attesa condizionata $\mathbb{E}[X\mid Z]$ è: **una variabile aleatoria che è funzione di $Z$**, definita punto per punto da: $$\mathbb{E}[X \mid Z] = g(Z) \quad \text{dove} \quad g(n) := \mathbb{E}[X \mid Z=n] \text{ per ogni valore } n$$
Sia, per ogni $n$ fissato: $$g(n) = \mathbb{E}[X \mid Z=n] = np$$
(perché $X\mid{Z=n}\sim\text{Bin}(n,p)$, e la Binomiale ha media $np$).
Quindi $g$ è la funzione $g(n) = np$, e per definizione: $$\mathbb{E}[X\mid Z] = g(Z) = Zp$$

$$\boxed{\mathbb{E}[X \mid Z] = g(Z) = pZ = \frac{\lambda_1}{\lambda_1+\lambda_2}Z}$$
---
# Esercizio 3 Esame 16.07.2024

Alice e Marcello collezionano le figurine dei Cucciolotti (e non fanno scambi!). L'album conta ben $N$ figurine, ed ipotizziamo che ogni nuovo pacchetto contenga una sola figurina, scelta a caso tra le $N$ figurine.
1. Calcolare la media di pacchetti che Alice dovrà comprare per finire l'album.
2. Calcolare la probabilità che almeno uno tra Alice e Marcello non abbia trovato la figurina numero 1 dopo aver comprato $M$ pacchetti ciascuno.
3. Utilizzare il punto (2) per limitare dall'alto la probabilità che, dopo aver comprato $2N\log N$ pacchetti ciascuno, almeno uno dei due non abbia ancora  terminato la collezione.

## Soluzione

Il punto (1) è semplice l'applicazione del coupon collector. Sia 
$$
X_{j} \text{\# di pacchetti per trovare la }j\text{-esima figurina avendone }j-1\text{ diverse}
$$
Siamo quindi interessati a $\mathbb{E}[X] = \sum_{j=1}^N \mathbb{E}[X_{j}]$, dove
$$
X_{j} \sim Geom\left( 1 - \frac{j-1}{n} \right),\quad \mathbb{E}[X_{j}] = \frac{n}{n - j + 1}
$$
Si ha quindi che
$$
\mathbb{E}[X] = \sum_{j=1}^N \mathbb{E}[X_{j}] = \sum_{j=1}^N \frac{N}{N - j + 1} = N \sum_{i=1}^N \frac{1}{i} = NH_{N} \approx N \log N
$$

Per quanto riguarda il punto due, sia per Alice che per Marcello vale che
$$
\begin{align}
P(\text{Alice non ha la fig. 1 dopo }M\text{ pacchetti}) &= \left( 1 - \frac{1}{N} \right)^M \\
P(\text{Marcello non ha la fig. 1 dopo }M\text{ pacchetti}) &= \left( 1 - \frac{1}{N} \right)^M
\end{align}
$$
di conseguenza,
$$
\begin{align}
P(\text{Alice ha la fig.1}) = P(\text{Marcello ha la fig. 1}) = 1 - \left( 1 - \frac{1}{N} \right)^M  \\
\implies P(\text{entrambi hanno la fig. 1}) = \left[ 1 - \left( 1 - \frac{1}{N} \right)^M \right]^2
\end{align}
$$
quindi
$$
\begin{align}
P(\text{almeno ad uno manca la fig. 1}) &= 1 - P(\text{entrambi hanno la fig. 1}) \\
&= 1 - \left[ 1 - \left( 1 - \frac{1}{N} \right)^M \right]^2
\end{align}
$$
Per il punto 3, dobbiamo dare un bound a questa probabilità.

$$
P(\text{Alice non ha la fig. } i) = \left( 1 - \frac{1}{N} \right)^M \underbrace{\leq}_{M = 2N\log N} e^{-2\log N} \leq \frac{1}{N^2}
$$
Quindi
$$
\begin{align}
P(\text{almeno ad uno manca la fig. } i) &= 1 - \left[ 1 - \left( 1 - \frac{1}{N} \right)^M \right]^2 \\
&\leq 1 - \left[ 1 - \frac{1}{N^2} \right]^2 \\
&= 1 - \left[ 1 + \frac{1}{N^4} - \frac{2}{N^2} \right] \\
&= \frac{2}{N^2} - \frac{1}{N^4} \leq \frac{2}{N^2}
\end{align}
$$

A questo punto, dobbiamo considerare ciascuna figurina $i = 1, \dots, N$, quindi
$$
\begin{align}
&P(\text{almeno uno dei }2 \text{ non ha completato dopo } 2N\log N \text{ pacchetti ciascuno}) \\
&=P\left( \bigcup_{i=1}^N \text{esiste almeno una fig. } i \text{ che manca ad uno dei due} \right)  \\
&\leq \sum_{i=1}^NP(\text{esiste almeno una fig. } i \text{ che manca ad uno dei due})  \\
&= \sum_{i=1}^N \frac{2}{N^2} = N \frac{2}{N^2} = \frac{2}{N}
\end{align}
$$

---

# Esercizio 2 Esame 19.06.2024

Si vuole condurre un sondaggio per scoprire quante persone sono a favore del divieto di vendità di auto con con motore a combustione entro il 2035. Sia $p$ la vera percentuale della popolazione a favore e supponiamo di sapere che $p$ è almeno il $10\%$. Utilizzare una disuguaglianza di Chernoff per stimare quante persone prese a caso dalla popolazione devono essere intervistate affinché la frazione $X$ di coloro che si dicono a favore della misura approssimi $p$ con un errore al più del $10\%$ con probabilità superiore a $0.99$, cioè tale che
$$
P(|X - p| \leq 0.1p) \geq 0.99
$$
Come cambia il numero di persone da intervistare se vogliamo stimare $p$ con un errore dell'$1\%$?

---
# Esercizio 1 Esame 07.07.2026

Siano $X_{1}, X_{2}, \dots, X_{N}$ variabili aleatorie i.i.d con distribuzione uniforme su $\{1, \dots, L\}$. Sia
$$
X = \sum_{i=1}^N X_{i}
$$
##### 1. Calcolare $\mathbb{E}[X]$ e $VAR[X]$.

Sapendo che
- $\mathbb{E}[X_{i}] = \sum_{i=j}^L j\ P(X_{i} = j) = \frac{L+1}{2}$.
- $\mathbb{E}[X_{i}^2] = \sum_{j=1}^L j^2\ P(X_{i} = j) = \frac{(L+1)(2L + 1)}{6}$
- $VAR[X_{i}] = \mathbb{E}[X_{i}^2] - \mathbb{E}[X_{i}]^2 = \frac{L^2 - 1}{12}$

$$
\begin{align}
\mathbb{E}[X] &= \sum_{i=1}^N \mathbb{E}[X_{i}] = \frac{N(L+1)}{2} \\
VAR[X] &= \sum_{i=1}^N VAR[X_{i}] = \frac{N(L^2 - 1)}{12}
\end{align}
$$

##### 2. Per $\epsilon > 0$, limitare dall'alto con la disuguaglianza di Chebychev la probabilità che $X$ ecceda di più $\epsilon N$ la propria media, ovvero
$$
P(X \geq \mathbb{E}[X] + \epsilon N)
$$

La disuguaglianza di Chebychev dice che:
$$
P(|X - \mathbb{E}[X]| \geq a) \leq \frac{VAR[X]}{a^2}
$$
quindi,
$$
\begin{align}
P(X \geq \mathbb{E}[X] + \epsilon N) &= P(X - \mathbb{E}[X] \geq \epsilon N)  \\ \\
&\leq P(|X - \mathbb{E}[X]| \geq \epsilon N)  \\ \\
&\leq \frac{1}{\epsilon^2N^2} \frac{N(L^2-1)}{12} = \frac{L^2 - 1}{\epsilon^2N}
\end{align}
$$

##### 3. Limitare la stessa probabilità con una disuguaglianza di Hoeffding

Ricordiamo la disuguaglianza di Hoeffding:
$$
P\left( \left|\frac{1}{N}(X - \mathbb{E}[X])\right| \geq \epsilon N \right) \leq 2\exp\left( -\frac{2N\epsilon^2}{(b-a)^2} \right)
$$
quindi,
$$
\begin{align}
P(X \geq \mathbb{E}[X] + \epsilon N)  &= P(X - \mathbb{E}[X] \geq \epsilon N)   \\
&= P(\frac{1}{N}(X - \mathbb{E}[X]) \geq \epsilon)  \\
&\leq \frac{1}{2} 2\exp\left( -\frac{2N\epsilon^2}{(L - 1)^2} \right)  \\
&= \exp\left( -\frac{2N\epsilon^2}{(L - 1)} \right)
\end{align}
$$

##### 4. Calcolare la funzione di distribuzione della variabile aleatoria
$$
Y = \max_{j=1, \dots, N} X_{j}
$$
ovvero calcolare $P(Y \leq k)$ per ogni $k \in \mathbb{N}$.
$$
P(Y \leq k) = 
\begin{cases}
1 &\iff k \geq L \\
\left( \frac{k}{L} \right)^N &\iff 1 \leq k \leq L \\
0 &\iff k < 1
\end{cases}
$$
*Nota:* Per $1 \leq k \leq L,\ P(Y \leq k) = \left( \frac{k}{L} \right)^N$ perchè:
$$
\begin{align}
P(Y \leq k) &= P(\max_{j = 1, \dots, N} X_{j} \leq k)  \\ \\
&= P(\{X_{1} \leq k \land X_{2} \leq k\ \land \dots \land X_{N} \leq k\})   \\ \\
&= \prod_{i=1}^N P(X_{j} \leq k) = \prod_{i=1}^N \frac{k}{L} =\left( \frac{k}{L} \right)^N
\end{align}
$$

##### 5. Calcolare  $P(X_{1} = \ell | Y \leq k)$ per ogni $k,\ell \in \mathbb{N}$

Dalla definizione di probabilità condizionata, abbiamo che
$$
P(X_{1} = \ell | Y \leq k) = \frac{P(X = \ell \land Y \leq k)}{P(Y \leq k)}
$$
Studiamo ora la varie casistiche:
1. $\ell > k \lor  \ell < 1 \lor \ell > L$. L'evento $\{X_{1} = \ell \land Y \leq k\}$ è impossibile poichè $$Y = \max X_{j} \leq X_{1} = \ell > k$$dunque la probabilità è 0.
2. $1 \leq \ell \leq k \leq L$. L'evento $$\{X_{1} = \ell \land Y \leq k\} = \{X_{1} = \ell\} \land \{X_{2} \leq k\} \land \dots \land \{X_{n} \leq k\}$$Quindi $$\begin{align}
P(X_{1} = \ell \land Y \leq k) &= P(X_{1} = \ell) \prod_{j=2}^N P(X_{j} \leq k)  \\
&= \frac{1}{L} \left( \frac{k}{L} \right)^{N-1} = \frac{k^{N-1}}{L^N}\end{align}$$ Quindi la prob. condizionata vale: $$P(X_{1} = \ell | Y \leq k) = \frac{k^{N-1}}{L^N} \cdot \left( \frac{L}{k} \right)^N = \frac{1}{k}$$
3. $k \geq L \land 1 \leq \ell \leq L$. L'evento $\{Y \leq k\}$ è certo, quindi la condizione non ristringe. $$P(X_{1} = \ell | Y \leq k) = P(X_{1} = \ell) = \frac{1}{L}$$
Riassumendo,
$$
P(X_{1} = \ell | Y \leq k) = 
\begin{cases}
0 &\iff \ell > k \lor \ell < 1 \lor \ell > L \\
\frac{1}{k} &\iff 1 \leq \ell \leq k \leq L \\
\frac{1}{L} &\iff k \geq L \land 1\leq \ell \leq k
\end{cases}
$$
##### 6. Calcolare  $P(Y \leq k | X_{1} = \ell)$ per ogni $k, \ell \in \mathbb{N}$

Usando Bayes, abbiamo che
$$
\begin{align*}
&P(Y \leq k \mid X_1 = \ell)
    = \frac{P(X_1 = \ell \mid Y \leq k)}{P(X_1 = \ell)} \\[16pt]
    &= \begin{cases}
        0 &\iff \ell > k \ \lor \ \ell < 1 \ \lor \ \ell > L \\[6pt]
        \dfrac{\dfrac{1}{k}\left(\dfrac{k}{L}\right)^N}{\dfrac{1}{L}}
        = \left(\dfrac{k}{L}\right)^{N-1} &\iff 1 \leq \ell \leq k \leq L \\[6pt]
        \dfrac{\dfrac{1}{L} \cdot 1}{\dfrac{1}{L}} = 1 &\iff k \geq L \ \land \ 1 \leq \ell \leq L
    \end{cases}
\end{align*}
$$
