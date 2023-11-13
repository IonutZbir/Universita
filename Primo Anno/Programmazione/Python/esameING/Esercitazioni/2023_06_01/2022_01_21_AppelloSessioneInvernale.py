#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE



# Riempire le stringhe con il vostro nome, cognome e matricola
nome = ""  # LASCIARE UNA STRINGA
cognome = ""  # LASCIARE UNA STRINGA
matricola = ""  # LASCIARE UNA STRINGA




# =================================================================================================
#    IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE
#    IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE
#    IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE
#
#    Durante il compito, potete usare tutto ciò che avete sul vostro PC
#                        e tutto ciò che trovate in internet.
#    Se li usate, dovete INDICARE LA FONTE con le seguenti alternative:
#                 - indirizzo web (verrà controllata l'esistenza della pagina
#                   sull'archivio di internet)
#                 - nome del file sul vostro pc (che deve avere data di
#                   ultima modifica antecedente all'orario di inizio della
#                   prova d'esame)
#
#   NON SI PUO' USARE:
#         - conoscenza proveniente da persone che stanno facendo l'appello con voi
#         - aiuti esterni di qualsiasi genere forniti da persone a vario titolo
#
#
#    Se, a nostro insindacabile giudizio, due compiti sono troppo simili e
#    non hanno la FONTE indicata e provabile, saranno annullati
#
#
# =================================================================================================



#            PRIMA DI COMINCIARE
#    SCARICARE QUESTO FILE SUL DESKTOP E CAMBIARGLI IL NOME
#
#           [NUMERO_MATRICOLA].py
#
# dove [NUMERO_MATRICOLA] è il vostro numero di matricola
#
# ESEMPIO : 00713042.py
#
## LAVORARE SEMPRE IN QUESTO FILE
#
#
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
# Cambiare estensione del file da .py a .doc e caricarlo nell'apposito spazio del modulo
#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCHEMA DI VALUTAZIONE
#  - 2 ESERCIZI FUNZIONANTI DA 16 A 20
#  - 3 ESERCIZI FUNZIONANTI DA 16 A 23
#  - 4 ESERCIZI FUNZIONANTI DA 16 A 26
#  - 5 ESERCIZI FUNZIONANTI DA 16 A 29
#  - DOMANDA TEORICA DA 0 A 3 PUNTI
# LA VALUTAZIONE DIPENDE ANCHE DA COME SONO STATI RISOLTI GLI ESERCIZI



# Il compito è composto da:
# - un esercizio globale che comprende esercizi da 1 a 4
# - un esercizio sulle classi (esercizio 5)
# - un esercizio teorico (esercizio 6)


#     Esercizio globale
#
# Possediamo una catena di fast-food e dobbiamo ottimizzare il processo di servizio.
# Dunque, ci prefiggiamo di definire alcune funzionalità che dovranno essere richiamate
# dalla funzione compito attraverso dei comandi

def compito(comando,input):
    if comando == "prova1":
        output = funzione_di_prova(input)
    elif comando == "prova2":
        output = funzione_di_prova(input)
    else:
        output = False
    return output

def funzione_di_prova(input):
    return None

# Naturalmente dovrete liberamente definire una funzione per ogni comando.
# Tale funzione dovrà essere richiamata dalla funzione compito(comando,output)
# quando riceve la stringa del comando


# ESERCIZIO N. 1
# per il comando
#        "valuta magazzino"
# si vuole generare una sorta di istogramma per valutare la presenza dei cibi nel magazzino.
# Il magazzino è rappresentato da una stringa di lettere e ogni lettera è un cibo.
# L'istogramma di output è una stringa in cui le barre sono lunghe esattamente quante volte
# appare il cibo nel magazzino. I cibi sono ordinati lessicograficamente.
#
# esempio di input:
#  "BACACDCBAC"
# deve dare questo output
# "  C
#  A C
#  ABC
#  ABCD"
#
# ESERCIZIO N. 2
# per il comando
#        "valuta soddisfazione"
# si vuole generare una funzione che prenda in input un messaggio e restituisca in un booleano
# se la persona è soddisfatta del pranzo appena mangiato.
# Si ritiene che una persona sia soddisfatta se usa una parola con due doppie nella frase.
#
# esempio di input:
#  "ho mangiato un cibo fatto con tanto affetto"
# deve dare questo output
#  True
#
# esempio di input:
#  "ho mangiato un cibo fatto bene"
# deve dare questo output
#  False

#
# ESERCIZIO N. 3
# per il comando:
#      "analizza ordini"
# si ha a disposizione un file di testo dove ogni riga rappresenta il prodotto, la quantità desiderata e la quantità
# presente in magazzino.
# Si vuole sapere quali prodotti sono da ordinare poiché mancanti.
#
# Dato il file la tripla:
# "2022_01_21_prova.txt"
# e dato il contenuto del file:
# mele 9 10
# pere 9 8
# arance 10 1
# albicocche 8 10
# l'output è:
# {"pere","arance"}
#
#
#
# ESERCIZIO N. 4
# per il comando:
#      "cibo bilanciato"
# gli ingredienti dei cibi sono rappresentati in una stringa
# come consonanti se sono zuccheri e vocali se sono proteine.
# Il cibo è bilanciato (True) se si hanno le proteine sono il doppio
# degli zuccheri altrimenti non è bilanciato (False)
#
# Input:
# "abatee"
# Output:
# True
# Input:
# "abate"
# Output:
# False

