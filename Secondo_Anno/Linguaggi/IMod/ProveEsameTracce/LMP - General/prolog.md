# Controllare se un elemento si trova in testa ad una lista
testa(X,[X|_]).

?- testa(a,[b,c]).

# Controllare se un elemento si trova al'interno di una lista
## Controllo se è in testa
contenuto(X,[X|_]).
## Controllo se è nella coda
contenuto(X,[_|T]) :-
    contenuto(X,T).

?- contenuto(a,[b,c,a])

# Controllare se 2 liste sono appicciate
## Caso base in cui la prima lista è vuota
appicciata([],L2,L2).
## Caso che itera la lista svuotando la prima lista sempre di un pezzo facendola diventare vuota
appicciata([H|T],L2,[H|G]) :-
    appicciata(T,L2,G).

# Controllare se un elementp è l'ultimo della lista
## Caso base in cui c'è solo un elemento
last(X,[X]).
## Caso che itera svuotando la lista e andando a confrontare sempre la coda rimanente ad ogni ciclo
last(X,[_|T]) :-
    last(X,T).

# Controllare se una coda è pari, togliamo gli elementi 2 a 2 e se la lista è vuota vuol dire che ci sono elementi pari
## Caso base in cui la lista è vuota
pari([]).
## Caso riscorsivo togliendi 2 elementi alla volta
pari([H1,H2|T]) :-
    pari(T). 

# Contare quanti elementi ci sono
## Caso base con lista vuota e 0 al contatore
conta([],0).
## Caso ricorsivo in cui svuoto la lista ed aumento il contatore tornando indietro quando la lista è stata svuotata
conta([H|T],X) :-
    conta(T,X1),
    X is X1 + 1.

# Controllo se un elemento è l'ultimo della lista
last(X,[X]).
last(X,[H|T]) :- last(X,T).

# Controllo se un determinato elemento si trova in una determinata posizione della lista, sintassi (X,lista,Y)
# dove X è l'elemento da cercare, lista è la lista in questione e Y è l'index in cui cercare l'elemento X.
element_at(X,[X|_],1).
element_at(X,[_|L],K) :- K1 is K - 1, element_at(X,L,K1).

# Somma di una lista
## Caso base
somma([],0).
## Caso ricosrivo in cui vado a scomporre la lista e a sommare la testa ad ogni ritorno di chiamata
somma([H|T],X) :-
    somma(T,Y),
    X is Y + H.

# Elimina le duplicazioni di una lista
elimina([],[]).

elimina([H|T],ListaOut) :-
    \+ member(H,T),
    elimina(T, ListaIntermedia),
  	append([H], ListaIntermedia, ListaOut).

elimina([H|T], ListaOut) :-
  member(H, T),
  elimina(T, ListaOut).

