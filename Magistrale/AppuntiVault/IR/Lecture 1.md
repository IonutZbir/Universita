---
date: 2022-10-11
draft: true
---
## Information Retrieval
**Information Retrieva**: trovare del materiale in una **larga** collezione di dati non necessariamente strutturati (generalmente del test), che soddisfano degli **information need** (dei **bisogni informativi**).

Alcuni esempi di collezioni:
- web
- e-mail
- laptop file system
- conoscenze in una azienda
- informazioni legali
- tweet

Inizialmente (fino a qualche anno fa) avevamo più dati **non strutturati** che **strutturati** (80-20)
Però in genere i soldi giravano più su quelli strutturati.

Adesso però anche il mercato sui dati non strutturati è cresciuto molto, superando quello sui dati strutturati.

## Basic assumptions
- **Collection**: un insieme (assumendola **statica**) di documenti. ^da9c63
- **Goal**: recupeare un insieme **rilevante** (rispetto alle **information need**) di questi docuementi.

## IR vs DB
- **DB** accesso ai dati in base a dei **metadati** che descrivono un documento.
- **IR** consentono di trovare un documento in base al suo contenuto.

IR | DBMS
---|---
Semantica libera | Semantica rigorosa e precisa
Ricerco in base al contenuto | SQL (linguaggio rigoroso)
Dati non strutturati (documento) | Dati rigorosamente strutturati
Principalmente in lettura. Più richiesto di lettura che scrittura (leggo più tweet di quanti ne scrivo) | Più o meno lettura e lettura equivalenti
Si richiedono i primi $k$ elementi, ordinati per qualità. | Si richiedono **tutti** i possibili risultati.


## "Bag of Words" Model
Le tecniche tradizionali sono:

- Modello tipico di IR:
	- ogni **document** è considerata una **bag** (**multiset**) di **words** (**termini**).

- **Stop Word**: rimuovere certi termini irrilevanti, come gli articoli, le preposizioni, ecc...

## Rilevanza
Quello che ci serve è definire una **funzione di rilevanza** che mi definisce uno **score** dei documenti nella soluzione.

Vogliamo definire come poter **implementare praticamente** tali funzioni, e come poterli approssimare all'atto pratico.


## Performance
- **DBMS**: in genere garantisce efficienza (generica) su ogni operazione, SELECT, INSERT, UPDATE, DELETE
- **IR**: in genere si fanno sono SELECT, e raramente un INSERT. Per implementare una DELETE, in genere si usa un **flag** `delete`.

## Scalabilità
È importante riuscire a implementare tali motori di ricerca anche in maniera **scalabile**, oltre che efficiente.

