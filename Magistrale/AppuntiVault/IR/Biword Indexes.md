Un primo approccio per il [[Positional postings and phrase queries#^017df1|nostro problema]] è quello di considerare ogni coppia di termini **consecutivi** in un documento come una singola frase.
Tali coppie di termini sono anche detti **biword**.

Per esempio, se abbiamo il documento `Friends, Romans, Countrymen` generiamo le biword:
- `friends romans`
- `romans countrymen`

In tale modello la query `stanford university palo alto` verrà trattata come
$$\text{stanford university} \land \text{university palo} \land \text{palo alto}$$

Ci aspettiamo che questa query funzioni bene in pratica, ma può incorrere in svariati **falsi positivi**.
Infatti senza esaminare il contenuto dei documenti, non si può verificare che il risultato della query ritorni tutti i documenti che contengano l'intera sequenza **consecutiva** delle 4 parole.