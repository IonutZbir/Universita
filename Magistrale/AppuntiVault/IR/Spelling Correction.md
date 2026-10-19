La spelling correction è un problema presente in moltissimi contesti, tra cui i motori di ricerca, in cui è necessario correggere errori di battituta o di ortografia nelle query degli utenti. 

Distinguiamo tra due tipologie di errori di battitura: 
- **Spelling Error Detection**: identificare se una parola è scritta in modo errato, ad esempio riconoscere che la parola `mony` non è una parola corretta.
- **Spelling Error Correction**: essere in gradi di capire se l'utente digitando `mony` intendesse  `money`.

Il sistema può approcciare alla correzione in modi diversi: sostituire direttamente oppure suggerire una singola alternativa oppure una lista di alternative candidate (come fa google search). Osservare che l'approccio diretto di *autocorrect* comporta un problema di **usability** dal momento che se il sistema corregge in modo errato, l'utente potrebbe non accorgersene e quindi non riuscrire a trovare ciò che stava cercando. Per questo affinché si arrivi a fare autocorrect è necessario un alto livella di confidenza.

Esistono due tipologie di spelling error:

1. **Non word errors**: Sono errori che producono una una stringa che *non è presente nel dizionario* (es. `mony` invece di `money`). Questo errore è più facie da identificare, in quanto basta solo controllare se la parola è presente o meno all'interno del dizionario e per correggerla basta sostituirla con la parola **più vicina** (il concetto di vicinanza lo vedremo dopo) a essa errata. Sono errori facili da gestire
2. **Real word errors**: Sono errori che producono una stringa che è *presente all'interno del dizonario* ma non è quella che l'utente intendeva (es. `i have a pen` invece di `i have a pan`). Questa tipologia di errori è più complessa da gestire in quanto dipende dal **contesto**.

Riassumendo, per quanto riguarda i **non word errors**, la *detection* è facile. Tuttavia bisogna fare attezione in quanto i dizionari stessi potrebbero contenere dei mispellings. Per quanto riguarda invece la *correction*, questa fase è più complessa in quanto bisogna generare dei candidati ed estrarre il migliore. Per fare questo si usano alcune misure: **shortest weighted edit distance** e **highest noisy channel probability**.

## Noisy Channel & Edit Distance

Per **Noisy Channel** intendiamo un modello probabilistico utilizzato per la correzione degli errori di battitura. Supponiamo che la parola corretta è stata *rovinata* da un determinato rumore. L'obiettivo è quello di poter risalire dalla parola sbagliata **noisy word** alla parola originale, ossia alla parola più probabile tra quelle che poteva produrre.

Questo modello può essere formalizzato con Bayes. Sia $x$ la parola mispelled, allora voglia calcolare:
$$\hat{w} = \arg \max_{w \in V} \mathcal{P}(w | x) = \arg \max_{w \in V} \frac{\mathcal{P}(x | w)\mathcal{P}(w)}{\mathcal{P}(x)}$$
Poiché $\mathcal{P}(x)$ è costante per ogni candidato $w$, lo possiamo ignorare, ottenendo:
$$\hat{w} = \arg \max_{w \in V}\mathcal{P}(x | w)\mathcal{P}(w)$$
Questa formula ci dice che la miglior parola $\hat{w}$ tra le possibili parole candidate $w$ è quella che massimizza il prodotto tra la probabilità che $w$ sià stata trasformata in $x$ ($\mathcal{P}(x | w)$) e la probabilità che $w$ sia una parola corretta ($\mathcal{P}(w)$). Infatti, diremo che:
- $\mathcal{P}(w)$ è la probabilità a **priori**, ossia che $w$ sia una parola corretta indipendentemente da $x$.
- $\mathcal{P}(x | w)$ è detta **likelihood** di $x$ dato $w$, probabilità che fa parte del noisy channel model. Questa rappresenta la probabilità che $w$ sia stata trasformata in $x$ a causa del rumore.

