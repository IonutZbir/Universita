Una *coda* va pensata come una coda di clienti che aspettano un qualche servizio. Esaminiamo un semplice modello di coda limitata a tempo discreto. Ad ogni passo, solo una delle seguenti azioni avviene:
- Se la coda ha meno di $n$ persone, arriva un nuovo cliente che si accoda con probabilità $\lambda$.
- Se la coda è *NON*-vuota, con probabilità $\mu$ il primo cliente della coda viene servito e se ne va.
- Col resto della probabilità non succede niente.

Se chiamiamo
$$
X_{t} = \# \text{ numero di clienti al tempo } t 
$$
ci accorgiamo che il processo stocastico $(X_{t})_{t\in \mathbb{N}}$ è una catena di Markov su $V = \{1, 2, \dots, n\}$. $\lambda$ e $\mu$ sono reali in $(0,1)$ con $\lambda + \mu < 1$. La catena di Markov ha come matrice di transizione $P$ tale che
$$
\begin{align}
&P_{j, j+1} = \lambda \iff j < n \\
&P_{j, j-1} = \mu \iff j > 0 \\
&P_{j,j} =  \begin{cases}
1 - \lambda &\iff j = 0 \\
1 - \lambda - \mu &\iff 1 \leq j \leq n-1 \\
1 - \mu &\iff j = n
\end{cases}
\end{align}
$$

![[teoria_delle_code|700]]

La catena è finita (cioè $|V| < \infty$), irriducibile ed aperiodica, ed ha perciò un'unica distribuzione stazionaria $\bar{\pi}$. Poiché $\bar{\pi} = \bar{\pi}P$, si ottiene il sistema di equazioni
$$
\begin{cases}
\pi_{0} = (1-\lambda)\pi_{0} + \mu \pi_{1}  \\
\pi_{i} = \lambda \pi_{i-1} + (1 - \lambda - \mu)\pi_{i} + \mu \pi_{i+1} \quad 1 \leq i \leq n-1 \\
\pi_{n} = \lambda \pi_{n-1} + (1-\mu)\pi_{n}
\end{cases}
$$
Si può verificare che $\pi_{i} = \pi_{0}\left( \frac{\lambda}{\mu} \right)^i$ è soluzione del sistema. Aggiungendo la condizione $\sum_{i=1}^{n} \pi_{i} = 1$ si ottiene
$$
\begin{align}
\sum_{i=0}^n \pi_{i} = \sum_{i=0}^n \pi_{0}\left( \frac{\lambda}{\mu} \right)^i = 1 \\ \\
\implies \pi_{0} = \frac{1}{\sum_{i=0}^n\left( \frac{\lambda}{\mu} \right)^i}  \\ \\
\pi_{i} = \frac{\left( \frac{\lambda}{\mu} \right)^i}{\sum_{i=0}^n \left( \frac{\lambda}{\mu} \right)^i}
\end{align}
$$

### Caso $V$ Infinito

Consideriamo il caso in cui $n = \infty$, ossia il caso in cui la coda può essere arbitrariamente lunga. $(X_{t})_{t \in \mathbb{N}_{0}}$ diventa una catena di Markov con $V = \mathbb{N}_{0}$ e le stesse probabilità di transizione di prima. In questo caso l'esistenza di una distribuzione stazionaria *NON* è garantita! Applichiamo il Teorema 7.11, la catena di Markov ha una distribuzione stazionaria se e solo se il sistema seguente di equazioni lineari ha una soluzione con tutti i $\pi_{i} > 0$:

$$
\begin{cases}
\pi_{0} = (1-\lambda)\pi_{0} + \mu \pi_{1} \\
\pi_{i} = \lambda \pi_{i-1} + (1-\lambda-\mu)\pi_{i} + \mu \pi_{i+1} \quad \forall i \geq 1
\end{cases}
$$

Si può nuovamente verificare che
$$
\pi_{i} = \frac{\left( \frac{\lambda}{\mu} \right)^i}{\sum_{i=1}^n \left( \frac{\lambda}{\mu} \right)^i} > \left( \frac{\lambda}{\mu} \right)^i\left( 1 - \frac{\lambda}{\mu} \right) \iff \lambda < \mu
$$
è una soluzione del sistema. Notiamo che il denominatore è finito se e solo se $\lambda < \mu$. Perciò:
- **CASO $\lambda < \mu$:** si ha che $\forall i \in V$ $$\pi_{i} = \left( \frac{\lambda}{\mu} \right)^i \left( 1 - \frac{\lambda}{\mu} \right) > 0$$ è l'unica distribuzione stazionaria della catena (parte 1 del Teorema 7.11). Questo è il caso in cui i clienti vengono processati più velocemente di quanto ne arrivino di nuovi. (Osserviamo che $\pi_{i}$ è la probabilità che una $Geom\left( 1-\frac{\lambda}{\mu} \right)$ sia uguale a $i+1$).
- **CASO $\lambda > \mu:$** Non c'è una distribuzione stazionaria (parte 2 del Teorema 7.11). I clienti arrivano più rapidamente di quanto vengano processati e la fila diventerà sempre più lunga: tutti gli stati sono transienti.
- **CASO $\lambda = \mu$:** Anche in questo caso *NON* c'è distribuzione stazionaria, la coda diventerà sempre più lunga ma gli stati (si può provare che) sono tutti ricorrenti nulli.

*Osservazione:* Quando esiste la distribuzione stazionaria (a $V$ finito o infinito) si può verificare che $\bar{\pi}$ è una misura reversibile.