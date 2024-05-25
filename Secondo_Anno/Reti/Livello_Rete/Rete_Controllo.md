# Livello di rete, piano di controllo

## Introduzione

Nel piano di controllo, il router ha il ruolo di determinare il percoso seguito dai pacchetti dalla sorgente alla destinazione (**Instradamento**).

Ci sono due approcci per eseguire l'istradamento:

- *Controllo per router*: Ogni router ha una componente di instradamento che comunica con le componenti di instradamento degli altri router per calcolare la propria tabella di inoltro (protocolli OSFP e BGP).
- *Controllo logicamente centralizzatoé (SDN)*: Controller logicamente centralizzato calcola e distribuisce le tabelle di inoltro che devono essere utilizzate da ogni router.

## Algoritmi di instradamento

L'obiettivo di tali algoritmi è di determinare percorsi (sequenze di router) o cammini "buoni", di solito quelli di costo minimo tra le sorgenti e i destinatari attraverso la rete dei router.

Per analizzare il problema dell'instradamento, consideriamo un grafo $G = (V, E)$ non orientato dove $V$ è l'insieme dei nodi, che nel contesto dell'instradamento rappresentano i router e $E$ è l'insieme dei archi, ovvero i collegamenti fisici tra i router.

<img src="img/grafo.pnf" width="300" />

Per ogni arco $(x, y)$ tra i nodi $x, y$ denotiamo con $c(x, y)$ il costo di tale collegamento (arco). Poniamo $c(x, y) = +\infty$ se l'arco $(x, y) \notin E$. L'obiettivo è dunque quello di trovare il percorso di costo minimo tra due nodi.

- Un **algoritmo di instradamento centralizzato** calcola il percorso a costo minimo tra una sorgente e una destinazione avendo una conoscenza globale e completa della rete. In altre parole, l’algoritmo riceve in ingresso tutti i collegamenti tra i nodi e i loro costi. Questi algoritmi sono detti **algoritmi link-state**.
- In un **algoritmo di instradamento decentralizzato** il percorso a costo minimo viene calcolato in modo distribuito e iterativo. Nessun nodo possiede informazioni complete sul costo di tutti i collegamenti di rete. Inizialmente i nodi conoscono soltanto i costi dei collegamenti a loro incidenti. Questi algoritmi sono detti **algoritmi distance-vector**.

### Instradamento "link-state", algoritmo di Dijkstra

In un instradamento link-state la topologia di rete e tutti i costi dei collegamenti sono noti, ossia disponibili in input all’algoritmo. Ciò si ottiene facendo inviare a ciascun nodo pacchetti sullo stato dei suoi collegamenti a tutti gli altri nodi della rete. Questi pacchetti contengono identità e costi dei collegamenti connessi al nodo che li invia.

L’algoritmo di calcolo dei percorsi che presentiamo associato all’instradamento link-state è noto come **algoritmo di Dijkstra**. (Vedi lezione algoritmi!!!)

### Instradamento "distance-vector", algortimo di Bellman-Ford