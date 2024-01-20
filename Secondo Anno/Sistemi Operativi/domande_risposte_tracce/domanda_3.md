## Quesito

Discutere dell'importanza dei file, delle tipologie di file e della loro implementazione.

## Risposta

In UNIX everything is a file! Un file è un astrazione del disco andando a risolvere il problema della memorizzazione, consentendo la persistenza, l' accesso multiplo e la gestione di grandi volumi di dati. Fornisce un metodo per scrivere e leggere informazioni dal disco. Ogni file ha un suo nome, la quale struttura può essere diversa in diversi file system.
Per esempio in FAT 12/16/32 i nomi dei file non erano case sensitive, ovvero Maria era uguale a maRia. Oltre al nome, 
i file hanno anche un estensione, un'ulteriore informazione riguardo al file, per esempio file C hanno estensione .c e
cosi via. In UNIX le estensioni sono puramente convenzionali, ovvero al sistema operativo non interessa sapere il 
contenuto di un file. Ma un compilatore C, può richiedere che il file abbia estensione .c. In Windows, invece, le estensioni
hanno un ruolo ben preciso, poiche l'utente può assegnare ad un file un applicazione con cui aprire il file.

In UNIX e Windows i file sono una sequenza non struttura di byte, quindi è compito del'applicazione utente capire il 
contenuto all'interno di un file. I file possono essere binari o ASCII. I file ASCII sono file di testo normali mentre i 
file binari sono i file eseguibili o gli archivi. 
