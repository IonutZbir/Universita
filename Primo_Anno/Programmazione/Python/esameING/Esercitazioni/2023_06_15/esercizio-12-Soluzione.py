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
        if isinstance(elemento, list):  # oppure, type(elemento) == list
            somma += somma_lista_ricorsiva(elemento)
        else:
            somma += elemento
    return somma

# Si assuma che p sia una istanza della classe Persona,
# che è a sua volta sottoclasse della classe Animale

# isinstance(p, Animale) è True
# type(p) == Animale è False (perché type(p) restituisce Persona)

# se si vuole considerare anche le sottoclassi, si può scrivere
# issubclass(type(p), Animale) (perché issubclass verifica
# che Persona è sottoclasse di Animale)

# si noti che issubclass(Animale, Animale) è True, pertanto non c'è
# bisogno di gestire separatamente le istanze dirette della classe
# d'interesse

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
