# Sequence Alignment

Date due stringhe $s_{1}$ e $s_{2}$, vogliamo in qualche modo capire quanto sono simili queste stringhe tra loro. Un approccio è di mettere le stringhe una sotto l'altra e di tenere conto dei "mismatch" tra i singoli caratteri, ovvero se due caratteri sono diversi tra loro, dati due carattere $a_{i}^{'} \in s_{1}$ e $a_{i}^{''} \in s_{2}$, $a_{i}^{'} \neq a_{i}^{''}$. Oltre ai "mismatch", prendiamo in considerazione anche i "gap", cioè se allineiamo le due stringhe, magari con lunghezze diverse, risulta un "buco".

> [!NOTE]
> - Per esempio: ocurrance e occurrence.

<img src="seqAl/misgapex.png" width="300" />

Per definire meglio questo concetto, è stato definita **EDIT DISTANCE**.
> [!IMPORTANT]
> **Edit Distance**  
> - Gap penalty $\delta$: il costo da pagare per gap.
> - Mismatch penalty $\alpha_{pq}$: il costo da pagare per un mismatch dati due caratteri $p$ e $q$. Questo costo può variare in base ai caratteri.
> - Costo: $\delta + \alpha_{pq}$ per ogni mismatch tra i caratteri $p$ e $q$.

## Definizione del problema

> [!IMPORTANT]
> **SEQUENCE ALIGNMENT**
> - **Goal**: Date due stringhe $X = x_{1}x_{2}...x_{m}$ e $Y = y_{1}y_{2}...y_{3}$, trovare il costo minimo di allineamento.
> - **Def**: Un *allineamento* $M$ è un insieme ordinato di coppie $x_{i}$ - $y_{i}$ tale che ciascun carattere appare al massimo in una coppia e senza incroci, $x_{i}$ - $y_{j}$ e $x_{i^{'}}$ - $y_{j^{'}}$ si incrociano se $i < i^{'}$ ma $j > j^{'}$.
> - **Def**: Il *costo* di un allineamento $M$ è:  
$$
cost(M)
=
\sum_{x_{i}, y_{j}\in M}{\alpha_{x_{i}, y_{j}}} + 
\sum_{i: x_{i} unmatched}{\delta} + 
\sum_{j: y_{j} unmatched}{\delta} + 
$$

<img src="seqAl/allineamento.png" width="300" />

## Definizione della soluzione

> [!IMPORTANT]
> - **Def**: $OPT(i, j)$: minimo costo per allineare i prefissi $x_{1}$, $x_{2}$, ..., $x_{i}$ e $y_{1}$, $y_{2}$, ..., $y_{j}$ delle stringhe $X$ e $Y$
> - **Goal**: $OPT(m, n)$.
> - **Caso 1**: $OPT(i, j)$ è il costo della mancata corrispondeza (*mismatch*) tra il carattere $x_{i}$ e il carattere $y_{j}$ più il costo minimo dell'allineamento dei prefissi $x_{1}$, ..., $x_{i - 1}$ e $y_{1}$, ..., $y_{j - 1}$.
> - **Caso 2a**: $OPT(i, j)$ lascia $x_{i}$ senza corrispondeza. Di conseguenza paghiamo il costo di un gap $x_{i}$ più il minimo costo dell'allineamento $x_{1}$, ..., $x_{i - 1}$ e $y_{1}$, ..., $y_{j}$.
> - **Caso 2b**: $OPT(i, j)$ lascia $y_{j}$ senza corrispondeza. Di conseguenza paghiamo il costo di un gap $y_{j}$ più il minimo costo dell'allineamento $x_{1}$, ..., $x_{i}$ e $y_{2}$, ..., $y_{j - 1}$.

**Equazione di Bellman**

- $OPT(i, j) = j \cdot \delta$ se $i = 0$. 
- $OPT(i, j) = i \cdot \delta$ se $j = 0$. 
- $OPT(i, j) = min${ $\alpha_{x_{i}y_{i}} + OPT(i - 1, j - 1)$, $\delta + OPT(i - 1, j)$, $\delta + OPT(i, j - 1)$ }.

