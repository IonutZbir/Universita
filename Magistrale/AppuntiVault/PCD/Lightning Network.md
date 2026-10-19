Il problema principale di Bitcoin è la **scalabilità:** la dimensione e il tempo medio di creazione dei blocchi limitano fortemente il numero di transazioni che possono essere registrare sulla blockchain.

- Con SegWit la size di un blocco è aumentata (circa 4 MB) e il numero di transazioni che possono essere registrate all'interno è aumentato di qualche migliaio.
- Rispetto però ai metodi classici di pagamento (VISA, MasterCard), il numero di transazioni al secondo è comunque molto basso rispetto al numero di transazioni gestite dai metodi classici.

Per questa ragione si distingue tra **Bitcoin (Layer 1)** che è la blockchain stessa e soluzioni **Layer 2** che sono protocolli costruiti sopra il layer 1 che non registrano ogni pagamento sulla blockchain permettendo quindi di aumentare notevolmente il numero di transazioni al secondo.

**DEF:** La *Lightning Network* è una soluzione Layer 2 che permette di effettuare molti pagamenti off-chain, usando la blockchain solo in alcuni momenti chiave. I pagamenti tra due parti avviene mediante i cosidetti *canali di pagamanto*.

Possiamo pensare alla Lightning Network come un contratto:
- 2 parti, Alice e Bob decidono di aprire un canale di pagamento depositando una certa quantità di Bitcoin;
- Finché entrambi seguono correttamente il contratto, possono aggiornare privativamente il proprio bilancio senza coninvolgere la blockchain;
- Appena uno dei due non rispetta il contratto, entra in gioco la blockchain e il protocollo fa in modo di *punire* chi non rispetta le regole.

*GOAL:* Definire una rete di canali di pagamento tra più entità.
```
Alice <-> Bob
Alice <-> Bob <-> Carol
```
Quindi se Alice deve effettuare un pagamento a Carol, non deve necessariamente aprire un canale diretto con Carol, ma può usufruire del canale tra Bob e Carol.

## Funding, Refunding & Commitment Transaction

Supponiamo che Alice e Bob vogliano aprire un canale di pagamento tra di loro di $x$ BTC.
- $x$ rappresenta la *capacità del canale*. È la quantità di fondi bloccati nel canale. Questa informazione è visibile a tutti in quanto deriva dalla funding transaction.
- I successvi aggiornamenti del bilancio invece avvengono tramite messaggi privati non venendo quindi resi pubblici. Solo alla chiusura del canale, un'unica transazione verrà pubblicata sulla blockchain riflettendo l'ultimo stato del canale.

Lo scopo del protocollo è **fare in modo che ogni aggiornamento del bilancio sia sicuro: nessuna delle due parti deve poter pubblicare uno stato vecchio e per lui vantaggioso senza rischiare una penalizzazione.**

Quindi, per aprire il canale, Alice deve costruire una *Funding Transaction*, la quale prende in input $x$ BTC che Alice possiede già sulla blockchain e come output un *multisig 2-of-2* spendibile solo con la firma sia di Alice che di Bob.

Banalmente, uno script (semplificato) di questo tipo potrebbe essere:
```python
scriptPubKey (locking_script)
2 <pkA> <pkB> 2 OP_CHECKMULTISIG

scriptSig (unlocking_script)
0 <sigA> <sigB>
```

Definito in questo modo, abbiamo il seguente problema:
1. Se Alice dovesse pubblicare la FundingTx sulla blockchain, i suoi $x$ BTC finirebbero in un output spendibile soltanto con la firma sua e di Bob. Ma se Bob dovesse perdere la sua chiave segreta o decidesse di non colaborare, questi $x$ BTC andrebbero persi per sempre.

Serve quindi un meccanismo che permetta di rendere le transazioni revocabili da un punto di vista economico, ma poiché in Bitcoin, una transazione una volta inserita nella blockchain non può essere revocata, l'idea di revocabilità deve essere implementata con il concetto di punizione.

La revoca consiste nel dare la possibilità all'altra parte di punire chi non segue il contratto prendendosi tutti i fondi.

Questa è l'idea alla base della *Refunding Transaction* e delle *Commitment Transactions*.

