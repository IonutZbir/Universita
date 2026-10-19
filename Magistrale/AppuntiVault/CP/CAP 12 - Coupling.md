Abbiamo visto sotto quali condizioni una catena di Markov converge alla sua misura stazionaria, ma...
**Domanda:** Quanto velocemente?

# 12.1 Distanza in Variazione e Mixing Time

**DEF 12.1:** La *distanza in variazione totale* tra due distribuzioni $\mu$ e $\nu$ su uno spazio degli stati misurabile $S$ è data da
$$
\lvert| \mu - \nu |\rvert_{TV} = \frac{1}{2}\sum_{x \in S} \lvert \mu(x) - \nu(x) \rvert  
$$
*Esempio:* Consideriamo il seguente modo di mischiare un mazzo di $n$ carte: ad ogni passo prendiamo una carta a caso e la mettiamo in cima.
Pensiamola come una catena di Markov:
- Gli stati $S$ sono le possibili configurazioni del mazzo (i.e. permutazioni di $N$ oggetti), $\boxed{|S| = n!}$
- $(X_{n})$ è irriducibile ed aperiodica
- La distribuzione stazionaria è la misura uniforme $\boxed{\pi_{i} = \frac{1}{n!}}$
Se potessimo mischiare all'*infinito*, il mazzo diventerebbe perfettamente mischiato (i.e., ogni permutazione avrebbe probabilità $\frac{1}{n!}$).
Quanto devo mischiare per avere
$$
\lvert | \text{distribuzione}(X_{t}) - \pi | \rvert_{TV} < \epsilon \qquad \text{?} 
$$
Questo implica ad esempio che ogni permutazione delle carte avrebbe probabilità $\leq \frac{1}{n!} + \epsilon$ e $\frac{1}{n!} - \epsilon$.

*Osservazione:*
- L'$\frac{1}{2}$ della definizione fa sì che $\lvert |\mu - \nu| \rvert_{TV} \in [0,1]$. $$\lvert | \mu -\nu | \rvert_{TV} = \frac{1}{2} \sum_{i} \lvert \mu(i) - \nu(i) \rvert \leq \frac{1}{2} \sum_{i} |\mu(i)| + \sum_{i}|\nu(i)| = 1 $$
- $|\cdot|_{TV}$ è una era e propria distanza tra misure di probabilità
	- $\lvert |\mu - \nu| \rvert_{TV} \geq 0$ ed è $= 0 \iff \mu = \nu$
	- $\lvert |\mu - \nu| \rvert_{TV} = \lvert |\nu - \mu| \rvert_{TV}$
	- $\lvert |\mu - \nu| \rvert_{TV} \leq \lvert |\mu -\eta| \rvert_{TV} + |\eta -\nu| \rvert_{TV}\ \forall \mu, \nu, \eta$

**LEMMA 12.1:**
Per ogni $A \subseteq S$, sia $\mu(A) = \sum_{i \in A} \mu(i)$. Allora vale la formula alternativa
$$
\lvert |\mu - \nu| \rvert_{TV} = \max_{A \subseteq S}\ \lvert \mu(A) - \nu(A) \rvert  
$$
**DIMOSTRAZIONE:** Omessa.

*Osservazione:* Per la dimostrazione si vede che
$$
\lvert |\mu - \nu| \rvert_{TV} = \mu(S^+) - \nu(S^+)
$$
dove
$$
S^+ = \{ x \in S: \mu(x) \geq \nu(x) \}
$$

