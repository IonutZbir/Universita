
# L'Indicizzazione Dinamica nei Sistemi di IR

Nei modelli teorici di Information Retrieval si assume spesso che la collezione di documenti sia **statica** (o che cambi molto raramente). Nella realtà (es. motori di ricerca web, piattaforme social, database aziendali), le collezioni sono **altamente dinamiche**: nuovi documenti vengono inseriti continuamente, altri vengono modificati o eliminati.

Ciò comporta la necessità di aggiornare l'**indice invertito** (aggiungendo nuovi termini al vocabolario o modificando le _posting lists_ esistenti) senza interrompere il servizio di ricerca.

Di seguito vengono analizzate le tre strategie principali per affrontare questo problema.

## 1. Trivial Approach - Ricostruzione Periodica

È l'approccio più semplice (o _naïve_). Consiste nel trattare la collezione come temporaneamente statica e **ricostruire l'intero indice da zero** a intervalli di tempo regolari (ad esempio, ogni notte).

- **Vantaggi:** 
	- Estremamente semplice da implementare.
    - Computazionalmente economico nel breve termine se l'indice è piccolo.
    - L'indice finale è perfettamente ottimizzato e memorizzato in un unico file contiguo, garantendo la massima velocità di query.
- **Svantaggi:**
    - **Mancanza di Real-Time:** Un documento inserito subito dopo la ricostruzione notturna non sarà rintracciabile fino al giorno successivo.
    - Non scalabile se la frequenza di aggiornamento richiesta è alta o se la collezione è enorme.

## 2. Main and Auxiliary Index

Per consentire la ricerca immediata dei nuovi documenti, si divide l'indice in due componenti:

1. **Main Index (Indice Principale):** Memorizzato su disco, contiene la stragrande maggioranza dei documenti ed è statico.
2. **Auxiliary Index (Indice Ausiliario):** Mantenuto in memoria RAM, di dimensioni ridotte ($n$). Accoglie tempestivamente tutti i nuovi inserimenti.

### Funzionamento delle Operazioni

- **Ricerca (Query):** Quando arriva una query, il sistema interroga **sia** il Main Index **sia** l'Auxiliary Index. I due insiemi di risultati vengono poi fusi (_merge_) prima di essere restituiti all'utente.
- **Rimozione dei Documenti:** Modificare direttamente il Main Index su disco per rimuovere un documento sarebbe troppo costoso. Si utilizza quindi un **Bit-Vector (Vettore di bit)** di cancellazione. A ogni documento è associato un bit: `0` se il documento è valido, `1` se è stato rimosso. Durante la fase di query, il Bit-Vector funge da filtro: se un documento soddisfa la query ma il suo bit è `1`, viene scartato.
- **Svuotamento:** Quando l'indice ausiliario in memoria si riempie (raggiunge la dimensione limite $n$), viene effettuata una fusione (_merge_) con l'indice principale su disco, svuotando la memoria per i successivi inserimenti.
### Vantaggi e Svantaggi

- **Vantaggi:** Molto più flessibile; permette la ricerca in tempo reale dei nuovi documenti.
- **Svantaggi (Il problema del collo di bottiglia del File System):** Se l'indice principale e quello ausiliario mantenessero le _posting lists_ separate in file distinti per ogni termine (_one-file-per-postings-list_), il merge consisterebbe in una semplice operazione di `append`. Tuttavia, questo genererebbe milioni di file nel File System, portando al collasso del Sistema Operativo (esaurimento degli _inode_ e lentezza di gestione). Per questo motivo, l'indice deve risiedere in **un unico grande file concatenato**. Di conseguenza, ogni volta che l'indice ausiliario si riempie, siamo costretti a **riscrivere l'intero Main Index su disco** per fondervi i nuovi dati. Se gli inserimenti sono frequenti, il sistema passa troppo tempo a fare operazioni di I/O, rallentando drasticamente il tempo di risposta alle query.

## 3. Logarithmic Merge 

Il **Logarithmic Merge** nasce per risolvere il problema dell'eccessivo costo di riscrittura del metodo precedente, ammortizzando i costi di fusione su disco.