Prima di procedere con le transazioni, introduciamo l'$\texttt{OP\_CODE}$ $\texttt{OP\_CHECKSEQUENCEVERIFY}$, che permette di imporre un vincolo temporale sulla spesa di una vecchia transazione: *un certo output può essere speso solo dopo che è passato un certo numero di blocchi da quello in cui la transazione è stata confermata.*
Ad esempio
$$
\texttt{10 OP\_CHECKSEQUENCEVERIFY OP\_DROP TRUE}
$$
indica che l'output con questo $\texttt{scriptPubKey}$ può essere speso solo dopo che sono passati almeno 10 blocchi da quello nella quale la transazione è stata inserita e confermata. Quindi
- $\texttt{OP\_CHECKSEQUENCEVERIFY}$ controlla che la differenza tra il blocco attuale e quello della transazione sia almeno 10;
- In caso affermativo non fa nulla e $\texttt{OP\_DROP}$ rimuove il 10 dallo stack, rimanendo solo $\texttt{TRUE}$ sullo stack valindando la transazione.

### Funding & Refunding TX

A questo punto possiamo definire la Funding e la Refunding TX. Lo schema è il seguente:

Supponiamo che Alice abbia $x$ BTC chiusi all'interno di UTXO controllabili interamente da lei.

1. Alice *prepara la FundingTx* senza inserirla nella blockchain.
```
FundingTx, txId: 123...ff
Input: fondi precedenti di Alice nella blockchain
Output: x BTC spendibili da pkA & pkB (multisig 2-of-2)
```
2. Alice *genera* una *coppia di chiavi* $(sk_{AR0}, pk_{AR0})$ di *revoca*.
3. Alice *prepare la RefundingTx* che spende l'output della FundingTX.
```
RefundingTx, txId: 33...ef
Input: output FundingTx, txId: 123...ff
Output: x BTC spendibili da:
	- pkA dopo n blocchi
	- pkB & pkAR0 (subito, multisig 2-of-2)
```
4. Bob *firma la RefundingTx* e la invia ad Alice. Ricevuta questa firma Alice pubblica sulla blockchain la *FundingTx*, aprendo così il canale.

Ora che Alice ha in mano la RefundingTx già firmata da Bob, è al sicuro:
- Alice trasmette la *FundingTx* alla blockchain.
- *Garanzia di uscita unilaterale:* se in qualsiasi momento Bob dovesse sparire o rifiutarsi di collaborare, ad Alice basterà apporre la propria firma con $sk_A$ sulla RefundingTx, pubblicarla sulla rete, attendere $n$ blocchi e riappropriarsi interamente dei suoi $x$ BTC creando una nuova transazione che spende quel input.

La seconda condizione dell'output entra in gioco al primo aggiornamento del bilancio (ad esempio quando Alice paga Bob):

- Per rendere definitivo il nuovo bilancio, Alice ha l'obbligo contrattuale di rivelare a Bob la chiave segreta di revoca $sk_{AR0}$.
- Da quel momento la vecchia RefundingTx diventa *economicamente revocata:
    - Se Alice tentasse di fare la furba pubblicando la vecchia RefundingTx per riprendersi tutti gli $x$ BTC, dovrebbe comunque attendere $n$ blocchi prima di poter muovere i fondi.       
    - Bob, conoscendo ora sia la propria chiave $sk_B$ sia la chiave rivelata $sk_{AR0}$, può spendere l'output *immediatamente*, senza attendere. Durante la finestra di $n$ blocchi, Bob pubblicherà una transazione di penalità firmata con entrambe le chiavi confiscando l'intero importo e lasciando Alice a mani vuote.

*NOTA:* Implementazione con $\texttt{OP\_CODE}$ dei due rami.
- $\texttt{OP\_IF}$: Se nello stack incontra $\texttt{TRUE}$ esegue questo ramo;
- $\texttt{OP\_ELSE}$: Se nello stack incontra $\texttt{FALSE}$ esegue questo ramo;

```
ScriptPubKey:
OP_IF
    2 <pkAR0> <pkB> 2 OP_CHECKMULTISIG
OP_ELSE
    <n> OP_CHECKSEQUENCEVERIFY OP_DROP <pkA> OP_CHECKSIG
OP_ENDIF

ScriptSig Bob:
0 <sigAR0> <sigB> TRUE

ScriptSig Alice:
<sigA> FALSE
```

### Commit Tx

Quindi, una volta aperto il canale di pagamento pubblicando la FundingTx, lo stato del canale è il seguente:
```
Alice ----------------------- Bob
  x                            0
```
dove,
- Alice ha ancora in mano la RefundingTx firmata da Bob;
- Bob non è ancora a conoscenza di $sk_{RA0}$.