*Esempio:* Esempio del mazzo: se $\lvert |\text{dist.}(X_{t}) - \pi| \rvert \leq \epsilon$, non solo ogni permutazione ha probabilità $\frac{1}{n!} + \epsilon$, ma anche ogni possibile evento!
Ad esempio
 $$
 A = \text{ C'è un asso in cima al mazzo}
 $$
 ha probabilità $\leq \pi(A) + \epsilon$.
 Se invece $\mu$ fosse la distribuzione del mazzo (52 carte) lasciando $A$ in cima e mischiando perfettamente il resto del mazzo, si avrebbe
 $$
 \begin{align}
 \lvert |\mu - \pi| \rvert_{TV} &= \max_{A \subseteq S} \lvert \mu(A) - \pi(A) \rvert   \\
 B=\text{ A in cima } &\geq \lvert \mu(B) - \pi(B) \rvert   \\
 &= 1 - \frac{1}{52} = \frac{51}{52}
 \end{align}
 $$

**DEF 12.2:** Sia $\pi$ la distribuzione stazionaria di una catena di Markov ergodica su $S$. Sia $P^t_{x}$ la distribuzione della catena dopo $t$ passi. Definiamo
$$
\Delta_{x}(t) = \lvert |P_{x}^t - \pi | \rvert_{TV} \quad e \quad \Delta(t) = \max_{x \in S} \Delta_{x}(t) 
$$
Inoltre siano
$$
\tau_{x}(\epsilon) = \min \{ t: \Delta_{x}(t) \leq \epsilon \} \quad e \quad \tau_{mix}(\epsilon) = \max_{x \in S} \tau_{x}(\epsilon)
$$
$\tau_{mix}$, visto come funzione di $\epsilon$, è detto *mixing time* (tempo di mescolamento) della catena.

Una catena è detta *rapidly mixing* se $\tau_{mix}(\epsilon)$ è polinomiale in $\log\left( \frac{1}{\epsilon} \right)$ e in $|S|$.

# 12.2 Coupling

**Domanda:** Come limitare il $\tau_{mix}$?

**DEF 12.3:** Sia $(M_{t})_{t \in \mathbb{N}_{0}}$ una catena di Markov con matrice di transizione $P$ su $S$. Un coupling di $(M_{t})$ è una catena di Markov $Z_{t} = (X_{t}, Y_{t})$ su $S \times S$ tale che
$$
\begin{align}
P(X_{t+1} = x' | Z_{t} = (x,y)) &= P_{x x'} \\
P(Y_{t+1} = y' | Z_{t} = (x,y)) &= P_{y y'}
\end{align}
$$

Cioè, un coupling di $(M_{t})$ consiste in due *copie* $X_{t}, Y_{t}$ di $M_{t}$ che si muovono contemporaneamente. $X_{t}$ ed $Y_{t}$ possono essere indipendenti o dipendenti tra loro, basta che marginalmente abbiano lo stesso comportamento di $M_{t}$.
Noi cercheremo dei coupling che:
- Facciano incontrare $(X_{t})$ e $(Y_{t})$ il prima possibile.
- *Incolliamo* $X_{t}$ e $Y_{t}$ da quando si sono incontrate.

**LEMMA 12.2 (Coupling Lemma):**
Sia $Z_{t} = (X_{t}, Y_{t})$ un coupling di una catena di Markov $(M_{t})$ su $S$. Se esiste un tempo $T$ tale che $\forall\ x,y \in S$
$$
P(X_{t} \neq Y_{t} | X_{0} = x, Y_{0} = y) \leq \epsilon
$$
allora
$$\tau_{mix}(\epsilon) \leq T$$
**DIMOSTRAZIONE:**
Consideriamo il coupling con 
$$
\begin{align}
&Y_{0} \sim \pi \quad \text{ (distribuzione stazionaria)} \\
&X_{0} = x \quad (x \text{ arbitrario})
\end{align}
$$

Definiamo
$$
\begin{align}
P(Y_{t} \in A) &= \sum_{i \in A} \pi_{i} = \pi(A) \\
P(X_{t} \in A) &= \sum_{i \in A} P_{X}^t(i) = P_{X}^t(A)  \\
P(Y_{t} \not\in A) &= 1 - P(Y_{t} \in A) = 1 - \pi(A)
\end{align}
$$

Allora, $\forall A \subseteq S$
$$
\begin{align}
P(X_{t} \in A) &\geq P(\{ X_{t} = Y_{t} \} \cap \{ Y_{t} \in A \}) \\
&= 1 - P(\{ X_{t} \neq Y_{y} \} \cup \{ Y_{t} \not\in A \} \\
&\geq 1 - \underbrace{P(X_{t} \neq Y_{t})}_{\leq \epsilon \text{ per ipotesi: vale } \forall x,y} - \underbrace{P(Y_{t} \not\in A)}_{= \pi(A)} = 1 - \epsilon - 1 + \pi(A) \\
&\geq \pi(A) - \epsilon
\end{align}
$$
In maniera del tutto analoga si può mostrare che
$$
P(X_{t} \not\in A) = P(X_{t} \in S \setminus A) \geq \pi(S \setminus A) - \epsilon \quad \text{risultato precedente}
$$
il che implica che
$$
P(X_{t} \in A) = 1 - P(X_{t} \not\in A) \leq 1 - \pi(S \setminus A) + \epsilon = \pi(A) + \epsilon
$$
Abbiamo perciò mostrato che
$$
\max_{x \in S, A \subseteq S} \lvert P^T_{x} - \pi(A) \rvert \leq \epsilon 
$$
e quindi per il Lemma 12.1
$$
\lvert P_{x}^T(\cdot) - \pi \rvert_{TV} \leq \epsilon 
$$
e quindi $\tau_{mix}(\epsilon) \leq T$.

*Esempio:* Torniamo al mescolamento delle carte. Una possibilità di coupling è: scelgo la $j$-esima carta da entrambi i mazzi e la porto in cima. Ma è un coupling intuile! Se i due mazzi partono da configurazioni differenti, non si incotreranno mai.
Se prendiamo le carte indipendentemente a caso dai due mazzi, prima o poi la configurazione sarà la stessa, ma ci vuole tantissimo tempo!

Considerimo invece il seguente coupling:
Scegliamo dal mazzo $X_{t}$ una carta a  caso, sia $C$, e la portiamo in cima ottenendo $X_{t+1}$. Da $Y_{t}$ prendiamo la stessa carta $C$ e la portiamo in cima.

*Osservazione:*  Il coupling è valido: in entrambe le catene la probabilità che ogni carta sia spostata in cima è uguale a $\frac{1}{n}$.

 Quanti passi ci vogliono affinché $X_t = Y_{t}$? Ad esempio $X_{t} = Y_{T}$ se ogni carta differente è stata scelta almeno una volta: *è un problema del collezionatore di figurine!*
$$
\begin{align}
P(X_{t} \neq Y_{t} | X_{0} = x, Y_{0} = y) &\leq P(\exists \text{ una carta NON pescata in T passi}) \\
\text{Union Bound}&\leq n P(\text{carta C non pescata in T passi}) \\
= n\left( 1 -\frac{1}{n} \right)^T
\end{align}
$$
Prendendo $T = n \log\left( \frac{n}{\epsilon} \right)$ si ha che la probabilità è
$$
\leq n\left( 1 - \frac{1}{n} \right)^{n \log n + n\log 1/\epsilon} \leq n \exp\left( -\log n - \log \frac{1}{\epsilon} \right) = \epsilon
$$
Perciò
$$
\tau_{mix}(\epsilon) \leq n \log\left( \frac{n}{\epsilon} \right)
$$

*Esempio (Ipercubo)*
Consideriamo la passeggiata aleatoria sull'ipercubo
$$
\mathcal{H}_{d} = \{0,1\}^d \qquad \text{con } 2^d \text{ nodi}
$$
Per $x,y \in \mathcal{H}_{d}$, esiste l'arco $(x,y) \in E \iff x$ ed $y$ differiscono per un solo bit.
Consideriamo il RW sul grafo risultante. La RW può essere definita cosi:
$X_{t+1}$ è realizzato da $X_t$ scegliendo una coordinata a caso e rimpiazzandola con una $Ber\left( \frac{1}{2} \right)$, quindi
$$P_{ij} = P(\text{scelgo coordinata a caso}) \cdot P(\text{scelgo se stare fermo}) = \frac{1}{d} \cdot \frac{1}{2}$$
*NOTA:* Questa è la versione *lazy* con la catena che rimane ferma con probabilità $1/2$ evitando problemi di periodicità.

**Couplig:** Consideriamo due copie della catena $X_{t}$ e $Y_{t}$, che partono da due *stati iniziali arbitrari* $X_{0} = x$ e $Y_{0} = y$. Ad ogni passo $t$:
- Si estrae lo *stesso indice $i \in [1, d]$ per entrambe le catene*.
- Si estra lo *stessa nuovo bit $b \in \{0,1\}$* e lo si assegna alla coordinata $i$ di entrmbe le catene:
$$
X_{t}(i) = b \qquad Y_{t}(i) = b
$$
Non appena una coordinata $i$ viene estratta almeno una volta, da quel momento in poi $X_{t}(i) = Y_{t}(i)$. Le due stringhe diventano identiche $(X_{t} = Y_{t})$ *non appena tutte le $d$ coordinate sono state selezionate almeno una volta*, **Coupons'Collector Problem!**
$$
\begin{align}
&P(X_{t} \neq Y_{t} | X_{0} = x, Y_{0} = y)  \\
&\leq P(\text{Esiste indice i ancora non scelto in T passi}) \\
&\leq nP(\text{Indice i ancora non scelto in T passi}) \\
&= n\left( 1 - \frac{1}{n} \right)^T \leq n e^{-T/n}
\end{align}
$$
A questo punto,
$$
\begin{align}
ne^{-T/n} \leq \epsilon &\iff e^{-T/n} \leq \frac{\epsilon}{n} \\
&\iff -\frac{T}{n} \leq \ln(\frac{\epsilon}{n}) \\
&\iff T \geq n \ln (\frac{n}{\epsilon})
\end{align}
$$
Avendo dimostrato che per $T = n \ln (\frac{n}{\epsilon})$ vale 
$$
P(X_{t} \neq Y_{t} | X_{0} = x, Y_{0} = y) \leq \epsilon
$$
per qualsiasi coppia di stati iniziali, per il *Coupling Lemma* segue che
$$
\tau(\epsilon) \leq n \ln (\frac{n}{\epsilon})
$$
