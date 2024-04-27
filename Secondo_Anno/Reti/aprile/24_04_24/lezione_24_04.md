# Il protocollo Internet, IPv4, IPv6

## Formato dei datagrammi IP

<img src="img/ip.png" width="300" style="display: block; margin-left: auto; margin-right: auto;" />

- **Numero di versione**. Quattro bit che specificano la versione del protocollo IP (IPv4 o IPv6).
- **Lunghezza dell'intestazione**. Quattro bit che indicano dove iniziano i dati nel datagramma. Multipli di 32 bit
- **Tipo di servizio**. Bit relativi al tipo di servizio. Diversi servizi da 0 a 5, mentre il sercizio ECN i bit 6 e 7.
- **Lunghezza dell'datagramma**. 16 bit che rappresentano la lunghezza totale del datagramma IP. $Max_{len} = 65535\ byte$, $Average_{len} = 1500\ byte$.
- **Identificatore, flag, offset di frammentazione**. Questi 3 campi servono per la frammentazione. Un datagramma IP grande viene frammentato in datagrammi IP più piccoli e inoltrati in modo indipendete che poi vengono riassemblati prima che i dati vengano passati al livello di trasporto.
- **Tempo di vita**. Il campo TTL è stato incluso per assicurare che i datagrammi non restino in circolazione per sempre nella rete. Questo campo viene decrementato ogni volta che viene elaborato da un router.
- **Protocollo**. Indica il protocollo a livello di trasporto a cui deve inviare i dati. 6 indica UDP mentre 17 indica TCP.
- **Checksum dell'intestazione**. Consente ai router di rilevare gli errori sui bit nei datagrammi ricevuti. È calcolato trattando ogni coppia di byte dell’intestazione come numeri che sono poi sommati in complemento a 1.
- **Indirizzi IP sorgente e destinazione**. Quando un host crea un datagramma, inserisce il proprio indirizzo IP nel campo indirizzo IP sorgente e quello della destinazione nel campo indirizzo IP destinazione. Entrambi gli indirizzi a 16 bit (4 byte). 
- **Opzioni**. Altre opzioni da inserire nel datagramma IP.
- **Dati**. Nella maggior parte dei casi, il campo dati contiene il segmento a livello di trasporto (TCP o UDP) da consegnare alla destinazione. Tuttavia, può trasportare anche altri tipi di dati, quali i messaggi ICMP.