Supponiamo ora che Alice deve pagare $y < x$ BTC, facendo si che lo stato del canale diventi
```
Alice ----------------------- Bob
 x-y                           y
```
Vediamo ora cosa deve succedere e quali transazioni devono essere create.

Per rappresentare questo nuovo stato del canale, vengono create due nuove transazioni chiamata *Commitment Transaction*, una per Alice e una per Bob.

Innanzitutto, sia Alice che Bob generano una coppia di chiavi di revoca:
- *Alice:* $(sk_{AR1},\ pk_{AR1})$;
- *Bob:* $(sk_{BR1},\ pk_{BR1})$;

Entrambe le transazioni spendono lo stesso output della FundingTx ($x$ BTC 2-of-2 multisig).

```
CommitTx1(Alice)
Input: output 2-of-2 multisig della FundingTx
Output:
	1. x-y BTC spendibili da:
		- pkA dopo n blocchi
		- pkAR1 & pkB (subito, multisig 2-of-2) 
    2. y BTC spendibili da pkB (subito)
       
CommitTx1(Bob)
Input: output 2-of-2 multisig della FundingTx
Output:
    1. x-y BTC spendibili da pkA (subito)  
	2. y BTC spendibili da:
		- pkB dopo n blocchi
		- pkBR1 & pkA (subito, multisig 2-of-2) 
```

Quindi
- *CommitTx1(Alice)* è la transazione che tiene in mano Alice e che può pubblicare se vuole chiudere unilateralmente il canale di pagamento nel caso in cui Bob non volesse più collaborare. *Questa transazione è firmata da Bob*.
- *CommitTx1(Bob)* è la transazione che tiene in mano Bob e che può pubblicare se vuole chiudere unilateralmente il canale di pagamento nel caso in cui Alice non volesse più collaborare. *Questa transazione è firmata da Alice*.

Affinché il bilancio sia ufficialmente aggiornato, Alice deve rivelare la sua $sk_{AR0}$ (quella della RefundingTx) a Bob, *revocando* cosi la RefundingTx.

*Analisi CommitTx1(Alice):* Una volta effettuato l'aggiornamento del bilancio, se Bob dovesse sparire Alice firma questa transazione e la pubblica sulla blockchain, aspetta $n$ blocchi, dopodiché può spendere quell'output ottenendo i suoi $x-y$ BTC e Bob i suoi $y$ BTC.
Se invece questa CommitTx1(Alice) diventa vecchia, ossia il canale è stato aggiornato di nuovo e Alice dovesse pubblicare questa transazione, Bob, conoscendo $sk_{AR1}$ può creare una nuova transazione e spendere *subito* gli $x-y$ BTC di Alice.

### Closing TX

**DOMANDA: Cosa avviene alla fine della vita del canale?**
Supponendo che Alice e Bob siano stati collaborativi fino alla fine, allora se si vuole chiudere il canale basta che entrambi collaborino per pubblicare una transazione 2-of-2 multisig di chiusura del canale che spende l'output della FundingTx e che assegna i bitcoin a ciascuno secondo l'ultimo bilancio aggiornato. Questa transazione è detta **Closing Transaction**. Chiaramente se poi nel momento di mandare la firma uno dei due sparisce, allora l'altro può sempre chiudere unilateralmente il canale usando la sua CommitTx più recente, e aspettare $n$ blocchi per prendere i suoi soldi.

Il vantaggio della chiusura collaborativa è che ovviamente non necessita che la parte onesta deve aspettare $n$ blocchi per recuperare i suoi fondi.

#### Diagrammi sequenza di messaggi

![[ln1.png]]

![[ln2.png]]

## HTLC - Hash Time Locked Contracts

Finora abbiamo visto il funzionamento della LN tra due nodi A e B. Vediamo ora come è possibile creare un meccanismo di *routing* dei pagamenti, ossia la possibilità che un nodo A (Alice) paghi un nodo C (Carol) passando per il nodo intermedio B (Bob).

Affinché si possa effettuare l'aggiornamento dei nuovi bilanci *non* devono accadere due cose:
- A paga B ma B non paga C;
- B paga C ma A non paga B;

Per ottenere questa garanzia, la LN utilizza gli HTLC. L'idea alla base è di usare un *segreto* $r$ e il suo hash $\mathcal{H}(r)$ nel seguente modo:

