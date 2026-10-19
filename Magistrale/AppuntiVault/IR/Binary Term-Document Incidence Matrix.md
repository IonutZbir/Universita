Supponiamo di avere una grande collezione con tutte le opere di Shakespeare.
Supponiamo di voler identificare quali opere contengono le parole
- *Brutus* **AND** *Caesar*
- **NOT** *Calpurnia*

Un primo approccio è quello di leggere tutti i documenti, **selezionando** quelli che contengono le parole *Brutus* e *Caesar* e **scartando** quelli che contengono *Calpurnia*.
Questa alla fine è una sorta di **scansione lineare** tra i documenti, ritornando i soli documenti che rispettano l'**espressione logica** desiderata.
Questo processo è noto come **grep** dei documenti.

Finché siamo in un solo computer di un utente, il comando `grep` va più che bene.
Invece, su sistemi con un'enorme quantità di dati (come il *web*), si richiede di più:
1. Processare un'enorme quantità **molto** velocemente (<u>frazione di secondi</u>). E purtroppo sul web un approccio lineare come il *grepping* indurrebbe risultati disastrosi.
2. La possibilità di avere operazioni più sofisticate. Per esempio abbiamo l'espressione "*Romans* **NEAR** *countrymen*" dove l'operatore **NEAR** può significare "*entro 5 parole*" oppure "*nella stessa frase*". Questo operatore è impraticabile con il grepping.
3. Ottenere un **ranking** del risultato della query, in base alla "*significatibilità*" dei documenti rispetto a quanto richiesto.

Un primo modo per evitare uno **scanning lineare** dei documenti è quello di **indicizzare** a priori ogni documento.
Per ogni documento a disposizione identifichiamo l'inseme di tutte le parole, o **termini**.
Costruiamo poi una matrice $M \times N$ dove ad ogni riga è associato un termine, e ad ogni colonna un documento.
In tale matrice, poniamo la cella $(i,j)$ pari a $1$ se il termine $i$-esimo è contenuto nel documento $j$-esimo, $0$ altrimenti.
Questa è detta **matrice d'incidenza**.

\\ | **Antony and Cleopatra** | **Julius Caesar** | **The Tempest** | **Hamlet** | **Othello** | **Macbeth** | ...
---|---|---|---|---|---|---|---
**Antony** | 1 | 1 | 0 | 0 | 0 | 1 | ...
**Brutus** | 1 | 1 | 0 | 1 | 0 | 0 | ...
**Caesar** | 1 | 1 | 0 | 1 | 1 | 1 | ...
**Calpurnia** | 0 | 1 | 0 | 0 | 0 | 0 | ...
**Cleopatra** | 1 | 0 | 0 | 0 | 0 | 0 | ...
**mercy** | 1 | 0 | 1 | 1 | 1 | 1 | ...
**worser** | 1 | 0 | 1 | 1 | 1 | 0 | ...
... | ... | ... | ... | ... | ... | ... | ...

Perciò, per ottenere i documenti che rispettano l'espressione $$\text{Brutus } AND \text{ Caesar } AND \; NOT \text{ Calpurnia}$$ basta prendere la riga **indicizzata** dai termini `Brutus` e `Caesar`, poi prendere la riga indicizzata da `Calpurnia` ma **complementata**, per poi fare il **bitwise AND**
$$\begin{align}
&&110100\\
\land &&110111\\
\land &&101111\\
\hline
= &&100100
\end{align}$$
Alla fine i documenti interessati saranno quelli per i quali il relativo bit è pari ad 1, nel nostro caso i documenti `Antony and Cleopatra` e `Hamlet`.

Questo approccio è detto **Boolean retrieval model**.
In tale modello le query sono della forma di **espressioni booleane di termini**, dove i termini sono combinati tramite gli **opeartori logici** `AND`, `OR` e `NOT`.

```julia
M::BitMatrix

brutus, caesar, calpurnia = M[2,:], M[3,:], M[4,:]

return brutus .& caesar .& (.! calpurnia) 
```

## Efficienza - Tempo
L'applicazione di un **operatore** booleano è **lineare** nel numero $N$ di documenti.
La risoluzione di una espressione ha quindi una complessità di $O(kN)$, dove $k$ è il numero di operatori nella query.

Per quanto riguarda invece la ricerca delle righe necessarie per la query è lineare nel numero di termini $M$.
Perciò abbiamo una complessità di $O(kN + kM)$.

Tale complessità non è per niente ragionevole, in quanto $M$ può crescere a dismisura.

Perciò si può pensare di **ordinare** i termini in fase di costruzione della matrice d'incidenza.
I tal caso si può effettuare una **ricerca dicotomica** sui termini, ottenendo una complessità di $O(kN + k\log{M})$ (decisamente più ragionevole).

## Efficienza - Spazio
Purtroppo in termini di **spazio** tale struttura dati non è praticabile.
Infatti per larghe collezioni di documenti la matrice quasi sicuramente potrebbe non entrare in RAM, mentre per piccole collezioni conviene fare il *grepping*.
Infatti, supponiamo di avere $N = 500K$ documenti ed $M = 1M$ di termini.
Se per ogni cella abbiamo bisogno di un bit, avremo una matrice grande $NM = 500,000,000,000$ di bit, ovvero $62,500,000,000B \approx 58GB$.
