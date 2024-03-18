# si consideri questa lista di nomi di persone
# si assuma per semplicità che ogni persona abbia un nome e un cognome
persone = ["leonardo albanese", "michela ramazzotti", "adam sandler"]


def estrai_cognome(nome_completo):
    return nome_completo.split()[1]


def estrai_nome(nome_completo):
    return nome_completo.split()[0]


def lunghezza_nome(nome_completo):
    return len(estrai_nome(nome_completo))


print("Ordinamento come stringhe")
print(sorted(persone))

# e se le voglio ordinare per cognome?
# * creo una nuova lista di coppie (cognome, nome completo)
# * ordino questa lista (ricordarsi che le liste/tuple sono confrontate lessicograficamente, quindi a partire dal primo elemento)
# * genero una nuova lista contenente solo la seconda componente (nome completo) di ciascun elemento della lista di cui sopra

lista_per_lunghezza_nome = []
for nome_completo in persone:
    l = estrai_cognome(nome_completo)
    coppia = (l, nome_completo)
    lista_per_lunghezza_nome.append(coppia)

lista_per_lunghezza_nome.sort()  # il metodo sort ordina la lista su cui viene invocato, anziché produrne una copia ordinata

persone_ordinate_per_lunghezza_nome = []
for coppia in lista_per_lunghezza_nome:
    nome_completo = coppia[1]
    persone_ordinate_per_lunghezza_nome.append(nome_completo)

print("Ordinamento per cognome usando le tuple")
print(persone_ordinate_per_lunghezza_nome)

# e se le vogliamo ordinare per la lunghezza del nome?
# * creo una nuova lista di coppie (lunghezza nome, nome completo)
# * ordino questa lista (ricordarsi che le liste/tuple sono confrontate lessicograficamente, quindi a partire dal primo elemento)
# * genero una nuova lista contenente solo la seconda componente (nome completo) di ciascun elemento della lista di cui sopra

lista_per_lunghezza_nome = []
for nome_completo in persone:
    l = lunghezza_nome(nome_completo)
    coppia = (l, nome_completo)
    lista_per_lunghezza_nome.append(coppia)

lista_per_lunghezza_nome.sort()  # il metodo sort ordina la lista su cui viene invocato, anziché produrne una copia ordinata

persone_ordinate_per_lunghezza_nome = []
for coppia in lista_per_lunghezza_nome:
    nome_completo = coppia[1]
    persone_ordinate_per_lunghezza_nome.append(nome_completo)

print("Ordinamento per lunghezza del nome usando le tuple")
print(persone_ordinate_per_lunghezza_nome)

# si dovrebbe notare come entrambi i casi sono di fatto gestiti dallo stesso algoritmo
# semplicemente cambiando la funzione da invocare.
# come possiamo farlo? assegnando la funzione da usare a una variabile
# ancora meglio incapsuleremo il tutto in una funzione

def ordina_per_chiave(lista, estrattore_chiave):
    lista_supporto = []

    for elemento in lista:
        # poiché il parametro "estrattore_chiave" contiene il riferimento a una funzione,
        # si può usare la notazione della chiamata di funzione per invocare tale funzione riferita
        chiave = estrattore_chiave(elemento)
        coppia = (chiave, elemento)
        lista_supporto.append(coppia)

    lista_supporto.sort()

    lista_ordinata = []
    for coppia in lista_supporto:
        elemento = coppia[1]
        lista_ordinata.append(elemento)

    return lista_ordinata


print("Ordinamento per cognome usando la procedura generica")
print(ordina_per_chiave(persone, estrai_cognome))  # come secondo argomento sto passando il riferimento alla funzione estrai_cognome:
                                                   # si noti che non ci sono una coppia di parentesi tonde affianco a questa funzione
                                                   # perché non la sto invocando in questo istante

print("Ordinamento per lunghezza del nome usando la procedura generica")
print(ordina_per_chiave(persone, lunghezza_nome))  # come secondo argomento sto passando il riferimento alla funzione lunghezza_nome
                                                   # si noti che non ci sono una coppia di parentesi tonde affianco a questa funzione
                                                   # perché non la sto invocando in questo istante

# In realtà, non c'è bisogno d'inventare questa funzione perché la funzione standard "sorted" già possiede il parametro
# "key" atto allo scopo

print("Ordinamento per cognome usando sorted")
print(sorted(persone, key=estrai_cognome))  # il codice key=estrai_cognome è un esempio di keyword argument, che ci permette
                                            # di assegnare un valore a un parametro di una funzione identificato attraverso
                                            # il suo nome anziché attraverso la sua posizione

print("Ordinamento per lunghezza del nome usando sorted")
print(sorted(persone, key=lunghezza_nome))


# ------------------------------------------

# Se confronto due date gg/mm/aaaa come stringhe, ottengo un risultato sbagliato perché confrontando i caratteri da
# sinistra verso destro, sto effettivamente confrontando lessicograficamente le due date considerando nell'ordine
# giorno, mese, anno

data_1 = "10/01/2022"
data_2 = "10/02/2018"

print(data_1 + " < " + data_2)
print(data_1 < data_2)

# occorre riscrivere le due date da confrontare nel formato aaaa/mm/gg
gg_1, mm_1, aaaa_1 = data_1.split("/")
data_1_riscritta = aaaa_1 + "/" + mm_1 + "/" + gg_1

gg_2, mm_2, aaaa_2 = data_2.split("/")
data_2_riscritta = aaaa_2 + "/" + mm_2 + "/" + gg_2

# si noti che questa riscrittura è un candidato ideale per una nuova funzione

print(data_1_riscritta + " < " + data_2_riscritta)
print(data_1_riscritta < data_2_riscritta)

# si noti che confrontare due interi come stringhe produce il risultato atteso solo se le stringhe hanno la stessa
# lunghezza, eventualmente inserendo degli 0 a sinistra

print("2022/03/10 < 2022/10/10")
print("2022/03/10" < "2022/10/10")

print("2022/3/10 < 2022/10/10")
print("2022/3/10" < "2022/10/10")
