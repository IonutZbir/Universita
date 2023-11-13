# Modificare la funzione sottostante invocando, per ciascun comando,
# la funzione corrispondente.
def stub_funzione(comando, input):
    output = None
    if comando == "comando di esempio":
        output = funzione_di_esempio(input)
    elif comando == "somma lista ricorsiva":
        output = somma_lista_ricorsiva(input)

    return output


def funzione_di_esempio(parametro):
    return "Hello"

# Comando: "somma lista ricorsiva"
#
# Scrivete una funzione ricorsiva che sommi tutti i numeri contenuti in una lista (di liste, di liste, etc.)
#
# Esempio:
# Dato l'input
# [1, [2, 3], [4, [5]]]
# la funzione deve restituire
# 15


def somma_lista_ricorsiva(input):
    somma = 0
    for elemento in input:
        if isinstance(elemento, list): # oppure, type(elemento) == list
            somma += somma_lista_ricorsiva(elemento)
        else:
            somma += elemento
    return somma



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
    test_suite = [("somma lista ricorsiva",
                   [([1, [2, 3], [4, [5]]], 15)])]

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
