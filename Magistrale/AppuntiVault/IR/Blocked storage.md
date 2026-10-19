Un'idea per diminuire la grandezza dei un puntatori nella struttura [[Dictionary as a String|dictionary-as-a-string]] è quella di preservare un puntatore per ogni $k$ termini.

Così facendo, riduco la grandezza dei puntatori e il loro numero di un fattore $k$.

C'è però bisogno di salvare la lunghezza di ogni termine, per sapere quanti bytes leggere.
Per fortuna un solo byte extra mi basta per salvare tale numero, in quanto non esistono parole più lunghe di $2^8 = 256$ caratteri.

![](./img/IR_blocking_1.png)

 Avremo un occupazione di memoria pari a:
- 4 bytes per la **term frequency**.
- 4 bytes per i **puntatori** alle aree di memoria in cui si trovano le **posting lists**.
- 3 bytes ogni $k$ per il **puntatore** che indica l'inzione del **termine** all'interno della stringa.
- 1 byte per ogni termine (per la sua **lunghezza**)

Per esempio, per $k = 4$ e con 400.000 termini avremo $400.000B = 0.38MB$ per le lunghezze dei termini, più $400.000 \times 8B$ per l'intera stringa, $400.000 \times \frac{3}{k}B \approx 0.28MB$ per i puntatori ai blocchi e $400.000 \times 4B \approx 1.5MB$ per i puntatori alle posting lists.
Per un totale quindi di
$$400.000 \times (1 + 8 + 3/4 + 4 + 4)B \approx 7.1MB$$
ovvero abbiamo salvato un ulteriore $0.5MB$ rispetto al metodo [[Dictionary as a String|dictionary-as-a-string]].

## Prestazioni
Ciò che viene intaccato in tale struttura dati sono le operazioni di lettura.
Infatti, una volta individuato un blocco, per accedere alla parola interessata è necessario eseguire un numero **lineare** in $k$ di operazioni.

Perciò generalmente non conviene far crescere troppo $k$, lo si tiene **costante**.