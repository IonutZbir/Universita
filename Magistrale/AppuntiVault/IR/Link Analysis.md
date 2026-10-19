Ci   interessa ora analizzare come sono collegate le pagine web tra loro. Sappiamo che nel web, una pagina è una risorsa memorizzata all'interno di un server. Ciascuna risorsa è identificata medinante una URL (Uniform Resource Locator), banalmente chiamati `link`.

Ognuno di questi link contiene un' **ancora** che è un testo che descrive la pagina a cui si punta. Intuitivamente una pagina molto linkata potrebbe essere considerata più importante di una pagina isolata.

La distribuzione dei link non è uniforme e segue una distribuzione potenza **Power Law**, per cui pochissime pagine sono molto linkate, mentre moltissime pagine sono poco linkate. Questo porta ad un problema di SPAM.

Per quanto riguardo il modo dell'IR, le applicazioni principali della Link Analysis sono:
- **Scoring e Ranking**: i link posso aiutare a decidere quali documenti mostrare prima nei risultati di ricerca.
- **Link-based Clustering**: i link posso essere usati per individuare comunità tematiche.
- **Crawling**: i link possono essere usati per scoprire nuove pagine da indicizzare. I cosidetti *crawler* che navigano il web.

## Formalizzazione Problema

Si formalizza il web come un grafo diretto, dove i nodi rappresentano le pagine e gli archi rappresentano gli hyperlink tra le pagine.

Inoltre, diremo che
- Un Hyperlink conferisce autorità, se presente in una pagina reputata autorevole.
- L'anchor text descrive la pagina di destinazione.

Come usare l'anchor text? Quando un documento $D$ viene indicizzato all'interno dell'inverted index, oltre a memorizzare il contenuto di $D$, si memorizza anche l'anchor text relativo ai link che puntano a $D$. In questo modo è possibile recuperare $D$ anche con query che non contengono solo parole in $D$. Inoltre, è buona pratica memorizzare anche il testo intorno all'anchor text.

**Problema**: Per *spam* e *miserable failure* si fa riferimento al fenomento per cui alcune pagine possono usare anchor text fallaci verso una pagina per far si che motori di ricerca siano portati a restituire quella pagina anche per query che non c'entrano nulla. Per ovviare a questo problema si da un peso all'anchor text in base all'autorità della pagina.

## Compressione dei Link

Il **Connectivity Server** è un sistema che memorizza il grafo del web in modo efficiente permettendo di fare query rapide legate alla connettività delle pagine.

Il grande problema del grafo del web è la sua dimensione. Di conseguenza, per memorizzarlo servono delle tecniche di compressione che permettano di memorizzarlo.

Si usa la compressione di **Boldi** e **Vigna**, che permette di rappresentare il grafo del web arrivando a circa 3 bit per link. L'idea è quella di ordinare lessicograficamente tutti gli URL in e sfruttare il fatto che URL vicini hanno spesso liste di adiacenza simili. Si sfruttano diverse proprietà del web per comprimere le liste, tra cui:

- **Similarità tra liste**: Pagine simili o vicine nello stesso sito spesso hanno link simili: 
```python
www.univ.it/informatica/corsi
www.univ.it/informatica/docenti
www.univ.it/informatica/esami
```
Tutte queste pagine probabilmente hanno link comuni, quindi l'idea è invece di memorizzare ogni link da 0, memorizzarne una come riferimento e rappresentare le altre come differenze rispetto a quella.
- A causa dell'ordinamento lessicografico, le pagine dello stesso sito hanno ID numerici molto vicini. Dato che la maggior parte dei link di una pagina punta a pagine dello stesso sito (link interni), gli ID destinazione saranno numericamente vicini all'ID sorgente. Invece di memorizzare gli ID assoluti a 32 o 64 bit, l'algoritmo ordina i link uscenti di un nodo e ne memorizza solo gli **gap**.
## PageRank

L'idea di PageRank è la seguente: immaginiamo un utente, detto **random surfer**, che naviga casualmente nel web, nel seguente modo: parte da una pagina *u.a.r.*, guarda i link uscenti presenti nella pagia e ne sceglie uno *u.a.r.*, passa alla pagina e continua questo processo all'infinito.