### Generazione dei candidati applicando il noisy channel

Sia $x = \text{ "acress" }$ la query mispelled (osserviamo che si tratta di un *non word error*). I possibili candidati possono venire da due fonti principali: parole con *spelling simile (small edit distance)* o parole con *pronuncia simile*. Per ora consideriamo solo il primo caso.

Definiamo **Edit Distance** tra due stringhe $x$ e $y$ come il numero minimo di caratteri diversi tra $x$ e $y$ se sono consentite le seguenti operazioni elementari:
- `insert(str, char)`: inserimento di un solo carattere all'interno della stringa. Ad esempio `acress` $\to$ `actress`,
- `delete(str, char)`: rimozione di un solo carattere dalla stringa. Ad esempio `acress` $\to$ `acres`,
- `replace(str, char)`: sostituizione di un solo carattere con un altro. Ad esempio `acress` $\to$ `access`,
- `swap(str)`: trasposizione di due caratteri *adiacenti* nella stringa. Ad esempio `the` $\to$ `teh`.

In generale si imposta una soglia dell'edit distance piccola, ad esempio 1, in quanto l'80% degli errori è entro 1. Inoltre bisogna considerare come caratteri anche lo spazio ` `.

Alcune tecniche usate per la generazione dei candidati sono:

1. **Ricerca Lineare nel Dizionario**: Si controlla l'edit distance tra l'errore e tutti i termini del dizionario, e si selezionano quelli entro la soglia. Poco efficiente, se il dizionario è troppo grande.
2. **Generare Candidati entro una Soglia**: Si generano tutte le stringhe entro una distanza 1 o 2, per poi fare l'intersezione con il dizionario.
3. **Usando i K-grams** Scomponiamo la parola della query in $k$-grammi (`accress` $\to$ {`$a, ac, cr, re, es, ss, s$`}) e poi cercare all'interno del dizionario tutte quelle parole che contengono tali $k$-grammi. A questo punto si possono determinare quelle che gli assomigliano di più applicando per esempio la Jaccard Similiraty: $\frac{|A \cap B|}{|A \cup B|}$, dove $A$ è l'insieme dei $k$-grammi della parola della query e $B$ è l'insieme dei $k$-grammi di un candidato.
4. **Levenschtein Finite State Trasducer**;
5. **Mappa Precalcolata**: usare una tabella precalcolata con gli errori più comuni e le correzioni. Una mappa del genere può essere costruita manualmente oppure automaticamente, generandola dal dizionario o ancora meglio sfruttando i log degli utenti. È molto efficiente in quanto basta un `look-up` all'interno della tabella.

Nessuna di queste tecniche è migliore delle altre, nella pratica si segue il seguente schema:

1. Si costruisce un insieme ristretto di candidati abbastanza buoni (ad esempio a distanza 2).
2. Si sceglie il migliore tra questi.

In questo modo non è detto che la correzione scelta sia la migliore in assoluto, ma è un compromesso tra efficienza e accuratezza, ed è quello pià usato nei modelli di IR.

Vediamo ora quindi come calcolare i candidati, ossia $$\mathcal{P}(w | x) = \mathcal{P}(x | w)\mathcal{P}(w)$$ e scegliere poi il migliore tra questi.

