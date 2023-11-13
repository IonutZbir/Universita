# Modificare la funzione sottostante invocando, per ciascun comando,
# la funzione corrispondente.
# Il parametro "input" contiene l'argomento del comando,
# eventualmente una tupla se la funzione da scrivere
# deve prendere più parametri.
#
# A differenza del compito dove in genere l'input viene passato così
# come è alla funzione implementata, qui si richiede eventualmente
# di passare i singoli elementi della tupla di input attraverso
# parametri distinti
def stub_funzione(comando, input):
    if comando == "inverti stringa":
        return inverti_stringa(input)
    elif comando == "trova massimo":
        return trova_massimo(input)
    else:
        return ""


# Comando: "inverti stringa"
#
# Scrivete una funzione ricorsiva che inverta una stringa.
#
# Esempio:
# Dato l'input
# "Hello!"
# la funzione deve restituire
# "!olleH"

def inverti_stringa(stringa):
    if len(stringa) <= 1:
        return stringa
    else:
        # return inverti_stringa(testo[1:]) + testo[0]
        return stringa[-1] + inverti_stringa(stringa[:-1])


# Comando: "prima occorrenza"
#
# Scrivete una funzione ricorsiva che restituisca la posizione della prima
# di una stringa (secondo argomento) all'interno di un'altra stringa
# (secondo argomento), oppure -1 se non c'è nessun riscontro.
#
# Esempio:
# Dato l'input
# ("Mississippi", "sip")
# la funzione deve restituire
# 6
#
# Suggerimento: utilizzare una funzione ausiliaria che prenda come argomento la distanza dall'inizio di
# text in cui effettuare la ricerca.




# Comando: "trova massimo"
#
# Scrivete una funzione ricorsiva che restituisca il valore massimo all'interno di una lista
# passata.

# versione 1

# def trova_massimo(lista):
#     if len(lista) == 1:
#         return lista[0]
#     else:
#         primo_elemento = lista[0]
#         massimo_resto_lista = trova_massimo(lista[1:])
#         if primo_elemento < massimo_resto_lista:
#             return massimo_resto_lista
#         else:
#             return primo_elemento

# versione 2 (tail recursion)

def trova_massimo(lista):
    if len(lista) == 1:  # il massimo è presto trovato in una lista di lunghezza 1
        return lista[0]
    else:  # altrimenti, con due o più elementi
        if lista[0] < lista[1]:  # se il primo elemento è minore del secondo
            # il primo elemento non può essere il massimo
            # quindi si ricorre su una copia della lista a partire dal secondo
            # elemento (indice 1)
            return trova_massimo(lista[1:])
        else:
            # altrimenti, è il secondo elemento a non poter essere il massimo
            # e pertanto si ricorre su una copia della lista in cui viene
            # escluso il secondo elemento (indice 1).
            # In realtà, la copia viene create concatenando la sottolista
            # dall'indice 0 all'indice 1 escluso con la sottolista
            # dall'indice 2 incluso fino alla fine
            return trova_massimo(lista[:1] + lista[2:])


# Comando: "genera sottostringhe"
#
# Scrivete una funzione ricorsiva che restituisca tutte le sottostringhe
# di una stringa data. Le sottostringhe devono essere elencate scrivendo
# prima quelle che iniziano prima e in ordine crescente di lunghezza (a parità
# d'inizio).
#
# Esempio:
# Dato l'input
# "rum"
# la funzione deve restituire
# ["r", "ru", "rum", "u", "um", "m", "" ]
#
# Suggerimento: generare tutte le sottostringhe che iniziano con il primo carattere e quindi proseguire con la
# generazione delle sottostringhe a partire dal secondo carattere.




# Comando: "genera sottoinsiemi"
#
# Scrivete una funzione ricorsiva che restituisca tutti i sottoinsiemi di caratteri
# (non necessariamente adiacenti) di una stringa data
#
# Esempio:
# Dato l'input
# "rum"
# la funzione deve restituire
# {"rum", "ru", "rm", "r", "um", "u", "m", ""}
#
# Suggerimento: capire come derivare i sottoinsiemi richiesti per una stringa data, avendo calcolato i
# sottoinsiemi per la sottostringa che parte dal secondo carattere.


def main():
    test_suite = [("inverti stringa",
                   [("", ""), ("a", "a"), ("ab", "ba"), ("abc", "cba")]),
                  ("prima occorrenza",
                   [(("Mississippi", "sip"), 6), (("", ""), -1), (("", "a"), -1),
                    (("a", "a"), 0), (("b", "a"), -1), (("b", "aa"), -1), (("ba", "aa"), -1),
                    (("abaa", "aa"), 2), (("abaa", "aaa"), -1)]),
                  ("trova massimo",
                   [([1], 1), ([1, 2], 2), ([2, 1], 2), ([1, 2, 3], 3),
                    ([1, 3, 2], 3), ([2, 1, 3], 3), ([2, 3, 1], 3), ([3, 1, 2], 3), ([3, 2, 1], 3)]),
                  ("genera sottostringhe",
                   [("rum", ['r', 'ru', 'rum', 'u', 'um', 'm', ''])]),
                  ("genera sottoinsiemi",
                   [("rum", {'rum', 'ru', 'rm', 'r', 'um', 'u', 'm', ''})])]

    funzioni_corrette = 0
    funzioni_non_corrette = 0

    for comando, casi_di_test in test_suite:
        funzione_passa_i_test = True

        for input_di_test, risultato_atteso in casi_di_test:
            risultato_effettivo = stub_funzione(comando, input_di_test)

            if risultato_effettivo != risultato_atteso:
                print("La funzione per il comando " + repr(comando) + " ha prodotto il valore " +
                      repr(risultato_effettivo) + " per l'input " + repr(input_di_test) + "invece che " +
                      repr(risultato_atteso))
                funzione_passa_i_test = False

        if funzione_passa_i_test:
            funzioni_corrette += 1
        else:
            funzioni_non_corrette += 1

    print("Funzioni (presumibilmente) corrette:", funzioni_corrette)
    print("Funzioni errate:", funzioni_non_corrette)


main()