**Domanda**: Dopo moltissimi passi, quale pagina visiterà più spesso il random surfer? Le pagine visitate più spesso saranno quelle con PageRank più alto.

La misura che usa PageRank è la seguente: data una pagina, tiene conto sia dei link che puntano a quella pagina, sia dei link a cui punta la pagina.

Inoltre, poiché ci sono pagine che non puntano ad altre pagine, se il random surfer vi finisce vi rimane (*dead ends*). Nasce perciò l'idea di *teleporting*: ad ogni istante il random surfer ha alta probabilità di eguire uno dei link uscenti e bassa probabilità di passare ad una pagina completamente a caso (*teletrasporto*).
### PageRank come Catene Di Markov

È possibile modellare PageRank mediante un processo stocastico - le Catene di Markov. Sono un modello matematico che descrivono un processo stocastico in cui una v.a. passa da uno stato a un altro con una certa probabilità, che dipende solo dallo stato attuale.

Nel nostro caso, gli stati sono le pagini web, e la scelta di un link rappresenta la transizione da uno stato a un altro. Il comportamento della catena è descritto mediante la **matrice di transizione** $\mathbf{P}$, dove
$$
\begin{align}
P_{ij} = P(X_{t} = j | X_{t-1} = i)
\end{align}
$$
ossia è la probabilità che la catena passi dallo stato $i$ allo stato $j$. Poiché la matrice è $n \times n$, ogni colonna $j$ rappresenta uno stato mentre ogni riga rappresenta la probabilità di passare dalla pagina $j$ a tutte le pagine $i$.  

#### Probabilità di Teleporting

Per inserire il teleporting nella matrice $\mathbf{P}$ si fa quanto segue: Se ci sono $n$ pagine ed $\alpha$ è la probabilità di teleporting, allora la probabilità di saltare verso una pagina specifica è $\frac{\alpha}{n}$, mentre la probabilità di seguire un link uscente è $1 - \alpha$. Ora, mediante il seguente calcolo matriciale si distribuisce la probabilità su tutti i link uscenti: $$\mathbf{P}' = (1 - \alpha)\mathbf{P} + \frac{\alpha}{n}\mathbf{E}$$dove $\mathbf{E}$ è una matrice $n \times n$ in cui ogni cella è 1.

#### Catena Ergodica

Diremo che una catena di Markov è **ergodica** se è aperiodica ed irriducibile. Se una catena è ergodica e ha un numedo di stati finiti, allora esiste una distribuzione stabile (**stazionaria**) di probabilità sulle pagine per il random surfer, indipendentemente dal punto di partenza.

Sia $\bar{\pi} = [\pi_{1}, \pi_{2}, \dots, \pi_{n}]$ la distribuzione stazionaria. Consideriamo ora una distribuzione iniziale $\mathbf{x}$, allora
$$\mathbf{x}^{(k)} = \mathbf{x}\mathbf{P}^k$$
e se prendiamo il limite $k \to \infty$ $$\lim_{ k \to \infty } \mathbf{x}\mathbf{P}^k = \bar{\pi}$$
per la quale vale $$\bar{\pi}\mathbf{P} = \bar{\pi}$$
A quel punto, la probabilità che il random surfer si trovi su una data pagina, a quel punto, resta la stessa indipendentemente da quanti passi fa.

Nel contesto di PageRank, $\pi_{i}$ rappresenta proprio il **PageRank della pagina** $i$, quindi le pagine con valore $\pi_{i}$ più alto saranno propri quelle più importanti secondo **PageRank**.

Per risolvere **PageRank**, secondo le catene di Markov, basta risolvere il sistema di $n+1$ equazioni 
$$
\begin{cases}
\bar{\pi}\mathbf{P} &= \bar{\pi}  \\
\sum_{i = 1}^{n} \pi_{i} &= 1
\end{cases}
$$
In pratica si usa un algoritmo iterativo detto **Power Iteration**.
## HITS

