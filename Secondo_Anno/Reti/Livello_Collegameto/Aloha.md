# Protocolli ad accesso causale

## Slotted ALOHA

Slotted ALOHA è uno dei più semplici algoritmi di acceso casuale ad un canale per trasmissioni multiple.

- Tutti i frame hanno la stessa dimensione.
- Il tempo è diviso in slot temporali uguali, pari al tempo di trasmissione di un frame.
- I nodi cominciano la trasmissione solo all'inizio degli slot.
- I nodi sono sicronizzati in modo tale che tutti sappiano quando iniziano i slot.
- Se due nodi trasmettono in contemporanea nello stesso slot, tutti i nodi rilevano l'evento prima del termine dello slot.

Sia $p$ una probabilità, ovvero un numero tra 0 e 1. Allora le operazioni dei nodi in slotted ALOHA sono:

1. Quando un nodo ha un nuovo frame da spedire, attende fino all'inizio dello slot successivo e poi trasmette l'intero frame.
2. **Se non si verifica una collisione**, l'operazione ha avuto successo, quindi non occorre effettuare una ritrasmissione e il nodo può predisporre l'invio di un nuovo frame.
3. **Se si verifica una collisione**, il nodo la rileva prima della terminazione dello slot e ritrasmette con probalità $p$ il suo frame durante gli slot successivi, fino a quando l'operazione non ha successo.

Per capire meglio il concetto di **ritrasmissione con probabilità $p$** possiamo immaginare che il nodo lanci una moneta truccata: l'evento testa corrisponde alla ritrasmissione, che si verifica con probabilià $p$, quello croce corrisponde a "salta questo slot e lancia di nuovo la monete in quello successivo". Questo accade con probabilità $(1 - p)$. I nodi coinvolti nella collisione lanciano le proprie monete indipendentemente gli uni dagli altri.

### Vantaggi

1. Quando c'è un solo nodo attivo, esso continua a trasmettere frame a massima velocità.
2. Fortemente decentralizzato in quanto ciascun nodo rileva le collisioni e decide indipendentemente dagli altri quando ritrasmettere.
3. Molto semplice.

### Svantaggi

1. Se ci sono collisioni, esse portano a sprecare slot.
2. Un grande numero di slot risulterà inutilizzato, in quanto la ritrasmissione è probabilistica.

### Efficienza

**L'efficienza** di un protocollo di accesso multiplo che fa uso di slot temporali è definita come la frazione di slot riusciti in presenza di un elevato numero di nodi attivi che hanno sempre un elevato numero di frame da trasmettere.

Dopo tanti calcoli che non sto qua a fare perché non me va, otteniamo che l'effienza massima di slotted ALOHA è $\frac{1}{e} = 0.37$. Vale a dire che quando un gran numero di nodi ha molti pacchetti da trasmettere, allora solo il **$37\%$** degli slot compie lavoro utile.

## ALOHA

La prima versione di slotted ALOHA, fu ALOHA puro, che non faceva utilizzo degli slot ed era fortemente decentralizzato. Dunque appena arriva un frame il nodo lo trasmette immediatamente e integralmente nel canale broadcast. Se il frame va in collisione allora lo ritrasmette immediatamente con probabilità $p$.

L'efficienza di questo protocollo è $\frac{1}{2e} = 0.18$ esattamente la metà di slotted ALOHA.

## CSMA: Carrier Sense Multiple Access

Se in ALOHA e slotted ALOHA i nodi prendono la decione di trasmettere indipendentemente dall'attività degli altri nodi collegati in broadcast (analogia: maleducato che parla sopra ad altre persone senza preoccuparsi che stiano conversando tra di loro), i protocolli CSMA e CSMA/CD si basano su due regole fondamentali:

1. *Ascoltare prima di parlare*, nel mondo delle reti questo prende il nome di **rilevamento della portante (carrier sens)**, ovvero un nodo ascolta il canale prima di trasmettere. Se il canale sta già trasmettendo un frame allora si mette in attesa, altrimenti se il canale è libero inizia la trasmissione (CSMA).
2. *Se qualcun altro comincia a parlare insieme a voi, smettere di parlare*, nel mondo delle reti questo prende il nome di **rilevamento della collisione (collisione detection)**. Se un nodo osserva che un altro nodo sta trasmettendo un frame che interferisce col suo, arresta la propria trasmissione (CSMA/CD).

> [!NOTE]  
>
> In ALOHA e slotted ALOHA questo non era possibile fare, in quanto sono protocolli utilizzati per le connessione wireless, nelle quali non banale osservare che un canale è occupato. CSMA e CSMA/CD sono utilizzati nei collegamenti Ethernet.