1. $\mathcal{P}(w) = \frac{C(w)}{N}$, dove $C(w)$ è il numero di occorenze di $w$ nella collezione ed $N$ è il numero di termini della collezione. L'idea è che parole più frequenti sono più probabili di essere quelle corrette. In alcuni contesti, se il dizionario non è suffieciente, si utilizzano anche le query degli utenti per stimare $\mathcal{P}(w)$. Sfortunatamente non basta solo considerare la parola più frequente, ma dobbiamo tener conto anche della probabilità che avvenga un determinato errore.
2. $\mathcal{P}(x | w)$ infatti rappresenta questa probabilità di errore. Consideriamo la frequenza che avvenga un determinato errore (`insert, delete, swap, replace`). Calcolarla direttamente è abbastanza diffcile, e per stimarla si usano 4 famiglie di conteggi. Siano $x$ e $y$ caratteri, allora
	1. `del[x, y]`: numero di volte in cui $xy$ è stato digitato come $x$
	2. `ins[x, y]`: numero di volte in cui $x$ è stato digitato come $xy$
	3. `sub[x, y]`: numero di volte in cui $y$ è stato digitato come $x$
	4. `trans[x, y]`: numero di volte in cui $xy$ è stato digitato come $yx$
	Per `del` e `ins` consideriamo anche il carattere precedente e non il singolo perché `del[q, w] > del[q, p]`, ossia è più proabile che un utente si sbagli a inserire  `w` dopo `q` rispetto a `p` dopo `q`. Dunque:
	$$\mathcal{P}(x | w) = 
	\begin{cases}
	\frac{\texttt{del}[w_{i-1}, w_i]}{\texttt{count}[w_{i-1}w_i]}, \quad \text{if deletion} \\
	\frac{\texttt{ins}[w_{i-1}, x_i]}{\texttt{count}[w_{i-1}]}, \quad \text{if insertion} \\
	\frac{\texttt{sub}[x_i, w_i]}{\texttt{count}[w_i]}, \quad \text{if substitution} \\
	\frac{\texttt{trans}[w_i, w_{i+1}]}{\texttt{count}[w_iw_{i+1}]}, \quad \text{if transposition} \\
	\end{cases}
			$$
	dove al **numeratore** si ha il *conteggio del tipo di errore specifico* e al **denominatore** il *conteggio del numero di volte in cui è apparso il bigramma* $w_{i-1}w_i$ *nella collezione*.
	Nel caso di $\texttt{del}[w_{i-1}w_i]$, quante volte il bigramma $w_{i-1}w_i$ è stato digitato come solo $w_{i-1}$, ossia quante volte $w_i$ è stato omesso dopo $w_{i-1}$.

Rimane un unico problema da risolvere, ossia come calcolare il conteggio al numeratore? Per fare ciò, si sfruttano le **Confusion Matrices**, una per ognuno dei 4 tipi di errore. Consideriamo la confusion matrix per l'errore di sostituzione. In posizione $(x, y)$ c'è il numero di volte in cui $y$ (corretto) è stato digitato come $x$ (sbagliato). Ovviamente i valori all'interno della matrice sono dati euristici che si basano su dati empirici.

Infine, l'ultima tecnica applicata è lo **smoothing**, ossia aggiungere un uno ad ogni conteggio, ossia sulle probabilità delle matrici di confusione nel channel model. Questo è dovuto al fatto che senza smoothing ogni errore che non è mai stato osservato nelle confusion matrix verrebe zero, e ciò implicherebbe che la probabilità complessiva per il candidato diventerebbe zero. Facendo tutti questi ragionamenti, si arriva a stimare che il candidato più probabile per `acress` è `across`.

### Real word errors: caso context sensitive

Concentriamoci adesso sui real word errors (circa il 25-40%). In questi casi non possiamo più analizzare parola per parola, ma dobbiamo analizzare tutta la frase in quanto abbiamo bisogno di capire il **contesto** in cui ci troviamo. In generale si procede nel seguente modo:

1. Sia $Q = q_1, \dots q_n$ la nostra query, generiamo per ogni $q_i$ un insieme di candidati $C_i$ che devono contenere la stessa parola $q_i$ e parole simili, ad esempi con edit distance pari 1-2.
2. Si generano poi frasi candidate $W$, e si riapplica il noisy channel model, stavolta sull'intera frase e non sulla singola parola, per cercare il candidato $\hat{W}$  che massimizza la probabilità: $$\hat{W} = \arg \max_{W} \mathcal{P}(W | Q) = \arg \max_{W} \mathcal{P}(X | W)\mathcal{P}(W)$$

