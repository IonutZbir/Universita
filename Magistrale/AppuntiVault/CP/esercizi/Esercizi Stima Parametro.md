# Esercizio 2 (22.06.2026)

Andrea acquista da un baro a Porta Portese un dado truccato. Il dado mostra le facce da 2 a 6 con uguale probabilità, ma la faccia 1 con probabilità maggiore di $\frac{1}{6}$. Andrea vuole stimare qual è la probabilità che il dado mostri un 1. Quante volte dovrà lanciare il dado in modo da essere sicuro al 95\% di aver trovato la probabilità che il dado mostri un 1 a meno di un possibile errore di 0.02?

## Soluzione - Applicazione Stima Parametro

Sia $\tilde{p} = P(\text{ esce 1 })$ la probabilità *VERA* da stimare. Sia $n$ il numero di lanci. Definiamo l'intervallo di confidenza $[\tilde{p} - \delta, \tilde{p} + \delta]$ dove $\delta = 0.02 = \frac{2}{100}$. Vogliamo calcolare
$$
\begin{align}
P(p \in [\tilde{p} - \delta, \tilde{p} + \delta]) &\geq 1 - \gamma  \\ \\
\iff \\ \\
P\left( p \in \left[ \tilde{p} - \frac{2}{100}, \tilde{p} + \frac{2}{100} \right] \right) &\geq 1 - \frac{5}{100} 
\end{align}
$$
Sia $X = n \tilde{p}$ il numero di volte che è uscito 1 (allora $\tilde{p} = \frac{1}{n}X$ che è lo stimatore MLE di una binomiale, e si procede con la stima per intervallo classica oppure applicando Chebychev).

Imponendo $\gamma = \exp\left( -\frac{n\delta^2}{2} \right) + \exp\left( -\frac{n\delta^2}{3} \right) \leq 2\exp\left( \frac{-n\delta^2}{3} \right) \leq 0.05 = \gamma$
$$
\boxed{2\exp\left( \frac{-n\delta^2}{3} \right) \leq \gamma}
$$
A questo punto, dobbiamo esplicitare $n$ dalla seguente formula, e otteniamo
$$
\begin{align}
n &\geq \frac{3}{\delta^2}\ln\left( \frac{2}{\gamma} \right) \iff \\
&\text{Sostituendo } \delta = 0.02,\ \gamma = 0.05\\
n &\geq 7500\ln(40) \approx 28000
\end{align}
$$