Quando un utente effettua una ricerca su un argomento molto ampio (una query _broad-topic_), spesso non esiste una singola "pagina migliore" in assoluto. L'algoritmo **HITS** risolve questo problema catalogando il web in due tipologie di pagine distinte, ma strettamente connesse tra loro:

- **Authorities (Le Fonti Autorevoli):** Pagine che contengono contenuti di altissima qualità, dati concreti e informazioni definitive sull'argomento (ad esempio, il sito ufficiale di un software o un articolo scientifico).
    
- **Hubs (I Collezionisti di Link):** Pagine che non contengono necessariamente informazioni originali, ma fungono da eccellenti guide o cataloghi, raccogliendo e organizzando i migliori link che puntano verso le fonti autorevoli (ad esempio, un blog post che elenca "i 10 migliori strumenti per programmatori")

La vera forza di HITS sta nel fatto che queste due pagine si auto-definiscono: un buon _Hub_ è una pagina che punta a molte _Authority_; una buona _Authority_ è una pagina puntata da molti _Hub_

La differenza più grande tra HITS e PageRank è che PageRank, nella versione standard è del tutto **query-independent**: si misura l'importanza di una pagina a prescindere dalla query dell'utente. Al controario HITS è **query-dependent** dal momento che parte da una query testuale, costruisce un sottoinsieme di pagine rilevanti per quella query e poi calcola hub e authorities dentro quel sottografo.

In particolare HITS funziona bene per **broad topic queries**, ossia query ampie a livello di argomento. Al contrario se la query è troppo specifica, il metodo è poco efficiente.


### Algoritmo e Convergenza

HITS funziona in due fasi:

1. **Costruzione di un insieme di pagine candidate (base set)**;
	Quanto un utente fa una query, vengono recuperate un insieme di pagine, **root set**. A questo punto il root set viene espanso nel seguente modo: $$\text{base set = root set + in-links + out-links}$$
2. **Calcolo iterativo dei punteggi hub e authority**. Ad ogni pagina si assegnano i seguenti punteggi: $$\begin{align}
h(x) &= \text{hub score della pagina } x \\
a(x) &= \text{authority score della pagina } x
\end{align}$$
Inzialmente entrambi a 1. Iterativamente, si calcolano nel seguente modo:
$$
h(x) = \sum_{y: x \to y} a(y), \qquad a(x) = \sum_{y: y \to x} h(y)
$$
Dopo ogni iterazione è fondamentale normalizzare i punteggi, ad esempio dividendo ogni elemto per la norma del vettore $$h(x) = \frac{h(x)}{\sqrt{ \sum_{x} h(x)^2 }}$$
Per dimostrare la convergenza di questo metodo, si passa ad una notazione matriciale. Infatti, possiamo scrivere le relazioni precedenti come $$\mathbf{h} = \mathbf{A}\mathbf{a}, \qquad \mathbf{a} = \mathbf{A}^T\mathbf{h}$$
Dove $\mathbf{A}$ è la matrice di adiacenza del grafo. Osserviamo una relazione ricorsiva, infatti
$$
\begin{align}
\mathbf{h} &= A \mathbf{a} = A (A^T \mathbf{h}) = (A A^T) \mathbf{h}  \\
\mathbf{a} &= A^T \mathbf{h} = A^T (A \mathbf{a}) = (A^T A) \mathbf{a}
\end{align}
$$
Quindi HITS sta iterativamente calcolando, con normalizzazione ad ogni passo, l'autovettore principale di $AA^T$ per i punteggi hub e l'autovettore principale $A^TA$ per i punteggi authority.

### Limiti

- **Topic Drift**: avviene quando l'algoritmo si allontana dal topic originale. Ad esempio potrei partire da una query specifica, ma espandendo il root set con link entranti e uscenti potrei finire in una zona del grafo con argomento più generale o addirittura diverso.
- **Mutually Reinforcing Affiliates**: se un gruppo di pagine appartenenti alla stessa organizzazione si linka molto internamente, può aumentare artificialmente i punteggi di hub e authorities.