dove $W$ è una frase candidata e $Q$ la nostra frase/query originale. Analogamente, $\mathcal{P}(W)$ è la probabiltà che $W$ sia una frase corretta mentre $\mathcal{P}(Q|W)$ è la probabilità che la frase corretta $W$ sia stata trasformata in $Q$ a causa del rumore.

1. Dobbiamo ora calcolare $\mathcal{P}(W)$. Non possiamo più applicare $\frac{C(W)}{N}$, come nel *Unigram Language Model*, ossia tenere in considerazione la frequenza delle parole all'interno del corpus, ma bisogna capire quale delle due parole è più plausibile in quella posizione della frase, ossia il contesto. Per semplicità limitiamoci al caso **Bigram Language Model**. L'idea di questo modello è quella di stimare la probabilità di una parola all'interno di una frase, guardando per ogni parola, solo la parola precedente: $$\mathcal{P}(W) = \mathcal{P}(w_1, w_2, \dots, w_n) \approx \mathcal{P}(w_1)\mathcal{P}(w_2|w_1) \dots \mathcal{P}(w_n|w_{n-1})$$ In questo modo, il modello permette di determinare quale frase sia più probabile. Tornando all'esempio precedente, la frase `versatile actress whose` è più probabile di `versatile across whose`, in quanto le coppie `versatile actress` e `actress whose` sono più plausibili rispetto a `versatile across` e `across whose`. Infine,  $$\mathcal{P}(w_k | w_{k-1}) = \frac{C(w_{k-1}, w_k)}{C(w_{k-1})}$$dove $C(w_{k-1}, w_k)$ è *il numero di volte in cui il bigramma* $w_{k-1}w_k$ *è apparso nella collezione* e $C(w_{k-1})$ è il numero di volte in cui la parola $w_{k-1}$ è apparsa nella collezione. Si osserva che $P(w_k | w_{k-1}) = 0$ se il bigramma $w_{k-1}w_k$ non è mai apparso nella collezione. Al fine di risolvere tale problema, possiamo:
	1. Applicare lo **smoothing**, esattamente come visto prima, si aggiunge 1 a ogni conteggio, in modo da evitare che la probabilità sia 0.
	2. **Interpolazione unigram + bigram**: non consideriamo solo la probabilità che ci sia il bigramma, ma consideriamo anche la probabilità dell'unigramma, dandogli però meno importanza, avremo quindi $$\mathcal{P}_{li}(w_k | w_{k-1}) = \lambda\mathcal{P}_{uni}(w_k) + (1 - \lambda)\mathcal{P}_{bi}(w_{k} | w_{k-1})$$In questo modo, anche se il bigramma non è mai apparso, si tiene conto della frequenza dell'unigramma assicurandoci di non avere probabilità zero. Inoltre, se $w_k$ è molto frequente, si da la possibilità al bigramma nella collezione di essere scelto anche se non è apparso nella collezione, rendendo il tutto più flessibile.
2. $\mathcal{P}(X|W) ?$ Si applica sempre il noisy channel, ma generalizzato a livello di frase.

Consideriamo il seguente esempio: 
$$
\begin{align}
\texttt{a stellar and versatile } \textbf{acress}  \\
\texttt{ whose combination od sass and glamour...}
\end{align}
$$
E calcoliamo la probabilità della parola più plausibile all'interno della frase tra `actress` e `across`.
$$\mathcal{P}(\text{actress | versatile}) = .000021 \cdot \mathcal{P}(\text{whose | actress}) = .0010$$
$$\mathcal{P}(\text{across | versatile}) = .000021 \cdot \mathcal{P}(\text{whose | across}) = .000006$$
Ottenendo infine
$$\mathcal{P}(\text{versatile actress whose}) = .000021 \cdot .0010 = 210 \cdot 10^{-10}$$
$$\mathcal{P}(\text{versatile across whose}) = .000021 \cdot .000006 = 1 \cdot 10^{-10}$$
Mostrando quindi analiticamente che la parola `actress` è quella più probabile.

