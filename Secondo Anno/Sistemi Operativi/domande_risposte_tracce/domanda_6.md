## Quesito 

Discutere almeno 3 algoritmi di paginazione, specificando vantaggi e funzionamento.

## Risposta

Quando avviene un page fault, il sistema operativo attraverso algoritmi di sostituzione delle pagine, deve cercare e trovare una pagina da sfrattare per poter fare spazio.

1. Uno dei algoritmi pià facile da implementare è NRU (Not Recently Used). Questo algoritmo tiene traccia delle pagine attraverso i bit R (Riferimento) e M (Modificato)
è le suddivide in 4 classi. Inoltre ad ogni interrupt, il bit R impostato a 0. 

- 00 - R = 0, M = 0 (nessun riferimento, non modificata)
- 01 - R = 0, M = 1 (riferimento, non modificata)
- 10 - R = 1, M = 0 (nessun riferimento, modificata)
- 11 - R = 1, M = 1 (riferimento, modificata)

Al primo sguardo, la classe 1 sembra impossibile, ma si ottiene quando viene impostato a 0 il bit R dopo l'interrupt del clock di una pagina di tipo 3.
L'algoritmo rimuove una pagina a caso dalla classe con numero più basso. E' facile da implementare, semplice, e prestazioni accettabili.

2. Second Chance

3. Clock

