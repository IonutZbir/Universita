**Problema:** Usando VSM, BM25, LM, NON *siamo in grado di catturare la semantica dei documenti, ci limitiamo esclusivamente ad usare approcci del tipo term-match*. 

Questo comporta che, anche se due documenti parlano dello stesso argomento ma usano termini diversi allora il modello li considererà come documenti poco simili tra loro.

Un altro problema in questo senso è legato alle parole *polisemiche*: se una parola ha più significati, il modello classico non è in grado di distiguere bene il contesto.

**Latent Semantic Index** è stato uno dei primi approcci per cercare di superare questi limiti.

## Richiami di Algebra Lineare

Ricordiamo che VSM si basa su una matrice *term $\times$ documents* $A$. LSI si basa su una tecnica di decomposizione di questa matrice, chiamata *Singular Value Decomposition (SVD)*.

### Autovettori e Autovalori

Sia $A$ una matrice $n \times n$. Diremo che $\lambda$ è un autovalore per $\mathbf{v}$ se $$A \mathbf{v} = \lambda \mathbf{v}$$
Se moltiplichiamo la matrice $A$ per il suo autovettore $\mathbf{v}$, il risultato sarà un vettore avente la stessa direzione solo che più lungo/accorciato o cambiato di verso a seconda del suo autovalore $\lambda$.

Se $A$ ha $n$ autovettori linearmente indipendenti, allora questi formano una base in $\mathbb{R}^n$, e qualsiasi vettore $\mathbf{u} \in \mathbb{R}^n$ può essere scritto come combinazione lineare di essi.

Gli autovalori ci dicono quindi quanto **pesa ciascuna direzione**. Più l'autovalore è grande e più la direzione è importante, vicerversa più è piccolo e meno importante è. In altre parole, ci sono direzioni che spiegano tanto mentre altre che spiegano poco. In LSI, quelle che spiegano poco posso essere eliminate senza perdere troppa informazione.

Diremo che la matrice $A$ è simmetrica se e solo se $A = A^T$. Se $A$ è simmetrica, allora:
- Ammette $n$ autovalori reali.
- Ammette una base di autovettori **ortonormale**.
- Possiamo applicare la decomposizione spettrale.

Se inoltre $A$ è **semidefinita positiva**, ossa $\forall \mathbf{w} \in \mathbb{R}^n, \mathbf{w}^TA\mathbf{w} \geq 0$, allora **tutti i suoi autvalori sono non negati**, $\lambda_{i} \geq 0$.

### Eigen/diagonal Decomposition

Sia $A \in \mathbb{R}^n$ una matrice quadrata con $n$ autovalori linearmente indipendenti. Allora è possibile decomporre $A$ com segue: $$A = U \Lambda U^{-1}$$dove le colonne di $U$ sono gli autovettori di $A$ e $\Lambda$ è una matrice diagonale con gli autovalori di $A$ sulla diagonale.

**Proof**: Sia $U$ la matrice avente come colonne gli autovettori di $A$, ossia: $$U = [\mathbf{v_{1}}, \mathbf{v_{2}}, \dots, \mathbf{v_{n}}]$$Allora, possiamo scrivere $AU$ come $$AU = A[\mathbf{v_{1}}, \mathbf{v_{2}}, \dots, \mathbf{v_{n}}] = [\lambda_{1}\mathbf{v_{1}}, \lambda_{2}\mathbf{v_{2}}, \dots, \lambda_{n}\mathbf{v_{n}}] = [\mathbf{v_{1}}, \mathbf{v_{2}}, \dots, \mathbf{v_{n}}]\Lambda = U\Lambda$$Quindi, $$AU = U\Lambda \implies \Lambda = U^{-1}AU \implies A = U\Lambda U^{-1}$$
## Singular Value Decomposition (SVD)

