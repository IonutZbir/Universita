Una prima ottimizzazione è quella di rappresentare nelle posting list i **gap** tra i vari *docID*.

Esempio
- Posting list $\rightarrow 33,47,154,159,202, \dots$
- Gap encoding $\rightarrow 33,14,107,5,43, \dots$

L'idea è che per termini molto frequenti abbiamo bisogno di usare numeri molto piccoli, i quali richiedono un numero minore di bit per essere rappresentati.

Posting list del termine `the`
- Posting list  $\rightarrow 1,2,3,4,5, \dots$
- Gap encoding $\rightarrow 1,1,1,1,1,1, \dots$

Ovviamente abbiamo bisogno di una **codifica variabile** dei numeri, perché se uso un numero fissati di bit per i numeri, la dimensione delle posting list non varia (sia che usiamo la posting semplice, sia la sua *gap encoding*).

Infatti per il termine `arachnocentric` usare 20 bits per i suoi postings va bene, però per il termine `the` si potrebbe usare un **bit vector**, così da usare 1 solo bit per ogni suo posting.