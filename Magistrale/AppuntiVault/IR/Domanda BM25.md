
## BM25: Modello Probabilistico per il Ranked Retrieval

---

## 1. Motivazione e contesto

Il modello vettoriale con TF-IDF e cosine similarity interpreta il retrieval come un problema geometrico: documenti e query sono vettori, e la rilevanza corrisponde alla loro vicinanza angolare. Sebbene efficace, questo approccio presenta alcune limitazioni fondamentali:

- la term frequency cresce in modo **lineare**: passare da 1 a 2 occorrenze di un termine ha lo stesso effetto di passare da 100 a 101, il che non è realistico;
- la normalizzazione con la norma L2 non tiene conto in modo esplicito della **lunghezza** del documento come fonte di distorsione.

BM25 (_Best Match 25_), derivato dal modello probabilistico  nasce per rispondere a queste critiche introducendo una gestione più controllata della frequenza dei termini e della lunghezza dei documenti.

---

## 2. Modello matematico

BM25 deriva da un framework probabilistico. Si considera la rilevanza di un documento rispetto una query come una v.a. bernoulliana. 
$$
R_{d,q} = 
\begin{cases}
1 \iff d \text{ is relevant for } q \\
0 \text{ otherwise}
\end{cases}
$$
Lo scopo a questo punto è ordinare i documenti per gli odds dell'evento $R = 1 |d,q$
$$
O(R = 1 | d,q) = \frac{P(R=1 | d,q)}{P(\bar{R}=1 | d,q)}
$$

Si parte dalla formula di Bayes
$$
P(R = 1 | d,q) = \frac{P(d | R, q)P(R|q)}{P(d|q)} \propto P(d|R,q)
$$

Assumendo che:
- $P(d|q) = P(d)$ ed è uniforme e indipendente per tutti i documenti.
- $P(R|q)$ è costante.

Quindi, la probabilità che un documento $d$ sia rilevante rispetto alla query $q$ la possiamo vedere come la probabilità di osservare un documento $d$ dall'insieme dei documenti rilevanti $R$ per la query $q$.

Stimando questa probabilità, il primo modello che si ottiene è il *Binary Indipendent Model BIM*.
$$\text{BIM}_{d,q} = \sum_{t \in q \land d} IDF(t)$$
Modellando i documenti nello stesso modo di VSM, quello che si ottiene è un modello simile al modello VSM con pesatura TF-IDF. Il problema di questo modello è che non tiene conto della lunghezza dei documenti e della term frequency.

Il modello usato nella pratica, che risolve questi problemi è BM25.
Lo score BM25 di un documento $d$ rispetto a una query $q$ è definito come:

$$ \text{BM25}(d, q) = \sum_{t ,\in, q^*} \text{IDF}(t) \cdot \frac{(k_1 + 1) \cdot tf_{t,d}}{k_1 \left[(1 - b) + b,\dfrac{L_d}{\bar{L}}\right] + tf_{t,d}} $$

dove $q^*$ indica l'insieme dei **termini distinti** della query.

### 2.1 Componente IDF

$$ \text{IDF}(t) = \log\left(\frac{N}{df_t}\right) $$

|Simbolo|Significato|
|---|---|
|$N$|numero totale di documenti nella collezione|
|$df_t$|numero di documenti in cui il termine $t$ compare almeno una volta|
Assegna peso elevato ai termini rari e peso basso ai termini ubiqui.

### 2.2 Componente TF saturante

$$ \text{TF-saturation}(t, d) = \frac{(k_1 + 1), tf_{t,d}}{k_1 \cdot B_d + tf_{t,d}} $$

dove il fattore di normalizzazione della lunghezza è:

$$ B_d = (1 - b) + b,\frac{L_d}{\bar{L}} $$

|Simbolo|Significato|
|---|---|
|$tf_{t,d}$|frequenza del termine $t$ nel documento $d$|
|$L_d$|lunghezza del documento $d$ (numero di token)|
|$\bar{L}$|lunghezza media dei documenti nella collezione|
|$k_1$|parametro di saturazione della term frequency|
|$b$|parametro di normalizzazione per lunghezza|

---

## 3. Interpretazione degli iperparametri

### Parametro $k_1$ — saturazione della TF

Il parametro $k_1 \geq 0$ controlla **quanto velocemente il contributo di un termine satura** all'aumentare delle sue occorrenze.

Per un documento di lunghezza media ($B_d = 1$), il fattore TF vale:

$$ \frac{(k_1 + 1), tf}{k_1 + tf} $$

- quando $tf \to \infty$, il fattore si avvicina asintoticamente a $(k_1 + 1)$: le occorrenze aggiuntive smettono di contribuire;
- con $k_1 = 0$, il modello conta solo la **presenza** del termine (binario);
- con $k_1$ grande, le ripetizioni contano di più a lungo (saturazione lenta);
- valori tipici: $k_1 \in [1.2,\ 2.0]$.

**Intuizione**: la prima occorrenza di un termine è molto informativa; la centesima aggiunge pochissima evidenza aggiuntiva.