Da questo esempio inoltre, osserviamo che le probabilità che si ottengono sono molto basse, arrivando ad ottenere numeri minuscoli. Ciò è problematico a livello pratico in quanto può portare i computer ad andare in overflow e non riuscire a rappresentarli. Di conseguenza si preferisce effettuare una trasformazione logartimica di tale probabilità, ottenendo 
$$\log \mathcal{P}(W) = \log \mathcal{P}(w_1) + \sum_{i = 2}^n \log \mathcal{P}(w_i | w_{i-1})$$
Un'ulteriore trasformazione che si applica è quella di specificare che $w_1$ è la prima parola di una frase, introducendo un simbolo speciale $<s>$ dovendo quindi ora calcolare $\mathcal{P}(w_1 | <s>)$. Tuttavia nel caso di query di ricerca non è mai detto che la prima parola sia effettivamente la prima parola di una frase, di conseguenza ha senso trattare $w_1$ come un unigramma.

### Algoritmo di Viterbi

In realtà, il processo per trovare la miglior parola si può modellare come una **Hidden Markov Chain**, la quale è formata da due strati:
1. **Hidden State**: quello che l'utente voleva scrivere, che non sono visibili ma che vogliamo indovinare.
2. **Observable State**: quello che l'utente ha scritto ossia la query.

Per trovare quindi la sequenza di parole più probabile, abbiamo visto che il modello usa due probabilità fontamentli:

1. **Probabilità di Transizione** $\mathcal{P}(w_i | w_{i-1})$: Ossia quanto è probabile che $w_i$ segue $w_{i-1}$, e questo segue dal contesto della frase.
2. **Probabilità di Emissione** $\mathcal{P(x_i | w_i)}$: Quanto è probabile di aver voluto scrivere $w_i$ e invece ho scritto $x_i$? 

![[IR_Spell_HMC.png]]

Come possiamo vedere dall'immagine, data una sequenza di unigrammi, dovremmo calcolare tutte le possibili combinazioni, e da esse tirar fuori la miglior in assoluto. Ovviamente questo ha un costo esponenziale, e per fare ciò in maniera più efficiente si utilizza **l'algoritmo di Viterbi**, che permette di trovare il cammino più probabile attraverso questo grafo senza dover calcolare tutte le combinazioni possibili.

Rimane un'ultima probabilità che non abbiamo discusso, ossia la **probabilità che non ci sia nessun errore** $\mathcal{P}(w | w)$.
- Nel caso dei non-word errors, dal momento che la parola viene identificata in quanto non presente dal dizionario, il sistema suppone dall'inizio che la parola sia sbagliata, quindi l'impatto di tale probabilità è minimo. 
- Nel caso invece di real-word errors, dal momento che le parole osservate sono tutte valide, si deve prendere in considerazione la possibilità che la parola osservata sia effettivamente corretta. Tale probabilità di solito viene stimata empiricamente e dipende molto dall'applicazione specifica. Una stima potrebbe essere la frequenza con cui la parola $w$ è stata digitata correttamente dagli utenti. Tale probabilità è importante per la *usability* del sistema: il modello **deve preferire non correggere se non è sufficientemente sicuro**.

### State of Art Noisy Channel

Nella realtà, le parole candidati sono calcolate nel seguente modo $$\hat{w} = \arg \max_{w \in V} \mathcal{P}(x | w)\mathcal{P}(w)^\lambda$$
dove il paramatro $\lambda$ è un peso calcolato in modo empirico mediante un test set scegliendo poi quello che massimizza la performance. Intuitivamente, all'aumentare di $\lambda$ si da più peso alla lingua (quindi alla probabilità che la parola appaia nella collezione), mentre se $\lambda$ è piccolo allora si da maggiore peso al channel model e quindi alla probabilitò di errori.