- [[https://learnmeabitcoin.com/technical/]]

Finora abbiamo studiato protocolli e sistemi distribuiti nel modello *permissioned*, dove il numero di nodi che partecipano al protocollo è noto a priori da tutti i nodi.

Vediamo ora un protocollo diverso, quello di Bitcoin ideato per un sistema *permissionless*, dove il numero di nodi non è fisso. Bisogna quindi introdurre misure atte a mitigare la possibilità dei *sybil attacks*, ossia limitare la capacità di un singolo nodo *corrotto* di generare più identità, quindi *simulare* più nodi.

Senza identità certificate, un singolo nodo avversario potrebbe generare milioni di identità virtuali. Se il consenso si basasse sul principio "un'identità = un voto", l'attaccante avrebbe la maggioranza assoluta a costo zero. Per neutralizzare questa vulnerabilità, Bitcoin impone un costo fisico e non falsificabile alla partecipazione: **il costo computazionale tramite Proof-of-Work**

## Bitcoin Proof of Work

**DEF:** Con il termine *Proof of Work* si intende una breve "dimostrazione" (da un punto di vista computazionale) che può essere facilmente "verificata" che una certa quantità di lavoro computazionale è stata eseguita.

In Bitcoin la PoW si basa sulla funzione hash crittografica SHA256 e sulle proprietà di essa. È usata dal protocollo sia per impedire che un singolo nodo corrotto possa agire come più nodi onesti, sia per fare in modo che tutti i nodi onesti concordino su quali sono i dati "corretti" da tenere in memoria.

**DEF:** Sia $$\mathcal{H}: \{0,1\}^* \to \{0,1\}^l$$ una funzione hash crittografica, allora
1. *Preimage Resistance:* Dato un valore di hash $h \in \{0,1\}^l$ deve essere computazionalmente difficile trovare $m \in \{ 0,1 \}^*$ tale che $\mathcal{H}(m) = h$.
2. *Second Preimage Resistance:* Dato un messaggio $m_{1} \in \{ 0,1 \}^*$, deve essere computazionalmente difficile trovare un secondo messaggio $m_{2} \in \{ 0,1 \}^*$ tale che $\mathcal{H}(m_{1}) = \mathcal{H}(m_{2})$.
3. *Collision Resistance:* Dati due messaggi $m_{1}, m_{2} \in \{ 0,1 \}^*,\ m_{1} \neq m_{2}$ deve essere difficile che i due messggi abbino lo stesso hash, ossia che $\mathcal{H}(m_{1}) = \mathcal{H}(m_{2})$.

*Note tecniche su SHA256:*

## Algoritmo di Consenso di Nakamoto

Prima di studiare il protocollo di consenso di Nakamoto, definiamo formalmente la *blockchain*.

Sia $\mathcal{H}$ una funzione hash crittografica definita come prima. Nel caso di bitcoin la funzione hash crittografica usata è SHA256, in particolare, dato un messaggio $m \in \{ 0,1 \}^*$, il digest di $m$ è definito come:
$$\texttt{hash}_{256}(m) = \texttt{SHA256(SHA256(m))}$$
Un blocco $B_i$ al passo temporale o indice di altezza $i \in \mathbb{N}$ è una tupla formata da un'intestazione (_header_) $H_i$ e da un carico utile di transazioni (_data_) $D_i$:
$$B_i = (H_i, D_i)$$
L'header $H_i$ è formalizzato come una tupla di campi:
$$H_i = (\mathtt{ver}, h_{i-1}, m_i, \tau_i, \tau_{\text{target}}, \eta)$$
dove:
- $\mathtt{ver} \in \{0, 1\}^{32}$: la versione del protocollo.
- $h_{i-1} \in \{0, 1\}^{256}$: il puntatore al blocco precedente, definito formalmente come $h_{i-1} = \mathcal{H}(H_{i-1})$.
- $m_i \in \{0, 1\}^{256}$: l'impronta delle transazioni contenute in $D_i$. In Bitcoin corrisponde alla radice dell'albero di Merkle calcolato sul vettore ordinato di transazioni $D_i = \langle tx_1, \dots, tx_k \rangle$, ovvero $m_i = \text{MerkleRoot}(D_i)$.
- $\tau_i \in \mathbb{N}_{< 2^{32}}$: il timestamp Unix (secondi trascorsi dalla mezzanotte UTC del 1 gennaio 1970).
- $\tau_{\text{target}} \in \{0, 1\}^{32}$: la rappresentazione compatta (in formato `nBits`) del target numerico $T \in [1, 2^{256}-1]$.
- $\eta \in \{0, 1\}^{32}$: il valore del *nonce*.
#### La Catena di Blocchi

La catena $\mathcal{C}$ di lunghezza $\vert{}\mathcal{C}\vert{} = t + 1$ è una sequenza finita ordinata di blocchi:
$$\mathcal{C} = \langle B_0, B_1, B_2, \dots, B_t \rangle$$
sotto i seguenti vincoli di consistenza interna:
1. **Blocco Genesi:** $B_0 = (\text{GENESIS.header}, \text{GENESIS.data})$ è una costante pubblica deterministica hardcoded nel client. Per convenzione formale, $h_{-1} = 0^{256}$.
2. **Integrità Crittografica:** $\forall i \in \{1, \dots, t\}$, l'header $H_i$ soddisfa: $$H_i.h_{i-1} = \mathcal{H}(H_{i-1})$$
3. **Validità della Proof-of-Work:** $\forall i \in \{1, \dots, t\}$, interpretando l'output di $\mathcal{H}(H_i)$ come un intero a 256 bit: $$\mathcal{H}(H_i) < T_i$$dove $T_i = \mathtt{UPDATE\_TARGET}(\mathcal{C}[0:i-1])$.
4. **Validità Semantica delle Transazioni:** $\forall i \in \{1, \dots, t\}$, tutte le transazioni in $D_i$ sono valide rispetto al modello contabile di stato (nessuna doppia spesa, firme crittografiche valide e bilanci coerenti con l'insieme degli UTXO generati da $\mathcal{C}[0:i-1]$).

Inoltre, affinchè un blocco sia valido deve valere anche che il timestamp del blocco non sia troppo lontano dall'ora corrente per il nodo $u$.

### Protocollo

Il protocollo di consenso ha lo scopo di coordinare una rete aperta e non fidata (_permissionless_), garantendo il rispetto di quattro proprietà cardine:
- Ogni nodo onesto memorizza e aggiorna in autonomia una copia locale della blockchain, nella quale periodicamente può aggiungere nuovi blocchi in cima della catena.
- *Eventual Consistency:* Le copie locali della blockchain dei vari nodi onesti convergono verso il medesimo storico condiviso. Eventuali divergenze sono temporanee e circoscritte unicamente a una finestra instabile di prefisso, limitata agli ultimi blocchi in testa alla catena (_fork_ transitori dovuti alla latenza di rete).
- *Liveness:* Il protocollo assicura che il sistema compia costantemente progressi utili: se un nodo onesto riceve una transazione valida, questa non rimane bloccata a tempo indefinito, ma viene prima o poi inclusa stabilmente all'interno di un blocco confermato della blockchain.
- Un nodo onesto che si connette alla rete deve essere in grado di identificare la versione canonica del registro in modo deterministico e completamente autonomo. Ricevendo copie discordanti da nodi sconosciuti o potenzialmente malevoli, il nodo non fa affidamento su autorità terze o votazioni per identità, ma applica una regola di verifica oggettiva basata sul lavoro computazionale cumulato (*longest Proof-of-Work*).


![[nakamotoconsensus.png]]

### Mining e Target

Un nodo oneso $u$ riesce a creare un blocco nuovo se 
$$
\texttt{hash}_{256}(\texttt{header}) < \texttt{target}
$$
Poichè la funzione hash SHA256 è crittograficamente sicura, l'unico modo per trovare un intero `nonce` tale che $\texttt{hash}_{256}(\texttt{header}) < \texttt{target}$ è procedere per *brute-force*. Dato che lo spazio totale delle immagini di SHA256 è $2^{256}$, la probabilità $p$ che un singolo hash soddisfi la disuguaglianza è:
$$
p = \frac{\texttt{target}}{2^{256}}
$$
Sia $X$ il numero di tentativi necessari prima di trovare un valore valido. Si ha che $X \sim Geo(p)$, quindi
$$
\mathbb{E}[X] = \frac{1}{p} = \frac{2^{256}}{\texttt{target}}
$$
Poichè $\texttt{target} \ll 2^{256}$, questo calcolo richiede mediamente miliardi/trilioni di operazioni hash.

Al contrario, quando un nodo riceve un blocco contente il target, per verificare se aggiungerlo o meno alla sua catena, gli è sufficiente verificare che:
$$
\texttt{hash}_{256}(\texttt{header}) < \texttt{target}
$$

Consideriamo ora una sequenza di blocchi $\langle B_0, B_1, B_2, \dots, B_t \rangle$ ciascuno estratto con un target $B_{i}.\texttt{header.target}$. Possiamo definire la funzione $\texttt{WORK}$ che ci indica quanto lavoro è necesarrio in media per produrre una blockchain di $t$ blocchi:
$$
\texttt{WORK} = \sum_{i=1}^t \frac{2^{256}}{ B_{i}.\texttt{header.target}}
$$
Un nodo onesto $u$ per verificare quale catena sia quella canonica calcola la funzione $\texttt{WORK}$ e sceglia quella con maggiore PoW.

Inoltre, un nodo per verificare un intera catena di $t$ nodi, non deve rifare tutto il lavoro di ricerca ma basta che ricalcola esattamente $t$ hash, uno per ciascun header, verificando per ogni $i \in \{ 1, \dots t \}$ che
$$
\text{SHA256}(\text{header}_i) < \text{target}_i
$$

**DOMANDA:** È possibile che uno/più nodi corrotti provino ad alterare lo stato della catena, creando un nuovo ramo che sorpassa in lunghezza quello principale?
Supponiamo che un attaccante volesse alterare retroattivamente una transazione contenuta nell'ennesimo blocco $i \leq t$. Allora deve:
1. Modificare i dati del blocco $B_{i}$ alterando l'hash del blocco.
2. Modificando l'hash, il precedente `nonce` non soddisferà quasi sicuramente più la condizione della PoW: deve quindi ricalcolare da zero un nuovo `nonce` per il blocco $i$.
3. Questo provoca un effetto a valanga, in quanto l'header de blocco successivo contiene ne puntatore `prev_hash` l'hash precendente. Deve quindi modificare il `prev_hash` del blocco $i+1$ violando nuovamente cosi la condizione di PoW.
4. Questo effetto si propaga a cascata su tutti i blocchi successivi: l'attaccante è obbligato a ricalcolare la PoW per tutti i blocchi dall'indice $i$ fino all'indice $t$

Dovendo rifare da solo una quantità cumulativa di lavoro pari a $\sum_{j=i}^{t} \frac{2^{256}}{\text{target}_j}$ mentre il resto della rete continua a minare nuovi blocchi sulla catena onesta, riscrivere lo storico passato diventa computazionalmente impraticabile a meno di non possedere la maggioranza assoluta dell'hashrate dell'intera rete.

#### Come scegliere il target?

Il meccanismo di scelta del target deve soddisfare due principali proprietà:
- Garantire che la produzione dei blocchi avvenga in media a una frequenza di *1 blocco ogni 10 minuti*, indipendentemente dal numero di minatori connessi e dalla potenza computazionale complessiva;
- Ogni singolo nodo a conoscenza della cronologia dei blocchi deve poter determinare in modo univoco ed esatto qual è il target che il blocco successivo deve rispettare, senza dover chiedere a terzi.

La scelta di Nakamoto è stata la seguente:
Invece di aggiornare il target continuamente, il parametro rimane **costante per un intervallo prefissato di $N = 2016$ blocchi**.
- A un ritmo nominale di 1 blocco ogni 10 minuti (600 secondi), 2016 blocchi corrispondono esattamente a: $$2016 \times 10 \text{ minuti} = 20.160 \text{ minuti} = 336 \text{ ore} = 14 \text{ giorni }$$
Al termine dell'epoca, ogni nodo esamina i metadati già validati e presenti nella catena:
- Legge il `timestamp` del primo blocco dell'epoca e quello dell'ultimo blocco.
- Calcola la differenza: $$T_{\text{reale}} = \text{timestamp}_{\text{ultimo}} - \text{timestamp}_{\text{primo}}$$
- Confronta $T_{\text{reale}}$ con il valore ideale di riferimento $T_{\text{target}} = 14 \text{ giorni} = 1.209.600 \text{ secondi}$.
La regola di aggiornamento corregge il parametro in modo direttamente proporzionale al tempo effettivo:
- **Se $T_{\text{reale}} > 14 \text{ giorni}$:** la rete ha impiegato più tempo del dovuto, segno che l'hashrate è diminuito. Il target deve **aumentare** (la soglia numerica si alza, rendendo il puzzle crittografico più facile).
- **Se $T_{\text{reale}} < 14 \text{ giorni}$:** la rete ha estratto i blocchi troppo rapidamente, segno che la potenza di calcolo è aumentata. Il target deve **diminuire** (la soglia si abbassa, rendendo la ricerca del nonce più difficile).

Tutti i dati necessari per la funzione `UPDATE_TARGET(block)` (i timestamp, il target precedente e l'indice del blocco) sono memorizzati in modo immutabile negli header dei blocchi precedenti della blockchain. Di conseguenza:
- Qualsiasi nodo onesto esegue lo stesso identico calcolo deterministico.
- Se un miner provasse a generare un blocco per l'epoca successiva usando un target diverso da quello calcolato con questa formula, tutti gli altri nodi rifiuterebbero il blocco considerandolo non valido, garantendo il consenso senza bisogno di coordinamento centrale.

## Transazioni

Nel linguaggio comune, quando parliamo di un bitcoin tipicamente intendiamo una unità della criptovaluta corrispondente (un po’ come parliamo di un euro o di un dollaro). In realtà, non esiste
nessun “oggetto digitale” che corrisponda a un bitcoin (o a una frazione o a un multiplo di bitcoin), ciò che invece esiste come oggetto digitale nel sistema Bitcoin sono le *transazioni*: il contenuto della parte che abbiamo chiamato data di un blocco della Blockchain di Bitcoin è infatti una sequenza di transazioni. Per capire come l’astrazione di un bitcoin come una unità di criptovaluta è legata
alle transazioni dobbiamo dare un’occhiata più approfondita alla struttura di queste ultime.

### Legacy Tx

Nella sua versione originale (legacy) un transazione è una struttura formata dai campi *inputs (dim. variabile), outputs (dim. variabile), version (4 byte), locktime (4 byte)*.

Ogni transazione contiene uno o più input (l'unica transazione senza input è la *coinbase transaction*) e uno o più output.

![[legacytx.png]]

Diciamo che una transazione $\texttt{tx}_{a}$ spende l’output $\texttt{tx}_{b}.\texttt{output}$ di una precedente transazione $\texttt{tx}_{b}$ se uno degli input di $\texttt{tx}_{a}$ punta all’output $\texttt{tx}_{b}.\texttt{output}$. Ogni output può essere speso da una sola transazione, se ci sono due o più transazioni che spendono lo stesso output, una sola sarà quella considerata "valida": quella che viene inserita in un blocco.

Se un blocco dovesse contenere una transazione che spende un output già speso da una transazione in un blocco precedente (oppure se il blocco dovesse contenere due o più transazioni che spendono lo stesso output - non speso - di una transazione precedente), allora il blocco non sarebbe considerato valido e non verrebbe aggiunto alla catena dai nodi onesti.

#### Input e Output

Un output contiene due campi: un valore, ossia un numero intero che corrisponde all’ammontare di quell’output e un *locking script*. Un input è una struttura formata da:
1. Puntatore all’output di una precedente transazione, indicato con la coppia $(\texttt{prev\_tx, prev\_id)}$, dove $\texttt{prev\_tx}$ è la transazione e $\texttt{prev\_id}$ è l’indice dell’output all’interno della transazione;
2. *Unlocking script*;

Inoltre, ogni transazione ha anche un sequence number, ma per il momento non ce ne occupiamo.

![[inputsoutputs.png]]

Locking script nell’output e unlocking script nell’input, sono dei veri e propri "programmi" scritti in un linguaggio che tutti i nodi della rete possono interpretare. 

**DEF:** L'input $\texttt{tx.input}$ è **valido** se e solo se la concatenazione  
$$  
\texttt{unlocking\_script} \Vert \texttt{locking\_script}  
$$
costituisce un programma che, eseguito, restituisce $\texttt{True}$.

Nel gergo di Bitcoin, il locking script è detto **scriptPubKey** (o $\texttt{scriptPk}$) e lo unlocking script è detto **scriptSig**. Il nome riflette la loro forma più comune: nel caso standard (P2PKH), lo $\texttt{scriptSig}$ contiene una firma digitale, mentre lo $\texttt{scriptPk}$ contiene una chiave pubblica. In questo caso, la concatenazione dei due script restituisce $\texttt{True}$ se e solo se la firma è valida rispetto alla chiave pubblica, ovvero se e solo se chi ha creato l'input possiede la chiave privata corrispondente.

#### Validità Tx e Fee

**DEF:** Un UTXO (unspent transaction output) è un output ancora non speso. L'insieme degli output non spesi definisce l'UTXO Set.

Una transazione tx è valida se 
1. Tutti i suoi input puntano a degli output che non sono già stati spesi da qualche altra transazione e sono validi;
2. Se la somma dei valori degli output, $\sum \texttt{tx.output.valore}$ è minore o uguale alla somma degli valore degli output puntati dagli input, $\sum \texttt{tx.input.(prev\_tx, prev\_id).valore}$.  Se una transazione creasse output con un valore complessivo maggiore agli input consumati, creerebbe moneta dal nulla. La differenza, maggiore o uguale a zero, fra questi due valori è la *transaction fee* della transazione tx.
$$\texttt{tx.fee} = \sum_{\texttt{tx.input}} \texttt{tx.input.valore}\ - \sum_{\texttt{tx.output}}\texttt{tx.output.valore}$$
Gli output consumati da un input (UTXO) non possono essere spesi solo parzialmente. Se si consuma un output da $0.5\text{ BTC}$ per inviare un pagamento da $0.2\text{ BTC}$, il mittente deve creare esplicitamente due output:
- Un output da $0.2\text{ BTC}$ destinato al ricevente.
- Un output da $0.299\text{ BTC}$ (il _change_) reindirizzato a un proprio indirizzo.
La differenza rimanente di $0.001\text{ BTC}$ (non assegnata a nessun output) costituisce automaticamente la **fee** per il miner.
### Coinbase Tx

Le commissioni di tutte le transazioni inserite all'interno di un blocco non vengono inviate singolarmente con bonifici separati. Vengono invece aggregate e assegnate al miner nella **prima transazione del blocco**, la cosiddetta **coinbase transaction**.

Questa transazione è speciale in quanto non ha input, mentre nell'output della transazione ci sono bitcoin che non esistevano prima, quindi quelli *coniati* con quel blocco.

L'ammontare che il miner può legittimamente assegnarsi nell'output della coinbase per l'ennesimo blocco $i$ è la somma di due componenti distinte:

$$\text{valore\_coinbase}[i] = \text{new\_btc}[i] + \sum_{tx \in \text{blocco}} tx.\text{fee}$$
L'ammontare specificato dal protocollo per i nuovi bitcoin creati per ogni blocco parte da 50 e si dimezza ogni 210000 blocchi
$$
\texttt{new\_btc}[i] = \frac{50}{2^{\lfloor 210000 \rfloor} }
$$
in questo modo, il totale dei bitcoin in circolazione sarà sempre minore o uguale a 21 milioni.

**DOMANDA:** A partire da che anno i nuovi blocchi non genereranno più nuova valuta?

Si presume che dal 2141, i nuovi blocchi non genereranno più valuta, infatti: 

Consideriamo l'unità più piccola di misura in bitcoin, ossia il $\texttt{satoshi}$:
$$
\begin{gather*}
1 \text{ satoshi} = 10^{-8} \text{ BTC} \\
\Downarrow \\
1 \text{ BTC} = 100.000.000 \text{ satoshi (100 milioni di satoshi)} 
\end{gather*}
$$
Quindi, la ricompensa del primo blocco in satoshi è:
$$
50 \text{ BTC} = 50 \times 10^8 \text{ satoshi} = 5.000.000.000 \text{ satoshi}
$$

Inoltre, ad ogni $k$-esima epoca, la ricompensa in satoshi per il blocco $i$ subisce una divisione intera 
$$
\text{satoshi}[k] = \left\lfloor  \frac{5.000.000.000}{2^k}  \right\rfloor 
$$
I nuovi blocchi non genereranno più nuova valuta non appena il risultato della divisione intera diventa strettamente inferiore a 1 satoshi, ovvero quando
$$
2^k > 5.000.000.000 \iff k \geq 33
$$
Sapendo che ogni epoca vale 4 anni, si ha che 
$$
\begin{gather*}
\text{tot anni} = 33 \cdot 4 = 132 \\
\Downarrow \\
\text{ultimo anno } = 2009 + 132 = 2141 
\end{gather*}
$$

A partire da quel momento, la ricompensa per i miner sarà costituita **esclusivamente dalle transaction fee**. Saranno proprio le commissioni a dover garantire l'incentivo economico necessario affinché i miner continuino a impiegare elevata potenza computazionale (hashrate), proteggendo la blockchain dal rischio di riorganizzazioni della catena e attacchi del 51%.
#### Merkle Tree

**DEF:** *Merkle Tree* è una struttura dati ad albero binario in cui ogni nodo contiene un'impronta crittografica (hash):
- *Foglie:* contengono l'hash dei dati elementari di partenza (ad esempio, le singole transazioni). Se i dati sono $D_0, D_1, D_2, D_3$, le foglie saranno $H_0 = \mathcal{H}(D_0)$, $H_1 = \mathcal{H}(D_1)$, $H_2 = \mathcal{H}(D_2)$ e $H_3 = \mathcal{H}(D_3)$.
- *Nodi interni:* contengono l'hash della concatenazione dei loro due nodi figli: $$H_{01} = \mathcal{H}(H_0 \,\Vert{}\, H_1), \quad H_{23} = \mathcal{H}(H_2 \,\Vert{}\, H_3)$$Se a un determinato livello il numero di nodi è dispari, l'ultimo nodo viene tipicamente duplicato per consentire l'accoppiamento.
- *Merkle Root:* il singolo hash al vertice dell'albero $$H_{\text{root}} = \mathcal{H}(H_{01} \,\Vert{}\, H_{23})$$che funge da riassunto crittografico e compatto dell'intero insieme di dati sottostanti.

La caratteristica fondamentale del Merkle Tree è l'*effetto a cascata dell'integrità*: alterare un singolo bit in qualsiasi elemento alla base modifica il suo hash foglia, propagando a cascata la variazione a tutti i nodi intermedi fino a generare una Merkle Root completamente diversa.

![[merkletree.png]]

**DOMANDA:** Come vengono usati in Bitcoin?

Nel protocollo di Bitcoin, il Merkle Tree risponde a due esigenze essenziali:

1. *Compressione dei dati nell'Header (`data_hash`):* L'header di ogni blocco ha una dimensione strettamente fissa di **80 byte**, mentre il corpo delle transazioni (`data`) può pesare megabyte e contenere migliaia di transazioni. Invece di serializzare tutte le transazioni nell'header, Bitcoin memorizza nel campo di 32 byte chiamato **`data_hash`** unicamente la **Merkle Root** di tutte le transazioni di quel blocco. Questo collega in modo immutabile l'intero insieme di dati all'header sottoposto a Proof-of-Work.
2. *Verifiche leggere ed efficienti (SPV / Proof di Merkle):* Per verificare che una specifica transazione $tx$ appartenga a un blocco valido, non è necessario scaricare l'intero blocco. Un nodo leggero (come un wallet mobile) può richiedere a un nodo completo una **Merkle Proof**:
    - La prova include soltanto gli hash dei "nodi fratelli" lungo il percorso dal ramo della transazione fino alla radice, ovvero solo $\lceil \log_2 n \rceil$ hash per $n$ transazioni.
    - Il client ricostruisce la radice risalendo l'albero in tempo logaritmico $O(\log n)$ e controlla che il risultato coincida con il `data_hash` presente nell'header del blocco valido già in suo possesso.

### Script

Il software del sistema Bitcoin, in esecuzione su ogni nodo della rete, contiene l’interprete di un semplice linguaggio di programmazione che viene chiamato Script. Il linguaggio Script è stateless (non ci sono variabili che possono salvare localmente un dato e andare a rileggerlo successivamente).
Un programma (uno script) è una sequenza di comandi (istruzioni o dati) che vengono eseguiti secondo un modello stack-based : i dati e le istruzioni vengono inseriti in una pila (lo stack );
quando una istruzione viene inserita nella pila, può estrarre uno o più dati dalla pila, eseguire delle computazioni sui dati ed eventualmente inserire il risultato delle computazioni nella pila. Facciamo un esempio. L’istruzione `OP_ADD` nel linguaggio Script estrae due dati dalla pila e ne esegue la somma, quindi il seguente script
$$
\texttt{<2> <3> OP\_ADD}
$$
verrebbe eseguito dall’interprete Script presente sui nodi della rete Bitcoin in questo modo: viene inserito nella pila il dato 2, poi viene inserito nella pila il dato 3, poi viene inserito nella pila l’istruzione `OP_ADD` che estrae dalla pila i due dati sottostanti e inserisce nella pila 5.

![[opadd.png]]

#### Pay-to-Public-Key (p2pk)

- [[https://learnmeabitcoin.com/technical/script/p2pk/]]

È il più semplice $\texttt{locking\_script}$ usato in Bitcoin ed è formato da due comandi:
$$
\texttt{OP\_PUSHBYTES\_65 <pk> OP\_CHECKSIG}
$$
dove il comando $\texttt{<pk>}$ è una public key. Il secondo, $\texttt{OP\_CHECKSIG}$ è un istruzione (chiamata anche $\texttt{OP\_CODE}$) che estrae dalla pila i due comandi sottostanti e verifica se il secondo è un firma valida della transazione rispetto alla chiave pubblica contenuta nel primo dato, in caso affermativo inserisce $\texttt{TRUE}$ nella pila, altrimenti inserisce $\texttt{FALSE}$.

*NOTA:* $\texttt{OP\_PUSHBYTES\_X}$ è un $\texttt{OP\_CODE}$ che dice all'interprete che i prossimi $X$ bytes devono essere inseriti nella pila. 
- $X = 65$ è la dimensione di una chiave pubblica *non compressa*.
- $X = 33$ è la dimensione di una chiave pubblica *compressa*.

Se una transazione $\texttt{tx}_{a}$ ha un output $\texttt{tx}_a.\texttt{output}$ con un $\texttt{locking\_script}$ di questo tipo, allora per spendere quell’output una transazione $\text{tx}_{b}$ dovrà avere un input con un $\texttt{unlocking\_script}$ costituito da un solo comando
$$
\texttt{OP\_PUSHBYTES\_72 <sig>}
$$
In modo che la concatenazione di $\texttt{tx}_{b}\texttt{.input.unlocking\_script}$ con $\texttt{tx}_{a}\texttt{.output.locking\_script}$ sia
$$\texttt{<sig> <pk> OP\_CHECKSIG}$$
e l’interprete Script che esegue lo script avrà sullo stack alla fine dell’esecuzione $\texttt{TRUE}$ o $\texttt{FALSE}$ a seconda che $\texttt{<sig>}$ sia oppure no una firma della transazione $\texttt{tx}_{b}$ valida rispetto alla chiave pubblica $\texttt{<pk>}$.

![[p2pk.png]]

Si noti che $\texttt{<sig>}$ non può contemporaneamente essere parte della transazione $\text{tx}_b$ ed essere una firma valida per $\text{tx}_b$ stessa (si creerebbe una dipendenza circolare).

Più precisamente, affinché lo script inserito in una transazione $\text{tx}_b$ restituisca $\texttt{TRUE}$, $\texttt{<sig>}$ deve essere una firma valida della copia serializzata di $\text{tx}_b$ in cui, nel campo $\texttt{tx}_{b}.\texttt{input.unlocking\_script}$ dell'input corrente, viene temporaneamente inserito l'intero $\texttt{locking\_script}$ dell'output precedente che si sta spendendo (ossia $\texttt{<pk> OP\_CHECKSIG}$), mentre gli altri input hanno script vuoto.

Quindi, per firmare la transazione $\text{tx}_b$, si genera una copia della transazione con questo $\texttt{locking\_script}$ temporaneo, se ne calcola l'hash crittografico (unitamente al byte di $\texttt{SIGHASH}$), si esegue la firma e infine si assegna $\texttt{<sig>}$ al vero $\texttt{tx}_{b}.\texttt{input.unlocking\_script}$ prima della trasmissione.

#### Pay-to-Public-Key-Hash (p2pkh)

- [[https://learnmeabitcoin.com/technical/script/p2pkh/]]

Tutte le prime transazioni di Bitcoin avevano negli output dei $\texttt{locking\_script}$ del tipo $p2pk$. Una volta inviata una transazione contenente uno script di quel tipo, la chiave pubblica quindi diventa nota a tutti, e i bitcoin associati a quella chiave pubblica sono protetti "soltanto" dallo schema di firma digitale *ECDSA*.

Se qualcuno dovesse riuscire a trovare un metodo per risalire a una
chiave privata partendo da una chiave pubblica potrebbe spendere i bitcoin di quell’output. 
Per fornire un ulteriore livello di protezione, sin dalle origini il sistema Bitcoin prevede $\texttt{locking\_script}$ cosiddetti $\texttt{Pay-to-Public-Key-Hash}$ ($p2pkh$) (la prima transazione con un output di questo tipo si trova nel blocco 728).

In questo tipo di locking script non compare direttamente
la chiave pubblica, ma l’hash della chiave pubblica $\texttt{<pkhash>}$. 
L'$\texttt{unlocking\_script}$ necessario per spendere un tale output deve contenere sia la chiave pubblica il cui hash corrisponde a quello nel
$\texttt{locking\_script}$, sia una firma valida rispetto a quella chiave pubblica. 

In questo modo la chiave pubblica non viene resa nota a tutti nel momento in cui la transazione con il locking script viene
inviata alla rete, ma soltanto quando quell’output viene speso.
Un $\texttt{locking\_script (ScriptPubKey)}$ del tipo $p2pkh$ è formato dai seguenti comandi:
$$
\begin{align}
&\texttt{OP\_DUP} \\
&\texttt{OP\_HASH160} \\
&\texttt{OP\_PUSHBYTES\_20} \\
&\texttt{<pkhash>} \\
&\texttt{OP\_EQUALVERIFY } \\
&\texttt{OP\_CHECKSIG}
\end{align}
$$
Un $\texttt{unlocking\_script (ScriptSig)}$ del tipo $p2pkh$ è formato dai seguenti comandi:
$$
\begin{align}
&\texttt{OP\_PUSHBYTES\_72} \\  
&\texttt{<sig>} \\
&\texttt{OP\_PUSHBYTES\_33} \\
&\texttt{<pk>} \\
\end{align}
$$

*NOTA:* La chiave pubblica fornita nello $\texttt{ScriptSig}$ può essere sia compressa (33 bytes) che non compressa (65 bytes).
È possibile utilizzare entrambi all'interno di un P2PKH, purché si utilizzi lo stesso formato della chiave pubblica impiegato per creare l'hash della chiave pubblica nello ScriptPubKey.

- $\texttt{OP\_DUP}:$ è un istruzione che inserisce nello stack una copia dell'elemento sottostante.
- $\texttt{OP\_HASH160}:$ *estrae* dallo stack l'elemento sottostanto ed effettua $\texttt{ripemd160(sha256(el))}$. 
- $\texttt{OP\_EQUALVERIFY}:$ estrae due elementi sottostanti dallo stack e se sono uguali non fa nulla, altrimenti interrompe l'esecuzione dello script dichiarando la transizione invalida.

Quindi, lo script $p2pkh$ effettua questo:
- La chiave pubblica originale viene duplicata con l'operazione $\texttt{OP\_DUP}$ e successivamente viene creato l'hash con OP_HASH160.
- Questo valore sottoposto a hash viene confrontato con l'hash della chiave pubblica contenuto in $\texttt{ScriptPubKey}$ per verificare che siano uguali con $\texttt{OP\_EQUALVERIFY}$.
- Se corrisponde, lo script prosegue e $\texttt{OP\_CHECKSIG}$ verifica la firma rispetto alla chiave pubblica, inserendo un $\texttt{OP\_1}$ nello stack se è valida (proprio come uno script P2PK).

#### Pay-to-Multi-Sig (p2ms)

- [[https://learnmeabitcoin.com/technical/script/p2ms/]]

Ci sono situazioni reali nelle quali è necessario che la possibilità di spendere un determinato valore sia vincolata all’accordo di due o più persone.
Nei $\texttt{locking\_script}$ del tipo $p2pk$ e $p2pkh$ chiunque conosca la chiave segreta associata alla chiave pubblica con cui è stato creato il $\texttt{locking\_script}$ puà spendere quell’output. 
Questo problema potrebbe essere risolto con uno dei sistemi che si trovano in letteratura, per generare in modo congiunto una chiave segreta fra $n$ partecipanti che sia utilizzabile solo se un sottoinsieme di $t$ partecipanti collaborano (_threshold cryptography_, *shamir secret sharing*). 
In Bitcoin c’è un $\texttt{locking\_script}$ dedicato a questo, chiamato $\texttt{Pay-to-Multisig}$ ($p2ms$), nel quale si può inserire il numero $n$ di
partecipanti, le $n$ chiavi pubbliche e la *threshold* $t$, e per spendere l’output è necessario inviare un $\texttt{unlocking\_script}$ che contenga $t$ firme valide rispetto a $t$ delle $n$ chiavi pubbliche contenute nel $\texttt{locking\_script}$.
Per esempio, un $\texttt{locking\_script}$ $p2ms$ che richieda 2 firme valide su 3 per essere speso sarà fatto così:
$$
\begin{align}
&\text{OP\_2} \\
&\text{OP\_PUSHBYTES\_65} \\  
&\text{<pk>} \\
&\text{OP\_PUSHBYTES\_65} \\
&\text{<pk>} \\
&\text{OP\_PUSHBYTES\_65} \\  
&\text{<pk>} \\
&\text{OP\_3} \\
&\text{OP\_CHECKMULTISIG} \\
\end{align}
$$

Lo $\texttt{unlocking\_script}$ corrispondente dovrà contenere due firme della transazione, valide rispetto a due delle tre chiavi pubbliche inserite nel $\texttt{locking\_script}$:
$$
\begin{align}
&\texttt{OP\_0} \\  
&\texttt{OP\_PUSHBYTES\_72} \\  
&\texttt{<sig>} \\
&\texttt{OP\_PUSHBYTES\_72} \\
&\texttt{<sig>} \\
\end{align}
$$

*NOTA:* $\texttt{OP\_CHECKMULTISIG}$ ha un bug dove estrae dalla pila un valore in più, per questo ne aggiungiamo uno "dummy" $\texttt{OP\_0}$.

#### Pay-to-Script-Hash (p2sh)

- [[https://learnmeabitcoin.com/technical/script/p2sh/]]

Nei $\texttt{locking\_script}$ di tipo $p2ms$ è chi crea l’output (il mittente dei fondi) che deve includere nella transazione le condizioni con cui quell’output possa essere successivamente speso. 
Per poter affidare questo onere al destinatario dei fondi invece che al mittente, sono stati successivamente introdotti gli script $\texttt{Pay-to-Script-Hash}$ ($p2sh$). Con $p2sh$ è il destinatario dell’output che crea lo script con le condizioni di spesa (chiamato *redeem script*) e invia al mittente soltanto l’hash di questo script; il mittente include quindi questo hash nel $\texttt{locking\_script}$ dell’output della transazione senza sapere quale sia il *redeem script* che corrisponde a quell’hash.
Quando il destinatario vuole spendere l’output deve includere nello $\texttt{unlocking\_script}$ il *redeem script*.

Un $\texttt{locking\_script}$ del tipo $p2sh$ è formato semplicemente dai seguenti comandi:
$$
\texttt{OP\_HASH160 OP\_PUSHBYTES\_20 <redeemScritpHash> OP\_EQUAL}
$$

L'$\texttt{unlocking\_script}$ corrispondente deve includere il redeem script il cui hash è $\texttt{<redeemScritpHash>}$ e le corrispondenti condizioni che rendono $\texttt{TRUE}$ quello script. Quando un nodo Bitcoin riceve una transazione con un input che spende un output $p2sh$, il nodo esegue prima un controllo sull’hash del *redeem script* per verificare che corrisponda a quello specificato nell’output; successivamente esegue il *redeem script* stesso per validare le condizioni di spesa.

#### OP_RETURN

Siccome la Blockchain di Bitcoin è un registro permanente e immutabile replicato su decine di migliaia di nodi, gli utenti hanno cominciato ad usarlo per "salvare" dei dati, per esempio includendo
nei $\texttt{locking\_script}$ delle sequenze di byte che non corrispondevano a delle chiavi pubbliche, ma codificavano dei dati

L’istruzione $\texttt{OP\_RETURN}$ è stata introdotta per consentire l’inserimento di dati arbitrari nella blockchain in modo esplicito, senza creare output che formalmente risulterebbero spendibili anche
se di fatto non lo sono, andando a "sporcare" lo UTXO set. 

Dal punto di vista operativo, uno script che contiene $\texttt{OP\_RETURN}$ termina immediatamente la propria esecuzione restituendo un fallimento nel momento in cui l’istruzione op return viene eseguita. Tipicamente, un $\texttt{locking\_script}$ di questo tipo ha la forma
$$\texttt{OP\_RETURN <data>}$$
dove $\texttt{<data>}$ è una sequenza di byte che viene semplicemente inserita nella transazione. Poichè lo script fallisce sempre quando eseguito, non esiste uno unlocking script che possa sbloccare tale output per cui l’output non viene mantenuto dai nodi nello UTXO set.
### Addresses

TODO: DA FARE

### Rete Bitcoin

**DOMANDA:** Cosa succede quando un nuovo nodo si unisce alla rete Bitcoin?

- [[https://learnmeabitcoin.com/technical/networking/node/]]


## SegWit


