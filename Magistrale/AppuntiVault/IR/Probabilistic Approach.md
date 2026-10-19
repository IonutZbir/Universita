Vogliamo che dato un **information need** espresso sottoforma di **query** ed una **collezione di documenti**, un sistema di IR sia in grado di misurare quanto i documenti siano inerenti alla query.

Dato che c'è sempre un livello di **incertezza** sul significato di una query $q$ (dato che sono espresse in **linguaggio naturale**), il livello di rilevanza di un documento diventa una variabile aleatoria. Quando viene fatta una query, il sistema *non capisce veramente il bisogno informativo dell'utente* ma ha solo una rappresentazione di esso (come vettore di termini).

Infatti l'incertezza può essere data da vari fattori:
- diversi utenti potrebbero avere diverse opinioni sulla rilevanza di $d$ rispetto a $q$.
- uno stesso utente potrebbe definire $d$ rilevante o meno rispetto a $q$ dipendentemente dal contesto.
- la rappresentazione dei documenti nel sistema di IR potrebbe non catturare a pieno il concetto di rilevanza. Infatti per esempio il [[Vector Space Model]] definisce la rilevanza dei documenti solamente rispetto alla similitudine (intesa come insieme di parole) con la query. Però sappiamo che una cosa si può dire in molti modi diversi e con parole differenti.

Possiamo quindi definire un **modello probabilistico** in cui il ranking è basato sulla *probabilità che un documento $d$ sia effettivamente rilevante rispetto ad una query $q$*.
$$P(d \text{ è rilevante rispetto a }q)$$

## Introduzione

Definiamo una prima nozione di **rilevanza probabilistica**. Assumeremo che la rilevanza di un documento sia un variabile aleatoria.

Dato un documento $d$ e una query $q$ definiamo la **variabile aleatoria binaria**
$$R_{d,q}\begin{cases}
1 &\text{se } d \text{ è rilevante rispetto a } q\\
0 &\text{altrimenti}
\end{cases}$$

Possiamo quindi *interpretare* la probabilità $P(R_{d,q} = 1) = P(R = 1 \vert d,q)$ come la probabilità che un qualsiasi utente **a caso** giudichi $d$ **rilevante** rispetto alla query $q$. 

Poichè questa probabilità deve dipende anche dagli utenti, dal momento che la rilevanza è soggettiva, e assumendo che tutti gli utenti siano indipendenti, abbiamo che: se denotiamo con $U$ lo spazio degli utenti, definiamo quindi
$$P(R_{d,q} = 1) = \sum_{u \in U} P(R_{d,q} = 1 \vert u) P(u)$$
dove $P(R_{d,q} = 1 \vert u)$ è la probabilità che l'utente $u$ identifichi il documento $d$ come rilevante ripsetto alla query $q$.

**Assumiamo inoltre che gli utenti siano ugualmente probabili** quindi alla fine consideriamo solo $P(R|d,q)$.

Una buona idea è quella di ritornare un documento $d$ come risultato di una query $q$ se la probabilità che sia inerente è **maggiore** di $1/2$, ovvero se $P(R_{d,q} = 1) > 0.5$.
In termini di [[Appendice Probabilità#Odds|odds]] se $$O(\lbrace R_{d,q} = 1 \rbrace) = \frac{P(R_{d,q} = 1)}{P(R_{d,q} = 0)} > 1$$
```ad-info
Per semplicità, indichiamo con $R \vert d,q$ l'evento $\lbrace R_{d,q} = 1 \rbrace$.
Analogamente indichiamo con $\overline{R} \vert d,q$ l'evento $\lbrace R_{d,q} = 0 \rbrace$.
```


Tuttavia, **non abbiamo informazioni sui giudizi di rilevanza da parte degli utenti per ogni documento e query, quindi sfruttando Bayes, otteniamo:**

1. **Classical Probabilistic Retrieval Model** $$P(R | d, q) = \frac{P(d | R, q) \cdot P(R|q)}{P(d | q)}$$cioè stimiamo quanto è probabile che il documento sia rilevante guardando quanto è probabile osservare quel documento tra i documenti rilevanti per la query fissata $q$.
	Analogamente: $$P(\bar{R} | d, q) = \frac{P(d | \bar{R}, q) \cdot P(\bar{R}|q)}{P(d | q)}$$cioè stimiamo quanto è probabile  che il documento non sia rilevante guardando quanto è probabile osserva quel documento tra i documenti non rilevanti per la query fissata $q$.
2. **Language Model for IR** $$P(R | d, q) = \frac{P(q | R, d) \cdot P(R|d)}{P(q | d)}$$cioè stimiamo la probabilità che il documento sia rilevante guardando quanto è probabile osservare la query a partire dal documento, assumendo che $R$ sia rilevante.
	Analogamente: $$P(\bar{R} | d, q) = \frac{P(q | \bar{R}, d) \cdot P(\bar{R}|d)}{P(q | d)}$$cioè stimiamo la probabilità che il documento non sia rilevante guardando quanto è probabile osservare la query a partire da un documento non rilevante.

- [[Appendice Probabilità]]
- [[Probabilistic Ranking Principle]]
- [[Binary Independent Model]]
- [[Introducing term frequency in BIM]]
- [[Okapi BM25]]