La decomposizione è possibile solo per **matrici quadrate**. In IR, se prendiamo VSM, la matrice termini-documenti in generale è una matrice rettangolare: $A \in \mathbb{R}^{m \times n}$, dove $m$ è il numero di termini ed $n$ è il numero di documenti. Per questo motivo, per decomporrere questa matrice utilizziamo una tecnica più generale, chiamata **SVD**, che ci permette di decomporre $A$ come segue: $$A = U \Sigma V^T$$dove, 
- $U \in \mathbb{R}^{m \times m}$ è una matrice contenente come colonne gli autovettori di $A A^T$. Tale matrice è simmetrica ($(AA^T)^T = AA^T$), di conseguenza ammette una base di ortonormale di autovettori.
- $V \in \mathbb{R}^{n \times n}$ è una matrice contenente come colonne gli autovettori di $A^TA$. Anche questa matrice è simmetrica, quindi i suoi autovettori sono ortonormali.
- $\Sigma \in \mathbb{R}^{m \times n}$ è una matrice che contiene i valori singolari di $A$, ossia $\sigma_{i} = \sqrt{ \lambda_{i} }$ lungo la diagonale, dove $\lambda_{i}$ è l'$i$-esimo autovalore di $AA^T$ oppure di $A^TA$.

**Cosa sono $\mathbf{U, V, \Sigma}?$

- $U = AA^T$: **rappresenta la relazione termine-termine**. Misura quanto i termini sono collegati tra loro attraverso i documenti. Due termini saranno collegati se compaiono in documenti simili. Intuitivamente $U$ contiene tutti autovettori che rappresentano le direzioni importanti nello spazio dei termini, più precisamente **direzioni latenti nello spazio dei termini**, ossia direzioni che rappresentano un pattern di associazione tra termini diversi.
- $V = A^TA$: **rappresenta la relazione documento-documento**. Misura quanto i documenti sono simili tra loro in base ai termini che contengono. Due documenti saranno collegati se contengono termini simili o pattern simili di termini.
- $\Sigma$: I valori singolari di rappresentano l'importanza di ogni direzione latente: più è grande un valore singolare, più la direzione latente associata è importante per rappresentare le relazioni nei dati. I valori singolari sono ordinati in modo non crescente sulla diagonale di $\Sigma$: $$\sigma_{1} \geq \sigma_{2} \geq \dots \geq \sigma_{r} > 0$$dove $r = \text{rank}(A)$, ossia il numero di dimensioni indipendenti della matrice, e quindi il numero di valori singolari non nulli. L'ordinamento è importante **affinché sappiamo che le dimensioni più importanti sono quelle associate ai primi valori singolari**. Vedremo che sarà possibile ridurre la dimensione mantenendo solo i primi $k$ valori singolari più grandi.

Con **SVD** non abbiamo cambiato la matrice $A$, ma l'abbiamo solo riscritta come prodotto di 3 matrici.

### Low Rank Approximation

Dopo aver visto che è possibile scomporrere la matrice $A$ con SVD, ci chiediamo se è possibile **sostituire** $A$ con una matrice $A_{k}$ di rango $k$, che **sia quanto più vicina ad** $A$.

Vogliamo fare questo perchè la matrice $A$ è troppo grande e troppo rumorosa e sparsa. Le proprietà che deve soddisfare $A_{k}$ sono:
- deve conservare le strutture importanti
- eliminare il rumore inutile
- $k < n$
$$A_{k} = \text{argmin}_{r(X) = k} \lvert A - X \rvert_{F} $$ossia stiamo cercando, tra tutte le matrici $X$ di rango $k$, quella più vicina ad $A$ in termini di **norma di Frobenius** $$\lvert A \rvert_{F} = \sqrt{ \sum_{i}^{m}\sum_{i}^{n} a_{ij}^2 } $$
A questo punto, otteniamo $A_{k}$ applicando la tecnina di **Low-Rank Approximation**: sapendo di aver ordinato in ordine non crescente i valori singolari di $A$ nella matrice $\Sigma$, per ottenere $A_{k}$ manteniamo solo i primi $k$ **valori singolari più grandi, e azzerare il resto**:
$$A_{k} = U \text{ diag}(\sigma_{1}, \sigma_{2}, \dots, \sigma_{k}, 0, \dots, 0)\ V^T$$
ossia
$$A_{k} = \sum_{i}^{k}\sigma_{i}\mathbf{u_{i}}\mathbf{v_{i}}^T$$
ricordando che $\mathbf{u_{i}}$ è l'$i$-esimo autovettore di $AA^T$ e $\mathbf{v_{i}}$ è l'$i$-esimo autovettore di $A^TA$.

