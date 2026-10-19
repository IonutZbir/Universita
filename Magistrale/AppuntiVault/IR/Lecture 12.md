Definiamo quindi un **modello generativo**, ovvero dato un documento $d$ calcoli la probabilità che la query $q$ sia la query a cui $d$ risponde.
$$P(R \vert d,q) = \frac{P(q \vert R,d)P(R \vert d)}{P(q)}$$

Dato ogni documento $d$ definiamo un **automa probabilistico** che lo genera.
Tale automa è una **catena di markov** dove c'è un arco tra due stati $X_i,X_j$ etichettato con il termine $t$ e con probabilità $P(t \vert X_i)$ (probabilità che nello stato $X_i$ appaia il termine $t$ che porti allo stato $X_j$).

Per semplificare possiamo definire un automa con un solo stato tale che è **indipendente** dallo stato attuale: ho semplicemente la probabilità che appaia un termine qualsiasi.

Sia quindi $M_d$ il **modello** (semplice) del documento $d$: $P(t \vert M_d) = P(t \vert d)$.
La query migliore è quella che massimizza la probabilità $$P(q \vert M_d) = \prod_{t \in q}P(t \vert M_d)$$
(**Naive Bayes**)

Vogliamo quindi poter calcolare $P(t \vert M_d)$.

- **modo binomiale**: posso calcolare la probabilità che il termine $t$ appare nella query $$P(\text{tf}_{t,d} = k) = \binom{\vert q \vert}{k}p^k(1-p)^{\vert q \vert - k}$$
- **modo multinomiale** $$P(t_{t_i,q}= k_i \vert i = 1, ..., n) = \binom{n}{k_1,...,k_{n}} \prod_{i=1}^{n}p_i^{k_i}$$
Definiamo $$\hat{p}_i = P(t_i \vert M_d) = \frac{\text{tf}_{t_i,d}}{\vert d \vert}$$
FINO A SLIDE 25 - DA SLIDE 26 IN POI NO.