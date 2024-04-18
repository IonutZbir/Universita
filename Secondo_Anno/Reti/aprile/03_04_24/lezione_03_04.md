# Trasporto orientato alla connessione: TCP

> [!IMPORTANT]
>
> **TCP** viene detto **orientato alla connessione** in quanto, prima di effettuare lo scambio dei dati, i processi devono effettuare l'handshake, ossia devono inviarsi reciprocamente alcuni segmenti preliminari per stabilire i parametri del successivo trasferimento dati. Come parte dell'instaurazione della connessione TCP, entrambe le parti inizializzano molte variabili di stato associate alla connessione.

Una connessione TCP offre un **servizio full-duplex**, ovvero data una connessione tra due applicazioni, A e B su due host differenti,  i dati a livello di applicazione possono fluire dal processo A al processo B e in contemporanea dal processo B al processo A. (A <-> B).

Una connessione TCP è anche **punto a punto**, ossia ha luogo tra un singolo mittente e un singolo destinatario.

