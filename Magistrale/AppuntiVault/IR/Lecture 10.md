---
date: 2022-11-29
draft: true
---
Un sistema di retrieval dovrebbe modellare l'**incertezza** che un documento sia rilevante rispetto a una query oppure no.

Dobbiamo quindi definire un **modello probabilitstico** che modelli la probabilità che un documento sia rilevante rispetto a una query
$$P(d \text{ è rilevante rispetto a }q)$$

- $P(A \cap B) = P(A \vert B)P(B) = P(B \vert A)P(A)$
- $P(B) = P(A \cap B) + P(\overline{A} \cap B)$
- **ODDS** $$O(A) = \frac{P(A)}{P(\overline{A})}$$

