Vedremo ora come **costruire** un [[Inverted Index]].
Questo processo è noto come **index construction** o **indexing** (**indicizzazione**).

Generalmente quando si progetta un sistema di IR lo si fa in base alle caratteristiche hardware sul quale dovrà essere implementato.

|  Symbol  | Statistic                                        | Value                                        |
| :------: | ------------------------------------------------ | -------------------------------------------- |
| $\sigma$ | average seek time                                | $5 \text{ ms} = 5 \times 10^{-3} \text{ s}$  |
|   $b$    | transfer time per byte                           | $0.02 \; \mu s = 2 \times 10^{-8} \text{ s}$ |
|   $p$    | lowlevel operation (e.g., compare & swap a word) | $0.01 \; \mu s = 10^{-8} \text{ s}$          |
|    \     | sizo of main memory                              | several Gb                                   |
|    \     | size of disk space                               | 1 Tb or more                                 |


Bisogna infatti tenere conto delle seguenti proprietà dell'hardware:
1. L'accesso alla memoria è ordini di grandezza più veloce rispetto all'accesso su disco. Di conseguenza vogliamo tenere in memoria quanti più dati possibili, specialmente quei dati per i quali abbiamo bisogno di frequente accesso. La tecnica di tenere in memoria i dati più frequentemente accessi è anche detta **caching**.
2. Quando bisogna fare una operazione di lettura o scrittura su disco, bisogna attendere il tempo necessario affinché la testa del disco si allinei col settore del disco interessato. Tale tempo è detto **seek time** e dura mediamente 5 ms. Perciò, per massimizzare la quantità di dati letti/scritti, è desiderabile che dati che vengono accessi insieme siano salvati in regioni di memoria *consecutive*. ^31e9e5
3. Le operazioni di lettura e scrittura da disco sono delegate al **sistema operativo**, il quale generalmente legge/scrive un intero blocco di memoria, anche se dobbiamo accedere a un singolo byte.
4. Il trasfetimento dei dati dal disco alla memoria è delegato al **bus dati** e non al processore. Perciò durante tali operazioni il processore è libero di processare altri dati.
5. I server usati per i sistemi di IR hanno spesso a disposizione decine di GB di memoria, e uno spazio di archiviazione <u>potenzialmente</u> illimitato.

I problemi che generalmente possiamo trovare nello sviluppo di un indice sono:
1. non abbiamo a disposizione abbastanza RAM per costruire l'intero indice e quindi dobbiamo aiutarci con il disco.
2. non abbiamo a disposizione nemmeno abbastanza spazio su disco per il nostro indice, e quindi abbiamo bisogno di implementarlo in maniera **distribuita**.
3. abbiamo bisogno di generare un indice che sia **dinamico**, ovvero che consenta nella maniera più efficiente possibile di effettuare operazioni di rimozione, inserimento e modifica dei documenti.

- [[Blocked sort-based indexing]] - BSBI
- [[Single-pass in-memory indexing]] - SPIMI
- [[Distributed indexing]]
- [[Dynamic indexing]]