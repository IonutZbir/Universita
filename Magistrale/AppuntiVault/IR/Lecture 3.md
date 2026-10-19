---
date: 2022-10-19
draft: true
---

## Boolean queries: Exact match
Il **boolean retrieval model** consente di effettuare tutte query che siano espreimibili tramite **espressioni booleane**.

Queste query utilizzano operatori logici AND, OR e NOT.

Questo sistema non è molto lontano da una base dati.
È comunque utilizzato in alcuni sistemi come: email, library catalog, macOS Spotlight
- se cerco *parola1 parola2* sul macOS Spotlight trova tutti i documenti che contengono *parola 1 AND parola 2*

Domanda:
> se ho un ssd da 500gb e ne ho riempiti 450gb di documenti, ho abbastanza spazio per costruire l'[[IR/Lecture 2#Inverted index|indice inverso]]?
> Ho abbastanza ram a disposizione ?

Quello che vogliamo noi è un sistema che supporti query:
- lunghe e precise
- con operatori di prossimità
- che si evolvano in maniera **incrementale** (man mano richiedo più cose e costruisco una nuova soluzione da quella precedente)


## Optimization Query
Se chiedo al mio motore tutti i documenti con

> **Brutus** AND **Calpurnia** AND **Caesar**

[img]

Ovviamente hanno complessità differenti le due sequenti implementazioni della query
1. (**Brutus** AND **Calpurnia**) AND **Caesar**
2. **Brutus** AND (**Calpurnia** AND **Caesar**)
3. **Calpurnia** AND (**Brutus** AND **Caesar**)

```
args::Vector{String}

word1 = min(s -> length(s), args)
word2 = min(s -> length(s), args - {word1})
```



L'idea è quella di iniziare a fare l'AND da quelle con **frequenza** (lunghezza delle liste) minori.

Similmente per l'OR si può ottimizzare il processo di *merge*.
Dato che il risultato dell'OR genera una nuova lista con **al più** la somma dei due argomenti.
Perciò, prendiamo la coppia di parole la cui somma di liste è **minima**.

```
args::Vector{String}

word1, word2 = min(t -> length(t[1]) + length(t[2]), args × args)
```


-------
# Phrase queries and positional indexes
Vogliamo rispondere a una query come **"Standfor University"** come una **frase**.

D1: I went to **standford university palo alto**
D2: I love **standford university** but I went to Tor Vergata University **palo alto**

Query: **standford university palo alto** (vorrei solamente D1)

Ma nel [[#Boolean queries: Exact match|modello booleano]] la query è implementato come:

	standford AND university AND palo AND alto

Fatta così, però il motore mi ritorna `<D1, D2>` 

### A first attempt: Biword indexes
Indicizza ogni coppia di **termini consecutivi** di un testo come se fosse un unico **indice**.

La query diventa quindi

	standford university AND university palo AND palo alto

[todo...]
[vedi anche index blowup]

### Solution 2: Positional indexes
Potremmo arricchire la posting list, salvando l'**ordine di parola** in cui occorre

```
<term, number of docs containing term; doc1: position1, position2 ... ;  
doc2: position1, position2 ... ;  
etc.>
```

```
term1 -> {
	1: [3, 45, 56],
	3: [9, 20, 21, 65, 66, 71, 92],
	9: [...]
	...
}
```

Così facendo, per trovare la frase **standford university palo alto** basta trovare i documenti in cui appaiono tutti e 4 i termini (con l'AND) e poi cerco i documenti in cui appaiono in **posizioni consecutive**
$$\langle k, k+1, k+2, k+3 \rangle$$

In termini di **tempo**, nel caso di **termini frequenti**, il costo aumenta tanto.
Però per termini non eccessivamente frequenti, empiricamente non si degradano troppo le prestazioni.

In termini di **spazio** invece, il costo potrebbe risultare eccessivo, soprattutto in presenza di molti termini altamente frequenti.
Bisogna quindi **comprimere** opportunamente tale struttura dati.

Dato che le lingue hanno una **struttura robusta**, empiricamente un **positional index** è circa 2-4 volte più grande di uno non posizionale (*non eccessivamente grande*).

```ad-tldr
Un positional index è $\approx 35\%-50\%$ del documento originale.
Perciò può essere visto come una forma di compressione del documento.
```


```ad-attention
Tutte queste osservazioni sono fate sulla lingua Inglese.
```