1. Carol (ossia il denstinatario del pagamento) genera un valore casuale segreto $r$ e comunica $h = \mathcal{H}(r)$ ad Alice (il mittente del pagamento);
2. Alice crea un contratto HTLC con Bob il cui ouput è spendibile solo se Bob riesce a mostrare ad Alice una preimmagine $r$ dell'hash $h$;
3. Bob a sua volta crea un contrattto HTLC con Carol il cui output è spendibile se e solo se Carol riesce a mostrare a Bob una preimmagine $r$ dell'hash h;

La logica del meccanismo funziona perché a questo punto Carol può rivelare il segreto $r$ a Bob e incassare il pagamento da Bob. Una volta che ciò accade, Bob può rivelare il segreto ad Alice e incassare l'output ritornando così al bilancio di prima.

Questo meccanisco però non è completo, in quanto se Carol per una qualche ragione non dovesse rivelare il segreto $r$, Alice e Bob si troverebbero in una situazione in cui non potrebbero riprendersi l'ammontare che hanno bloccare negli output precedenti.

Per ovviare a questo problema, gli HTLC combinano in generale due tipologie di condizioni:
- Una condizione basata su **hash**;
- Una condizione basata sul tempo (**time lock**), cioè per cui se il segreto non viene rivelato entro un certo limite di tempo, allora il pagamento può essere reclamato dal mittente.

Da qui il nome **Hash Time Locked Contracts**. Per implemetare tale meccanismo basato sul tempo, si utilizza il seguente $\texttt{OP\_CODE}$:
### $\texttt{OP\_CHECKLOCKTIMEVERIFY}$
Permette di rendere un output spendibile solo dopo un certo tempo o un certo numero di blocchi, in particolare permette di creare script del tipo:
- output spendibile dopo il blocco $x$;
- output spendibile dopo il tempo $t$;
Quando l'interprete Script incontra $\texttt{OP\_CHECKLOCKTIMEVERIFY}$, confronta il valore in cima allo stack con il campo `nLockTime` presente nell'intestazione della transazione che sta spendendo l'output.
Il campo `nLockTime` indica il *momento/blocco* assoluto prima del quale la transazione non può essere validata. Può essere interpretato in due modi:
- Se $\texttt{nLockTime} < 500.000.000$, allora viene interpretato come numero del blocco:
- Se $\texttt{nLockTime} \ge 500.000.000$ allora viene interpretato come timestamp UNIX.

*NOTA:* se il campo `nSequence` è fissato a `0xffffffff` allora `nLockTime` viene ignorato, altrimenti viene considerato attivo.

#### Script con preimmagine e hash

Di seguito lo script che permette di spendere un output solo se si conosce una preimmagine $r$ tale che $\mathcal{H}(r) = h$;
Sia $\mathcal{H} = \texttt{SHA256}$ e sia quindi $\texttt{OP\_SHA256}$ l'opcode che calcola il SHA256 di un dato sullo stack. Allora
```
ScriptPubKey
OP_SHA256 <h> OP_EQUALVERIFY <pk> OP_CHECKSIG

ScriptSig
<sig> <r>

-->
<sig> <r> OP_SHA256 <h> OP_EQUALVERIFY <pk> OP_CHECKSIG
```
Questo script sarà $\texttt{TRUE}$ se e solo se $\texttt{SHA256}(r) = h$ e $\texttt{<sig>}$ è una firma valida per la chiave pubblica $\texttt{<pk>}$.

### Costruzione HTLC

Ora abbiamo tutto il necessario per vedere nel dettaglio il meccanismo.

Tra Alice e Bob c'è un canale di capacità 10 e tra Bob e Carol c'è un canale di capacità 9. Questo significa che sulla blockchain ci sono le funding transaction dei due canali:
```
FundingTx A-B
Input: b8ff...11f0
Output: 10 BTC spendibili da pkA e pkB

FundingTx B-C
Input: 75a2...d41a
Output: 9 BTC spendibili da pkB e pkC
```
 
Supponiamo che il bilancio attuale del canale fra Alice e Bob sia di 8 per Alice e 2 per Bob; mentre il bilancio attuale del canale fra Bob e Carol sia di 4 per Bob e 5 per Carol. Significa che ci sono 4 transazioni off-chain

![[htlc1.png]]

