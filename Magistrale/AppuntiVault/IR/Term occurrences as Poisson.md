Abbiamo visto come poter modellare il numero di occorrenze di un termine in un documento con una [[Introducing term frequency in BIM#^2ee5f6|binomiale]].
Per valori di $L$ grandi, possiamo approssiamare questa binomiale come una [[Distribuzioni#Poisson|poisson]] di parametro $\lambda = L\tilde{p}_t$
$$\text{Binom}(L, \tilde{p}) \approx \text{Poisson}(\lambda = L\tilde{p}) \implies P(d_i = k) \approx e^{-L\tilde{p_i}}\frac{(L\tilde{p}_i)^k}{k!}$$

Sorge ora il problema:
> come poter stimare il parametro $\lambda = L \tilde{p}_t$?

Una prima idea sarebbe:$$\lambda_{j} \approx \frac{cf_{j}}{N}$$
cioè il numero atteso di occorenze del termine $j$ in un documento è dato approssimativamente dal numero totale di occorrenze del termine $j$ nella collezione ($cf_j$) diviso il numero totale di documenti ($N$). 
Ci rendiamo però conto che non ci basta un unico parametro $\lambda$, poiché un termine si comporta diversamente in base al fatto che appartenga o meno a documenti rilevanti o alla collezione in generale.

Per questo motivo si introduce un modello di Poisson con due parametri:
- $\rho_{j}$: frequenza attesa del termine $t_{j}$ nei documenti rilevanti;
- $\gamma_j$: frequenza attesa del termine $t_j$ nell'intera collezione.

Usando questo modello otteniamo che:

$$
\begin{align*}
P(d_i = n_i \vert R,q) &\sim \text{Poisson}(\rho_i)(n_i) = \frac{e^{-\rho_i}\rho_i^{n_i}}{n_i !} \\
P(d_i = n_i) &\sim \text{Poisson}(\gamma_i)(n_i) = \frac{e^{-\gamma_i}\gamma_i^{n_i}}{n_i !} \\
P(d_i = 0 \vert R,q) &\sim \text{Poisson}(\rho_i)(0) = e^{-\rho_i} \\
P(d_i = 0) &\sim \text{Poisson}(\gamma_i)(0) = e^{-\gamma_i}
\end{align*}
$$

Come sonseguenza avremo che
$$\begin{align*}
RSV_d
&= \sum_{t \in q}\log{\frac{P(d_t = n_t \vert R,q) P(d_t = 0)}{P(d_t = n_t)P(d_t = 0 \vert R, q)}}\\
&= \sum_{t \in q} \log{\frac{\dfrac{e^{-\rho_t}\rho_t^{n_t}}{n_t !} \cdot e^{-\gamma_t}}{e^{-\rho_t} \cdot \dfrac{e^{-\gamma_t}\gamma_t^{n_t}}{n_t !}}}\\
&= \sum_{t \in q} \log{\frac{\rho_t^{n_t}}{\gamma_t^{n_t}}}\\
&= \sum_{t \in q} n_t \log{\frac{\rho_t}{\gamma_t}}
\end{align*}$$
Analizziamo la formula appena ottenuta: abbiamo una sommatoria per ogni termine in comune tra query e documento di:
- $n_{t}$: quante volte il termine $t$ appare. Ogni occorrenza del termine aumenta il punteggio.
- Il peso $\log \frac{\rho_t}{\gamma_t}$: rappresenta il rapporto tra la frequenza attesa del termine nei documenti rilevanti e la frequenza attesa del termine in generale. Se $\rho_t \gg \gamma_{t}$ allora il peso è alto, altrimenti se appare più o meno con la stessa frequenza allora il rapporto è vicino a 1, e di conseguenza il logaritmo è vicino a 0.  

Si osservi inoltre che abbiamo ottenuto una formula del tipo:
$$RSV_{d} = \sum_{t \in q}n_{j}w_{j}$$ cioè **term frequency** $n_{j}$ per un perso $w_{j}$ che ricorda concettualmente idf. Stiamo quindi ricostruendo idf, ma da un punto di vista probabilistico.

**Problema**: Possiamo stimare $\gamma_{j} \approx \frac{cf_{j}}{N}$, ma per stimare $\rho_{j}$ serve sapere quali documenti sono rilevanti per le query, ma questo è esattamente quello che stiamo cercando di stimare a propri. Quindi questo modello non è direttamente utilizzabile.

Passiamo quindi ad un secondo modello.
[[Term occurrences as 2-Poisson]]