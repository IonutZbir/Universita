**DEF 1.1:** Uno spazio di probabilità $(\Omega, \mathcal{F}, P)$ è una tripletta formata da:
- $\Omega:$ spazio degli eventi;
- Una famiglia $\mathcal{F}$ di sottoinsiemi di $\Omega$, detti *eventi*;
- Una misura di probabilità $P$.

**DEF 1.2:** Una funzione $P: \mathcal{F} \to \mathbb{R}$ è detta misura di probabilità se:
1. $\forall E \in \mathcal{F}: 0 \leq P(E) \leq 1$
2. $P(\Omega) = 1$
3. Per ogni sequenza (finita o infinita) di eventi $E_{1}, \dots, E_{n} \in \mathcal{F}$ disgiunti a due a due $(E_{i} \cap E_{j} = \emptyset\ \forall i,j)$ si ha $$P\left(\bigcup_{i = 1, 2 \dots} E_{i}\right) = \sum_{i=1,2\dots} P(E_{i})$$
*Notazione:* Se $E \in \mathcal{F}$, chimiamo $E^c \in \Omega \setminus E$ l'evento complementare.

**CONSEGUENZE DELLA DEF 1.2:**
1. $\emptyset \in \mathcal{F},\quad P(\emptyset) = 0$;
2. Se $E \subseteq F,\quad P(E) \leq P(F)$;
3. $P(E^c) = 1 - P(E)\quad \forall E \in \mathcal{F}$;
4. $\forall E, F \in \mathcal{F}$ si ha $P(E) = P(E \cap F) + P(E \cap F^c)$.

**LEMMA 1.1:** Per ogni coppia di eventi $E_{1}, E_{2} \in \mathcal{F}$
$$
P(E_{1} \cup E_{2}) = P(E_{1}) + P(E_{2}) - P(E_{1} \cap E_{2})
$$

**LEMMA 1.2: (Union Bound):** Per ogni sequenza di eventi $E_{1}, E_{2}, \dots$ vale sempre che
$$
P\left(\bigcup_{i=1,2 \dots}\right) \leq \sum_{i=1,2 \dots}P(E_{i})
$$
**LEMMA 1.3 (Principio di Inclusione-Esclusione):**
Siano $E_{1}, \dots, E_{n}$ una sequenza di eventi, allora
$$
\begin{align}
P\left(\bigcup_{i=1}^n E_{i} \right) &= \sum_{i=1}^n P(E_{i}) - \sum_{i < j}^n P(E_{i} \cap E_{j}) + \sum_{i < j < k}^n P(E_{i} \cap E_{j} \cap E_{k})  \\
&+\dots + (-1)^{l+1} \sum_{i_{1} < i_{2} < \dots < i_{l}} P\left( \bigcap_{r=1}^l E_{ir} \right) + \dots
\end{align}
$$

**DEF 1.3:** Due eventi si dicono indipendenti se 
$$
P(E \cap F) = P(E)P(F)
$$

*NOTA:* Eventi indipendenti $\neq$ Eventi disgiunti.
In generale eventi $E_{1}, \dots, E_{n}$ si dicono *mutualmente indipendenti* se 
$$
\forall I \subseteq \{ 1, \dots, n \} \quad P\left( \bigcap_{i \in I}  E_{i} \right) = \prod_{i \in I} P(E_{i})
$$

**DEF 1.4:** La probabilità condizionata dell'eventi $E$ sapendo che $F$ è accaduto è
$$
(\star) = \boxed{P(E | F) = \frac{P(E \cap F)}{P(F)}}
$$

*Osservazione:* È come se il nuovo spazio degli stati fosse $F$ (si divide per la $P(F)$ cosi che $P(\Omega | F) = 1$).
- Si può verificare che $P(\cdot | F)$ è una misura di probabilità.
- Se $P(F) \neq 0$, allora $E, F$ sono indipendenti $\iff P(E|F)=P(F)$.
- È utile riscrivere a volte $(\star)$ come $$P(E \cap F) = P(E|F)P(F)$$oppure $$P(E | F) = \frac{P(E \cap F)}{P(F)} = P(E | F) \frac{P(E)}{P(F)}$$
**TEOREMA 1.6 (Formula Probabilità Totali):**
Siano $\{ E_{i} \}_{i = 1, 2, \dots, n}$ eventi disgiunti di $\Omega$ tali che $\bigcup_{i=1}^n E_{i} = \Omega$ (siano una partizione). Allora, $\forall B \in \mathcal{F}$
$$
P(B) = \sum_{i=1}^n P(E \cap E_{i}) = \sum_{i=1}^n P(B | E_{i})P(E_{i})
$$
![[prob_totali.png|300]]

**TEOREMA 1.7 (Formula di Bayes):**

