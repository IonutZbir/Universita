---
date: 2022-12-20
draft: true
---

# Lucene
Lucene è una delle librerie più famose per l'implementazione di un sistema di ranking.
È implementata e mantenuta dall'Apache Foundation.

Caratteristiche:
- fast indexing
- rank searching
- boolean and phrase query
- **date**-range searching

Le pagine vengono indicizzate con una struttura dati particolari.
Ogni documento è rappresentato da una **astrazione**, sul quale si possono definire dei **field** come:
- titolo
- abstract
- contenuto
- ecc...

Posso quindi effettuare la ricerca su combinazioni lineari di field.

Ogni **field** è composto da una sequenza di termini.
Ogni **classe di field** è indipendente dagli altri: avro gli tf-idf rispetto ai field titoli, poi rispetto agli abstract, ecc...

----
