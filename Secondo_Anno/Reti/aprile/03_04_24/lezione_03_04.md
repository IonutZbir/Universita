# Trasporto orientato alla connessione: TCP

## Connessione TCP

> [!IMPORTANT]
>
> **TCP** viene detto **orientato alla connessione** in quanto, prima di effettuare lo scambio dei dati, i processi devono effettuare l'handshake, ossia devono inviarsi reciprocamente alcuni segmenti preliminari per stabilire i parametri del successivo trasferimento dati. Come parte dell'instaurazione della connessione TCP, entrambe le parti inizializzano molte variabili di stato associate alla connessione.

Una connessione TCP offre un **servizio full-duplex**, ovvero data una connessione tra due applicazioni, A e B su due host differenti,  i dati a livello di applicazione possono fluire dal processo A al processo B e in contemporanea dal processo B al processo A. (A <-> B).

Una connessione TCP è anche **punto a punto**, ossia ha luogo tra un singolo mittente e un singolo destinatario.
Una volta instaurata una connessione TCP, i due processi applicativi si possono scambiare dati. Consideriamo l'invio di dati dal processo client al processo server. Il primo manda un flusso di dati attraverso la socket. Questi quando hanno attraversato il punto di uscita, sono nelle mani di TCP in esecuzione sul client. TCP dirige i dati al **buffer di invio** della connessione, uno dei buffer riservato durante l'handshake a tre vie, da cui, di tanto in tanto, preleverà blocchi di dati e li passerà al livello di rete.

<img src="img/tcp.png" width="300" />

La massima quantità di dati prelevabili e posizionabili in un segmento viene limitata dalla **dimensione massima del segmento (MSS)**. Questo valore viene generalmente impostato determinando prima la lunghezza del frame più grande che può essere inviato a livello di collegamento dall'host mittente locale, la cosidetta **unità trasmissiva massima (MTU)** e poi scegliendo un MSS tale che il segmentto TCP stia all'interno di un singolo frame a livello di collegamento, considerando anche la lunghezza dell'intestazione TCP/IP normalmente di 40 byte. I protocolli Ethernet e PPP hanno un MTU di 1500 byte, quindi un valore tipico di MSS è di 1460 byte.

## Segmenti TCP

TCP accoppia ogni blocco di dati del client a una intestazione TCP, andando a formare **segmenti TCP**. Questi vengono passati al sottostanze livello di rete, dove sono incapsulati separatamente in datagrammi IP che vengono poi immessi in rete. Dall'altro capo TCP riceve un segmento, i dati del segmento vengono memorizzati nel buffer di ricezione della connessione TCP. L'applicazione legge il flusso di dati da questo buffer, che è proprio per ogni lato della connessione.

<img src="img/tcp_seg.png" width="300" />

Come in UDP, l'intestazione include **numeri di porta di origine e di destinazione**, utilizzati per il multiplexing e il demultiplexing dei dati da e verso le applicazioni del livello superiore, e un campo **Checksum**. Inoltre TCP comprende anche i seguenti campi d'intestazione:

- **Numero di sequenza** e **Numero di acknowledgment**, entrambi di 32 bit, vengono utilizzati dal mittente e dal destinatario TCP per implementare il trasferimento dati affidabile.
- **Finestra di ricezione**, di 16 bit, viene utilizzato per il controllo di flusso.
- **Lunghezza dell'intestazione**, di 4 bit, specifica la lunghezza dell'intestazione TCP in multipli di 32 bit. L'intestazione TCP ha lunghezza dell'intestazione TCP in multipli di 32 bit.L'intestazione TCP ha lunghezza variabile a causa del campo delle opzioni TCP. Generalmente, il campo delle opzioni è vuoto e, pertanto la lunghezza consueta è di 20 byte.
- **Opzioni**, facoltativo e di lunghezza variabile, viene utilizzato quando mittente e destinatario negoziano la dimensione massima del segmento (MSS) o come fattore di scala per la finestra nelle reti ad alta velocità.
- **Flag**, campo di 6 bit. Il bit **ACK** viene usato per indicare che il valore trasportato nel campo di acknowledgment è valido. I bit **RST**, **SYN**, **FYN** vengono utilizzati per impostare e chiudere la connessione. I bit **CWR** ed **ECE** sono usati nel controllo di congestione. Se il bit **PSH** ha valore 1 il destinatario dovrebbe inviare immediatamente i dati al livello superiore. Il bit **URG** per indicare nel segmento la presenza di dati che l'entità mittente a livello superiore ha marcato come "urgenti".

