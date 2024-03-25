## DNS

Gli host Internet possono essere identificati in vari modi, più precisamente da uno o più **hostname** e da un unico **indirizzo IP**. Le persono 
ovviamente preferiscono identificare gli host mediante l'hostname, mentre i router ovviamente l'indirizzo IP. Al fine di conciliare i due approcci è 
necessario un servizio in grado di tradurre gli indirizzi IP in hostname e viceversa. 

> [!IMPORTANT]
> **DNS (Domain Name System)**, è un protocollo a livello applicazione che si occupa della traduzione dei nomi. Consiste in un database distribuito 
> implementato in una gerarchia di **DNS server**. Consente quindi agli host, di interrogare questo database per **risolvere** i nomi.

I server DNS sono generalmente macchine UNIX che eseguono il software **BIND (Barkeley Internet Name Domain)**. DNS utilizza UDP e la porta 53.

Oltre alla traduzione degli hostname, in indirizzi IP, DNS mette a disposizione altri importanti servizi:
- **Host aliasing**. Un host dal nome complicato può avere più sinonimi o *alias*. Per esempio `relay1.west-coast.enterprise.com` potrebbe avere due sinonimi, `enterprise.com` e `www.enterprise.com`. In questo caso, il nome originale si dice che è un **hostname canonico**.
- **Mail sever aliasing**. Per esempio un utente, diciamo Bob, potrebbe avere un indirizzo di posta elettronica `bob@yahoo.com`. Tuttavia l'hostname del mail server di Bob potrebbe essere assai più complicato. Un'applicazione di posta può invocare il DNS per ottenere il nome canonico di un sinonimo fornito,così come l'indirizzo IP dell'host.
- **Load distribution**. Il DNS viene utilizzato anche per distribuire il carico tra server replicati, per esempio dei web server. I siti con molto traffico vengono replicati su più server, ognuno eseguito su un host diverso con un IP diverso. Nel caso di web server replicati, va associato a ogni hostname canonico un insieme di indirizzi IP.

**Funzionamento DNS**

Supponiamo che una certa applicazione in esecuzione sull'host di un utente abbia necessità di tradurre un hostname in un indirizzo IP. L'applicazione 
invocherà il lato client DNS

