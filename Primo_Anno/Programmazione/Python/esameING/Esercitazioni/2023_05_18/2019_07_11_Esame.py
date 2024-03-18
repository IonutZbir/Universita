#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
# =================================================================================================
#                              *****TASSATIVO*****
#
# CONSEGNARE UN CODICE PER CUI ALMENO 2 ESERCIZI PASSINO LA VALUTAZIONE AUTOMATICA
#
# N.B. LA VALUTAZIONE EFFETTIVA UTILIZZERA' ALTRI INPUT E OUTPUT - SE IL COMPITO E' VALUTATO CORRETTO
#      CON I DATI DELLA VALUTAZIONE DI QUESTO FILE, NON VI E' GARANZIA CHE SIA CORRETTO SEMPRE
#
# =================================================================================================
#
# FASE DI CONSEGNA
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CONSEGNARE UN SOLO FILE CON TITOLO: [NUMERO_CODICE]_[NUMERO_MATRICOLA].py
#
# dove [NUMERO_CODICE] è il codice assegnato sul foglio e [NUMERO_MATRICOLA] è il vostro numero di matricola
#
# ESEMPIO : 071_00713042.py
#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCHEMA DI VALUTAZIONE
#  - 2 ESERCIZI FUNZIONANTI DA 16 A 20
#  - 3 ESERCIZI FUNZIONANTI DA 16 A 24
#  - 4 ESERCIZI FUNZIONANTI DA 16 A 28
#  - DOMANDA TEORICA DA 0 A 3 PUNTI
# LA VALUTAZIONE DIPENDE ANCHE DA COME SONO STATI RISOLTI GLI ESERCIZI

nome = "SOSTITURE QUI CON IL VOSTRO NOME NOME"  #LASCIARE UNA STRINGA
cognome = "SOSTITURE CON COGNOME"               #LASCIARE UNA STRINGA
matricola = "SOSTITUIRE CON MATRICOLA"          #LASCIARE UNA STRINGA
codice = "SOSTITUIRE CON CODICE SUL FOGLIO"     #LASCIARE UNA STRINGA



# ESERCIZIO N. 1  Difficoltà: Alta
# Si scriva una funzione
#    primoEsercizio(immagine)
# che prenda in input una figura in un quadrato e
# restituisca in output:
# 1) il carattere + se la figura rappresenta una croce disegnata da asterischi *
# 3) il carattere s se la figura non è una croce
#
# Esempio
#  immagine = "  *  \n #  output = "+"
#                *  \n #
#              *****\n #
#                *  \n #
#                *  \n"#
#                      #
#
#  immagine = "  *  \n #  output = "s"
#                *  \n #
#              *   *\n #
#                *  \n #
#                *  \n"#
#                      #
#
#  immagine = "   \n #  output = "s"
#              ***\n #
#                 \n"#
#                    #
# RICORDARSI: per vostra comodità, mostriamo gli \n (ritorni a capo) della stringa
# anche se questi non si vedono quando la stringa viene stampata


def primoEsercizio(immagine):
    return "non_fatto"


# ESERCIZIO N. 2 Difficoltà: Media
# Si scriva una funzione:
#      output = secondoEsercizio(L)
# che prende in input L che rappresenti una matrice
# attraverso una lista di n liste di n numeri
# e restituisca in output:
#  - la somma degli elementi della diagonale se L è una matrice diagonale
#  - 0 se la matrice L NON è una matrice diagonale
#
# Esempio
#         L =  [[2,0,0,0],   #  output = True
#               [0,1,0,0],   #
#               [0,0,3,0],   #
#               [0,0,0,1]]   #
#
#         L =  [[2,0,0,0],   #  output = False
#               [0,1,0,0],   #
#               [0,0,3,0],   #
#               [0,4,0,1]]   #
#
# Chiarimento: Una Matrice è detta Matrice Diagonale quando gli elementi L[i][j] fuori dalla digonale sono tutti nulli.
#              La diagonale di una matrice sono tutti quegli elementi L[i][j] per cui i è uguale a j.






def secondoEsercizio(L):
    return 0


# ESERCIZIO N. 3 Difficoltà: Bassa
# si scriva una funzione che prenda in input una frase in una stringa e restituisca
# in output un dizionario che conti il numero di ripetizioni delle parole nella frase.
#
#   output = terzoEsercizio(input)
#
#
# Esempio
#   input = "il gatto morde il gatto"
#   output = {'il':2,'gatto':2,'morde':1}


def terzoEsercizio(input):
    return None


# ESERCIZIO N. 4 Difficoltà: Molto Bassa
# si scriva una funzione che prende in input una stringa che rappresenta una frase e
# restituisca una stringa in cui le parole della stringa di input siano ordinate lessicograficamente
# (come in un dizionario)
#
# Esempio
# input = "sei stato un grande"
# output = "grande sei stato un"


