Le parole sono composte da una **radice** (una parte iniziale) e da una **desinza** (una parte finale).

Dato che moltissime parole hanno in comune la radice possiamo evitare di riscriverla ongi volta.
Possiamo salvare un **blocco per ogni radice**, e poi scrivendo in sequenza solo le desinenze.

Esempio:
$$\rightarrow8\text{automata}8\text{automate}9\text{automatic}10\text{automation}$$
$$\rightarrow 8\text{automat*a}1\square\text{e}2\square\text{ic}3\square\text{ion}$$

1. Come primo elemento di un blocco abbiamo la lunghezza della radice, così da poterla leggere.
2. Dopodichè abbiamo il simbolo $*$ che sta ad indicare che "*da qui in poi appendici la desinenza alla radice*".
3. La prima desindenza può essere letta consecutivamente finché non trovo un **numero**.
4. Il **numero** indica la lunghezza della prossima desinenza.
5. Ogni desinenza è poi separato da un **carattere separatore** $\square$.