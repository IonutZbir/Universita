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

