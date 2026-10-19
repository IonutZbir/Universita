Siano $A,B$ due **insiemi**.
Il **coefficente di Jaccard** è definito come $$J(A,B) = \frac{\vert A \cap B \vert}{\vert A \cup B \vert}$$
Il coefficiente di Jaccard restituisce sempre un numero compreso tra 0 ed 1, perciò possiamo usarlo come funzione di ordinamento per il risultato della nostra query.

Infatti abbiamo che:
- $J(A,B) = 0 \implies$ sono totalmente differenti.
- $J(A,B) = 1 \implies$ sono uguali.

Se poniamo $A = \text{query}$ e $B = \text{document}$, possiamo misurare la "*rilevanza*" del documento $B$ rispetto alla query $A$.

```ad-important
La misura di *Jaccard* non è una **metrica**, in quanto non vale che:
- $J(A,A) = 0$
- $J(A,B) = J(A,X) + J(X,B)$ (**disugagliaza triangolare**)

Abbiamo come proprietà solo la **simmetria**.
Non possiamo quindi definire una **spazio metrico**.
```

Per esempio se consideriamo la query `idles of march` e il documento `caesar died in march`, l'unico termine in comune è `march` e il numero di termini disting è 6, quindi la Jaccard Similarity vale 1/6.

### Problematiche
Questo coefficiente purtroppo non tiene conto della **frequenza** in cui i termini appaiono in un documento: tiene solo conto di quali termini della query appaiono nel documento.

Generalmente la frequenza di un documento in un documento è una sorta di **indice di rilevanza** del documento.

> **Esempio**
> Abbiamo due documenti $D_1$ e $D_2$.
> La query è $B = \{ \texttt{ termX } \}$.
> Supponiamo che il termine `termX` sia presente in entrambi i documenti, con frequenze relativamente $3$ volte e $88$ volte.
> Se la dimensione è la stessa, allora avremo che $$J(B,D_1) = J(B,D_2)$$ anche se in teoria il documento $D_2$ è più significativo.

Un altro problema è la **dimensione** del documento.
Infatti più un documento è grande, più esso verrà **penalizato** nello scoring. Infatti se consideriamo la query `car climate` e due documenti
- $D_1$: `car climate`
- $D_2$: `car climate change anc its impact on the enviroment`
La Jaccard Similarity tra query e $D_1$ è 1, mentre tra query e $D_2$ è 2/9, nonostante in $D_2$ ci siano tutti i termini della query.

Un accorgimento è quindi quello di normalizzare per la **radice** dell'unione degli insiemi, così da penalizzare un po' meno i documenti grandi.

$$J'(A,B) = \frac{\vert A \cap B \vert}{\sqrt{\vert A \cup B \vert}}$$
