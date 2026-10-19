Consideriamo problemi di soddisfacibilità Booleana o SAT. In una formula logica, *un letterale* è una varibiale Booleana oppure una sua negazione. Per una variabile $x$, indicheremo con $\bar{x}$ la sua negazione.

**DEF:** Un *problema SAT*, o *formula SAT*, è un espressione logica data dalla congiunzione (AND) di un insieme di clausole, dove ciascuna è la disgiunzione (OR) di letterali.

Una *soluzione* di un problema SAT è un'assegnazione di valori delle variabili che rende l'espressione vera. Cioè tale che in ogni clausola ci sia almeno un letterale vero.

Analizziamo ora un algoritmo aleatorio per trovare la soluzione din un sotto-problema più semplice, quello del 2-SAT, in cui ogni clausola ha solo due letterali.

L'idea per trovare una soluzione del problema 2-SAT è la seguente: si parte da una qualsiasi configurazione delle variabili. Poi, ad ogni passo, si sceglie una clausola falsa e si cambia il valore di una delle variabili in essa contenute.

## Algoritmo 2-SAT

**INPUT:** Un problema 2-SAT con $n$ variabili.
**OUTPUT:** Una soluzione del problema o fallimento.

1. Inizializzazione con una qualsiasi assegnazione delle variabili.
2. Per $2mn^2$ volte ripetere ($m \in \mathbb{N}$ da scegliere):
	1. Scegliere una qualsiasi clausola non soddisfatta;
	2. Scegliere una delle due variabili della clausola a caso ($p = \frac{1}{2}$) e cambiarne il valore.
	3. Se tutte le clausole sono soddisfatte, terminare il ciclo.
3. Se è stata trovata una soluzione, restituirla in output. Altrimenti fallimento.

*Osservazione:* $m\ \in \mathbb{N}$ è un intero che determina la probabilità di successo dell'algoritmo.

*Esempio:* Consideriamo il seguente problema 2-SAT:
$$
(x_{1} \lor \bar{x}_{2}) \land (\bar{x}_{1} \lor \bar{x}_{3}) \land (x_{1} \lor x_{2}) \land (x_{4} \lor \bar{x}_{3}) \land (x_{4} \lor \bar{x}_{1})
$$
Se cominciamo da $x_{1} = x_{2} = x_{3} = x_{4} = F$, la clausola $(x_{1} \lor x_{2})$ non è soddisfatta. L'algoritmo potrebbe allora scegliere questa clasuola e cambiare una tra $x_{1}$ e $x_{2}$. In questo caso $(x_{4} \lor \bar{x}_{1})$ diventerebbe non soddisfatta e l'algoritmo potrebbe cambiare $x_{1}$ o $x_{4}$. E cosi via...

Nel Lemma 7.1 studiamo il numero atteso di iterazioni dell'algoritmo se sappiamo a priori che esiste una soluzione. Nel Teorema 7.2 daremo l'analisi dell'algoritmo nel caso generale.

**LEMMA 7.1:** Assumiamo esista una soluzione al problema 2-SAT con $n$ variabili e che l'algoritmo sia lasciato ad eseguire finché non trova una soluzione. Allora il numero atteso di passi è al più $n^2$.

