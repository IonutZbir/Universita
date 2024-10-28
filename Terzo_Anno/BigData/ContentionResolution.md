# Contention resolution in distributed systen

Supponiamo di avere $n$ processi, $P_1,\ P_1,\ \dots,\ P_n$ ciascuno in competizione per accedere ad una risorsa condivisa, per esempio un database. L'accesso alla risorsa deve essere in mutua esclusione, ovvero se due o più processi provano ad accedere alla risorsa in contemporanea, allora tutti i processi vengono bloccati.

I processi in un sistema distribuito non possono comunicare direttamente tra loro, e non è possibile uno scheduling deterministico, come ad esempio uno schema in cui i processi siano numerati da $1$ a $n$ e al tempo $i$ acceda il processo $i$ (un tipo di Round Robin). Questo approccio richiederebbe che i processi fossero etichettati in modo fisso, ma in un sistema distribuito tale etichettatura non è attuabile. Inoltre, l'insieme dei processi potrebbe non essere statico: capita spesso che un processo sia inattivo in un certo momento o che se ne aggiungano di nuovi. Di conseguenza, uno scheduling deterministico risulta impraticabile.

Quindi uno schema tipico che si usa per lo scheduling nei sistemi distribuiti è la randomizzazione.

Come funziona l'algoritmo:
Qui c'è un problema classico che nei sistemi distribuiti viene chiamato **symmetry breaking**, è una tecnica usata nei sistemi distribuiti per prevenire che due processi eseguono le stesse azioni in simultaneo.

Ciascun processo ad ogni round (quindi ad ogni istante di tempo) richiede l'accesso al database/risorsa con probabilità $p = \frac{1}{n}$ e con probabilità $1 - p$ di non accedere.
Il round ha successo se esattamente un processo accede alla risorsa e tutti gli altri non accedono.

Inziamo con definire alcuni eventi.

- Sia $S[i, t]$: l'evento che $P_i$ tenta di accedere al database al tempo $t$. Usando $p = \frac{1}{n}$ possiamo massimizzare questa probabilità ottendo che
$$Pr(S[i, t]) = p (1 - p)^{n - 1} = \frac{1}{n}(1 - \frac{1}{n})^{n - 1}$$

Perchè la probabilità è $p(1 - p)^{n - 1}$? Il processo $P_i$ chiede di accedere alla risorsa con probabilità $p$ mentre i restanti $n - 1$ processi non devono acccedere alla risorsa con probabilità $1 - p$.

Quindi la probabilità che un round abbia successo è dell'ordine di $\frac{1}{n \cdot e}$ in quanto $(1 - \frac{1}{n})^{n - 1}$ per $n$ molto grande tende a $\frac{1}{e}$
