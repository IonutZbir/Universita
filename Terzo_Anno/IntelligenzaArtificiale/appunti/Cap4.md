# Capitolo 4 Ricerca in ambiento complessi

## 4.1 Ricerca Locale e problemi di ottimizzazione

Gli algoritmi di ricerca locale sono una classe di metodi usati per risolvere problemi in cui ci si sposta da uno stato a un altro cercando miglioramenti graduali, senza memorizzare il percorso compiuto o gli stati visitati.

Gli algoritmi di ricerca locale sono **non sistematici**, ovvero:

- Non tengono tracci degli stati già visitati.
- Non garantiscono di esplorare tutto lo spazio degli stati, potrebbero quindi ignorare parti importanti dove si trova una soluzione migliore. Questo li distingue dagli algoritmi sistematici, come A*, che esplorano lo spazio in modo organizzato.

Tali algoritmi fanno **uso di poca memoria** in quanto memorizzano solo lo stato corrente e quello adiacente da valutare, rendendoli ideali per spazi di stati molto grandi. Spesso trovano buone soluzioni anche in spazi di stati enormi o infiniti, dove gli algoritmi sistematici sarebbero impraticabili. Sono particolarmente utili per problemi di ottimizzazione, dove si cerca uno stato che massimizzi o minimizzi una funzione obiettivo.

### 4.1.1 Ricerca hill climbing

L'algoritmo di ricerca **hill climbing** tiene traccia di un solo stato corrente e a ogni iterazione passa allo stato vicino con valore più alto, cioè punta nella direzione che presenta l'ascesa più ripida senza guardare oltre gli stati immediatamente vicini a quello corrente.
L’algoritmo hill climbing viene talvolta chiamato **ricerca locale greedy**, perché sceglie uno stato vicino “buono” senza pensare a come andrà avanti.
Sfortunatamente, spesso l’hill climbing rimane bloccato per le seguenti ragioni:

```javascript
    function HILL-CLIMBING(problema) returns uno stato che è un massimo locale
    corrente = problema.STATO_INIZIALE
    while true do
        vicino = lo stato successore di corrente di valore più alto
        if VALORE(vicino) <= VALORE(corrente) then return corrente
        corrente = vicino
```

- **massimi locali**: un massimo locale è un picco più alto degli stati vicini, ma inferiore al massimo globale. Gli algoritmi hill climbing che raggiungono la vicinanza di un massimo locale saranno attirati verso il picco, ma rimarranno bloccati lì senza poter andare altrove.
- **creste**: le creste danno origine a una sequenza di massimi locali molto difficili da esplorare da parte degli algoritmi greedy.
- **plateu**: un plateau è un’area piatta del panorama dello spazio degli stati. Può essere un massimo locale piatto, da cui non è possibile fare ulteriori progressi, oppure una spalla (shoulder), da cui si potrà salire ulteriormente. Una ricerca hill climbing potrebbe perdersi sul plateau.

![Hill Climbing](img/hill_climbing.png){width=400px, style="display: block; margin: 0 auto"}

Alcuni miglioramenti dell'algoritmo dell'hill climbing:

In ognuno di questi casi, l’algoritmo raggiunge un punto dal quale non riesce a compiere ulteriori progressi. Per esempio per il problema delle 8 regine, risolve solo il 14% delle istanze.

1. Un modo per aumentare tale percentuale è quello di proseguire nella ricerca una volta raggiunto un plateau, consentendo una **mossa laterale** nella speranza che il plateau sia in realtà una spalla ma c'è sempre la possibilià di finire per vagare per un plateau. Possiamo quindi porre un limite al numero di mosse laterali consecutive, per esempio fermandoci dopo 100. Così si aumenta la percentuale di istanze di problemi risolte dall’algoritmo di hill climbing dal 14% al 94%.
2. **Hill climbing stocastico**: sceglie a caso tra tutte le mosse che vanno verso l’alto: la probabilità della scelta può essere influenzata dalla “pendenza” delle mosse. Normalmente questo algoritmo converge più lentamente di quello
che sceglie sempre la mossa più conveniente, ma in alcuni panorami di stati è capace di trovare soluzioni migliori.
3. **Hill climbing con prima scelta** implementa la precedente versione stocastica generando casualmente i successori fino a ottenerne uno preferibile allo stato corrente. Questa strategia è molto buona quando uno stato ha molti successori (per esempio migliaia).
4. **Hill climbing con riavvio casuale**, l’algoritmo conduce una serie di ricerche hill climbing partendo da stati iniziali generati casualmente, fino a quando raggiunge un obiettivo. È completo con probabilità 1, perché prima o poi dovrà generare, come stato iniziale, proprio un obiettivo. Se ogni ricerca hill climbing ha una probabilità $p$ di successo, il numero atteso di riavvii richiesti è $1/p$.

### 4.1.2 Simulated annealing

L'algoritmo **simulated annealing** cerca di combinare in qualche modo l’hill climbing con un’esplorazione casuale in modo da ottenere sia l’efficienza che la completezza.

La struttura complessiva dell’algoritmo simulated annealing è simile a quella dell’hill climbing: stavolta però, invece della mossa migliore, viene scelta una mossa casuale. Se la mossa migliora la situazione, viene sempre accettata; in caso contrario l’algoritmo la accetta con una probabilità inferiore a 1. La probabilità $p$ è inversamente proporzionale al peggioramento
e $T$ descresce col progredire dell’algoritmo (quindi anche $p$) secondo un piano definito.

```javascript
function SIMULATED-ANNEALING (problema, velocità_raffreddamento) returns uno stato soluzione
    corrente = problema.STATO_INIZIALE
    for t = 1 to ∞ do
        T = velocità_raffreddamento[t]
    if T = 0 then return corrente
        successivo = un successore scelto a caso di corrente
    Delta_E = VALORE(corrente) – VALORE(successivo)
    if Delta_E > 0 then corrente = successivo
    else corrente = successivo solo con probabilità pow(e, -Delta_E/T)
```

### 4.1.3 Ricerca local beam

L’algoritmo di ricerca local beam tiene traccia di $k$ stati anziché uno solo. All’inizio comincia con $k$ stati generati casualmente: a ogni passo, sono generati i successori di tutti i $k$ stati. Se uno qualsiasi di essi è un obiettivo, l’algoritmo termina; altrimenti sceglie i $k$ successori migliori dalla lista di tutti i successori e ricomincia.

La **ricerca beam stocastica**, analoga all’hill climbing stocastico, invece di scegliere i migliori $k$ successori, in questo caso si scelgono i successori con probabilità proporzionale al loro valore, aumentando così la diversificazione.

## 4.3 Ricerca con azioni non deterministiche