**DIMOSTRAZIONE:**
Sia $S$ una soluzione specifica del problema e chiamiamo $A_i$ l'assegnazione delle variabili all'$i$-esima iterazione dell'algoritmo.
Sia
$$
X_{i} = \text{\# variabili in }A_{i}\text{ che coincidono con quelle in }S
$$
Quando $X_{i} = n$, l'algoritmo termina avendo trovato la soluzione $S$ (l'algoritmo potrebbe anche terminare prima trovando un'altra soluzione, il che migliorerebbe la situazione).

Studiamo quanto ci mette $(X_{i})_{i \in \mathbb{N}_{0}}$ ad arrivare ad $n$.
- Se $X_{i} = 0$, allora qualsiasi cambio di variabili porta ad avere $X_{i+1} = 1 \implies P(X_{i+1} = 1 | X_{i} = 0) = 1$.
- Se $1 \leq X_{i} \leq n-1$, si ha quanto segue: ad ogni passo si sceglie una clausola falsa. Siccome $S$ è una soluzione, $A_{i}$ ed $S$ devono discordere in almeno una delle due variabili della clasuola. Perciò, $\forall j \in 1,\dots n$, $$P(X_{i+1} = j+1 | X_{i} = j) \geq \frac{1}{2}, \qquad P(X_{i+1} = j-1 | X_{i} = j) \leq \frac{1}{2}$$Nella prima probabilità vale il "$\geq$" perchè potrebbe essere 1 se $A_{i}$ ed $S$ sono in disaccordo sul valore della stessa variabile nella clausola.

*ATTENZIONE!* Il processo $X_{i}$ non è una catena di Markov poichè la probabilità che $X_{i}$ aumenti può dipendere su quali valori $A_{i}$ ed $S$ sono in disaccordo. È questo può dipendere dalle clausole considerate in passato.

Consideriamo però la catena di Markov accessoria $(Y_{i})_{i \in \mathbb{N}_{0}}$ definita nel seguente modo: $\forall j = 1, \dots, n$
$$
\begin{align}
Y_{0} &= X_{0}  \\
P(Y_{i+1} = 1 | Y_{i} = 0) &= 1 \\
P(Y_{i+1} = j+1 | Y_{i} = j) &= \frac{1}{2} \\
P(Y_{i+1} = j-1 | Y_{i} = j) &= \frac{1}{2} \\
\end{align}
$$

![[catena-2SAT.png|500]]

$(Y_{i})_{i \in \mathbb{N}}$ è una versione *pessimistica* di $(X_{i})_{i \in \mathbb{N}}$ poiché ad ogni passo ha meno probabilità di $(X_{i})$ di andare a destra. (Posso accoppiare 2 processi in modo che $Y_{i} \leq X_{i} \quad \forall i$, *dominanza stocastica*).

Quindi $(Y_{i})_{i \in \mathbb{N}}$ raggiungerà $n$ più lentamente di $(X_{i})$. Sfruttiamo quindi $(Y_{i})$ pe dare un *upper bound* del numero atteso di passi per raggiungere $n$. Sia $Z_{j}$ la v.a. 
$$
Z_{j} = \text{\# "passi che } (Y_{i})_{i\in \mathbb{N}} \text{ impiega per raggiungere } n \text{ partendo da } j \text{"}
$$
e sia $h_{j} = \mathbb{E}[Z_{j}]$. Se $(Y_{i})$ parte da $j$, al prossimo passo sarà in $j-1$ con probabilità $\frac{1}{2}$ e in $j+1$ con probabilità $\frac{1}{2}$. Quindi
$$
\begin{align}
\mathbb{E}[Z_{j}] &= \mathbb{E}\left[ \frac{1}{2} (1 + Z_{j-1}) + \frac{1}{2}(1 + Z_{j+1}) \right]  \\
&= 1 + \frac{1}{2}\mathbb{E}[Z_{j-1}] + \frac{1}{2}\mathbb{E}[Z_{j+1}] \\
&\implies h_{j} =  1 + \frac{h_{j-1}}{2} + \frac{h_{j+1}}{2} \quad \forall j=1,\dots,n-1
\end{align}
$$
Abbiamo quindi ottenuto il seguente sistema di equazioni
$$
\begin{cases}
h_{0} = 1 + h_{1} \\
h_{j} = 1 + \frac{h_{j-1}}{2} + \frac{h_{j+1}}{2} \quad \forall j=1,\dots,n-1 \\
h_{n} = 0
\end{cases}
$$
Risolvendo questo sistema, *otteremo i tempi attesi per raggiungere $n$ a partire da un qualsiasi stato $j$*.
$$
h_{j} = \frac{h_{j-1}}{2} + \frac{h_{j+1}}{2} \implies h_{j+1} = 2h_{j} - h_{j-1} - 2
$$
Riscrivendo questa relazione, otteniamo
$$
h_{j+1} - h_{j} = h_{j} - h_{j-1} - 2 \qquad (\star)
$$
Sia ora $d_{j} = h_{j} - h_{j+1}$, allora $(\star)$ diventa
$$
d_{j} = d_{j-1} - 2 \quad \text{progressione aritmentica di passo } 2
$$
Abbiamo quindi ottenuto la seguente ricorrenza
$$
\begin{cases}
d_{0} = h_{0} - h_{1} = 1 \\
d_{j} = d_{j-1} - 2
\end{cases}
\quad \text{srotolando}
$$
$$
d_{j} = (d_{j-2} +2) = [(d_{j-3} + 2) + 2] + 2 = \dots = (d_{j-i} + 2) + (i-1)2
$$
Ponendo $i = j$, otteniamo il passo base $(d_{0})$ e ci fermiamo, ottenendo
$$
\begin{align}
&d_{j} = d_{j-i} + 2i \underbrace{=}_{i=j} d_{0} + 2j = 1 + 2j  \\
&\implies d_{j} = h_{j} - h_{j+1} = 2j + 1 \\ \\
&\implies \boxed{h_{j} = h_{j+1} + 2j + 1}
\end{align}
$$
Riscrivendo il sistema di equazioni, abbiamo che
$$
\begin{cases}
h_{0} = 1 + h_{1} \\
h_{j} = h_{j+1} + 2j + 1 \\
h_{n} = 0
\end{cases}
$$
A questo punto possiamo trovare le soluzioni del sistema, srotolando la seconda equazione
$$
\begin{align}
h_{0} &= 1 + h_{1} = h_{2} + 3 + 1 = h_{3} + 5 + 3 + 1  \\
&=  \\
&\ \vdots \\
& = h_{i} + 2(i-1) + 1 + \dots + 3 + 1 \\
(i=n)& = h_{n} + (2(n-1) + 1) + \dots + 3 + 1 \\
& \implies \boxed{h_{0} = \sum_{i=0}^n (2i + 1) = n^2}
\end{align}
$$

*NOTA:* Il sistema ha come unica soluzione $h_{j} = n^2 - j^2$,
$$
\begin{align}
&\mathbb{E}[\# \text{ passi dell'algo. per trovare la sol. S}]  \\
&\leq \mathbb{E}[\# \text{ passi } (Y_{i})_{i\in \mathbb{N}} \text{ per raggiungere } n \text{ partendo da } 0] = h_{0} = n^2
\end{align}
$$

Torniamo al problema generale in cui *NON* sappiamo se esiste una soluzione e in cui eseguiamo il loop $2mn^2$ volte.

**TEOREMA 7.2:** L'algoritmo 2-SAT restituisce sempre fallimento se il problema non ha soluzioni. Se esistono soluzioni l'algoritmo ne restituisce una con probabilità maggiore di $1 - 2^{-m}$. Altrimenti restituisce fallimento erroneamente.

**DIMOSTRAZIONE:** La prima parte del teorema è ovvia. Supponiamo che esista una soluzione. Dividiamo l'esecuzione dell'algoritmo in blocchi da $2n^2$ passi ciascuno. Se non è stata trovata una soluzione durante i primi $i-1$ blocchi, qual è la probabilità di non trovarla nemmeno nell'$i$-esimo? Dal Lemma 7.1 sappiamo che il numero atteso di passi per trovare una soluzione è meno di $n^2$ indipendentemente dal punto d'inizio! Se chiamiamo
$$
\begin{align}
Z &= \# \text{"passi dall'inizio dell'}i\text{-esimo blocco} \\
&\text{prima che l'algoritmo trovi una soluzione"}
\end{align}
$$
abbiamo che 
$$
P(Z \geq 2n^2) \leq \frac{\mathbb{E}[Z]}{2n^2} = \frac{1}{2}
$$
Dunque la probabilità che l'algoritmo fallisca nel trovare una soluzione dopo $m$ blocchi è minore di $\left( \frac{1}{2} \right)^m$.