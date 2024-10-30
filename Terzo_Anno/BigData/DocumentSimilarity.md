# Finding Similar Itmes - Document Similarity

Consideriamo un primo problema di data mining: la ricerca di elementi simili in un insieme di dati di grandi dimensioni. Supponiamo di avere in input un insieme $X_1, X_2, \dots , X_N​$, dove $N$ è dell'ordine di milioni o miliardi. Ogni elemento è rappresentato da dati multidimensionali; ad esempio, un’immagine può essere rappresentata come una matrice di pixel, che a sua volta può essere trasformata in un vettore appartenente a uno spazio di dimensione $h$. Anche $h$ è dell’ordine di milioni, il che significa che i dati in input non solo sono numerosi, ma anche ad alta dimensionalità.

Inanzitutto bisogna introdurre una funzione di distanza, $d(X_1, X_2)$ che quantifica la "distanza" tra due elementi $X_1$ e $X_2$. L'obiettivo è **trovare tutte le coppie $(X_i, X_j)$** tale che $d(X_i, X_j) \leq S$, dove $S$ è una certa soglia.

Una soluzione banale impiegherebbe tempo $O(N^2 \cdot h)$, che per quanto abbiamo visto prima, con $N$ e $h$ dell'ordine dei milioni, questa soluzione è inammissibile, in quanto troppo inefficiente. Vedremo in seguito un'algoritmo che **magicamente** impiega tempo $O(N \cdot h')$, con $h' << h$.

## Document Similarity

Passiamo ora all'argomento **Similar Items**, concentrandoci su un caso specifico per approfondire: il problema **Document Similarity**. Questo implica individuare tutte le coppie di documenti di testo che risultano simili tra loro. Tale problema ha applicazioni molto importanti in vari campi, come:

- Rilevamento di Plagio
- Identificazione di pagine web simili

### Scegliere la funzione di distanza

Ogni applicazione necessità di una funzione di distanza approprita, nel caso del document similarity, la funzione di distanza sceltà e la **Jaccard Similarity**.

!!! success
    - Definiamo la **Jaccard Similarity** di due insiemi come:
    $$J.sim(C_1, C_2) = \frac{\bigm|C_1 \cap C_2 \bigm|}{\bigm|C_1 \cup C_2 \bigm|}$$
    - Definiamo la **Jaccard Distance** di due insiemi come:
    $$J.d(C_1, C_2) = 1 - J.sim(C_1, C_2)$$

![Jaccard Similarity](img/jaccard_sim.png){width="300" style="display: block; margin: 0 auto"}

La domanda che sorge spontanea è: come possiamo utilizzare la Jaccard similarity, dato che richiede di lavorare su insiemi, mentre noi stiamo trattando documenti di testo?

Ricapitolando, la nostra situazione è la seguente:

Abbiamo $Doc \in U^*$, dove $U$ rappresenta l'alfabeto, e dobbiamo trovare un modo per trasformare i documenti in insiemi, così da poter applicare la Jaccard similarity.

Prima di andare nel dettaglio, osserviamo ad alto livello l'algoritmo.

1. **Input**: In insieme grande di documenti;
2. **Shingling**: Convertire i documenti in **insiemi** (molto grandi);
3. **Min-Hashing**: Convertire gli insiemi molto grandi in piccole **firme (signatures)**, mantenendo la Jaccard similarity;
4. **Localitive-Sensitive Hashing (LSH)**: LSH si concentra su coppie di firme che probabilmente appartengono a documenti simili secondo la Jaccard similarity;
5. **Output**: Ritorna le coppie di documenti candidate ad essere simili.

### Step 1. Shingling: Convertire i documenti in insiemi

Consideriamo un documento come una stringa di caratteri. Sia $\Sigma$ l'alfabeto, per esempio l'alfabeto inglese composto da 27 caratteri ($\Sigma = \{a,\ b,\ c,\ \dots\}$) e sia $\Sigma^*$ l'insieme di tutte le stringhe costituie con i caratteri di $\Sigma$. Sia $Doc \in \Sigma^*$ un documento; definiamo un $k$-shingle di un documento come una qualsiasi sottostringa (*token, che può essere formato da caratteri o parole*) di lunghezza $k$ all'interno di quel documento. Allora, associamo a ciascun documento l'insieme composto da $k$-shingles che appaiono una o più volte nel documento $Doc$.

!!! example
    Supponiamo che il nostro documento $D$ sia la stringa `abcdabd` e scegliamo $k = 2$. Allora l'insieme 2-shingles per $D$ è $\{ab, bc, cd, da, bd\}$. Osserviamo che `ab` compare 2 volte nel documento, ma una volta sola nell'insieme. Una variazione sarebbe quella di usare multinsiemi invece che insiemi per rappresentare gli shingle.

Ci sono varie possibilità riguardo i caratteri "vuoto", "tabulazione", "nuova riga", un'idea sarebbe quella di sostuire tali caratteri con con semplice carattere vuoto.

