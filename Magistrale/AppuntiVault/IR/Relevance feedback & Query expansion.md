Abbiamo [[Evaluation of IR systems|visto in precedenza]] come valutare la **qualità** di un sistema di IR, in particolare abbiamo visto:
- come valutare rispetto al [[Set Based Measures|numero di documenti rilevanti]] restituiti.
- come valutare rispetto al [[Rank-Based Measures|ranking]] dei documenti restituiti.

Abbiamo anche visto che per misurare la qualità di un sistema abbiamo bisogno di un **evaluation benchmark**, il quale è composto da tre elementi:
1. una sottocollezione di documenti su cui fare i test.
2. un insieme di test-query da sottoporre al sistema rispetto alla sottocollezione di documenti di test.
3. un **etichettamento** di rilevanza (fatto a priori) di ogni coppia *documento-query* del nostro benchmark.

Tra le misure più semplici viste abbiamo:
- La [[Set Based Measures#^e84cfa|Precision]] $P$, ovvero la frazione di documenti rilevanti nella risposta $$P = \frac{\# \text{relevant document retrieved}}{\# \text{retrieved document}} = \frac{tp}{tp+fp}$$
- La [[Set Based Measures#^eed895|Recall]] $R$, ovvero la frazione di documenti rilevanti restituiti in totale $$R = \frac{\# \text{relevant document retrieved}}{\# \text{relevant document}} = \frac{tp}{tp+fn}$$
- La [[Set Based Measures#F-Measure|F-Measure]] $F$, ovvero una **media armonica** tra precision e recall. Un caso particolare è la $F_1$ measure, dove precision e recall sono ugualmente pesate $$F_1 = \frac{2PR}{P+R}$$
**Problema:** spesso precision e recall sono in conflitto tra loro, se voglio aumentare molto la recall recupero più documenti, ma rischio cosi di includere molti documenti non rilevanti abbassando la precision e viceversa.

Quindi ci concentreremo a risolvere il seguente problema: un utente potrebbe scrivere una query troppo semplice, usando parole diverse da quelle presenti nei documenti rilevanti e quindi non riuscire a recuperarli con un sistema di retrieval semplice. Vogliamo quindi **migliorare la Recall**.

Ad esempio, un documento rilevante potrebbe contenere `plane`, ma non `aircraft` che magari è la parola usata dall'utente. Dal momento che i motori di IR visti finora si basano solo sul match dei termini, allora questo non riuscirebbe a recuperare quel documento nonostante sia effettivamente rilevante per il bisogno informativo dell'utente.

**Come recuperare documenti rilevanti anche quando non contengono esattamente le parole della query originale?** 

Un primo metodo è quello della **Query Expansion**

Se l'utente cerca `aircraft`, il sistema potrebbe aggiungere in automatico le seguenti parole alla query: `plane, airplane, aviation, etc...`.


```ad-tldr
Due termini sono **sinonimi** se scambiandoli tra di loro le frasi in cui appaiono non cambiano di **senso**.
```


Esistono sostanzialmente due approcci per risolvere questo problema:
1. Approccio **locale**, in cui si fa un'analisi del risultato delle query per poi migliorare la query successiva. In pratica si va a vedere quali documenti l'utente ha giudicato rilevante e li sfrutta per migliorare la query: [[Relevance Feedback]]
2. Approccio **globale**, in cui si fa un'analisi globale della collezione per generare un [[#^dcdf9e|tesauro]] dei termini di dominio della collezione, per poi usarlo per **raffinare** la query: [[Query Expansion]]

```ad-tldr
title: Tesauro
Un **tesauro** è una sorta di vocabolario di termini di un dominio, strutturati e correlati tra loro in una struttura gerarchica. Ad esempio i sinonimi.
```

^dcdf9e

----
```ad-important
title: Obiettivo
1. Aumentare i **true positive**
2. Ridurre i **false negative**
```
