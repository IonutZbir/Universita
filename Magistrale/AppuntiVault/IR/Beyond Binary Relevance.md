Le metriche viste in [[Rank-Based Measures]] erano tutte metriche basate su un concetto **binario** di rilevanza: si teneva in considerazione se un termine era rilevante o meno.
Più precisamente abbiamo visto misure basate solamente sulla [[Set Based Measures|precision e recall]].

Per molte applicazioni reali, in particolare per il web, per un utente è più importante che ci siano buoni risultati sulla **prima pagina**, anziché sulle prime 3 o 10.
Infatti nella realtà esistono varie sfumature di rilevanza, spesso associate alla semantica della query.

-----
## DCG - Discounted Cumulative Gain

Il **DCG** (**Discounted Cumulative Gain**) è una misura molto importante nella valutazione di sistemi di IR per il web.

L'idea è che gli utenti sono generalmente **pigri**, e che quindi faranno uno **sforzo** maggiore nell'andare a usufruire di documenti che sono infondo alla prima pagina (o peggio ancora nella seconda).
Infatti generalmente se un utente non trova ciò che gli interessa tra i primi 3 o 4 documenti del risultato, rinuncia alla ricerca e assume che non c'è ciò che gli serve.

Perciò è ragionevole assumere che:
1. i documenti più **rilevanti** sono i più **utili** all'utente.
2. più un documento rilevante è posto in basso alla classifica, meno sarà utile (in quanto l'utente potrebbe non arrivare oltre i primi 3 o 4).

Perciò, mentre prima nel [[Evaluation of IR systems#^f2d730|gold standard]] avevamo una **rilevanza booleana**, adesso abbiamo una valutazione continua in un intervallo $\left[ 0, r \right]$, con $r > 2$.

Un primo approccio (banale) è quello di valutare la qualità di una query in maniera **cumulativa** rispetto all'utilità dei primi $n$ documenti ritornati dal mio sistema.
Siano quindi $r_1, ..., r_n$ i valori di utilità dei miei primi $n$ documenti ritornati dopo una query.
Definiamo quindi il **guadagno cumulativo** (o **Cumulative Gain** o **CG**) la somma $$CG@n = r_1 + ... +r_n$$

Dato che abbiamo detto che più un documento è in fondo al rank e minore sarà la sua utilità, possiamo **scalare** il contributo dei documenti rispetto alla loro posizione nel rank.
Definiamo quindi il **guadano cumulativo scontato** (o **Discounted Cumulative Gai** o **DCG**) come $$DCG@n = r_1 + \frac{r_2}{\log_2{2}} + \frac{r_3}{\log_2{3}} + ... + \frac{r_n}{\log_2{n}} = r_1 + \sum_{i = 2}^{n}\frac{r_i}{\log_2{i}}$$

```ad-info
Un'altra formula usata da alcuni motori di ricerca è la seguente $$DCG = \sum_{i=1}^{n} \frac{2^{r_i} - 1}{\log_2{(i+1)}}$$
```

L'idea è che ogni posizione viene "scontata": per la posizione 1 non c'è sconto (è il primo risultato restituito, se era un documento rilevante ha senso lasciare il punteggio pieno), per la posizione 2 si divide per $\log_2(2) = 1$ quindi anche qui non c'è nessun sconto, per la posizione 3 si divide per $\log_2(3) \approx 1.58$ (quindi che se era un documento molto rilevante, poichè si trova più in basso nel ranking, il suo contributo è minore).

In questo modo pià si scende nel ranking, meno vale il contributo dei documenti restituiti, anche se sono rilevanti. La somma cumulativa ci permette di dire quanto valore totale otteniamo dal ranking restituito per quella query.

**Problema**: *da solo non è confrontabile tra query diverse*. Supponiamo di avere un sistema di IR ottimale, ossia che per ogni query restituisci tutte i documenti rilevanti.
- Se una query ha molti documenti rilevanti, allora il DCG è molto alto. 
- Se una query ha pochi documenti rilevanti, allora il DCG ha basso valore.
In realtà, quello che vorremmo è che anche nel secondo caso, il DCG sia alto, in quanto il sistema ha restituito correttamente tutti i docuementi rilevandi alla query, anche se non sono tanti. 

Per risolvere questo problema, si dve normalizzare il DCG rispetto alla query, introducendo quindi **NDCG**

$$NDCG@n = \frac{DCG@n}{IDCG@n}$$
dove $IDCG@n$ è il $DCG$ calcolato fino all'$n$-esima query nel ranking *ideale*, che è quello in cui i documenti sono ordinati in maniera decrescente in base al loro grado di rilevanza (prima quelli con rilevanza $r$, poi quelli con rilevanza $r-1$, etc...)

In quest modo, se il sistema restituisce un ranking vicino a quello ideale, $NDCG@n$ sarà alto, mentre se il sistema restituisce un ranking molto diverso da quello ideale, sarà basso.

---

## MRR - Mean Reciprocal Rank

Immagiamo ora uno scenario dove l'utente è interessato a trovare **un solo documento rilevante** per soddisfare il suo bisogno informativo, quindi tale che esiste **solo un documento rilevante per ogni query**.

Ad esempio: 
- *known-item search*: quando si cerca un documento specifico, come un libro.
- *navigation query*: quando si cerca un sito web specifico.
- *looking for a fact*: quando si cerca una risposta per una sola domanda.

In questo caso non ci interessa trovare tanti documenti rilevanti, ma **vedere quanto in alto appare il documento utile**. In questo senso la metrica più usata è il **Mean Reciprocal Rank**.

Si definisce Reciprocal Rank per una specifica query come
$$RR = \frac{1}{K}$$
dove $K$ è la posizione in cui si trova il primo documento rilevante. Dopodiché si fa semplicemente la media su $Q$ query,
$$MRR = \frac{1}{Q}\sum_{q = 1}^{Q}\frac{1}{K_q}$$

## Valutazione con Comportamento Utenti

Abbiamo visto che la valutazione con giudizi di rilevanza umana, per determinare il Gold Standard è:
- **Molto Costosa**
- **Inconsistente**
- **Obsoleta**
- **Poco Realisitica**

Per migliorare l'etichettamento, l'idea potrebbe essere quindi di **utilizzare direttamente gli utenti** per ottenere/aggiornare i giudizi di rilevanza.

In questo senso l'intuizione più semplice è quella di utilizzare i **click degli utenti**: se data una query un risultato viene cliccato molte volte tra i vari utenti, probabilmente è più rilevante rispetto ad altri risultati restituiti per quella query.

**Problema - Positional Bias**: Si è verificato *empiricamente* che gli *utenti tendono a clicare maggiormente sui primi risultati ottenuti, indipendentemente dalla loro reale rilevanza*. Questo è dovuto al fatto che molti utenti danno per scontato che il sistema di IR funzioni correttamente.

Oltre a questo, i click sono anche **Title Biased, Snippet Biased** e dipende anche da fattori esterni, ad esempio gli abitudini dell'utente.

Per via del bias non è possibile quindi, dato un raking di risultati $$r_{1}, r_{2}, \dots, r_{n}$$
poter dire che $r_{1}$ è rilevante, $r_{2}$ non lo è, etc... . Non posso assegnare un labeling ai risultati sfruttando in modo diretto i clicks degli utenti.

Ciò che possiamo invece definire sono dei *confronti relativi*. Se L'utente clicca su $r_{1}$, è più plausibile dire che $r_{1} > r_{3}$ invece che dire $r_{3} > r_{1}$. Ovviamente questo vale a livello locale, ma non globale della query.

### Come Confrontare due Ranking?

Si usa la tecnica dell'**interleaving**. Dati due ranking $A$ e $B$, si mescolano creando un'unico ranking, *alternando i risultati* rimuovendo poi i duplicati. Siano $$A = [d_{1}, d_{2}, d_{3}] \qquad B = [d_{3}, d_{4}, d_{5}]$$
$$\implies R = [d_{1}, d_{3}, d_{2}, d_{4}, d_{5}]$$
Non ha importanza se si parte da $A$ o da $B$. Si fa ciò per ridurre il bias il più possibile. Una volta ottenuta la lista $R$, si contano i clicks degli utenti su di essa e si confrontano i click sui risultati di $A$ e su di $B$. **Se A ottiene più click di B, allora probabilmente A è migliore di B**.

I motori di ricerca attuali usano tipicamente la tecnica **A/B testing** per verificare se un aggiornamento del sistema migliora le performance rispetto alla versione precedente. In questo caso si sceglie una piccola porzione degli utenti per usare la nuova versione, mentre il resto la vecchia. Dopodiché si raccolgono le statistiche per capire se la nuova versione si adatta.