Sia $n$ lo stato attuale del canale $A-B$, allora, per il canale tra Alice e Bob:
```
CommitTx_n(Alice)
Input: FundingTx A-B
Output:
	1. 8 BTC spendibili da 
		- pkA dopo n blocchi
		- pkARN & PkB subito
	2. 2 BTC spendibili da pkB
Firmata da Bob con skB

CommitTx_n(Bob)
Input: FundingTx A-B
Output:
	1. 2 BTC spendibili da 
		- pkB dopo n blocchi
		- pkBRN & PkA subito
	2. 8 BTC spendibili da pkA
Firmata da Alice con skA
```

Sia $m$ lo stato attuale del canale $B-C$, allora, per il canale tra Bor e Carol:
```
CommitTx_m(Bob)
Input: FundingTx B-C
Output:
	1. 4 BTC spendibili da 
		- pkB dopo n blocchi
		- pkBRM & PkC subito
	2. 5 BTC spendibili da pkC
Firmata da Carol con skC

CommitTx_m(Carol)
Input: FundingTx B-C
Output:
	1. 5 BTC spendibili da 
		- pkC dopo n blocchi
		- pkCRM & PkB subito
	2. 4 BTC spendibili da pkB
Firmata da Bob con skB
```

Ora supponiamo che Alice voglia fare un pagamento di 1 BTC a Carol, sfruttando il cammino che passa per Bob. I bilanci dei due canali alla fine del pagamento dovranno quindi essere
![[htlc2.png]]

Quindi, Carol genera un segreto $r$, ne calcola l'hash $h = \mathcal{H}(r)$ e lo invia ad Alice. 

Alice costruisce le seguenti transazioni e chiede a Bob di firmarle:
```
HTLCTxA-B(Alice)
Input: FundingTx A-B
Output:
	1. 7 BTC spendibili da:
		- pkA dopo n blocchi
		- pkB & pkARK (pkARK: chiave di revoca dello stato K)
	2. 2 BTC spendibili da pkB
	3. 1 BTC spendibile da:
		- pkB & pkARK
		- pkB & preimmage r of h
		- pkA & pkB after expiry_time

HTLC-timeoutTX A-B
Input: HTCLTxA-B(Alice) output 3
Output: 1 BTC spendibili da
		- pkA dopo n blocchi
		- pkB & pkARK
```

Analizziamo gli output:
1. Il primo e il secondo output rappresentano quello del classico commitment: servono affiché se Bob sparisse allora Alice può riprendersi i suoi fondi lasciando comunque a Bob i suoi fondi e se Alice dovesse pubblicare questo commit quando ormai è revocata, allora Bob può punirla prendendosi i 7 BTC.
2. Il terzo output rappresenta l'HTLC:
	- Se Alice pubblica questa commit quando ormai è revocata allora Bob può punirla prendendosi anche questo 1 BTC;
	- Se Bob ha ricevuto $r$ da Carol allora Bob aggiorna il suo canale dandole 1 BTC avendo il diritto di incassarlo da Alice. Se Alice pubblica questa transazione prima del timeout, allora Bob se conosce $r$ può incassare questo 1 BTC.
	- Se Bob non conosce $r$ entro l'`expiry_time` e questa transazione non è revocata allora Alice può riprendersi il suo BTC pubblicando la transazione `HTLC-timeoutTX A-B`.

*NOTA:* Perché in `HTLC-timeoutTX A-B` Alice deve aspettare $n$ blocchi? Se Alice pubblica questra transazione dopo che è stata revocata, Bob ha il tempo per punirla.

*NOTA:* Perchè creare `HTLC-timeoutTX A-B` e non mettere tutto insieme in `HTLCTxA-B(Alice)`? Quando HTLC scade, Alice deve essere in grado di congelare la situazione on-chain spendendo l'output 3 traminte `HTLC-timeout`.

La necessità di usare un **multisig 2-of-2 dopo l'_expiry time_** combinato con la **`HTLC-timeoutTx`** (che impone un ritardo relativo di $n$ blocchi) serve a risolvere un problema critico di sicurezza ed evitare una **race condition** in caso di frode.

