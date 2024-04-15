/* In prolog è possibile in RT definire regole, predicti e fatti.
 *  E' possibile cambiare il programma in RT 
*/

/*
 * assert(.....) -> fatti che vogliamo "asserire", di default lo mette in coda
 * retract(.....) -> elimina fatti/predicati se esistono, il primo che unifica 
 * retractAll(.....) -> elimina tutti i fatti/predicati che si unificano insieme
 * assertz(.....) -> mette il predicato in coda
 * asserta(.....) -> mette il predicato in testa
 * consult(.....) -> legge una riga e fa assert
*/

/*
 *  :- dynamic (predicato/n), n numero di argomenti -> :- dynamic(lun/2)
 *  dichiara che per un predicato posso asserire rettrattare, e o uso per i predicati che sono gia scritti all interno del prog. 
*/

/*
 * =.. (univ) -> lun(0, 1) =.. [lun, 0, 1]
 * A =.. [lun, 0, 1] possiamo generaere predicati e unificarli ad una variabile
*/

/* Funtore = nome di A*/
/* funtore(lun([], 0), X)*/

funtore(A, Funtore) :-
    A =.. [Funtore|_].


