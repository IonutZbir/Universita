
Il **Probabilistic Ranking Principle** (in breve **PRP**) consiste nell'effettuare il ranking in base alle rispettive probabilità che i documenti ritornati siano rilevanti rispetto alla query: ordiniamo i documenti rispetto a $P(R \vert d,q)$.

Usando la [[Appendice Probabilità#Bayes' Rule|regola di Bayes]] abbiamo quindi che
$$P(R \vert d,q) = \frac{P(d \vert R, q) P(R \vert q)}{P(d \vert q)} = \frac{P(d \vert R, q) P(R \vert q)}{P(d)}$$^87f37c

dove 
- $P(d \vert R, q)$ è la probabilità di campionare un documento $d$  dal sottoinsieme dei **soli documenti rilevanti** rispetto a $q$.
- $P(R \vert q)$ è la probabilità di campionare a caso un qualsiasi documento rilevante rispetto a $q$.
- $P(d)$ è la probabilità che il documento $d$ sia campionato dalla collezione. Osservare che $P(d \vert q) = P(d)$ perché a priori un campionamento di un documento è **indipendente** dalla query $q$.

Una prima assunzione che stiamo facendo è che la rilevanza di ogni documento $d$ è **indipendente** dalla rilevanza degli altri documento, ovvero $$P(R_{d,q} \vert R_{d',q}) = P(R_{d,q})$$
Un'altra assunzione è che i documenti sono **uniformemente campionati**, ovvero dati due documenti $d,d'$ abbiamo che $P(d) = P(d')$.

Osserviamo che data la [[#^87f37c|precedente formula]] possiamo benissimo **ignorare** il fattore $P(R \vert q)$ e $P(d)$, visto che $P(R \vert q)$ è una costante per ogni $d$ dato che $d$ è **equiprobabile**.
$$\overbrace{P(d \vert R, q)}^{\text{depending on } d} \cdot \underbrace{\frac{P(R \vert q)}{P(d)}}_{\text{uguale per ogni }d}$$
Ci concentreremo quindi sulla sola probabilità $P(d \vert R,q)$.

L'idea sotto il **Probabilistic Ranking Principle** in breve può essere descritta come:
> Se l'insieme di documenti restituiti a seguito di una query sono ordinati rispetto alla loro **probabilità** di essere rilevanti (per la query) allora la qualità del sistema di IR è il **migliore ottenibile**.


## Problemi
Purtroppo non è possibile calcolare esplicitamente queste probabilità, dato che avremmo bisogno a priori di aver già incontrato ogni query possibile $q$.
Perciò è necessario **stimarle** al meglio possibile rispetto ai dati che il sistema ha a disposizione, con degli stimatori appositi.

## Proof of PRP

L'obiettivo di un motore di IR è quello di ritornare il **miglior** insieme di documenti a seguito di una query, ordinati nella maniera **migliore**.

Per modellare il concetto di *"migliore"*, definiamo una funzione che misuri il **costo di errore**.
- $C_{1}(d,q)$: *costo di non restituire un documento rilevante* (FN)
- $C_{2}(d,q)$: *costo di restituire un documento non rilevante* (FP)

Ovvero associamo un valore ad ogni documento **non** rilevante restituito, e ad ogni documento rilevante **non** restituito.

Più formalmente definiamo le seguenti due funzioni
$$C_1(d,q) =
\begin{cases}
1 &\text{if } d \text{ is relevant but not returned}\\
0 &\text{if } d \text{ is relevant and returned}
\end{cases}$$
$$C_2(d,q) =
\begin{cases}
1 &\text{if } d \text{ is not relevant but returned}\\
0 &\text{if } d \text{ is not relevant and not returned}
\end{cases}$$

O in altri termini
- $C_1(d,q) = 1$ se $d$ è un **falso negativo**.
- $C_2(d,q) = 1$ se $d$ è un **falso positivo**.

Sia $D(q)$ l'insieme dei documenti restituiti dal sistema di IR in questione a fronte della query $q$, e sia il suo costo (in termini di funzine errore)
$$err(D(q)) = \sum_{d \in D(q)} C_2(d,q) + \sum_{d \notin D(q)} C_1(d,q)$$

Sfruttando un framework probabilistico possiamo calcolare l'errore solamente in **media**.
Perciò avremo che
$$\begin{align*}
\mathbb{E}\left[ err(D(q)) \right]

&= \sum_{d \in D(q)} C_2(d,q) \cdot P(\overline{R} \vert d,q) + \sum_{d \notin D(q)} C_1(d,q) \cdot P(R \vert d,q)\\
&= \sum_{d \in D(q)}(1 - P(R \vert d,q)) + \sum_{d \notin D(q)} P(R \vert d,q)\\
&= \vert D(q) \vert + \sum_{d \notin D(q)}P(R \vert d,q) - \sum_{d \in D(q)}P(R \vert d,q)
\end{align*}$$

Il sistema di IR *migliore* è quindi quello che **minimizza in media** l'errore del risultato $D(q)$.
Tale media è quindi **minimizzata** quando è **massimizzata** la quantità $$\sum_{d \notin D(q)}P(R \vert d,q) - \sum_{d \in D(q)}P(R \vert d,q)$$ e ciò accade quando in $D(q)$ sono riportati i $k$ documenti con probabilità più alta $\square$.

Tuttavia bisogna fare attenzione: questa ottimalità è vera solo dal momento che le probabilità di rilevanza sono stimate correttamente. Quindi il problema diventa quello di stimare correttamente $P(R|d,q)$. Se le stime sono errate, il PRP non è più ottimale.