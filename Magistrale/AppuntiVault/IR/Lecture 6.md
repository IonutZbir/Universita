---
date: 2022-11-02
draft: true
---

# Index Compression
Spesso può capitare che anche gli indici sono troppo grandi, perciò è vantaggioso cercare di comprimere i documenti.

Mentre la codifica di **Huffman** è **general purpose**, sono stati definiti algoritmi di compressione estremamente specifici ed ottimizzati per gli indici.

Quello che vogliamo inoltre è che la **decompressione** deve essere il più veloce possibile, possibilmente *gratuita*.
Questo perché ci sono principalmente operazioni di **query** al mio indice, perciò un numero elevato di operazioni in lettura.

[TABELLA DELLE DIMENSIONI DEGLI INDICI]

## Vocabulary size vs Collection Size

### Heaps' Law
Data una collezione di documenti, si vuole stimare la dimensione del dizionario.
- $M$ la dimensione del vocabolario.
- $T$ il numero di token nella mia collezione.

> **Heaps' Law**
> $$M \approx k T^b$$
> dove $30 \leq k \leq 100$ e $b \approx .5$.

Se facciamo il grafico **log-log** otteniamo una retta di pendenza $\approx 0.5$
$$\log{M} \approx \log{k} + b \log{T}$$

```ad-success
Infatti, al crescere dei miei documenti la dimensione non tende ad *"esplodere"*.
Infatti ci si aspetta che man mano che processo documenti, incontrerò termini già incontrati in precedenza, e che quindi eseguiamo sempre meno operazioni d'inserimento.
```


### Zipfs' Law
Si vuole stimare la frequenza dei termini che appaiono nel nostro corpus.

> **Zipfs' Law**
> L'$i$-esimo termine più frequenza ha frequenza proprozionale a $i^{-1}$.

Ovvero la frequenza dei termini segue una **powerlaw**, ovvero come un'inversa di un polinomio.

Sia $cf_i$ la frequanza della parola $i$-esima, e $K$ un **fattore di normalizzazione** tale che $$cf_i = \frac{K}{i}$$

Perciò, se abbiamo dato $cf_1$, avremo che
- $cf_2 = cf_1/2$
 - $cf_3 = cf_1/3$
 - ...
 - $cf_h = cf_1/h$

Applicando il grafico **log-log** 
$$\log{cf_i} = \log{K} - \log{i}$$

```ad-note
Osservare che se ricerchiamo una parola a **bassa frequenza** ci consente di avere un sottoinsieme di documenti molto più piccolo e mirato.

Perciò, possiamo costruire un indice che da priorità alle parole con più bassa frequenza, e meno a quelli con frequenza alta.
```

-----
# Compression

# Dictionary Compression
Si vuole comprimere il dizionario, perché è necessario tenere il dizionario per intero in memoria.

Importante anche osservare che il dizionario compresso deve poter essere utilizzabile già da compresso, e soprattutto no vogliamo perdita di informazioni.

## naive version
La struttura dati per il dizionario generalmente è piccola, e cresce logaritmicamente rispetto alla dimensione del dizionario.
Dopodichè mediamente abbiamo
- 20Byte per i termini.
- 4Byte per la frequenza.
- 4Byte per il riferimento alla posting list.

```ad-note
- lunghezza media delle parole nell'inglese scritto: 4.5 bytes
- lunghezza media di tutte le parole nell'inglese: 8 bytes
```

### Dictionary as a String
Salvo tutti i termini in una unica **stringa** concatenandoli tutti.
Nell struttura, salvo semplicemente il puntatore alla porzione della stringa in cui si trova.

Freq. | Posting Ptr | String Ptr
---|---|---
4 byte | 4 byte | 3 byte

- [VEDI DIMENSIONI NECESSARIE]

400k termini per 19 byte (4+4+3+ 8 avg len) abbiamo circa 7.6MB di memoria.

