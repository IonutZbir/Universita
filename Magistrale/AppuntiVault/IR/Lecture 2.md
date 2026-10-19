---
date: 2022-10-12
draft: true
---

## Classic Search model
Data una **query** che soddisfa le **information need** di un utente, un **search engine** accede ad una **collection** di documenti e genera un **risultato**.
In base al risultato, se non soddisfa a pieno le **information need** allora parte un porcesso di **query refinement**, e così via finché non si soddisfa il task.

![](img/IR_02_1.png)

### How good are the retrieved documents?
È necessario nel mondo reale **misurare** la qualità di un sistema di IR.
- **Precision**: la frazione di documenti (del risultato) che soddisfano la infromation need. $$\frac{\# \text{ documenti buoni restituiti}}{\# \text{ documenti restituiti}} = \frac{\# \texttt{ treu positive}}{\# \texttt{ treu}}$$
- **Recall** la capacità del sistema di recuperare informazioni rilevanti. $$\frac{\# \text{ documenti buoni restituiti}}{\# \text{ documenti buoni esistenti}} = \frac{\# \texttt{ treu positive}}{\# \texttt{ positive}}$$

1. `true` = pagine restituite.
2. `positive` = pagine *rilevanti*.

```ad-warning
Aumentare la **recall** è facile, perché basta aumentare il numero di documenti restituiti.
Però questo va a scapito della **precision**.
```

### Esempio Shekspier
[esempio slides - grep]
> **Brutus** AND **Cesar** BUT NOT **Calpurnia**.

^1ec961

# Term-Document incidence matrices
Definisco una matrice $m \times n$ dove sulle righe ho i **termini** e nelle colonne i **documenti**.

Ci sta un 1 in cella $(i,j)$ se c'è il termine $i$ in colonna $j$.

Perciò, per trovare i documenti nell'espressione [[#^1ec961|precedente]], faccio prima l'**AND logico** tra tutte le colonne, trovando dove sta l'1 in riga `Brutus` e `Cesar`.
Infine posso fare il **NOT logico** e vedere dove sta 1 sulla riga `Calpurnia`.

## Bigger Collection
Purtroppo la matrice risultante può essere **eccessivamente grande** per poter **scalare bene**.

- Mediamente 1000 parole per documento.
- Mediamente parole lunghe 6, con un byte per char.
	- Perciò ogni documento pesa 6 MB
- Diciamo che ci sono $M = 500.000$ termini **distinti** tra questi documenti.
- Supponiamo di avere $1$ **milione** di dicumenti.
- Perciò avremo una matrice grande circa $500.000 \times 1.000.000$.

Però di questi 1 (**empiricamente**) sono **MOLTO** di meno degli 0 (all'incirca un solo miliardo).
Perciò possiamo usare una **implementazione sparsa**.

## Inverted index
Per ogni termine $t$ ci basta salvare la lista dei **soli** documenti che contengono il termine $t$.
Identifichiamo questi documenti con dei **puntatori**, o **docID**.

In pratica abiamo una **lista di trabbocco**.

**Brutus** -> \[ 1 | 2 | 4 | 11 | ... \]
**Cesar** ->  \[ 1 | 2 | 4 | 5 | ... \]
**Calpurnia** ->  \[ 1 | 2 | 4 | 5 | ... \]

```ad-important
Per il momento usiamo **array di lughezza fissa**, perché stiamo assumendo che la [[1 - Introduzione#^da9c63|collezione è statica]], quindi non aggiungo altri documenti.
```

Assumiamo inoltre gli array ordinati.

```julia
inverted_index = Dict{String, Vector{DocID}}()
```

```ad-warning
Rimuovere le **stop word** non è sempre buono.
Se rimuovo il termine `da` e cerchiamo `Leonardo Da Vinci`, potrebbero essere restituite pagine che parlano di Leonardo delle Tartarughe Ninja.
```

## Stages
1. **Tokenizzazione**
2. **Normalizzazione**
3. **Stemming** (o **Lemmizzazione**)
4. **Stop Word**

----
Per trovare le pagine che contengono `Brutus` lo faccio in tempo **logaritmico** nel numero di termini, perché assumo che la collezione è statica e i termini sono ordinati.

Per trovare l'intersezione tra `Brutus` e `Cesar`  prendo le due liste inerenti e faccio il **merge**.
Se gli indici non fossero ordinati ci metteremmo tempo **quadratico**.
Ma per fortuna abbiamo assunto che anche gli indici sono ordinati, perciò si può fare intempo **lineare** nella lunghezza delle due sequenze di indici.