Supponiamo per assurdo che nell'Output 3 della `HTLCTxA-B - Alice` non ci fosse la transazione ausiliaria a due stadi, ma una clausola diretta del tipo:
$$\text{spendibile da } pk_A \text{ dopo l'expiry time } x$$
Cosa accadrebbe se questo stato del canale diventasse vecchio e venisse **revocato** (cioè Alice ha rivelato a Bob la chiave di revoca $sk_{Ara}$)?
- Se Alice agisce disonestamente e pubblica questa vecchia transazione dopo che il blocco $x$ è già passato, si troverebbe di fronte a due rami contemporaneamente validi per l'Output 3:
    1. Bob può spendere l'output con la revoca ($pk_B \ \& \ pk_{Ara}$).
    2. Alice può spendere l'output con la sua chiave ($pk_A$), poiché il tempo $x$ è già scaduto.
- Poiché entrambi potrebbero spendere **subito**, si creerebbe una **corsa nella mempool (_race condition_)**: Alice potrebbe offrire una fee più alta a un miner, facendosi confermare la transazione prima di Bob e riuscendo a rubare l'$1\text{ BTC}$ nonostante la revoca.


Bob costruisce le seguenti transazioni e ad Alice di firmarle:
```
HTLCTxA-B(Bob)
Input: FundingTx A-B
Output:
	1. 7 BTC spendibili da pkA
	2. 2 BTC spendibili da:
	   - pkB dopo n blocchi
	   - pkA & pkBRK
	3. 1 BTC spendibile da:
		- pkA & pkBRK
		- pkA after expiry_time
		- pkA & pkB

HTCT-successTX A-B
Input: HTCLTxA-B(Bob) output 3
Output: 1 BTC spendibili da
		- pkB & preimmage r of h dopo n blocchi
		- pkA & pkBRK
```

Questa transazione serve a Bob nel caso in cui Alice pubblicasse `HTLCTxA-B(Alice)` dopo `expiry_time` e ancora non ha ricevuto $sk_{ARK}$.
Infatti, analizzando gli output:
1. Per il primo e secondo ouput vale lo stesso discorso di prima;
2. Il terzo output riguarda il caso in cui la revocation key deve favorire Alice dal momento che il commitment è di Bob:
	- 1 BTC ad Alice se Bob l'ha pubblicata quando è revocata;
	- 1 BTC ad Alice se Bob prova a pubblicarla non conoscendo $r$ entro `expiry_time`; In questo caso Alice aspetta che si sblocchi l'output per riprendersi il suo BTC.
	- Se la transazione non è stata revocata entro `expiry_time` allora Bob può creare `HTCT-successTX A-B` per poter incassare il BTC dopo $n$ blocchi se conosce la preimmagine $r$.

Ricapitolando, si deve gestire il caso in cui Bob non abbia mostrato $r$ ad Alice entro `expiry_time`. In questo caso Alice può pubblicare la sua HTLC e HTLC timeout, ma solo dopo $n$ blocchi può recuperare i suoi fondi in modo da tutelare Bob.
Analogamento, Bob deve poter recuperare i suoi fondi se ha risolto il contratto con Carol ricevendo $r$ ma Alice non collabora.

Per quel che riguarda il canale tra Bob e Carol, la costruzione è esattamente la stessa, con la differenza che è Bob a essere il mittente e Carol la destinataria.

###  Timelock

È importante precisare che non possiamo mettere lo stesso timelock nel canale A-B e nel canale B-C.
Infatti, se Alice desse un timelock di un'ora a Bob per ricevere $r$, è chiaro che Bob non può usare lo stesso timelock anche per Carol perché se Carol gli rivelasse $r$ all'ultimo, Bob non avrebbe il tempo per rivelare $r$ ad Alice prima che scada il suo timelock, e quindi Bob sarebbe in competizione con Alice nella pubblicazione dell'HTLC.

In generale Bob metterà sempre un timelock pià corto nel canale con Carol rispetto a quello che Alice gli ha messo nel canale con lui, quindi:
- Alice - Bob: $\texttt{expiry\_time} = x$;
- Bob - Carol: $\texttt{expiry\_time} = x - \Delta$;
dove $\Delta$ è un margine di sicurezza che serve a Bob per avere il tempo di reagire se Carol non gli rivelasse $r$ entro il timeout previsto.
In quel caso Bob non ha mai aggiornato il suo canale con Carol. Tuttavia non può nemmeno dimostrare ad Alice che Carol non gli ha rivelato $r$, quindi Alice aspetta il timeout impostato nel canale A-B per poi pubblicare HTLC e HTLC-timeout per recuperare i suoi fondi.