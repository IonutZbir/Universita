---
date: 2022-12-14
draft: true
---

# Relevance feedback & query expansion

> Posso sfruttare il **feedback** dell'utente per migliorare la qualità del ranking?

## Migliorare la recall
- $q$ = \[aircraft\]

Se un documento contiene "aereo" esso non verrà restituito perché non ha ilt ermine "aricraft", anche se è un perfetto sinonimo.

Contrassegnamo i documenti restituiti che sono (secondo l'utente) rilevante.
Osservare che tutti questi documenti introducono **nuovi termini**.

> Se c'è un termine non presente nella query, ma che in realtà hanno dei termini in comune, vuol dire che in realtà tali termini sono utili per la query. Perché non sfruttarli?

Perciò
- faccio una query.
- l'utente contrassegna i documenti che ritiene migliori (magari leggendo il solo titolo).
- prendo i termini in comune tra i documenti "migliori".
- inserisco quelli più "significativi" e li inserisco nella query, in maniera opportunamente pesati.

Ricordiamo che un documento è rappresentato come un vettore.
Se prendo tutti i documenti **migliori**, posso definirne uno **medio** (centroide), e sfruttarlo per la query.
$$\mu(D_r) = \frac{1}{|D_r|}\sum_{d \in D_r}\overline{d}$$

Posso anche sfruttare i documenti giudicati non rilevanti, per definire un centroide usato per tenere fuori i non rilevanti

$$\overline{q}_{opt} = \overline{q} \cdot (\mu(D_r) -  \mu(D_{nr}))$$

$$\overline{q}_m = \alpha \overline{q}_{m-1} + \beta\mu(D^{(m-1)}_r) - \gamma \mu(D^{(m-1)}_{nr})$$
con $\alpha, \beta, \gamma$ fissati.

Quali assunzioni?
1. Assumo che l'utente conosca abbastanza bene i termini della collezione per fare la query.
2. I documenti rilevanti hanno molti termini in comune (non è detto).

Perché non funziona?
1. Le persone non vogliono dare un feedback.
2. 

```ad-tldr
title: Ad hoc retrieval
I sistemi di IR in cui non si rifanno i rank a seguito di un feedback di un utente.
```


----------
# Pseudo relevance feedback
Assumiamo che il sistema di IR funzioni bene.
Prendiamo i primi $k$ documenti nello score, e li usiamo per espandere la query (senza chiedere il feedback agli utenti), così da considerare tutti quei termini non presenti nella query che potrebbero essere utili.

Obiettivo.
- aumentare i veri positivi.
- ridurre i falsi negativi.

Cosa rischiamo se la applichiamo troppe volte?
- di aumentare i falsi positivi

------------
# Query expansion
Nel vector space model consideriamo i documenti come vettori di termini, e due docuemnti sono simili se hanno vettori simili.

Viceversa, possiamo vedere i termini come vettori di documenti nella nostra collezione.
Se due vettori-termine hanno in comune molti documenti, può voler dire che all'interno della nostra collezione questi due termini hanno una sorta di relazione.

## Polisemia
La capacità di una parola di avere differenti significati.

### Relazione Paradigmatiche
Due parole sono in **relazione paradigmatica** se interncambiandole in un contesto, la frase continua a rimanere sensata ma il senso cambia.

### Sinonimia
Due parole sono **sinonime** se interncambiandole in un contesto, il significato non cambia.

### Quasi Sinonimia
Due parole sono **quasi sinonimi** se intercambiandole il significato cambia ma non di troppo.

### Topical Relation
Due termini sono in topical relation se concorrono negli stessi documenti, ma non è detto che siano sinonimi o in relazione paradigmatica.

Non conviene usare i termini in topical relatcion, altrimenti rischi di essere trascinato verso documenti che non sono rilevanti.

- termini sinonimi $\implies$ relazione paradigmatica $\implies$ topical relation