### Blocking
Creiamo blocchi composti da $k$ termini.
Abbiamo bisogno però di salvare, tra ogni termine, il numero di byte necessarie per raggiungere la parola successiva.

Quindi per ogni parola, salvo il puntatore alla prima parola del proprio blocco, e la sua posizione relativa all'interno del blocco.

Con $k = 4$ risparmiamo 2 byte, e quindi $0.5MB$.
Potremmo aumentare $k$, però l'operazione di lettura cresce troppo.

### Front Coding
Le parole sono composte da una radice e da una desinza.
Per non ripetere sempre la stessa radice per molti termini, possiamo salvare un blocco per ogni radice, e scrivere solo le desinenza.

$$\rightarrow8\text{automata}8\text{automate}9\text{automatic}10\text{automation}$$

$$\rightarrow 8\text{automat*a}1\square\text{e}2\square\text{ic}3\square\text{ion}$$

Il primo numero dice quante lettere leggere per la prima parola.
Dal secondo numero invece, so quanti caratteri leggere dopo il quadrato, appendendo il risultato dove sta l'asterisco.

Technique | Size in MB
---|---
Fixed Width | 11.2
Dictionary-as-a-String | 7.6
\+ blocking con $k = 4$ | 7.1
\+ blocking \+ front coding | 5.9

Purtroppo non possiamo comprimere di più senza perdere informazione, oppure senza dover decomprimere per accedere al dizionario (noi non vogliamo dover decomprimere).

-------
# Postings Compression
Partiamo dalle posting list non posizionali.
Avendo 800,000 dicumenti, e usando un numero seriale come docID, ci bastano circa 20 bit a disposizone.

Per parole poco frequenti, per esempio **arachnocentric**, ci saranno pochi documenti nella posting list, perciò 20 byte sono più che sufficienti.

Ma per termini estremamente frequenti come **the**?

### Gap encoding
Invece di salvare i documenti in ordine cui appaiono, usiamo il **gap** tra i doc id, così per i termini estramente frequenti avremo numeri molto piccoli
-> 33,47,154,159,202...
-> 33,14,107,5,43...

oppuer per **the**
-> 1,2,3,4,5, ...
-> 1,1,1,1,1,1, ...

```ad-note
Ovviamente abbiamo bisogno di una **codifica variabile** dei numeri, perché se uso un numero fissati di bit per i numeri, la dimensione delle posting list non varia (sia che usiamo la posting semplice, sia la gap encoding).
```

### Unary code
Se il gap è $G$ tra due termini, in meno di $\log_2{G}$ bit non possiamo salvare la sua informazione.

Per rappresentare un gap lungo $G$ possiamo usare $G$ 1 seguiti da uno $0$.
Per esempio $G = 3 \to 1110$.

Ovviamente per gap molto grandi, questo metodo è estremamente dispendioso.

[VEDI SVANTAGGIO DISTRIBUZIONE]

### Gamma code
Osserviamo che se rappresentiamo in maniera variabile una sequenza di numeri, non sappiamo quando inizia e quando finisce un numero.

Però possiamo rappresentare in maniera **unaria** la lunghezza in bit del numero che segue.
Così facendo, in $2\log{G}$ bits riusciamo a rappresentare in **maniera variabile** la sequenza di numeri della mia **gap list**.

[VEDI VANTAGGIO DISTRIBUZIONE]

Anche se teoricamente è un metodo ottimo, purtroppo nel modo reale non funziona bene perché i processori operano in sequenze di **lunghezza fissa** di bit (8, 16, 32, 64, ...).

### Variable Byte (VB) codes
Possiamo rappresentare quindi un numero con una sequenza **variabile** di bit possiamo rappresentarlo come una sequenza variablie di **byte**.

Uso 7 bit per la codifica di un numero, e con l'ottavo bit indico che 
- se 0 continuo a interpretare il numero col prossimo byte
- se 1 ho finito di interpretare il numero nel blocco corrente.