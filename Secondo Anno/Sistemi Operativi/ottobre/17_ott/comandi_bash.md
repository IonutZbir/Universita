# Comandi Bash

## Comandi Base

- <span style="color:blue">**`sudo su`**</span> -> *modalità super user (root)*
- <span style="color:blue">**`cd dir`**</span> -> *cambio cartella*
- <span style="color:blue">**`mkdir dir`**</span> -> *crea cartella*   
- <span style="color:blue">**`ls`**</span> -> *mostra contenuti nella cartella corrente*
    - <span style="color:blue">**`-a`**</span> -> *mostra anche i file nascosti (.files)*
    - <span style="color:blue">**`-h`**</span> -> *human readable*
    - <span style="color:blue">**`-l`**</span> -> *long listing*
    - <span style="color:blue">**`-F`**</span> -> *aggiunge un carattere speciale dopo ogni nome di file o directory
            per indicare il tipo di file.*  
            '/' per cartelle  
            '*' per eseguibili  
            '@' per link simbolici  
            '|' per file FIFO, pipes  
            '=' per socket  
- <span style="color:blue">**`pwd`**</span> -> *mostra cartella corrente*
- <span style="color:blue">**`wget link`**</span> -> *scarica il file dal link*
- <span style="color:blue">**`mv foo.txt foo.tsv`**</span> -> *rinomina un file, ma lo sposta anche*
- <span style="color:blue">**`cp foo.tsv foo2.tsv`**</span> -> *copia un file*
- <span style="color:blue">**`wc foo.tsv`**</span> -> *conta in numero di parole, righe, caratteri all'interno di un file*
- <span style="color:blue">**`history`**</span> -> *mostra i comandi passati*
- <span style="color:blue">**`echo $foo`**</span> -> *permette di stampare*
- <span style="color:blue">**`less log_stdout.txt`**</span> -> *mostra a schermo il contenuto di un file, caricandolo permettendo
                         di caricarlo man mano che si scorre, opposto di more*
- <span style="color:blue">**`echo $PATH`**</span> -> *stampa la variabile path di ambiente*
- <span style="color:blue">**`man command`**</span> -> *un manuale per visualizzare cosa fa ciascun comando*
- <span style="color:blue">**`w`**</span> -> *mostra gli utenti collegati*
- <span style="color:blue">**`cat`**</span> -> *stampa il contenuto di un file sullo standard output*
- <span style="color:blue">**`grep`**</span> -> *stampa le righe di un file che corrispondono ad un pattern*
- <span style="color:blue">**`tail`**</span> -> *stampa l'ultima parte di un file (permette di scegliere quale righe)*
    - <span style="color:blue">**`-n NUM`**</span> -> *stampa le ultime NUM righe*
- <span style="color:blue">**`head`**</span> -> *stampa la prima parte di un file (permette di scegliere quale righe)*
    - <span style="color:blue">**`-n NUM`**</span> -> *stampa le prime NUM righe*
- <span style="color:blue">**`awk`**</span> -> *potente linguaggio di scripting, usato specialmente per lavorare con file*
- <span style="color:blue">**`sort`**</span> -> *ordina un file*
    - <span style="color:blue">**`-r`**</span> -> *reverse sort*
- <span style="color:blue">**`uniq`**</span> -> *è utilizzato per rimuovere o riportare le linee duplicate da un file di testo o
          da un flusso di input.*
    - <span style="color:blue">**`-c`**</span> -> *conta in numero di occorenze di ciascuna linea*
- <span style="color:blue">**`sed`**</span> -> *permette l'editing di testo, tipo replace*
- <span style="color:blue">**`1>`**</span> or <span style="color:blue">`>`</span> -> *ridireziona l'output di un comando o il contenuto di un file nello STDOUT o 
             se specificato in un altro file.*
- <span style="color:blue">**`2>`**</span> -> *ridireziona l'output di un comando o il contenuto di un file nello STDERR*

- ps faux
- mount
- ln
- top
- rsync
- free 


## Comandi annidati attraverso Pipes

- <span style="color:blue">**`cat foo.txt | tail -n 2`**</span> -> *ultime 2 righe*
- <span style="color:blue">**`cat foo.txt | tail -n 2 | head -n 1`**</span> -> *penultima riga*
- <span style="color:blue">**`cat foo.txt | tail -n 2 | head -n 1 | wc`**</span> -> *conto le righe, parole, char della penultima
                                              riga*
- <span style="color:blue">**`cat foo.txt | awk '{print $3}'`**</span> -> *usando awk, stampo la 3 colonna (per 3 colonna si intende la terza parola di una riga, separatate dallo spazio)*
- <span style="color:blue">**`cat foo.txt | awk -F" " '{print $3}'`**</span> -> *specifico il separatatore delle colonne ("\t": tab, " ": spazio, "\n": a capo)*
- <span style="color:blue">**`cat foo.txt | awk -F" " '{print $3}' | sort`**</span> --> *ordino la terza colonna*
- <span style="color:blue">**`cat foo.txt | awk -F" " '{print $3}' | sort | uniq`**</span> -> *elimino i duplicati*
- <span style="color:blue">**`cat foo.txt | awk -F" " '{print $3}' | sort | uniq -c`**</span> -> *conto le occorenze delle colonne duplicate*
- <span style="color:blue">**`cat foo.txt | awk -F" " '{print NR/NF}'`**</span> -> *NR: stampa il numero di riga, NF: stampa il numero di colonne per ciascuna riga*
- <span style="color:blue">**`cat foo.txt | sed 's/APRIL/PAPPAGALLO/g'`**</span> -> *indica che deve sostituire tutte le occorrenze di "APRIL" con "PAPPAGALLO" e il flag g indica che deve farlo globalmente.*
- <span style="color:blue">**`cat foo.txt | grep JULY`**</span> -> *prendo tutte le righe che contengono la stringa JULY*
- <span style="color:blue">**`cat foo.txt | grep -v JULY`**</span> -> *prendo tutte le righe che non contengono la stringa JULY*
- <span style="colot:blue">**`history | awk '{if($1>n) print}'`**</span> -> *prendo da history tutte le righe da una certa righa n in poi*

## Comandi per salvare un file

- cat foo.tsv | awk -F"\t" '{print $3}' | sort | uniq -c > log_stdout.txt -> manda lo standard output sul file log_stdout.txt
- cat foo.tsv | awk -F"\t" '{print $3}' | sort | uniq -c 2> log_stderr.txt -> manda lo standard error sul file
- cat foo.tsv | awk -F"\t" '{print $3}' | sort | uniq -c 2> log_stdout.txt 1> log_stout.txt -> se li voglio separare

## Combinazione tasti
- '~' -> altgr + ì tilde r
