## Language Models per il Ranked Retrieval

---

## 1. Motivazione e contesto

Nei modelli visti finora (TF-IDF, BM25) il ranking è costruito assegnando esplicitamente un peso ai termini e sommando i contributi. I **Language Models per IR** adottano un punto di vista radicalmente diverso, di natura **generativa**:

> Invece di chiedersi _"quanto è rilevante il documento per la query?"_, ci si chiede _"quanto è probabile che questo documento abbia generato la query?"_

Formalmente, per ogni documento $d$ si stima un modello linguistico $M_d$ e si ordinano i documenti secondo la **query likelihood**:

$$ P(q \mid M_d) $$

Il documento che, secondo il proprio modello linguistico, assegna la probabilità più alta alla query viene restituito per primo.

---

## 2. Modello matematico

### 2.1 Modello unigramma

Nella sua forma più semplice si usa un modello **unigramma**: i termini della query sono considerati indipendenti, e la probabilità della query è il prodotto delle probabilità dei singoli termini:

$$ P(q \mid M_d) = \prod_{t \in q} P(t \mid M_d) $$

Per evitare underflow numerico si lavora in log-spazio:

$$ \log P(q \mid M_d) = \sum_{t \in q} \log P(t \mid M_d) $$

Il documento con log-likelihood più alta vince il ranking.

### 2.2 Stima di massima verosimiglianza

La stima più naturale di $P(t \mid M_d)$ è la **Maximum Likelihood Estimation (MLE)**:

$$ P_{\text{MLE}}(t \mid M_d) = \frac{tf_{t,d}}{L_d} $$

dove $tf_{t,d}$ è la frequenza del termine $t$ nel documento $d$ e $L_d$ è la sua lunghezza. Questa stima è intuitiva ma presenta un problema critico.

### 2.3 Il problema dello zero

Se un termine della query non compare nel documento, allora:

$$ P_{\text{MLE}}(t \mid M_d) = \frac{0}{L_d} = 0 $$

e di conseguenza:

$$ P(q \mid M_d) = \prod_{t \in q} P(t \mid M_d) = 0 $$

**Un solo termine assente azzera l'intero score**, anche se il documento contiene tutti gli altri termini della query. Questo rende la MLE inutilizzabile nella pratica: è necessario lo **smoothing**.

---

## 3. Vantaggi dei Language Models

**Fondamento probabilistico rigoroso** — il ranking emerge direttamente da una probabilità ben definita, con una semantica chiara: la verosimiglianza che il documento abbia generato la query.

**Gestione naturale della query likelihood** — sommare log-probabilità è computazionalmente stabile e interpretabile: ogni termine contribuisce in modo additivo e indipendente.

**Effetto IDF implicito** — non esiste un termine IDF esplicito come in BM25, ma lo smoothing introduce implicitamente un effetto analogo: i termini rari nella collezione producono un guadagno maggiore quando compaiono nel documento (si veda la sezione 4.3).

**Flessibilità** — il framework si estende facilmente a modelli di ordine superiore (bigrammi, trigrammi), a query espanse, o a modelli neurali.

---

## 4. Smoothing

L'idea comune a tutte le tecniche di smoothing è **interpolare il modello del documento con un modello di background della collezione** $P(t \mid C)$, stimato come:

$$ P(t \mid C) = \frac{cf_t}{\sum_{t'} cf_{t'}} $$

dove $cf_t$ è la collection frequency del termine $t$.

Questo garantisce che nessun termine abbia probabilità zero: anche se $t$ non compare in $d$, la sua probabilità nel background è positiva.

---

### 4.1 Laplace Smoothing (Add-one)

La tecnica più semplice aggiunge 1 a ogni conteggio, distribuendo una piccola massa di probabilità uniformemente su tutto il vocabolario $V$:

$$ P_{\text{Laplace}}(t \mid M_d) = \frac{tf_{t,d} + 1}{L_d + |V|} $$

**Vantaggi**: semplice, garantisce probabilità positive per ogni termine.

**Svantaggi**: aggiungere 1 indiscriminatamente è una scelta arbitraria che può distorcere molto le probabilità, specialmente su vocabolari grandi. Non tiene conto della frequenza del termine nella collezione.