Stesse ipotesi del Teorema 1.6. Se $P(B) \neq 0$, allora
$$
P(E_{j} | B) = \frac{P(B | E_{j})P(E_{j})}{\sum_{i=1}^n P(B | E_{i})P(E_{i})}
$$

**CONSEGUENZA:** Se consideriamo due eventi $E$ ed $F$, la formula è
$$
P(E | F) = \frac{P(F|E)P(E)}{P(F)} = \frac{P(F | E)P(E)}{P(F|E)P(E) + P(F | E^c)P(E^c)}
$$

## Alcuni Esempi di Utilizzo di Bayes

#### Esercizio 1 — Classico test medico

Una malattia rara colpisce l'1% della popolazione. Un test diagnostico ha:

- Sensibilità: $P(\text{test}^+ \mid \text{malato}) = 0.95$
- Specificità: $P(\text{test}^- \mid \text{sano}) = 0.90$

Una persona risulta positiva al test. Qual è la probabilità che sia effettivamente malata?

##### Soluzione

- $P(M) = 0.01$ $\implies$ probabilità di essere malato (prior)
- $P(S) = 0.99$ $\implies$ probabilità di essere sano (dove $S = M^c$)
- $P(+ \mid M) = 0.95$ $\implies$ sensibilità
- $P(- \mid S) = 0.90$ $\implies$ specificità, quindi $P(+ \mid S) = 0.10$ (falso positivo)

Vogliamo: $P(M \mid +)$
$$P(M \mid +) = \frac{P(+ \mid M) , P(M)}{P(+)}$$
Il denominatore va calcolato con la **legge della probabilità totale**, condizionando sui due possibili stati (malato/sano):

$$
\begin{align}
P(+) = P(+ \mid M)P(M) + P(+ \mid S)P(S) &= \frac{95}{100} \frac{1}{100} + \frac{10}{100}\left( 1 - \frac{1}{100} \right) \\
&= \frac{1085}{10000} = 0.1085
\end{align}
$$
Quindi
$$
P(M | +) = \frac{\frac{95}{100} + \frac{1}{100}}{\frac{1085}{10000}} = \frac{0.0095}{0.1085} \approx 0.0876
$$

##### Interpretazione

Anche con un test sensibile al 95%, se risulti positivo hai solo circa l'**8.8%** di probabilità di essere davvero malato.

Perché un risultato così controintuitivo? Perché la malattia è **rara** (1%): il numero assoluto di sani che ricevono un falso positivo ($0.10 \times 0.99 \approx 99$ persone su 1000) supera di gran lunga il numero di malati veri identificati correttamente ($0.95 \times 0.01 \approx 9.5$ persone su 1000). Questo è lo stesso fenomeno alla base dell'Esercizio 5 (rilevamento intrusioni) — un pattern molto comune quando l'evento di interesse è raro rispetto al tasso di errore del test.

#### Esercizio 2 — Urne
Hai tre urne:
- $U_1$: 3 palline rosse, 7 blu
- $U_2$: 6 palline rosse, 4 blu
- $U_3$: 5 palline rosse, 5 blu

Scegli un'urna a caso (uniformemente) ed estrai una pallina, che risulta rossa. Qual è la probabilità che provenga da $U_2$?

##### Soluzione

Tre urne, scelte con probabilità uniforme $P(U_1) = P(U_2) = P(U_3) = \frac{1}{3}$:
- $U_1$: 3 rosse, 7 blu $\implies$ $P(R \mid U_1) = \frac{3}{10}$
- $U_2$: 6 rosse, 4 blu $\implies$ $P(R \mid U_2) = \frac{6}{10}$
- $U_3$: 5 rosse, 5 blu $\implies$ $P(R \mid U_3) = \frac{5}{10}$
Vogliamo: $P(U_2 \mid R)$

$$P(U_2 \mid R) = \frac{P(R \mid U_2) , P(U_2)}{P(R)}$$

dove, per la probabilità totale:

$$P(R) = P(R \mid U_1)P(U_1) + P(R \mid U_2)P(U_2) + P(R \mid U_3)P(U_3)$$
$$P(R \mid U_1) = 0.3, \quad P(R \mid U_2) = 0.6, \quad P(R \mid U_3) = 0.5$$
**Denominatore:** $$P(R) = \frac{1}{3}(0.3 + 0.6 + 0.5) = \frac{1}{3}(1.4) = \frac{1.4}{3} \approx 0.4667$$
**Numeratore:** $$P(R \mid U_2),P(U_2) = \frac{1}{3} \times 0.6 = 0.2$$
**Risultato finale:** $$P(U_2 \mid R) = \frac{0.2}{1.4/3} = \frac{0.2 \times 3}{1.4} = \frac{0.6}{1.4} = \frac{3}{7} \approx 0.4286$$
