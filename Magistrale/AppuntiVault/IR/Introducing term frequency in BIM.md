Una delle problematiche del [[Binary Independent Model#Problemi|Binary Independent Model]] era che non teneva affato in considerazione il numero di occorrenze di un termine in un documento.
Generalmente, se una parola chiave appare molte volte in un documento potrebbe voler dire che il documento è rilevante.

Ricordando come era definito il [[Binary Independent Model#^ab2996|Retrieval Status Value]]
$$RSV_d = \sum_{t \in q \cap d} \log{\frac{P(t \vert R,q) (1- P(t \vert \overline{R},q))}{P(t \vert \overline{R},q) (1-P(t \vert R,q))}} = \sum_{t \in q \cap d} \log{\frac{p_t (1- u_t)}{u_t (1-p_t)}}$$ dove
- $p_t = P(t \vert R,q)$ è la probabilità che il termine $t$ appaia in un documento **rilevante** per la query $q$.
- $u_t = P(t \vert \overline{R},q)$ è la probabilità che il termine $t$ appaia in un documento **non rilevante** per la query $q$.
- $1 - p_t = 1 - P(t \vert R,q)$ è la probabilità che il termine $t$ **non** appaia in un documento **rilevante** per la query $q$.
- $1 - u_t = 1 -P(t \vert \overline{R},q)$ è la probabilità che il termine $t$ **non** appaia in un documento **non rilevante** per la query $q$.

Abbiamo anche visto che in [[Binary Independent Model#Caso 2|mancanza di informazioni]] sulla rilevanza dei documenti, possiamo approssimare $$u_t \approx \frac{\text{df}_t}{N} = P(\lbrace d : t \in d \rbrace)$$ ovvero la probabilità di campionare un documento che contenga $t$ (sempre assumendo l'**indipendenza** tra termini e documenti).

Per introdurre il concetto di frequenza rappresentiamo i documenti come dei **count vector** $d = (d_1, ..., d_{\vert V \vert})$ dove $d_i$ è il numero di occorrenze del termine $t_i$ nel documento $d$.

Possiamo ridefinire il RSV in maniera [[Distribuzioni Multivariate|congiunta]] come
$$RSV_d = \sum_{t \in q}\log{\frac{P(d_t = n_t \vert R,q) P(d_t = 0)}{P(d_t = n_t)P(d_t = 0 \vert R, q)}}$$
dove ^2d7816
- $P(d_t = k \vert R,q)$ è la probabilità che il termine $t$ appaia esattamente $k$ volte in un documento rilevante.
- $P(d_t = k)$ è la probabilità che un termine $t$ appaia $k$ volte in un documento qualsiasi.

Una distribuzione semplice da calcolare che può modellare $P(d_t = k)$ è una **[[Distribuzioni#Binomiale|binomiale]]**.
Vediamo il documento $d$ come una serie di $\vert d \vert = L$ **celle**, contenenti ciascusa una parola/termine.
In maniera **semplificata** assumiamo che il termine $t_i$ abbia probabilità $\tilde{p}_i$ di apparire in una cella, e probabilità $1 - \tilde{p}_i$ di non apparire.
Avremo quindi che $$P(d_i = k) = \binom{L}{k}\tilde{p}_i^k(1-\tilde{p}_i)^{L-k}$$ ^2ee5f6

Tuttavia la distribuzione binomiale ha alcuni problemi: **dipende dal $L$, ha formule brutte ed è in generale difficile da usare nel ranking.** Pre questo motivo si preferisce fare affidamento a un trick matematico e passare alla Poissson.

- [[Term occurrences as Poisson]]
- [[Term occurrences as 2-Poisson]]