---

### 4.2 Jelinek-Mercer Smoothing

Interpola linearmente il modello del documento con il modello della collezione tramite un parametro fisso $\lambda \in (0, 1)$:

$$ P_{\text{JM}}(t \mid M_d) = (1 - \lambda) \cdot P_{\text{MLE}}(t \mid M_d)

- \lambda \cdot P(t \mid C) $$

$$ = (1 - \lambda) \cdot \frac{tf_{t,d}}{L_d} + \lambda \cdot \frac{cf_t}{\sum_{t'} cf_{t'}} $$

**Vantaggi**: intuitivo, facile da implementare. Con $\lambda$ grande si dà più peso al background (utile per query lunghe); con $\lambda$ piccolo si privilegia il documento (utile per query corte).

**Svantaggi**: $\lambda$ è fisso per tutti i documenti, indipendentemente dalla loro lunghezza. Un documento molto corto e uno molto lungo ricevono lo stesso grado di smoothing, il che non è sempre ottimale.

---

### 4.3 Dirichlet Smoothing

Deriva da una prior bayesiana di Dirichlet sul modello del documento. Aggiunge un numero $\mu \cdot P(t \mid C)$ di pseudo-conteggi proporzionale alla frequenza del termine nella collezione:

$$ P_{\text{Dir}}(t \mid M_d) = \frac{tf_{t,d} + \mu \cdot P(t \mid C)}{L_d + \mu} $$

Il parametro $\mu > 0$ controlla la forza dello smoothing.

**Proprietà chiave — adattività alla lunghezza**: per documenti lunghi ($L_d \gg \mu$) il denominatore è dominato da $L_d$ e il modello si fida del documento; per documenti corti ($L_d \ll \mu$) il denominatore è dominato da $\mu$ e il modello si fida di più della collezione. Lo smoothing è quindi **automaticamente più forte sui documenti corti**.

**Effetto IDF implicito**: riscrivendo la formula si può mostrare che un termine raro nella collezione (basso $P(t \mid C)$) produce un guadagno maggiore quando compare nel documento rispetto a un termine comune. Questo riproduce l'intuizione dell'IDF senza introdurlo esplicitamente.

**Valori tipici**: $\mu \in [500, 2000]$.

---

### 4.4 Confronto tra i tre metodi

|Laplace|Jelinek-Mercer|Dirichlet|
|---|---|---|---|
|Parametro|nessuno (add-1)|$\lambda \in (0,1)$|$\mu > 0$|
|Background|uniforme|$P(t \mid C)$|$P(t \mid C)$|
|Adattivo alla lunghezza|No|No|**Sì**|
|Effetto IDF implicito|No|Parziale|**Sì**|
|Uso pratico|Raro|Query lunghe|Query brevi/web|

---

## 5. Esercizio numerico

### Collezione e query

Siano dati tre documenti (già preprocessati):

> **$d_1$**: "cat eat fish" **$d_2$**: "dog eat meat" **$d_3$**: "cat play garden"

**Query** $q$: "cat eat"

Token della query: $q = [\texttt{cat},\ \texttt{eat}]$

---

### Statistiche della collezione ($N = 3$)

**Lunghezze dei documenti**:

$$L_{d_1} = 3, \quad L_{d_2} = 3, \quad L_{d_3} = 3$$

**Collection frequency** $cf_t$ (conteggio totale nella collezione):

|Termine|$d_1$|$d_2$|$d_3$|$cf_t$|
|---|---|---|---|---|
|`cat`|1|0|1|2|
|`eat`|1|1|0|2|
|`fish`|1|0|0|1|
|`dog`|0|1|0|1|
|`meat`|0|1|0|1|
|`play`|0|0|1|1|
|`garden`|0|0|1|1|
|**Totale**||||**9**|

**Probabilità di background** $P(t \mid C) = \dfrac{cf_t}{9}$:

$$P(\texttt{cat} \mid C) = \frac{2}{9}, \qquad P(\texttt{eat} \mid C) = \frac{2}{9}$$

**Parametro**: $\mu = 3$

---

