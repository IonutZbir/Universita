Scrivere un programma prolog significa sceivere un insieme di predicati.
- Fatti
- Regole


X è fratello di Y se (:-) [Z genitore di X e (,) Z genitore di Y] 

=> fratello(X, Y) :- [genitore(Z, X), genitore(Z, Y)] è un regola

=> genitore(mario, dario), genitore(mario, gino) sono fatti 

X (maiuscolo) - variabile di cui vogliamo sapere il valore
_x - variabile di cui non vogliamo sapere il valore
_ - variabile che non viene unificata

a....(minuscolo) - costanti
1.... - numeri

fratello(dario, gino) ? vero o falso
-> assovio dario a X e gino a Y

unificare: valore associato alla variabile, e sara associato a tutti i nomi in quel istante

funzione -> predicato
funzionare -> predicare
ricorsione -> indunzione
assegnamento -> unificare

## Liste 

Induzione strutturale

Lista: [a, b, c, d, e]

[H | T] -> modalità di scrivere la lista testa|coda

H: testa
T: elementi lista coda

[H | T] = [a, b, c, d, e]: unificato la modalità di lettura della lista
- H = a
- T = [b, c, d, e]

[H | T] = [a]
- H = a
- T = []

[H | T] = [] // non se pò fa, non è unificabile
- H = 
- T = []

a $\in$ A ? dato un elelemento, possiamo scrivere un predicare che è vero se l'elemento appartiene all'insieme
`appartiene(X, L)`

Una lista puo essere vista come un elemento e una parte restante

L = [H | T]

due casi:
1. X unifica con H
2. `appartiene(X, T)`

appartiene(X, [1, 2, 3]) -> elenca gli elementi della lista

[H1, H1 | T] = [a, b, c]
- H1 = a
- H2 = b
- T = [c]
  
[H1, H1, T] = [a, b, c]
- H1 = a
- H2 = b
- T = c
  
