il termine $\sigma_{i}\mathbf{u_{i}}\mathbf{v_{i}}$ è una matrice di rango 1 che rappresenta una direzione latente nello spazio dei termini e dei documenti, e il peso di questa direzione è dato dal valore singolare di $\sigma_i$.

Inoltre questa matrice è **ottimale** nella norma di Frobenius.

Ovviamente, al crescere di $k$ l'errore di approssimazione diminuisce: più valori singolari mantengo, più $A_{k}$ si avvicina ad $A$.

## Latent Semantic Indexing

Vediamo ora come usare $A_{k}$ per effettuare IR.

- Nella matrice $A$, ogni documento era una riga (50000 termini $\to$ vettori di dimensione 50000).
- Nella matrice $A$, i documenti vivono in uno spazio ridotto $k$, come ad esempio 200/300. Ognuna delle dimensioni di questo spazio **non sono gli assi originali**. Mentre in VSM classico ogni asse è un termine, in LSI ognuna delle $k$ dimensioni è detta **dimensione latente*** e rappresenta un pattern di associazione tra i termini.

Ad esempio, se consideriamo i termini `laptop, software, display, computer`, questi vivono in una dimensione latente che potremmo chiamare `informatica`.

Introdurre LSI in VSM ci permette di risovere due grandi problemi:
- **Polisemia:** parole che hanno più significato (`Saturn` come pianeta e `Saturn` come negozio di elettrocasnici).
- **Sinonimia:** parole diverse con lo stesso significato (`macchina` e `automobile`. Se un documento parla di `macchina` e un'altro di `automobile` e non hanno parole in comune, per VSM sono documenti diversi).

**LSI cerca di risolvere questi problemi costruendo uno spazio in cui i termini simili e documenti simili finiscono tutti vicini, seguendo la stessa direzione latente**.

### LSI in pratica

1. Si parte dalla matrice dei termini $A \in \mathbb{R}^{m \times n}$ e si applica **SVD** per decomporla in $A = U \Sigma V^T$.
2. Si applica il **low rank approximation** per ottenere $A_{k} = U_{k} \Sigma_{k}V_{k}^T$, dove $U_{k}$ sono i primi $k$ autovettori di $AA^T$, $\Sigma_{k}$ sono i primi $k$ valori singolari, e $V_{k}$ contiene i primi $k$ autovettori di $A^TA$.

Quindi $A_k$ non rappresenta esattamente lo spazio latente, ma la matrice termini-documenti approssimata utilizzandolo (infatti, lo spazio latente ha dimensione $k$, mentre $A_{k}$ ha dimensione $m \times n$).

In particolare:
- i documenti nello spazio latente sono tipicamente rappresentati da $$D_{k} = \Sigma_{k}V_{k}^T$$dove ogni colonna è un documento rappresentata nello spazio latente di $k$ dimensioni. Si moltiplica per $\Sigma_{k}$ per scalare le dimensioni latenti in base alla loro importanza.
- i temini nello spazio latente sono tipicamente rappresentati da $$T_{k} = U_{k}\Sigma_{k}$$dove ogni riga è un termine rappresentato nello spazio latente di $k$ dimensioni.

##### Come calcolare la similarità tra due documenti $\mathbf{d_{i}}$ e $\mathbf{d_{j}}$ nello spazio latente?

Riprendiamo la misura di similarità classica, la *cosine similarity*: $$\text{sim}(\mathbf{d_{i}}, \mathbf{d_{j}}) = \frac{\mathbf{d_{i}}^T \mathbf{d_{j}}}{||\mathbf{d_{i}} ||\ ||\mathbf{d_{j}}|| }$$
##### Come proiettare una query nello spazio latente, per poterla confrontare con i documenti?

Poiche il vocabolario ha $m$ termini, allora $\mathbf{q} \in \mathbb{R}^m$ è la rappresentazione della query nello spazio originale. Per proiettarla si applicano le seguenti due formule equivalenti: $$\mathbf{q}_{k}^T = \mathbf{q}^TU_{k}\Sigma_{k}^{-1} \qquad \mathbf{q}_{k} = \Sigma_{k}^{-1}U_{k}\mathbf{q}$$
A questo punto, per trovare il ranking, basta calcolare la similarità tra $\mathbf{q}_{k}$ e tutti i documenti in $D_{k}$. Abbiamo visto però che ci sono metodi che ci permettono di evitare di calcolare la similità per tutti i documenti ([[Efficient Scoring]]).

In generale con LSI si ha un **miglioramente delle recall**, in quanto riesce a recuperere anche quei documenti che sono correlati semanticamente tra loro, mantendo la precisione sopra la mediana TREC (standard di riferimento per IR).

![[IR_lsi.png]]

Supponiamo l'utente cerchi $q=$`automobile`. LSI cerca nello spazio latente i termini più simili ad `automobile`, che sono `macchina, veicolo, motore` ed espande la query usando questi temini aggiuntivi.

### Limiti di LSI

I principali problemi di LSI sono:

- **Negazioni:** LSI non è in grado di gestire frasi negate, ad esempio: `documenti su jaguar ma non la macchina`. Questo perché LSI lavora con similarità vettoriale e associazioni semantiche, non è in grado di gestire vincoli logici come il `NOT`.
- **Query Booleane:** Ovviamente questo modello non è pensato per rispondere a query rigide, ad esempio `jaguar AND lion`, ma ritornerà anche documenti correlati semanticamente.
- **Peggiormanto Precision:** LSI migliora la recall ma può peggiorare la precision, restituendo documenti che sono semanticamente correlati ma non rilevanti per la query.

**Osservazioni**

- C'è un legame con l'idea di clustering, ossia raggrupare termini correlati semanticamente.
- LSI gestisce i termini polisemici proiettandoli nello spazio latente puntanto parzialmente verso tutte le dimensioni latenti che rappresentano i vari significati del termine.
- LSI e SVD sono tecniche usate in situazioni in cui si ha a che fare con una matrice **features $\times$ objects**.
- $A_{k}$ diventa una matrice densa (il contrario di $A$, la quale è una matrice sparsa), quindi non posso più utilizzare una rappresentazione sparsa per memorizzarla. Ma, per LSI in realtà non ci interessa memorizzare $A_{k}$, ma conoscere solo i documenti e termini nello spazio latente, quindi è **sufficiente la decomposizione e l'approssimazione senza dovere memorizzare $A_{k}$**.
- È possibile calcolare i primi $k$ autovettori e valori singolari di $A$ usando algoritmi iterativi senza dover usare SVD.

## Query Expansion & LSI

LSI è lo spazio latente possono essere sfruttati per fare **query expansion**. Possiamo usare lo spazio latente per creare il thesaurus da cui poi prendere i termini per fare espandere la query.

Inoltre per **garantire una buona usability si deve comunque dare fiducia all'utente e ai termini precisi che decide di usare nella query**. Inoltre, i termini aggiunti *dovrebbero avere un peso minore rispetto a quelli originali nel calcolo dello score*.

Parlando invece di efficienza, usare LSI come l'abbiamo descritto prevede il calcolo della similarità confrontando tutti i documenti $k$-dimensionali con la query proiettata nello spazio latente, che risulta poco efficiente se consideriamo l'intera collezione. Si usa spesso la seguente strategia a due fasi:

1. **Candidate generation**: si usa un indice inverso tradizionale per recuperare un insieme di documenti candidati [[Efficient Scoring]]. In questa fase si può applicare anche la query expansion in modo da ottenere più documenti rilevanti possibili.
2. **Re-Ranking**: si applica LSI su questo insieme di candidati per calcolare la similarità e ottenere il ranking finale.