### Calcolo di $P_{\text{Dir}}(t \mid M_d)$

La formula applicata è:

$$ P_{\text{Dir}}(t \mid M_d) = \frac{tf_{t,d} + \mu \cdot P(t \mid C)}{L_d + \mu} = \frac{tf_{t,d} + 3 \cdot \frac{cf_t}{9}}{L_d + 3} = \frac{tf_{t,d} + \frac{cf_t}{3}}{L_d + 3} $$

Poiché tutti i documenti hanno $L_d = 3$, il denominatore è sempre $3 + 3 = 6$.

---

#### Documento $d_1$ — "cat eat fish"

$$ P_{\text{Dir}}(\texttt{cat} \mid M_{d_1}) = \frac{1 + \frac{2}{3}}{6} = \frac{\frac{5}{3}}{6} = \frac{5}{18} $$

$$ P_{\text{Dir}}(\texttt{eat} \mid M_{d_1}) = \frac{1 + \frac{2}{3}}{6} = \frac{\frac{5}{3}}{6} = \frac{5}{18} $$

$$ \log P(q \mid M_{d_1}) = \log\frac{5}{18} + \log\frac{5}{18} = 2\log\frac{5}{18} $$

---

#### Documento $d_2$ — "dog eat meat"

$$ P_{\text{Dir}}(\texttt{cat} \mid M_{d_2}) = \frac{0 + \frac{2}{3}}{6} = \frac{\frac{2}{3}}{6} = \frac{2}{18} = \frac{1}{9} $$

$$ P_{\text{Dir}}(\texttt{eat} \mid M_{d_2}) = \frac{1 + \frac{2}{3}}{6} = \frac{\frac{5}{3}}{6} = \frac{5}{18} $$

$$ \log P(q \mid M_{d_2}) = \log\frac{1}{9} + \log\frac{5}{18} = \log\frac{5}{162} $$

---

#### Documento $d_3$ — "cat play garden"

$$ P_{\text{Dir}}(\texttt{cat} \mid M_{d_3}) = \frac{1 + \frac{2}{3}}{6} = \frac{\frac{5}{3}}{6} = \frac{5}{18} $$

$$ P_{\text{Dir}}(\texttt{eat} \mid M_{d_3}) = \frac{0 + \frac{2}{3}}{6} = \frac{\frac{2}{3}}{6} = \frac{1}{9} $$

$$ \log P(q \mid M_{d_3}) = \log\frac{5}{18} + \log\frac{1}{9} = \log\frac{5}{162} $$

---

### Ranking finale

|Posizione|Documento|Score (log-likelihood)|
|:-:|---|:-:|
|**1°**|$d_1$|$2\log\dfrac{5}{18}$|
|**2°**|$d_2$|$\log\dfrac{5}{162}$|
|**2°**|$d_3$|$\log\dfrac{5}{162}$|

Numericamente, usando logaritmo naturale:

$$2\log\frac{5}{18} = 2 \times (-1.281) \approx -2.563$$

$$\log\frac{5}{162} = \log 5 - \log 162 \approx 1.609 - 5.088 \approx -3.476$$

Poiché $-2.563 > -3.476$, il ranking è:

$$d_1 \succ d_2 = d_3$$

---

### Interpretazione

**$d_1$ è primo** perché è l'unico documento che contiene **entrambi** i termini della query: `cat` e `eat` compaiono ciascuno con $tf = 1$, il che produce la probabilità smoothed più alta per entrambi i termini.

**$d_2$ e $d_3$ sono a pari merito**: ciascuno contiene uno solo dei due termini della query. Lo smoothing di Dirichlet assegna a entrambi una probabilità di background $\frac{1}{9}$ per il termine assente, e una probabilità smoothed $\frac{5}{18}$ per il termine presente. Il prodotto è identico, quindi i due documenti risultano indistinguibili rispetto a questa query.

**Ruolo di $\mu$**: con $\mu = 3$ lo smoothing è moderato. Aumentando $\mu$ le probabilità di tutti i documenti convergerebbero verso il background $P(t \mid C)$, riducendo le differenze tra i documenti e rendendo il ranking meno discriminativo.