def quartoEsercizio(sequenza1):
    return None



# Esercizio 5:
#
# Domanda teorica : Si descriva descriva il concetto di complessità nel caso peggiore e si calcoli la complessità
# nel caso peggiore di un algoritmo che deve sommare i numeri in una lista:
#
# L è la lista data
# somma = 0
# for i in lista:
#    somma += i
#
# Si inserisca la risposta in questa stringa:

risposta_teorica = "RISPONDERE QUI"





#### ESEMPIO DI VALUTAZIONE ----

def main() :
    test_primo_esercizio = [("  *  \n  *  \n*****\n  *  \n  *  \n","+"), ("  *  \n  *  \n*  **\n  *  \n  *  \n","s"),("  *  \n  ***\n*****\n  *  \n  *  \n","s")]


    test_sencondo_esercizio = [([[2,0,0,0],[0,1,0,0],[0,0,3,0],[0,0,0,1]],7),([[2,0,0,0],[0,1,0,0],[0,0,3,0],[1,0,0,1]],0)]


    test_terzo_esercizio = [("il gatto morde il cane",{'il':2,'gatto':1,'morde':1,'cane':1}),
        ("il cane rincorre un cane",{'il':1,'cane':2,'rincorre':1,'un':1})]

    test_quarto_esercizio = [("Ciaoneeee Ho finito gli eserciziiiiii","Ciaoneeee Ho eserciziiiiii finito gli"),
                             ("Sempre questi esercizi macchinosi ci assegna il tipo","Sempre assegna ci esercizi il macchinosi questi tipo"),
                             ("Questo esercizio in reatà è molto semplice quasi troppo semplice","Questo esercizio in molto quasi reatà semplice semplice troppo è")]

    primo_sorpassa_test_di_base = True
    secondo_sorpassa_test_di_base = True
    terzo_sorpassa_test_di_base = True
    quarto_sorpassa_test_di_base = True

    esercizi_corretti = 0

    for (input,expected_output) in test_primo_esercizio :
        output = primoEsercizio(input)
        if output != expected_output:
            print("PRIMO ESERCIZIO\n------------------------\nERRORE\n" + str(output) + "\nnon è quanto richiesto come ouput per input \n" + input + "\ndovrebbe invece essere così:\n" + str(expected_output) )
            primo_sorpassa_test_di_base = False
    if (primo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti  + 1


    for (L,expected_output) in test_sencondo_esercizio:
        output = secondoEsercizio(L)
        if output != expected_output :
            print("\n\nSECONDO ESERCIZIO\n------------------------\nERRORE\n" + str(output) + "\n non è quanto richiesto per la lista\n" + str(L)  + "\ndovrebbe invece essere così:\n" + str(expected_output) )
            secondo_sorpassa_test_di_base = False
    if (secondo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti  + 1



    for (dati,medie_attese) in test_terzo_esercizio :
        medie = terzoEsercizio(dati)

        if medie !=  medie_attese:
            print("\n\nTERZO ESERCIZIO\n------------------------\nERRORE\n" + str(
                medie) + "\nnon sembra essere giusto rispetto all'input\n" + str(
                dati) + "\ndovrebbe invece essere così:\n" + str(medie_attese))
            terzo_sorpassa_test_di_base = False
    if (terzo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti  + 1

    for (input_s1, expected_output) in test_quarto_esercizio:
        output = quartoEsercizio(input_s1)
        if output != expected_output:
            print("QUARTO ESERCIZIO\n------------------------\nERRORE\n" + str(output) + "\nnon è quanto richiesto per gli input \n" + input_s1 + "\ndovrebbe invece essere così:\n" + str(expected_output) )
            quarto_sorpassa_test_di_base = False
    if (quarto_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti  + 1




    print("\n\n\n\n ****************               ^ ^ ^                ****************")
    print(        " ****************               | | |                ****************")
    print(        " ****************      eventuali errori sopra        ****************\n")

    print(        " **************** CONTROLLARE LA RIGA DI VALUTAZIONE ****************\n Il numero di esercizi che passano il test di correttezza è ", esercizi_corretti , end=" ")
    print(" quindi NON puoi consegnare" if esercizi_corretti < 2 else ".  Consegna il compito!")
    print(" Riga valutazione: " + nome +":" +cognome+":" + matricola+":" + codice+":" + str(primo_sorpassa_test_di_base)+":" + str(secondo_sorpassa_test_di_base)+":" + str(terzo_sorpassa_test_di_base), ":" + str(quarto_sorpassa_test_di_base), ":",risposta_teorica)


if __name__ == '__main__':
    main()