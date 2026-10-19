## Chain Rule
$$P(A,B) = P(A \vert B)P(B) = P(B \vert A)P(A)$$
Oppure in generale
$$\begin{align*}
P(E_1 \cap ... \cap E_n)
&= P(E_1 \cap (E_2 \cap ... \cap E_n))\\
&= P(E_1 \vert E_2 \cap ... \cap E_n) \cdot P(E_2 \cap ... \cap E_n)\\
&= P(E_1 \vert E_2 \cap ... \cap E_n) \cdot P(E_2 \vert E_3 \cap ... \cap E_n) \cdot P(E_3 \cap ... \cap E_n)\\
&\vdots\\
&= P(E_n) \cdot \prod_{i=1}^{n-1}P\left(E_i \vert \bigcap_{j = i+1}^{n} E_j\right)
\end{align*}$$

### Partition Rule
$$P(B) = P(B \cap \Omega) = P(B \cap (A \cup \overline{A})) = P(B \cap A) + P(B \cap \overline{A})$$

### Bayes' Rule
$$P(A \vert B) = \frac{P(B \vert A) P(A)}{P(B)} = \frac{P(B \vert A)P(A)}{P(B \cap A) + P(B \cap \overline{A})} = \frac{P(B \vert A)P(A)}{P(B \vert A)P(A) + P(B \vert \overline{A})P(\overline{A})}$$

### Odds
Il rapporto tra la probabilità che un evento $A$ accada e la probabilità che non accada.
$$O(A) = \frac{P(A)}{P(\overline{A})} = \frac{P(A)}{1-P(A)}$$
- se $O(A) = 1$ allora $P(A) = 1/2$.
- se $O(A) > 1$ allora $P(A) > 1/2$. (il documento è piu probabile che sia rilevante)
- se $O(A) < 1$ allora $P(A) < 1/2$ (il documento è più probabile che non sia rilevante).
- $O(A) \in \left[ 0, \infty \right)$