# ESERCIZIO N. 5
# si vuole definire una classe Cibo che
class Cibo:
#  - memorizzi il nome del cibo
#       a = Cibo("hamburger")
    def __init__(self, nome):
        self.boh = 0

# aggiunge un ingrediente
#
#       a.aggiungi("pane")
    def aggiungi(self, ingrediente):
        self.boh = 0

# rimuove un ingrediente se c'è
#
#       a.rimuovi("pane")
    def rimuovi(self, ingrediente):
        self.boh = 0

# verifichi se c'è un ingrediente
#
#       a.verifica("pane")
    def verifica(self, ingrediente):
        return False


# Esercizio 6:
#
# Domanda teorica :
#
# Si commenti la frase "la complessità temporale e spaziale degli algoritmi sono inversamente correlate tra loro"
#
# Si inserisca la risposta in questa stringa:

risposta_teorica = "RISPONDERE QUI"


#### ESEMPIO DI VALUTAZIONE ----

def main():

    comando1 = "valuta magazzino"
    test_primo_esercizio = [("BACACDCBAC", "  C \nA C \nABC \nABCD"),("BACBACDCBAC", "  C \nABC \nABC \nABCD")]

    comando2 = "valuta soddisfazione"
    test_secondo_esercizio = [("ho mangiato un cibo fatto con tanto affetto", True),("ho mangiato un cibo fatto con tanto afetto", False)]

    comando3 = "analizza ordini"
    test_terzo_esercizio = [("2022_01_21_prova.txt", {"pere","arance"})]

    comando4 = "cibo bilanciato"
    test_quarto_esercizio =  [("abate", False), ("abatee",True)]


    primo_sorpassa_test_di_base = True
    secondo_sorpassa_test_di_base = True
    terzo_sorpassa_test_di_base = True
    quarto_sorpassa_test_di_base = True
    quinto_sorpassa_test_di_base = True

    esercizi_corretti = 0


    for (input1, expected_output) in test_primo_esercizio:
        comando = comando1
        output = compito(comando,input1)
        if output != expected_output:
            print("PRIMO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" +
                  ">"  + str(output) + "<" +
                  "\nnon è quanto richiesto come output per input \n>" + str(input1) + "<" +
                  "\ndovrebbe invece essere così:\n" + ">"+ str(
                expected_output )+ "<")
            primo_sorpassa_test_di_base = False
    if (primo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input1, expected_output) in test_secondo_esercizio:
        comando = comando2
        output = compito(comando,input1)
        if output != expected_output:
            print("SECODNO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" +
                  str(output) + "\n non è quanto richiesto come output per input \n" +
                  str(input1) + "\ndovrebbe invece essere così:\n" + str(expected_output))
            secondo_sorpassa_test_di_base = False
    if (secondo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input1, expected_output) in test_terzo_esercizio:
        comando = comando3
        output = compito(comando,input1)

        if output != expected_output:
            print("\n\nTERZO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" + str(
                output) + "\nnon sembra essere giusto rispetto all'input\n" + str(
                input1) + "\ndovrebbe invece essere così:\n" + str(expected_output))
            terzo_sorpassa_test_di_base = False
    if (terzo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input1, expected_output) in test_quarto_esercizio:
        comando = comando4
        output = compito(comando,input1)
        if output != expected_output:
            print("QUARTO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" + str(
                output) + "\nnon è quanto richiesto per gli input \n" + str(input1) +
                  "\ndovrebbe invece essere così:\n" + str(expected_output))
            quarto_sorpassa_test_di_base = False
    if (quarto_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    a = Cibo("il cane corre via")
    a.aggiungi("pane")
    a.aggiungi("salame")
    a.rimuovi("pane")
    m = a.verifica("pane")
    m1 = a.verifica("salame")
    #

    quinto_sorpassa_test_di_base = (not m and m1)


    if (quinto_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1


    print("\n\n\n\n ****************               ^ ^ ^                ****************")
    print(" ****************               | | |                ****************")
    print(" ****************      eventuali errori sopra        ****************\n")

    print(
        " **************** CONTROLLARE LA RIGA DI VALUTAZIONE ****************\n Il numero di esercizi che passano il test di correttezza è ",
        esercizi_corretti, end=" ")
    print(" quindi NON puoi consegnare" if esercizi_corretti < 2 else ".  Consegna il compito!")
    print(" Riga valutazione: " + nome + ":" + cognome + ":" + matricola + ":" + str(
        primo_sorpassa_test_di_base) + ":" + str(secondo_sorpassa_test_di_base) + ":" + str(
        terzo_sorpassa_test_di_base), ":" + str(quarto_sorpassa_test_di_base), ":" + str(quinto_sorpassa_test_di_base),
          ":", risposta_teorica)


if __name__ == '__main__':
    main()
