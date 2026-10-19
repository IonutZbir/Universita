Consideriamo ora un alternativa ai permuterm index, ossia i **k-grams**. Invece di ruotare i termini si costruisce un secondo indice che va dai **k-grammi** ai termini del dizionario che lo contengono.

In generale, un **k-gram** è una sequenza di $k$ caratteri consecutivi in un termine. Limitiamoci a considerare i **bi-grammi**. 

Per la parola `hello` $\to$ $\{\text{`\$h, he, el, ll, lo, o\$`}\}$ dove il `$h` e il `o$` servono per indicare l'inizio e la fine della parola. Per ogni parola nel dizionario, si estraggono i bigrammi e si costruisce un indice che va dai bigrammi **ai termini che li contengono**. Consideriamo il seguente esempio:

```python
s = "mon*"
bigram_index = {
	"$m": ["mace", "madden"],
	"mo": ["among", "amortize"],
	"on": ["along", "among"],
}
```

Per risolvere la query `mon*`, questa può essere interpretata come `$m AND mo AND on`. Questo perché usando `$m` dico che la parola inizia con `m`, poi i bigrammi obbligatori sono `mo` ed `on` ma non metto `n$` perchè la query non specifica che la parola debba finire con `n`.  Quindi tra i risultati della query otterremo ad esempio `money, monitor, month, moon`. Osserviamo che ci viene restituito anche `moon` poiché tra i bigrammi di `moon` ci sono anche `$m, mo, on`. Con questa tecnica è possibile ottenere dei **falsi positivi** perciò è necessario applicare un filtro tra i termini ottenuti prima di effettuare la ricerca nelle postings vere e proprie.

In conclusione, anche con i `k-grams`, dopo aver filtrato i termini, bisogna eseguire query booleane sui documenti per trovare quelli ce contengono ciascun termine enumerato, e quindi esattamente come per i permuterm ciò può voler dire fare merge tra le liste di posting molto lunghe. Inoltre, mantenere wildcard in un motore di ricerca non è una buona soluzione in quanto, le persone essendo pigre, tenderanno ad abusarne. Quindi in generale, i grandi motori di ricerca tendono a non supportare le wildcard.



