Un'idea migliore per ottimizzare la scrittura dei termini è quella di salvarli come una **unica grande stringa** fatta dalla concatenazione dei termini.

A questo punto, nella nostra struttura dati a dizionario mi serviranno:
- 4 bytes per la **term frequency**.
- 4 bytes per i **puntatori** alle aree di memoria in cui si trovano le **posting lists**.
- 3 bytes per il **puntatore** che indica l'inzione del **termine** all'interno della stringa.
![](IR_dictionary_as_a_string_1.png)

```ad-warning
title: Importante
Importante scrivere sulla *lunga stringa* i termini nell'ordine in cui appaiono nel dizionario.
Così facendo so identificare il **puntatore** al termine successivo e so dove **fermarmi** nella lettura del termine.
```

```ad-warning
title: Importante
In realtà i 3 byte vanno bene per la solita collezione di 400.000 termini.
Dato che mediamente ogni termine è lungo 8 byte, avremo una stringa lunga $400.000 \times 8B = 3.2MB$.
Perciò per indicizzare tutti i caratteri di questa stringa mi serviranno $\log_2{3.2MB} \leq 22\text{bits} \leq 3\text{Bytes}$.


Perciò il numero totale di bits necessari per l'indicizzazione dei termini sono **in media** $\lceil \log_2{(M \times 8)} \rceil$, dove $M$ è il numero di termini ed 8 è la lunghezza media. 
```


La dimensione di un dizionario di 400.000 termini sarà quindi  $$400.000 \times (11B + 8B) = 7.6 MB$$ risparmiando quindi circa 4MB rispetto agli $11.2MB$ del [[Dictionary storage|metodo semplice]].