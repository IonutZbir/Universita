Un buon compromesso tra spazio impiegato e efficienza di operazioni è la  **variable byte code**.

Invece di rappresentare un numero con una **sequenza variabile di bit** possiamo rappresentarlo come una **sequenza variablie di byte**.

- Ogni byte dedica il primo bit a indicare se quello è l'ultimo byte del numero. Se il primo bit è 0, significa che ci sono ancora byte da leggero per completare il numero, se invece è 1, significa che quello è l'ultimo byte del numero.
- Quindi, se $x \leq 127$ è sufficente un solo byte per rappresentarlo, il primo bit vale 1, mentre i restanti 7 sono usati per la codifica del numero.

Esempio:

**docIDs** | 824 | 829 | 215406
---|---|---|---
**gaps** | 824 | 5 | 214577
**VB code** | 00000110 10111000 | 10000101 | 00001101 00001100 10110001

Nonostante questa codifica sprechi spazio se ci sono gap molto piccoli, è molto più efficiente da decodificare rispetta la gamma code, che nella pratica è molto più usata nei sistemi reali.

Un ultima codifica utilizzata è la **simple-9**, dove si cerca di essere allineati con la prola macchina da 32 bit. Si prende il blocco da 32 bit e si cerca di codificare il maggior numero possibile di gap al suo interno. I 4 bit più significativi del blocco sono usati per dire che formato si sta usando, mentre i restanti 28 bit sono usati per codificare i gap.
