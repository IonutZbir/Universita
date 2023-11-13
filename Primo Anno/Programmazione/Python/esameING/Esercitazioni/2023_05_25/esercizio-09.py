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
    output = None
    if comando == "comando di esempio":
        output = funzione_di_esempio(input)

    return output


def funzione_di_esempio(parametro):
    return "Hello"

# Comando: "mese più piovoso"
#
# Si scriva una funzione che, prendendo una lista input di date
# che rappresentano i giorni in cui è piovuto nell’arco dell’anno,
# restituisca il mese con più giorni piovosi.
# A parità di giorni piovosi, deve essere restituito il mese più lontano al gennaio precedente.
# Esempio:
# elementi = ['10/01/2018', '11/02/2018', '11/01/2018', '18/03/2018', '12/02/2018']
# output = '02'
# perché 01 e 02 hanno lo stesso numero di giorni piovosi e 02 è più lontano al gennaio precedente.



def main():
    test_suite = [("mese più piovoso",
                   [(['10/01/2018', '11/02/2018', '11/01/2018', '18/03/2018', '12/02/2018'], '02')])]

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
