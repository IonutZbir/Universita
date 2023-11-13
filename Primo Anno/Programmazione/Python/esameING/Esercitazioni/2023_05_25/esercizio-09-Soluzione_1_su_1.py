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
    if comando == "mese più piovoso":
        return mese_piu_piovoso(input)
    else:
        return ""


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

def mese_piu_piovoso(giorni_piovosi):
    giorni_pioggia_per_mese = {}

    for data in giorni_piovosi:
        # componenti_data = data.split("/")
        # mese = componenti_data[1]

        # L'enunciato sottostante prende la lista prodotta
        # dal metodo split e ne assegna gli elementi alle variabili
        # elencate a sinistra. Si rammenti che _ viene qui usato come nome
        # speciale per le variabili corrispondenti al giorno e all'anno che non
        # il cui valore non è di interesse
        _, mese, _ = data.split("/")

        # Primo approccio: incremento il valore se c'è, altrimenti lo setto a 1

        # if mese in giorni_pioggia_per_mese:
        #     giorni_pioggia_per_mese[mese] += 1
        # else:
        #     giorni_pioggia_per_mese[mese] = 1

        # Secondo approccio: inizializzo il valore a zero se la chiave non è presente,
        # e in ogni caso successivamente la incremento di 1
        if mese not in giorni_pioggia_per_mese:
            giorni_pioggia_per_mese[mese] = 0
        giorni_pioggia_per_mese[mese] += 1

    numero_massimo = 0
    mese_massimo = ""  # A lezione avevamo notato che per essere precisi si sarebbe potuto mettere "12"

    # si deve iterare sulle chiavi (cioè i mesi) in ordine crescente, in modo tale che se ci sono due
    # mesi che hanno lo stesso numero massimo di giorni di pioggia, sarà quello più distante dal
    # gennaio precedente a essere assegnato per ultimo alla variabile "mese_massimo"
    for mese in sorted(giorni_pioggia_per_mese):
        giorni_piovuti_mese = giorni_pioggia_per_mese[mese]
        if giorni_piovuti_mese >= numero_massimo: # ci va l'uguale, per gestire gli ex-equo
            numero_massimo = giorni_piovuti_mese
            mese_massimo = mese

    # Qui l'uso di "sorted" è accettabile, perché stiamo ordinando un insieme prestabilito
    # (i mesi dell'anno). Tuttavia, a lezione vi è stato fatto notare che dovendo trovare
    # il minimo (o il massimo) di una lista non va bene ordinarla (in senso crescente) e poi prendere
    # il primo (o l'ultimo) elemento. Infatti, la ricerca del minimo/massimo è un problema meno complesso
    # dell'ordinamento, in quanto può essere risolta con una semplice scansione della lista.

    # soluzione alternativa senza l'uso di sorted
    # for mese in giorni_pioggia_per_mese:
    #     giorni_piovuti_mese = giorni_pioggia_per_mese[mese]
    #     # quando devo aggiornare le variabili "numero_massimo" e "mese_massimo"?
    #     # ci sono due casi, da cui consegue l'uso dell'or
    #     # caso 1: nel mese in esame ha piovuto di più del massimo visto finora
    #     # caso 2: nel mese in esame ha piovuto quanto il massimo visto finora e il mese è maggiore del mese cui è stato
    #     #         precedentemente il valore massimo
    #     if giorni_piovuti_mese > numero_massimo or (giorni_piovuti_mese == numero_massimo and mese > mese_massimo):
    #         numero_massimo = giorni_piovuti_mese
    #         mese_massimo = mese

    return mese_massimo


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
