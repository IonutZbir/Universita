---
date: 2022-10-25
draft: true
---

Poniamoci nel problema in cui non abbiamo abbastanza spazio in ram per poter conservare tutta la notra struttura dati utile per il nostro indice [[IR/Lecture 2#Inverted index|indice inverso]].

La prima idea è quella di usare il disco come *"memoria aggiuntiva"*.
Applichiamo un approccio **divide et impera**, in cui dividiamo in **blocchi** i nostri termini, **indicizziamo** tali blocchi e li appoggiamo su disco.
Dopodiché eseguiamo il merge.


## BSBI: Blocked Sort-Based Indexing
L'idea è quella ridurre il meno possibile gli accessi su disco.

```ad-important
title: Assunzione
Assumiamo che la mia collezione è salvata su disco in **aree consecutive**.

```

- Divido l'insieme dei miei documenti in $n$ blocchi di dimensione fissa.
- Uno alla volta lo carico in ram, e genero l'indice su di esso
- Quando ho finito con tutti, li unisco (**merge**)

## Costo
- ordinamento $(N \log{N})$.
- per fare il merge usiamo il **binary merge tree** in tempo logaritmico ogni coppia di blocchi.


-----
# SPIMI: Single-Pass In-Memory Indexing
- **key idea 1**: genera dizionari differenti per ogni blocco.
- **key idea 2**: non c'è bisogno di ordinare i termini, li salvo nell'ordine in cui arrivano. (uso una funzione hash per ricavarli). Ordino solo alla fine.

```ad-important
Ordino perché potrei dividire i blocchi per lettere.
Associo la lettera `A` al blocco 1, la lettera `B`al blocco 2, ecc..
(Si possono anche fare sottoblocchi per la seconda lettera, e così via, cosi da scalare illimitatamente).

Mantenere oridnata una strattura a fronte di un inserimento è costoso.
```

```ad-note
title: Size of Posting List

Le posting list, all'atto pratico, sono **array dinamici**.
Pensiamo però, che non tutti i termini hanno necessità di far **raddoppiare** la loro dimensione ogni volta.
Per esempio l'array dinamico del termine `the` avrà bisogno di raddoppiare quando pieno, perché la parole *"the"* è molto frequente.
Mentre per il termine `Marco` non c'è bisogno di raddoppiare, perché poco frequente.
Possiamo per essempio dargli un $10\%$ aggiuntivo alla volta.
```


---------
# Distributed indexing
Che succede se nella mia macchina non riesco a contenere tutta la mia collezione di documenti?

Se ho $n = 1000$ macchine in un data center, e ognuna che ha una garanzia di funzionamento del $99.9\%$.

In un anno, quanto tempo saranno tutte le $n$ macchine funzionanti?
$$P(\text{tutte le macchine attive}) = 0.999^n \approx .37$$
Perciò, in un anno, per il $63\%$ del tempo un operaio dovrà andare ad aggiustare una macchina.


- Mantengo una **macchina master** (considerata **safe**) che gestisce il processo di indicizzazione.
- Essa divide il lavoro tra differenti macchine che lavoreranno in parallelo.

[vedi immagine data flow]

## Map-Reduce
- **map phase**. Il master assegna i documenti divisi in blocchi a un **parser**, i quali genereranno le posting list di tale blocco.
- **reduce phase**: Date tutte le posting lists, un **inverter** fa il merge di positng lists (suddivisi per lettere). Per esempio un inverter per le lettere dalla a-f, uno per per g-p, ...

## Vantaggi
- **scalabile**
- **fault tollernat**: se si rompe una macchina, il master assegna il task al nodo più disponibile
- **macchine eterogenei**

## Parser
Il parter legge i documenti del blocco che gli è stato assegnato, e crea una struttura del tipo `<termine, documenti>`, generalmente suddivisi in blocchi lessico-graficamente partizionati.

## Inverter
L'inverter legge tutte le coppie `<termine, documenti>` tali che i termini appartengano ad un unico blocco (per esempio `a-f`), fonde le posting list e ordina i termini.

## Osservazione importante
Invece di partizionare per **lettere**, è più **robusto** partizionare per documenti.
Infatti, se si rompe il disco con i termini che iniziano per `a` il mio servizio crolla.

Viceversa, se crolla il blocco con i documenti di Wikipedia, continuerò ad avere altri documenti che hanno termini che iniziano per `a`. Anche se ne perdo di **recall**, il sistema non crolla.