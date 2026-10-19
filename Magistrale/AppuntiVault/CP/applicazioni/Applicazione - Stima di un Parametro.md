Supponiamo di voler stimare la probabilità che un particolare gene abbia una certa mutazione in una popolazione di individui. Dato un campione di DNA, un costoso test ci dice se il gene è mutato.

**Problema:** Minimizzare il più possibile il numero di test da fare per stimare con un certo errore la probabilità di mutazione. 

Sia $p$ la probabilità *VERA* sconosciuta della mutazione, cioè il parametro che vogliamo stimare. Supponiamo di poter fare $n$ test. Dai test risulta che $X = n \cdot \tilde{p}$ dei campioni hanno la mutazione del DNA ($\tilde{p}$ è la frequenza osservata della mutazione. In generale sarà diversa da $p$). Ci aspettiamo che più $n$ è grande, più $\tilde{p}$ si avvicina a $p$.

**DEF 4.2:** Un intervallo di confidenza al livello $1 - \gamma$ per un parametro $p$ è un intervallo $[\tilde{p} - \delta, \tilde{p} + \delta]$ tale che
$$P(p \in [\tilde{p} - \delta, \tilde{p} + \delta]) \geq 1 - \gamma$$
Non stiamo cercando di prendere l'esatto valore di $p$, ci basta un intervallo in cui $p$ cada con grande probabilità.

Più precisamente, il problema è:

**Problema:** Vogliamo in contemporanea $2\delta$ (ampiezza dell'intervallo), $\gamma$ (probabilità di errore) ed $n$ (numero di campioni) più piccoli possibili. Chiaramente, più $n$ è piccolo e più $\delta$ o $(\gamma)$ cresce.

Dato $n$, vogliamo trovare $\delta$ e $\gamma$ tali che, se abbiamo osservato $X = n\tilde{p}$ mutazioni,
$$P(p \in [\tilde{p} - \delta, \tilde{p} + \delta]) = P(np \in [n(\tilde{p} - \delta), n(\tilde{p} + \delta])) \geq 1 - \gamma$$
La v.a. $X = n\tilde{p} \sim Bin(n, p)$, quindi $\mathbb{E}[X] = np$. Notiamo che se $p \notin [\tilde{p} - \delta, \tilde{p} + \delta]$ deve succedere uno dei seguenti casi:
1. Se $p < \tilde{p} - \delta$, allora $X = n \tilde{p} > n(p + \delta) = \mathbb{E}[X]\left( 1 + \frac{\delta}{p} \right)$
2. Se $p > \tilde{p} + \delta$, allora $X = n \tilde{p} < n(p - \delta) = \mathbb{E}[X]\left( 1 - \frac{\delta}{p} \right)$
Applicando Chernoff Bound (*Teorema 4.4 e 4.5 punto 2*), otteniamo
$$
\begin{align}
P(p \notin [\tilde{p} - \delta, \tilde{p} + \delta]) &= P\left( X < np\left( 1 - \frac{\delta}{p} \right) \right) + P\left( X > np\left( 1 + \frac{\delta}{p} \right) \right) \\
&= P\left( X < \mathbb{E}[X]\left( 1 - \frac{\delta}{p} \right) \right) + P\left( X > \mathbb{E}[X]\left( 1 + \frac{\delta}{p} \right) \right)  \\
&\leq \exp\left( -\frac{np}{2}\left( \frac{\delta}{p} \right)^2 \right) + \exp\left( -\frac{np}{3}\left( \frac{\delta}{p} \right)^2 \right) \\
&= \exp\left( -\frac{n\delta^2}{2p} \right) + \exp\left( -\frac{n\delta^2}{3p} \right)
\end{align}
$$
Il problema di questo bound è che dipende da $p$ che **NON** conosciamo. Sapendo però che $p \leq 1$, troviamo che
$$
P(p \notin [\tilde{p} - \delta, \tilde{p} + \delta]) \leq \exp\left( -\frac{n\delta^2}{2} \right) + \exp\left( -\frac{n\delta^2}{3} \right) \leq 2\exp\left( -\frac{n\delta^2}{3} \right)
$$
In conclusione, impostanto $\gamma = \exp\left( -\frac{n\delta^2}{2} \right) + \exp\left( -\frac{n\delta^2}{3} \right)$, abbiamo trovato una relazione tra $\delta, n$ e $\gamma$.


Avendo dimostrato che
$$
P(\text{errore}) \leq 2\exp\left( -\frac{n\delta^2}{3} \right)
$$
conviene imporre che anche quest'ultima sia $\leq \gamma$.
$$2\exp\left(-\frac{n\delta^2}{3}\right) \le \gamma$$
Se questa condizione vale, per transitività si ha $P(\text{errore}) \leq \gamma$, che è quello che vogliamo. Possiamo quindi usare questa disuguaglianza per trovare $n$:
$$
\begin{align}
2\exp\left( -\frac{n\delta^2}{3} \right) \leq \gamma &\iff \exp\left( -\frac{n\delta^2}{3} \right) \leq \frac{\gamma}{2} \\
&\iff -\frac{n\delta^2}{3} \leq \ln\left( \frac{\gamma}{2} \right) \\
&\iff n\delta^2 \geq -3 \ln\left( \frac{\gamma}{2} \right) = 3\ln\left( \frac{2}{\gamma} \right) \\
&\iff \boxed{n \geq \frac{3}{\delta^2} \ln\left( \frac{2}{\gamma} \right)}
\end{align}
$$