**Numeri di sequenza e numeri di acknowledgment**

TCP vede i dati come un flusso di byte non strutturati, ma ordinati. Dato che i numeri di sequenza si applicano al flusso di byte trasmessi e non alla serie di segmenti trasmessi, pertanto, il **numero di sequenza del segmento** è il numero nel flusso di byte del primo byte del segmento.

Siano due host, A e B in comuncazione su un canale TCP.
Il **numero di acknowledgment** che l'host A scrive nei propri segmenti e il numero di sequenza del byte successivo che l'host A attende dall'host B.

Supponiamo che l’Host A abbia ricevuto un segmento dall’Host B contenente i byte da 0 a 535 e un altro segmento contenente i byte da 900 a 1000. Per qualche motivo l’Host A non ha ancora ricevuto i byte da 536 a 899. In questo esempio, l’Host A sta ancora attendendo il byte 536 (e i successivi) per ricreare il flusso di dati di B. Perciò il prossimo segmento di A destinato a B conterrà 536 nel campo del numero di acknowledgment. Dato che TCP effettua l’acknowledgment solo dei byte fino al primo byte mancante nel flusso, si dice che tale protocollo offre **acknowledgment cumulativi (cumulative acknowledgment)**.

## Timeout e stima del tempo di andata e ritorno (RTT)

TCP, utilizza un meccanismo di timeout e ritrasmissione per recupere i segmenti persi. Il timeout deve essere più grande del tempo di andata e ritorno sulla connessione (**RTT, Round-Trip Time**), ossia del tempo trascorso da quando si invia un segmento a quando se ne riceve l'acknowledgment, altrimenti ci sarebbero delle ritrasmissioni inutili.

**Stima RTT**

- `SampleRTT`: RTT misurato di un segmento, è la quantità di tempo che intercorre tra l'istante di invio del segmento (quando viene passato a IP) e quello di ricezione dell'acknowledgment del segmento.

I campioni variano da segmento a segmento in base alla congestione nei router e al diverso carico sui sistemi periferici. A causa di tale fluttuazione, ogni valore di `SampleRTT` può essere atipico. Per effettuare una stima più natuale, TCP effettua una media di `SampleRTT` chiamata `EstimatedRTT`, calcolato secondo questa formula:

$$EstimatedRTT = (1 - \alpha)\cdot EstimatedRTT + \alpha\cdot SampleRTT$$

Si noti che `EstimatedRTT` è una media ponderata dei valori `SampleRTT`. Tale media attribuisce maggiore importanza ai campioni recenti rispetto a quelli vecchi. In statistica una media costruita in questo modo è detta **media mobile esponenziale ponderata (EWMA)**.

$$EstimatedRTT_{n} = (1 - \alpha)^{n}\cdot Estimated_{n - 1} + \alpha\cdot SampleRTT_{n}$$

Oltre ad avere una stima di RTT è anche importante possedere la misura della sua variabilità. `DevRTT` è una stima di quanto `SampleRTT` generalmente si discosta da `EstimatedRTT`.

$$DevRTT = (1 - \beta)\cdot DevRTT + \beta\cdot \mid SampleRTT - EstimatedRTT \mid$$

Tipicamente il valore di $\beta$ è 0.25.

Dati i valori di `EstimatedRTT` e `DevRTT`, dobbiamo trovare il valore del timeout. L'intervallo non può essere minore di `EstimatedRTT` ma neanche troppo maggiore, altrimenti TCP non ritrasmetterebbe rapidamente il segmento perduto, il che comporterebbe gravi ritardi sul trasferimento dei dati.