### Il Principio di Funzionamento

Invece di avere un solo enorme indice su disco, manteniamo una serie di indici su disco di dimensioni geometricamente crescenti, contrassegnati come $I_0, I_1, I_2, \dots, I_k$.

Ciascun indice $I_i$ ha una dimensione massima pari a $n \cdot 2^i$, dove $n$ è la dimensione dell'indice gestibile in memoria RAM.

La logica segue esattamente il funzionamento del **sistema binario (addizione con riporto)**: ogni slot $I_i$ su disco può essere o "vuoto" o "pieno".

### Algoritmo di Inserimento Passo dopo Passo:

1. I nuovi token/documenti vengono inseriti in un indice temporaneo in memoria chiamato **$Z$**.
2. Quando $|Z| = n$ (l'indice in memoria è pieno), $Z$ deve essere riversato su disco.
3. Il sistema controlla lo slot $I_0$ su disco:
    - **Se $I_0$ è vuoto:** $Z$ viene scritto direttamente in $I_0$. $Z$ si svuota.
    - **Se $I_0$ è pieno:** Significa che sia $Z$ che $I_0$ hanno dimensione $n$. Viene effettuato un _merge_ tra $Z$ e $I_0$, generando un indice temporaneo di dimensione $2n$. A questo punto si controlla lo slot $I_1$:
        - **Se $I_1$ è vuoto:** L'indice combinato di dimensione $2n$ viene scritto in $I_1$. $I_0$ e $Z$ vengono svuotati.
        - **Se $I_1$ è pieno:** Si fonde l'indice temporaneo con $I_1$, ottenendo un indice di dimensione $4n$. Si passa a controllare $I_2$, e così via, propagando il "riporto" fino a trovare uno slot vuoto.

Grazie a questa struttura a cascata, le fusioni grandi avvengono molto raramente, riducendo drasticamente il tempo speso in riscritture complessive.

## 4. Analisi di Complessità: Confronto Formale

Definiamo i parametri:

- $T$: Numero complessivo di _postings_ (coppie termine-documento) da indicizzare nell'intera collezione.
- $n$: Dimensione massima dell'indice ausiliario mantenibile in RAM.
- Il numero totale di svuotamenti della memoria sarà pari a $T/n$.

| **Metodo**                 | **Costo Totale di Costruzione (Tempo di Indicizzazione)** | **Tempo di Risposta alla Query (Caso Peggiore)** |
| -------------------------- | --------------------------------------------------------- | ------------------------------------------------ |
| **Main + Auxiliary Index** | $\Theta\left(\frac{T^2}{n}\right)$                        | $O(1)$                                           |
| **Logarithmic Merge**      | $\Theta\left(T \log \left(\frac{T}{n}\right)\right)$      | $O\left(\log \left(\frac{T}{n}\right)\right)$    |

#### 1. Main + Auxiliary Index

- **Costruzione $\rightarrow \Theta(T^2/n)$:** Ogni volta che la memoria di dimensione $n$ si riempie, dobbiamo fare il merge con il Main Index su disco. Al primo step fondiamo $n$ elementi, al secondo $2n$, al terzo $3n$, fino all'ultimo step che fonderà $T$ elementi. $$
\begin{align}
\text{Costo Totale} &= n + 2n + 3n + \dots + T = n \cdot \sum_{i=1}^{T/n} i  \\
&\approx n \cdot \frac{(T/n)^2}{2} = \Theta\left(\frac{T^2}{n}\right)
\end{align}
$$Questo costo è quadratico rispetto a $T$, rendendolo inefficiente per collezioni molto grandi.  
- **Query $\rightarrow O(1)$:** Dobbiamo interrogare sempre e solo due indici (il Main su disco e l'Auxiliary in RAM), indipendentemente da quanti inserimenti sono avvenuti. Il tempo è costante rispetto al numero di indici.
#### 2. Logarithmic Merge

- **Costruzione $\rightarrow \Theta(T \log(T/n))$:** Pensiamo a quante volte una singola _posting_ viene toccata da un'operazione di merge. Essa nasce in $Z$, poi passa in $I_0$, poi in $I_1$, fino al livello massimo disponibile che è limitato superiormente da $\log_2(T/n)$. Poiché ogni elemento viene spostato/fuso al massimo $\log(T/n)$ volte, il costo complessivo per processare tutti i $T$ elementi è strettamente quasi-lineare.
- **Query $\rightarrow O(\log(T/n))$:** È lo svantaggio di questo metodo. Per rispondere a una query, il motore di ricerca non può limitarsi a guardare un solo file, ma deve interrogare $Z$ e **tutti gli indici attivi su disco** ($I_0, I_1, \dots$), che nel caso peggiore sono pari a $O(\log(T/n))$. Le risposte di ciascun sotto-indice devono poi essere fuse insieme.

## 5. Il Problema delle Statistiche Globali

I motori di ricerca moderni non si limitano a verificare la presenza di una parola, ma calcolano un punteggio di rilevanza (es. il peso **TF-IDF** o **BM25**). Per fare ciò, hanno bisogno di alcune **statistiche globali**, come la _Document Frequency_ ($df_t$): il numero totale di documenti nell'intera collezione che contengono il termine $t$.

Quando l'indice è frammentato in più sotto-indici (come nel Logarithmic Merge), calcolare accuratamente queste statistiche a runtime diventa straordinariamente complesso e dispendioso, poiché richiederebbe il coordinamento sincrono di tutti i sotto-indici.

### Soluzioni nel Mondo Reale

Per ovviare a questo problema, i sistemi industriali adottano un approccio ibrido:

1. **Uso del Main Index per le statistiche:** Si calcolano i pesi TF-IDF basandosi esclusivamente sulle statistiche del Main Index (l'indice più grande su disco), accettando una minima perdita di precisione per i documenti appena inseriti nell'indice ausiliario.
2. **Aggiornamenti Incrementali + Periodic Rebuild in Background:** Il sistema continua a ricevere aggiornamenti in tempo reale tramite indici ausiliari o Logarithmic Merge. Periodicamente, però, un processo a bassa priorità avviato in **background** (mentre il motore principale risponde alle query degli utenti senza alcun _downtime_) ricostruisce l'intero indice da zero. Una volta completato il nuovo indice monolitico e aggiornate le statistiche globali, il sistema effettua uno _switch_ invisibile (puntando al nuovo indice), garantendo statistiche precise e query veloci.

## 6. Caso di Studio: Real-Time Search at Twitter

Il motore di ricerca di una piattaforma come Twitter (X) rappresenta un caso estremo di indicizzazione dinamica: il volume di scritture (tweet pubblicati) e letture (ricerche e feed) è mastodontico e richiede una gestione del tempo reale assoluta.

### Caratteristiche del Modello Twitter

- **La Dimensione Temporale è Sfondata:** Nei tweet il fattore discriminante non è tanto la rilevanza semantica pura del testo, quanto la **recenza**. Un utente che cerca un termine vuole vedere cosa sta succedendo _adesso_, non i tweet più rilevanti di cinque anni fa.
- **Posting Lists con Politica LIFO (Last-In, First-Out):** A differenza dei motori di ricerca classici in cui le posting list sono ordinate per ID documento crescente (per facilitare l'intersezione lineare), Twitter ordina le sue posting list in modo **decrescente per timestamp** (i tweet più recenti sono in testa alla lista).
- **Architettura ad Indici Multipli e Flussi Paralleli:** Data l'esigenza del tempo reale, Twitter mantiene le posting list degli ultimissimi minuti interamente in memoria RAM ad altissima velocità. Quando si effettua una ricerca, il sistema scansiona queste liste LIFO partendo dalla testa (il presente) e tornando indietro nel tempo fino a quando non soddisfa il numero di risultati richiesti.
- **Hashtag come Indici Dedicati:** Gli hashtag agiscono come veri e propri indici invertiti prioritari e separati dal testo normale, consentendo aggregazioni e trend-topic calcolati in tempo reale senza dover scansionare l'intero corpus di testo.