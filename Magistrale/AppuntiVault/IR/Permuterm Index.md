L'idea dietro i **permuterm index** è quella di **trasformare ogni wildcard query in una query con \* alla fine**, in modo che basti una normale ricerca per prefisso all'interno del B-Tree. Per fare ciò faremo uso di un carattere speciale, il \$.

1. Ogni termine `word` all'interno del dizionario diventa `word$` (`hello` $\to$ `hello$`)
2. Dopodichè, si generano tutte le rotazioni del termine ottenuto:
	- `hello$`,
	- `ello$h`,
	- `llo$he`,
	- `lo$hel`,
	- `o$hell`,
	- `$hello`;
3. Infine, si aggiungono tutte le rotazioni all'interno del dizionario, ma puntano tutte allo stesso termine originale.

| **Tipo di Query**           | **Formato Originale** | **Trasformazione per il B-Tree** | **Logica e Intuizione**                                                                             |
| --------------------------- | --------------------- | -------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Esatta**                  | `X`                   | `X$`                             | Si cerca semplicemente il termine `X`.                                                              |
| **Prefisso**                | `X*`                  | `$X*`                            | Il simbolo `$` indica che la parola deve "ricominciare" esattamente con `X`.                        |
| **Suffisso**                | `*X`                  | `X$*`                            | Ruotando la parola, ciò che era alla fine (`X`) ora si trova prima del simbolo `$`.                 |
| **Sottostringa**            | `*X*`                 | `X*`                             | Se `X` è una sottostringa, esisterà sempre una rotazione che inizia proprio con `X`.                |
| **Parte Iniziale e Finale** | `X*Y`                 | `Y$X*`                           | Si cerca una rotazione che finisce per `Y` (prima del `$`) e inizia per `X` (dopo il `$`).          |
| **Multiple Wildcard**       | `X*Y*Z`               | `Z$X*` (+ filtro su `Y`)         | Si recuperano i termini che iniziano per `X` e finiscono per `Z`, filtrando poi la presenza di `Y`. |

Per capire meglio come funzionano le wildcard, vediamo i seguenti esempi pratici:
- Per cercare `hel*`, nel dizionario viene cercato `$hel*`. Questo perché ogni parola che inizia con `hel` avrà tra le sue rotazioni `$hel`, e quindi cercando `$hel*` ottengo tutte le parole che iniziano per `hel`.
- Per cercare `*llo`, nel dizionario viene cercato `llo$*`. Questo perché ogni parola che finisce per `llo` ha tra le sue rotazioni `llo$`, e quindi cercando `llo$*` punto a tutte le parole che finiscono per `llo`.
- Per cercare `*ell*`, ossia tutti i termini che contengono `ell` da qualche parte. Se una rotazione comincia per `ell`, vuol dire che nel termine originale `ell` appare come sottostringa (`hello, ello$h`), per cui cerco `ell*`, ossia `$ell*` e ottengo tutte le parole che contengono `ell` da qualche parte.
- Per cercare `hel*o`, viene cercata `lo$h*`. Questo perché la query `h*lo` vuol dire che la parola deve iniziare per `h` e finire per `lo`.
- Per cercare `h*a*o`, viene anzitutto trattata come `h*o`, quindi cerco `o$h*` e ottengo tutte le parole che iniziano per `h` e finiscono per `o`. Poi, tra i termini trovati, si applica un filtraggio per verificare la presenza della parte intermediaria (`hello` viene scartato perché non contiene `a`, mentre `halo` sarebbe tenuto).

Usare i permuterm porta:
- **Vantaggio**: query wildcard complicate di qualsiasi forma vengono trasformate in una semplice ricerca di prefisso nel B-Tree, che è molto efficiente.
- **Svantaggio**: empiricamente, aggiungere tutte le rotazioni di ogni termine al dizionario porta ad un aumento di almeno 4 volte la dimensione del dizionario (ogni termine di lunghezza $n$ genera $n+1$ rotazioni).

Un'alternativa sono i [[k-grams]]