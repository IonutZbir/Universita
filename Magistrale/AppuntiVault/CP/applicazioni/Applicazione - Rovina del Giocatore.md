
Abbiamo due giocatori: il giocatore 1 con capitale $l_1 \in \mathbb{N}$ e il giocatore 2 con capitale $l_{2} \in \mathbb{N}$. Si lancia una moneta ad ogni turno, con probabilità di testa $p \in (0,1)$. Se esce *testa* il giocatore 1 guadagna un'unità di capitale del giocatore 2, se esce *croce* il contrario. Il gioco termina quando uno dei due esaurisce il suo capitale iniziale, perdendo.

**Goal:** Calcolare la probabilità $q = q(l_1, l_2, p)$ che il giocatore 1 vinca il gioco. 

Sia $V = \{ j \in \mathbb{Z}: -l_{1} \leq j \leq l_{2} \}$ l'insieme dei valori del capitale guadagnato dal giocatore 1 durante il gioco.

Sia $(W_{t})_{t\in \mathbb{N}_{0}}$ la catena di Markov su $V$ tale che:
- $W_{0} = 0$
- $P(W_{t+1} = i+1 | W_{t} = i ) = p$
- $P(W_{t+1} = i-1 | W_{t} = i) = 1-p$
Per ogni $i \in V$, $i \neq l_{1}, l_{2}$
- $P(W_{t+1} = i| W_{t} = i) = 1$ per $i = -l_{1}$ oppure $i = l_{2}$. In questo caso il gioco finisce.

La corrispondente matrice di transizione è:
$$
P=
\begin{pmatrix}
1 & 0 & 0 & 0 & \cdots & 0 & 0\\
1-p & 0 & p & 0 & \cdots & 0 & 0\\
0 & 1-p & 0 & p & \cdots & 0 & 0\\
0 & 0 & 1-p & 0 & p & & 0\\
\vdots & & & \ddots & \ddots & \ddots & \vdots\\
0 & 0 & 0 & \cdots & 1-p & 0 & p\\
0 & 0 & 0 & \cdots & 0 & 0 & 1
\end{pmatrix}$$
aventi $l_{1} + l_{2} + 1$ righe e colonne.

![[gambler_ruin.png|500]]


### Classificazione degli stati

*Osservazione:*
- Gli stati $-l_{1}$ ed $l_{2}$ sono *ricorrenti* (anzi, visto che la catena se vi arriva vi rimane, sono detti *assorbenti*)
- Gli stati $i \neq l_{1}, l_{2}$ sono *transienti* (se la catena viene assorbita agli estremi *NON* ci torna più indietro)

