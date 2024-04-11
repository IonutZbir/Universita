/* tree(R, Children) */
/* R(Children) =..[] */
/* leaf(T, L) :- */
/* vero se L è una foglia di T, e T è un albero*/


/* somma(T, S) :-
    T =.. [t, A, B],
    S is A + B.
*/

/* 
t(a,
    [t(b,
        [t(a, []),
        t(b, [])]),
    t(c, []),
    t(d, [])])
*/

somma(t(X, Y), S) :-
    S is X + Y.


/*
leaf(T, R) :-
    T =.. [T, []].
leaf(T, L) :-
    T =.. [_, Children],
    memeber(C, Children),
    leaf(C, Children).
*/
leaf(t(R, []), R).
leaf(t(_, Children), L) :-
    member(C, Children),
    leaf(C, L).

node(t(R, _), R).
node(t(_, Children), L) :-
    member(C, Children),
    node(C, L).