### Parametro $b$ — normalizzazione per lunghezza

Il parametro $b \in [0, 1]$ controlla **quanto la lunghezza del documento penalizza i termini frequenti**.

- $b = 0$: nessuna normalizzazione; i documenti lunghi non sono penalizzati;
- $b = 1$: normalizzazione completa; un termine contribuisce in proporzione alla densità con cui appare nel documento, non alla sua frequenza assoluta;
- valore tipico: $b = 0.75$.

**Intuizione**: un documento di 1000 parole che contiene un termine 10 volte non è necessariamente più rilevante di uno di 100 parole che lo contiene 2 volte. BM25 corregge questa disparità attraverso $B_d$.

---

## 4. Vantaggi di BM25

**Saturazione della TF** — a differenza del TF-IDF grezzo, BM25 evita che documenti con molte ripetizioni vengano sopravvalutati. Il guadagno marginale di ogni occorrenza aggiuntiva decresce.

**Normalizzazione della lunghezza controllata** — la lunghezza del documento viene considerata in modo esplicito e modulabile, senza affidarsi alla sola norma L2 della cosine similarity.

**Robustezza dei parametri** — con i valori standard ($k_1 \approx 1.5$, $b \approx 0.75$) BM25 produce risultati competitivi su molte collezioni senza necessità di tuning; ciò ne ha favorito la diffusione come _strong baseline_ per il first-stage retrieval.

**Motivazione probabilistica** — la formula è derivata dal _Probabilistic Relevance Framework_, il che fornisce una giustificazione teorica coerente al modello di scoring.

---
## Esercizio Numerico

Consideriamo due documenti $d_{1}$ e $d_{2}$ e la query $q$
- $d_{1}$ = `image compression reduces file size`
- $d_{2}$ = `image format and image storage`
- $q$ = `image file`

Calcoliamo BM25($d_{1}, q$) e BM25($d_{2}, q$). Iniziamo con computare le statistiche necessarie.

### Statistiche

**Frequenze dei termini** ($tf_{t,d}$):

| Termine | $d_1$ | $d_2$ |
| ------- | ----- | ----- |
| `image` | 1     | 2     |
| `file`  | 1     | 0     |
  
**Lunghezze**: $L_{d_1} = 5$, $L_{d_2} = 5$, quindi $\bar{L} = 5$.
**Document frequency** su $N = 2$ documenti:

| Termine | $df_t$ |
| ------- | ------ |
| `image` | 2      |
| `file`  | 1      |
Come parametri, $k_{1} = 1.5 = \frac{3}{2}$ e $b = 0.75 = \frac{3}{4}$.

### IDF**
$$
\begin{align}
\text{IDF}(t) &= \log \frac{N}{df_{t}} \\
\text{IDF}(\texttt{image}) &= \log\left(\frac{2}{2}\right) = \log(1) = 0 \\
\text{IDF}(\texttt{file}) &= \log\left(\frac{2}{1}\right) = \log 2
\end{align}
$$
**Nota importante**: `image` compare in entrambi i documenti ($df = N$), quindi il suo IDF è esattamente zero e non contribuisce allo score. Solo `file` è discriminante.

**Calcolo $B_{d_{1}}$ e $B_{d_{2}}$

Poiché $L_{d_1} = L_{d_2} = \bar{L} = 5$, i due documenti hanno la stessa lunghezza media, quindi:
$$B_{d_1} = B_{d_2} = (1 - 0.75) + 0.75 \cdot \frac{5}{5} = \frac{1}{4} + \frac{3}{4} = 1$$
### Calcolo degli score BM25

$B_{d_1} = B_{d_2} = 1$ come prima (le lunghezze non cambiano).
#### Score di $d_1$
**Contributo di** `image` ($tf = 1$):
$$0 \cdot \frac{2.5 \cdot 1}{1.5 + 1} = 0$$
**Contributo di** `file` ($tf = 1$):
$$\log 2 \cdot \frac{2.5 \cdot 1}{1.5 + 1} = \log 2 \cdot \frac{2.5}{2.5} = \log 2 \cdot 1$$
$$\boxed{\text{BM25}(d_1, q) = \log 2 \approx 0.693}$$
#### Score di $d_2$
**Contributo di** `image` ($tf = 2$):
$$0 \cdot \frac{2.5 \cdot 2}{1.5 + 2} = 0$$

**Contributo di** `file` ($tf = 0$): termine assente, contributo $= 0$.
$$\boxed{\text{BM25}(d_2, q) = 0}$$
### Ranking finale

| Posizione | Documento |       Score BM25       |
| :-------: | --------- | :--------------------: |
|  **1°**   | $d_1$     | $\log 2 \approx 0.693$ |
|   **—**   | $d_2$     |          $0$           |

**Interpretazione**: con questa formula IDF, `image` — presente in tutti i documenti — vale zero e sparisce completamente dal calcolo. $d_2$ riceve score nullo perché l'unico termine discriminante della query, `file`, non vi compare. Il ranking è interamente determinato da `file`, il termine raro.