Intuitivamente $(W_{t})$ prima o poi verrà assorbita in $-l_1$ o $l_{2}$ (la probabilità che il gioco vada avanti all'infinito è 0).

*Osservazione:* La catena *NON* è irriducibile in quando abbiamo individuato *tre* classi di equivalenza:
- $\{-l_{1}\}$ e $\{ l_{2} \}$ sono due classi chiuse.
- $\{ i:\ i \neq -l_{1},l_{2}\}$ è una classe di equivalenza di stati transienti.
Inoltre gli stati $-l_{1}$ e $l_{2}$ sono assorbenti, di conseguenza una volta arrivati lì, non sarà possibile raggiungere gli altri stati.

*Osservazione:* Poiché la catena non è irriducibile, non si identifica un singolo periodo globale, ma dobbiamo analizzare ciascuna classe in parte:
- Gli stati assorbenti $\{ -l_{1} \}$ e $\{ l_{2} \}$ sono aperiodici in quanto c'è un self loop.
- Gli stati transienti $\{ i:\ i \neq -l_{1},l_{2} \}$ sono periodici di periodo 2.

### Misure invarianti

In una catena di Markov con stati assorbenti, la probabilità stazionaria per tutti gli stati transienti è zero. Tutta la *massa* di probabilità a lungo termine si concentra negli stati assorbenti.
Pertanto, le uniche misure invarianti della catena sono le combinazioni lineari convesse delle probabilità concentrate negli stati $-l_{1}, l_{2}$. L'insieme di tutte le misure invarianti è descritto dal vettore
$$
\bar{\pi} = \alpha(1, 0, 0 \dots, 0) + (1-\alpha)(0, 0, 0, \dots, 1) = (\alpha, 0, \dots, 0, 1-\alpha)  
$$

### Probabilità vittoria giocatore 1.

Quindi per quel valore $q$ che cerchiamo, si ha
$$
\lim_{ t \to \infty } P(W_{t} = j) =
\begin{cases}
q &\iff j = l_{2} \\
1-q &\iff j = -l_{1} \\
0 &\iff j \neq -l_{1},l_{2}
\end{cases}
$$

## Caso $p = \frac{1}{2}$

##### Approccio Intuitivo
Se $p = \frac{1}{2}$ il gioco è equo e quindi (intuitivamente) $\mathbb{E}[W_{t}] = 0\ \forall t \geq 0$. Allora,
$$
\begin{align}
0 &= \lim_{ t \to \infty } \mathbb{E}[W_{t}] = \lim_{ t \to \infty } \sum_{{j = -l_{1}}}^{l_{2}} j P(W_{t} = j) = \sum_{{j = -l_{1}}}^{l_{2}} j \lim_{ t \to \infty } P(W_{t} = j)  \\
&= ql_{2} + (-l_{1})(1-q) \implies \boxed{q = \frac{l_{1}}{l_{1} + l_{2}}}
\end{align}
$$

##### Approccio Sistema Lineare
Un altro approccio è il seguente: Sia 
$$
q_{i} = P(W_{t} \text{ venga assorbita in } l_2 \text{ partendo da } i)
$$
A noi interessa quindi $q = q_{-l_{1}}$. 

Per la proprietà di Markov, si ha
$$\boxed{q_{i} = \frac{1}{2} q_{i+1} + \frac{1}{2}q_{i-1}},\quad \forall i \neq l_{1},l_{2}$$
Chiaramente $q_{l_{2}} =1$ e $q_{-l_{1}} = 0$.
Abbiamo quindi ottenuto il seguente sistema di equazioni:
$$
\begin{cases}
q_{-l_{1}} = 0 \\
q_{i} = \frac{1}{2} q_{i+1} + \frac{1}{2}q_{i-1},\quad \forall i \neq l_{1},l_{2} \\
q_{l_{2}} = 1
\end{cases}
$$
Risolviamo ora questo sistema.
$$
2q_{i} = q_{i+1} + q_{i-1} \implies q_{i+1} - q_{i} = q_{i}-q_{i-1}
$$
Per risolvere ora il sistema consideriamo gli indici da $i = 0=-l_{1}, \dots, N=l_{2}$
Questa uguaglianza ci dice praticamente che lo scarto tra le probabilità di due stati consecutivi è una **costante**, sia essa $d$. Partendo dalle condizioni inziali, abbiamo che
$$
\begin{align}
&q_{1} - q_{0} = d \implies q_{1} = d \\
&q_{2} - q_{1} = d \implies q_{2} = 2d \\
&q_{3} - q_{2} = d \implies q_{3} = 3d \\
\end{align}
$$
Generalizzando, otteniamo l'equazione lineare
$$
\begin{align}
q_{i} = i \cdot d
\end{align}
$$
Sapendo che $q_{N} = q_{l_{2}} = 1$, troviamo 
$$
q_{N} = N \cdot d \implies d = \frac{q_{N}}{N} = \frac{1}{N}
$$
A questo punto, sostitendo $d$ nell'equazione generale, troviamo che
$$
q_{i} = \frac{i}{N}
$$

Ritornando alla nomenclatura precendente degli indici, abbiamo che
$$\boxed{q_{i} = \frac{l_{1} + i}{l_{1} + l_{2}}\quad \forall i \in V}$$
Quindi, $q = q_{0} = \frac{l_{1}}{l_{1} + l_{2}}$.

## Caso $p$ Generico

Sia $\alpha = \alpha(p) = \frac{1-p}{p}$, osserviamo che $\alpha > 0$ e $\alpha \neq 1$ ($\alpha = 1 \iff p = \frac{1}{2}$). Si ha che $\mathbb{E}[\alpha^{W_{t+1}}] = \mathbb{E}[\alpha^{W_{t}}],\ \forall t \in \mathbb{N}_{0}$. Infatti, questo si può dimostrare applicando il *teorema torre* nel seguente modo:
$$
\begin{align}
\mathbb{E}[\alpha^{W_{t+1}}] &= \mathbb{E}[\mathbb{E}[\alpha^{W_{t+1}} \mid W_{t}]] = \mathbb{E}[\alpha^{W_{t+1}}p + \alpha^{W_{t-1}}(1-p)] \\ \\
&= \mathbb{E}\left[\alpha^{W_{t}}\left(\alpha p + \frac{1}{\alpha}(1-p)\right)\right] = \mathbb{E}[\alpha^{W_{t}}]
\end{align}
$$
dove $\left(\alpha p + \frac{1}{\alpha}(1-p)\right) = 1$ se sostituiamo $\alpha = \frac{1-p}{p}$.
Quindi, $\forall t \in \mathbb{N}_{0}$,
$$
\mathbb{E}[\alpha^{W_{t}}] = \mathbb{E}[\alpha^{W_{t-1}}] = \dots = \mathbb{E}[\alpha^{W_{1}}] = \mathbb{E}[\alpha^{W_{0}}] = 1
$$
Allora, 
$$
\begin{align}
1 &= \lim_{ t \to \infty } \mathbb{E}[\alpha^{W_{t}}] = \lim_{ t \to \infty } \sum_{j = -l_{1}}^{l_{2}} \alpha^j P(W_{t} = j)  \\
&= \sum_{j = -l_{1}}^{l_{2}} \alpha^j \lim_{ t \to \infty } P(W_{t} = j) = \alpha^{l_{2}}q + \alpha^{-l_{1}}(1-q)
\end{align}
$$
A questo punto otteniamo che
$$
q = \frac{1 - \alpha^{-l_{1}}}{\alpha^{l_{2}} - \alpha^{l_{1}}} = \frac{\alpha^{l_{1}} - 1}{\alpha^{l_{1}} + l_{2}} - 1 
$$

Un altro approccio è il seguente: