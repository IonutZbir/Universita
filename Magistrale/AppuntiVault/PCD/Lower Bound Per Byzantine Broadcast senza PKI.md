**DOMANDA:** Cosa succede se rimuoviamo l'ipetesi che ci sia una PKI setup? Come vedremo, nessun protocollo può garantire *validity* e *consistency* contemporaneamente, se ci sono $f \geq \frac{n}{3}$ nodi corrotti.

## Intuizione

Consideriamo il seguente scenario con 3 persone (3 nodi):
- **F:** è il presidente uscente (la sorgente)
- **M e L:** sono i due candidati alla successione.
Nessuno vuole fare il presidente perché c'è troppo carico di lavoro. $F$ propone chi dovrà essere il nuovo presidente inviando un messaggio a entrambi.

![[lbBBIntuzione.png]]

1. *Round 1:* $F$ invia onestamente a entrambi lo stesso messaggio `Propongo M`.
2. *Round 2:* Poiché $L$ è onesto, riferisce a $M$ la verità: `F ha proposto M`. A questo punto, poichè non vuole fare il presidente, $M$ fa il nodo bizantino/corrotto, riferendo a $L$: `F ha proposto L`.

Senza firme digitali o prove crittografiche, si tratta solo della parola di $M$ contro quella di $F$. Per $L$ esistono due scenari:
- *Scenario A:* $F$ è onesto e ha detto `M` a tutti, ma $M$ sta mentendo per salvarsi;
- *Scenario B:* $F$ è disonesto, ha fatto il "doppio gioco", mentre $M$ è sincera nel dire che $F$ ha proposto $L$.
Poiché $L$ non può capire in quale scenario si trova, non può decidere in sicurezza. Se decide assumendo il scenario A, rischia di violare la consistenza/validità nello scenario B, e vicecersa.

Con una PKI setup invece, questo problema non sarebbe stato possibile, perchè:
- Se $F$ invia `M`, allega la propria firma digitale non falsificabile $<M>_{F}$.
- Quando $M$ vuole mentire a $L$, il protocollo le impone di mostrare la prova $<L>_{F}$.
- Poiché $F$ non ha firmato `L` e $M$ non pul falsificare la firma di $F$, $M$ non può esibire $<L>_{F}$.

## Teorema LB

**Teorema:** In assenza di PKI setup e con $f \geq \frac{n}{3}$ nodi corrotti, nessun protocollo per il problema Byzantine Broadcast può garantire *validity* e *consistency*.

**Proof:** Consideriamo il sistema $\mathcal{G}$ come in figura con 3 nodi, dove il nodo $A$ è la sorgente, e *supponiamo per assurdo che esista un protocollo $\Pi$* che garantisce *validity* e *consistency* nel sistema $\mathcal{G}$ anche in presenza di un nodo corrotto.

Consideriamo poi l'esperimento concettuale $\mathcal{H}$ come in figura, dove gli archi del grafo indicano i canali di comunicazione (quindi ogni nodo può comunicare soltanto con i suoi due vicini) e
- $x$ e $x'$ sono copie esatte di $A$ (quindi, in particolare, entrambi i nodi *credono* di essere la sorgente $A$ del problema BB);
- $y$ e $y'$ sono copie esatte di B;
- $z$ e $z'$ sono copie esatte di C.

![[lbBB.png]]

*Osservazione:* Un nodo non può distinguere se si trova nel sistema reale $\mathcal{G}$ o nell'esperimento concettuale $\mathcal{H}$: per esempio, il nodo $z'$ in $\mathcal{H}$ è una copia del nodo $C$ e comunica con 2 nodi, $x$ e $y'$, il primo è una copia del nodo $A$ e il secondo è una copia del nodo $B$. 

L'esecuzione del protocollo $\Pi$ può essere quindi *simulata* nell'esperimento concettuale $\mathcal{H}$ (i nodi $x$ e $x'$ eseguono le istruzioni previste per $A$, $y$ e $y'$ quelle previste per $B$ e $z$ e $z'$ quelle previste per $C$).
Ci chiediamo cosa danno in output i sei nodi in $\mathcal{H}$ se simuliamo l'esecuzione del protocollo $\Pi$ dove al nodo $x$ (una delle due copie di $A$) viene dato in input il bit 1 e al nodo $x'$ viene dato in input 0.

L'esecuzione di $\Pi$ su $\mathcal{H}$ produce un output 
$$
\text{out}_{\mathcal{H}}(x), \text{ out}_{\mathcal{H}}(x'), \dots, \text{ out}_{\mathcal{H}}(z') 
$$
Vogliamo mostrare un assurdo in tale output per dimostrare che $\Pi$ non può esistere.

**CLAIM 1:** $\text{out}_{\mathcal{H}}(x) = \text{out}_{\mathcal{H}}(y) = 1$.
Consideriamo un esecuzione del protocollo $\Pi$ nel sistema reale $\mathcal{G}$ con:
- $A$ sorgente con input 1 *onesta*;
- B nodo *onesto*;
- C nodo *corrotto*.
Poiché per ipotesi $\Pi$ risolve BB anche in presenza di un nodo bizantino, per la proprietà di validity (se la sorgente è onesta e ha in input $b$, *tutti i nodi onesti devono decidere $b$*), allora
$$
\text{out}_{\mathcal{G}}(A) = \text{out}_{\mathcal{G}}(B) = 1.
$$
Poiché $C$ è bizantino, si può comportare nel seguente modo:
- Simula internamente $\Pi$ su $\mathcal{H}$ con $\text{in}_{\mathcal{H}}(x) = 1$ e $\text{in}_{\mathcal{H}}(x') = 0$.
- Quando nel round $r$ deve mandare un messaggio a $B$ in $\mathcal{G}$, gli invia esattamente il messaggio che la copia $z$ ha inviato ad $y$ in $\mathcal{H}$;
- Quando deve mandare un messaggio ad $A$ in $\mathcal{G}$, gli invia esattamente il messaggio che la copia $z'$ ha inviato ad $x$ in $\mathcal{H}$;

Il punto chiave della dimostrazione è l'*indistinguibilità* per $A$ e $B$, infatti:
- $\text{vista}_{\mathcal{H}}(x) = \text{vista}_{\mathcal{G}}(A)$
- $\text{vista}_{\mathcal{H}}(y) = \text{vista}_{\mathcal{G}}(B)$
Non essendo una PKI, non esistono identificatori globali autenticati o firme che possano svelare la topologia: un nodo conosce solo i messaggi che transitano sulle proprie porte locali.

Quindi, dato che gli ingressi, i messaggi in transito e la memoria locale coicidono, la computazione deterministica impone che:
$$
\begin{align}
\text{out}_{\mathcal{H}}(x) = \text{out}_{\mathcal{G}}(A) \\ 
\text{out}_{\mathcal{H}}(y) = \text{out}_{\mathcal{G}}(B) \\
\end{align}
$$
Avendo stabilito che nel sistema reale $\mathcal{G}$, per validity deve valere che
$$
\begin{gather*}
\text{out}_{\mathcal{G}}(A) = 1 \qquad \text{e} \qquad \text{out}_{\mathcal{G}}(B) = 1 \\
\Downarrow \\
\text{out}_{\mathcal{H}}(x) = 1 \qquad \text{e} \qquad \text{out}_{\mathcal{H}}(y) = 1 \\
\end{gather*}
$$
ossia, in $\mathcal{H}$ le copie corrispondenti devono produrre lo stesso identico risultato.

**CLAIM 2:** $\text{out}_{\mathcal{H}}(x') = \text{out}_{\mathcal{H}}(z) = 0$.
Consideriamo un esecuzione del protocollo $\Pi$ nel sistema reale $\mathcal{G}$ con:
- $A$ sorgente con input 0 *onesta*;
- B nodo *corrotto*;
- C nodo *onesto*.
Come nel claim 1, la dimostrazione è la stessa. In questo caso $B$ si comporta come il nodo $C$ nel claim 1, e per la proprietà di indistinguibilità per $A$ e $C$ valgono gli stessi risultati del punto prima.

**CLAIM 3:** $\text{out}_{\mathcal{H}}(y) = \text{out}_{\mathcal{H}}(z)$.

Consideriamo un'esecuzione del protocollo $\Pi$ nel sistema reale $\mathcal{G}$ con:
- $A$ sorgente *corrotta*;
- $B$ nodo *onesto*;
- $C$ nodo *onesto*.

Poiché per ipotesi $\Pi$ risolve BB, per la proprietà di **consistency** i due nodi onesti devono decidere lo stesso valore:
$$\text{out}_{\mathcal{G}}(B) = \text{out}_{\mathcal{G}}(C)$$
La sorgente corrotta $A$ adotta la seguente strategia: simula internamente $\Pi$ su $\mathcal{H}$ (con $\text{in}_{\mathcal{H}}(x) = 1$ e $\text{in}_{\mathcal{H}}(x') = 0$) e ad ogni round $r$:
- invia a $B$ esattamente i messaggi che la copia $x$ invia a $y$ in $\mathcal{H}$;
- invia a $C$ esattamente i messaggi che la copia $x'$ invia a $z$ in $\mathcal{H}$.
Per indistinguibilità:
$$\text{vista}_{\mathcal{G}}(B) = \text{vista}_{\mathcal{H}}(y) \implies \text{out}_{\mathcal{H}}(y) = \text{out}_{\mathcal{G}}(B)$$
$$\text{vista}_{\mathcal{G}}(C) = \text{vista}_{\mathcal{H}}(z) \implies \text{out}_{\mathcal{H}}(z) = \text{out}_{\mathcal{G}}(C)$$
Poiché $\text{out}_{\mathcal{G}}(B) = \text{out}_{\mathcal{G}}(C)$, ne consegue che:
$$\text{out}_{\mathcal{H}}(y) = \text{out}_{\mathcal{H}}(z)$$
In conclusione, mettendo insieme il Claim 1, il Claim 2 e il Claim 3 otteniamo che
$$
\begin{align}
\text{out}_{\mathcal{H}}(y) &= 1 &\qquad \text{claim 1} \\
\text{out}_{\mathcal{H}}(z) &= 0 &\qquad \text{claim 2} \\
\text{out}_{\mathcal{H}}(y) &= \text{out}_{\mathcal{H}}(z) &\qquad \text{claim 3} \\ \\
\implies 1 = 0 \text{ ASSURDO!}
\end{align}
$$
L'ipotesi che esiste il protocollo $\Pi$ è falsa!
