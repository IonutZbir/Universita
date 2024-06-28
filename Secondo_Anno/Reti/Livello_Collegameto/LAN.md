# LAN

LAN (Local Area Network) è una rete locale di dipositivi, per esempio la rete di casa, della scuola etc.

In base al livello in cui ci troviamo la LAN è vista come:

- A livello di rete la LAN è vista come una **sottorete**.
- A livello di collegamento la LAN è vista come una **rete**.

Le LAN sono sia Ethernet, quindi cablate e anche wireless, si pensi alla rete di casa propria in cui c'è il WI-FI.

A livello di rete abbiamo visto che ogni host possiede un indirizzo IP che sia a 32 o 128 bit.
A livello di collegamento ciascun interfaccia possiede un indirizzo MAC (Medium Access Control), che appunto è associato ad ogni interfaccia, ovvero ad ogni scheda di rete. L'indirizzo MAC è un numero a 48 bit espresso in esadecimale e a differenza dell'indirizzo IP che può cambiare, l'indirizzo MAC accompagna il dispositivo dalla nascita fino alla morte. Quindi è il produttore stesso del dispositivo che si occupa di assegnare l'indirizzo MAC in fase di produzione, indirizzo preso da un blocco assegnato dall' IEEE (l'ente che gestisce gli indirizzi MAC).

Per fare un'analogia con il mondo reale, l'indirizzo IP è come il codice postale mentre l'indirizzo MAC è come il codife fiscale.

Abbiamo visto che al livello di rete, quando si crea il datagramma IP viene aggiunto l'indirizzo IP del mittente e in particolare del destinatario. A livello di collegamento, quando si crea il frame viene aggiunto l'indirizzo MAC del  mittente e del destinatario, in quanto il livello di collegamento si occupa della comunicazione tra nodi adiacenti. Quindi ha bisogno di sapere con esattezza qual'è l'interfaccia fisica a cui deve arrivare il frame.

Dunque, ci viene adesso spontaneo chiederci come si passa di indirizzo IP a indirizzo MAC? La riposta è ARP.

## ARP (Address Resolution Protocol)

ARP è un protocollo a livello di collegamento che ha il compito di tradurre gli indirizzi IP in indirizzi MAC.

Ogni nodo possiede al suo interno una tabella, **ARP Table** in cui ogni record è la mappatura indirizzo IP - MAC address e un campo **TTL (Time To Live)** che rappresenta il tempo per cui vale tale mappatura.

Per popolare questa tabella ci pensa appunto il protocollo ARP. Supponiamo che un nodo A deve scoprire l'indirizzo MAC di un nodo B. A crea un frame contentente il suo indirizzo MAC e IP l' indirizzo IP di B. Come indirizzo MAC inserisce **l'indirizzo di broadcast a livello 2 (FF FF FF FF FF FF)**. Tutti i nodi della rete riceveranno questo frame che lo passeranno al livello di rete, ma solo il vero destinatario, ovvero B risponderà a questo messaggio mandando ad A il proprio MAC address. A questo punto A salva la corrispondeza indirizzo IP - MAC address di B nella propria tabella ARP.  



