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

Abbiamo $Doc \in Sigma^*$, dove $\Sigma$ rappresenta l'alfabeto, e dobbiamo trovare un modo per trasformare i documenti in insiemi, così da poter applicare la Jaccard similarity.

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

Ora dobbiamo scegliere il valore di $k$. Se scegliamo un $k$ molto piccolo, ad esempio 1 o 2, è probabile che documenti completamente diversi risultino simili tra loro secondo la Jaccard Similarity, portando a molti falsi positivi. Per evitare ciò, la scelta di $k$ non dovrebbe essere casuale.

La regola generale è la seguente:

- Il valore di $k$ dovrebbe essere abbastanza grande da ridurre la probabilità che uno shingle specifico compaia casualmente in un documento qualsiasi.

Scegliendo un $k$ maggiore, riduciamo la probabilità che uno shingle si presenti in modo casuale in documenti diversi, rendendo il confronto più preciso. Un valore di $k$ più lungo permette di catturare pattern più specifici, migliorando l’affidabilità della similarità tra documenti.

In caso di documenti piccoli, come email, $k = 5$ è ragionevole. Mentre per documenti più grandi, $k = 9$ è un ottima scelta.

Sia $D \in \Sigma^*$ un documento rappresentato dal suo insieme di $k$-shingles. Se consideriamo $\Sigma^k$ l'insieme di tutti i possibili $k$-shingle ordinato, allora possiamo rappresentare $D$ come un vettore binario di dimensione $\bigm|\Sigma^k\bigm|$, dove ogni shingle è una componente di questo vettore e:

$$
v[i] = \begin{cases}
1 & \text{se l' i-esimo shingle dell'insieme ordinato } U \text{ sta nel documento} \\
0 & \text{se l' i-esimo shingle dell'insieme ordinato } U \text{ non sta nel documento}
\end{cases}
$$

![Shingle Vector](img/shingle_vec.png){width="600" style="display: block; margin: 0 auto"}

Possiamo rappresentare un insieme di documenti come una collezione di insiemi, dove ciascun insieme è descritto da un vettore binario. Questi insiemi formano la cosiddetta matrice caratteristica, in cui le colonne corrispondono ai documenti (vettori binari) e le righe agli shingle ordinati.

| Element | S₁ | S₂ | S₃ | S₄ |
| :-----: |----|----|----|----|
| a       | 1  | 0  | 0  | 1  |
| b       | 0  | 0  | 1  | 0  |
| c       | 0  | 1  | 0  | 1  |
| d       | 1  | 0  | 1  | 1  |
| e       | 0  | 1  | 1  | 0  |

### Step 2. MinHashing: Convertire gli insiemi molto grandi in piccole **firme (signatures)**, mantenendo la Jaccard similarity

Una volta calcolata la matrice caratteristica, possiamo già iniziare a determinare le coppie di elementi simili. Tuttavia, questo calcolo richiederebbe un tempo elevato, pari a $\theta(N^2 \cdot \bigm|\Sigma^k \bigm|)$. Per ridurre questa complessità, possiamo cercare di ridimensionare la matrice, riducendo il valore di $h = \bigm|\Sigma^k \bigm|$.

La tecnica utilizzata per questa operazione è chiamata **MinHashing**. Per eseguire il *minhash* di un insieme rappresentato da una colonna della matrice caratteristica, si applica una permutazione casuale delle righe. Il minhash di una colonna è quindi l'indice della prima riga, nella colonna permutata, in cui compare un 1.

!!! success
    Supponiamo che le righe della matrice $M$ sono permutate, secondo una permutazione casuale $\pi$.
    **Def**: Per ogni colonna $C$, definiamo **Min-Hash function** $h_{\pi}(c)$ l'indice della prima riga (nella permutazione $\pi$) in cui nella colonna $C$ appare il valore 1 (è lo chiamiamo $min(\pi(C))$).

Tra minhash e Jaccard similarity c'è una relazione, ovvero:

- La probabilità che la funzione di minhash, applicata su una permutazione casuale delle righe, produca lo stesso valore per due insiemi è uguale alla Jaccard similarity tra questi insiemi.

Questo significa che, se abbiamo due insiemi e applichiamo una permutazione casuale delle righe della matrice caratteristica, la probabilità che il minhash (ovvero l'indice della prima riga con un 1) sia lo stesso per entrambi gli insiemi è esattamente uguale al valore della similarità di Jaccard tra di loro.

- Se $J.sim(C_1, C_2)$ è **alta**, allora con alta probabilità $h(C_1) = h(C_2)$
- Se $J.sim(C_1, C_2)$ è **bassa**, allora con alta probabilità $h(C_1) \neq h(C_2)$
