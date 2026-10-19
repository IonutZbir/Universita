
# Ranked retrieval
Gli indici visti fin ora erano pensati per supportare [[Boolean Retrieval|query booleane]]: un documento può rispettare oppure no l'espressione booleana che forma la query.
Nel caso di enormi collezioni di documenti, un risultato di una query potrebbe eccedere di molto il numero di documenti che un umano è in grado di processare.
Se non si è in grado di processare il retrieval di una query per via della sua enorme mole, di fatto rende tale risultato inutile.

Un'altra problematica è che le query booleane sono un buono strumento di ricerca per utenti esperti o per sistemi automatici, ma non per l'utenza media che, invece, vorrebbe esprimere le proprie query in **linguaggio naturale**.

Un ulteriore problema è, data una espressione in linguaggio naturale, decidere in maniera **automatica** come convertirla in una espressione booleana che possa essere interpretata dal nostro motore di IR.
I risultati a diverse interpretazioni potrebbero incorrere in risultati del tutto differenti.
Infatti consideriamo la query `world climate change merkle`, espressa in **linguaggio naturale**.
Possiamo processarla come:
	- `world climate change` AND `merkle` $\rightarrow \emptyset$
	- `world climate change` OR `merkle` $\rightarrow$ **very big result**


Possiamo quindi definire le proprietà che si voglia che un motore di IR abbia:
1. Deve mostrare solo un **piccolo sottoinsieme** di pagine più **rilevanti** (per esempio le prime 10). ^79c83c
2. L'utente non dovrebbe esprimere le query in maniera troppo complessa, è preferibile che usi il **linguaggio naturale**.

Per il [[#^79c83c|punto 1]] possiamo assegnare uno **score** *di rilevanza* ai documenti, generalmente **normalizzato** in $\left[ 0,1 \right]$.
Così facendo possiamo **ordinare** il risultato in modo **non crescente**, e ritornare le prime $10$ o $20$ pagine con *score* più alto.

Tale *score* deve essere definito in modo tale da rappresentare una sorta di **indice di rilevanza** del documento rispetto alla query.

Per esempio, se cerco un termine `X` mi aspetto che più in documento appare il termine

- [[Jaccard coefficient]]
- [[Bag of words model - Term Frequency tf]]
- [[TF-IDF weight]]

Quantity | Symbol | Definitionterm
---|---|---
frequency | $\text{tf}_{t,d}$ | number of occurrences of $t$ in $d$
document frequency | $\text{df}_{t}$ | number of documents in the collection that $t$ occurs in
collection frequency | $\text{cf}_{t}$ | total number of occurrences of $t$ in the collection

^433f1d

- [[Vector Space Model]]
- [[Variants of weighting]]