Iniziamo con l'osservare che non possiamo rappresentare direttamente in binario una sequenza di numeri, altrimenti non sappiamo quando finisce la codifica di un numero e quando inizia quella di un altro.

Possiamo però sfruttare la [[Unary code|codifica unaria]] per rappresentare quanti bit sono necessari per la codifca del prossimo numero.

L'idea della codifica $\gamma$ è la seguente, sia $x \in \mathbb{N}$
1. Scrivi $x$ in binario;
2. Poiché ciascun numero in binario inizia con un **uno**, possiamo risparmiare un bit ed ometterlo.
3. Calcoliamo la lunghezza dell'offset, ossia della lunghezza del numero in binario.
4. Concateniamo length e offset ottenendo la codifica $\gamma$.

Consideriamo come esempio i numeri $9$ e $16$.
In binario essi sono codificati rispettivamente in $1001$ e $10000$.
Perciò la rappresentazine di tale sequenza sarà $$\overbrace{\underbrace{11110}_{\text{length}} \; \underbrace{1001}_{\text{binary code}}}^{9} \;\; \overbrace{\underbrace{111110}_{\text{length}} \; \underbrace{10000}_{\text{binary code}}}^{16}$$

Possiamo risparmiare un ulteriore bit, osservando il fatto che alla fine ogni numero (eccetto lo 0, ma tano non ci interessa) inizia **sempre** per 1.

Tale codifica è nota come **gamma code** $$\overbrace{\underbrace{1110}_{\text{length}} \; \underbrace{001}_{\text{binary code}}}^{9} \;\; \overbrace{\underbrace{11110}_{\text{length}} \; \underbrace{0000}_{\text{binary code}}}^{16}$$
Quindi, per decodificare, e sufficiente leggere gli 1 fino allo 0 identificando *length*, poi leggo *length* bit per identificare l'*offset* e aggiungo il primo 1 per ricostruire correttamente il `docId`.

Dato quindi un gap di valore $G$, ci serviranno $\lfloor \log_2{G} \rfloor + 1$ bits per la codifica unaria della lunghezza, e $\lfloor \log_2{G} \rfloor$ bit per la codifica stessa del numero.

Lo spazio complessivo usato è quindi $2\lfloor \log_2{G} \rfloor + 1$ bit.
Si può dimostrare che tale codifica è **ottima** perché:
- con meno di $\log_2{G}$ bit ho **perdita di informazione**.
- il fattore $2$ è **necessario** per sapere quanto è lunga una codifica.

**number** | **length** | **offset** | $\gamma$-**code**
---|---|---|---
0 | | | none
1 | 0 | | 0
2 | 10 | 0 | 10,0
3 | 10 | 1 | 10,1
4 | 110 | 00 | 110,00
9 | 1110 | 001 | 1110,001
13 | 1110 | 101 | 1110,101
24 | 11110 | 1000 | 11110,1000
511 | 111111110 | 11111111 | 111111110,11111111
1025 | 11111111110 | 0000000001 | 11111111110,0000000001


### Problematiche
Anche se teoricamente il $\gamma$-code è una codifica ottima, purtroppo in pratica non è particolarmente efficiente.
Infatti i processori moderni lavorano molto bene con sequenze di **lunghezza fissa** di bit, generalmente 8, 16, 32, o 64. 
Per tale ragione, in pratica, nei sistemi reali si utilizzano codifiche **byte-aligned**, come la tecnica [[Variable byte codes]].