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
# Cambiare estenzione del file da .py a .doc e caricarlo nell'apposito spazio el modulo
#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCHEMA DI VALUTAZIONE
#  - 2 ESERCIZI FUNZIONANTI DA 16 A 20
#  - 3 ESERCIZI FUNZIONANTI DA 16 A 23
#  - 4 ESERCIZI FUNZIONANTI DA 16 A 26
#  - 5 ESERCIZI FUNZIONANTI DA 16 A 29
#  - DOMANDA TEORICA DA 0 A 3 PUNTI
# LA VALUTAZIONE DIPENDE ANCHE DA COME SONO STATI RISOLTI GLI ESERCIZI

# Riempire le stringhe con il vostro nome, cognome e matricola
nome = ""  # LASCIARE UNA STRINGA
cognome = ""  # LASCIARE UNA STRINGA
matricola = ""  # LASCIARE UNA STRINGA


# ESERCIZIO N. 1
# Siamo nella piena emergenza e ci siamo accorti di aver stampato le
# etichette dei vaccini vanno su delle etichette trasparenti e
# devono essere stampate in maniera speculare.
# Capendo l'importanza di averla al senso giusto, ci hanno chiesto di
# realizzare una funzione
#         primoEsercizio(etichetta_speculare)
# che restituisca l'etichetta stampata specularmente
# - etichetta è una stringa che rappresenta l'etichetta
#
# Esempio (ma è solo un esempio):
#
#  etichetta = "Vaccino: MioVaccino\n
#               Lotto:   12345"
#  output    = "oniccaVoiM :oniccaV\n
#                    54321   :ottoL"
# Si noti che l'etichetta può essere composta di linee di differente lunghezza

def primoEsercizio(etichetta):
    # Abbiamo visto che non è corretto specchiare
    # la stringa contenuta nella variabile etichetta:
    # ne deriverebbe che le righe stesse sarebbero
    # riportate dall'ultima alla prima

    # occorre suddividere l'etichetta nelle righe che la
    # compongono, specchiare queste ultime e poi
    # ricombinarle insieme

    righe_etichetta = etichetta.split("\n")

    # determinare la lunghezza massima delle righe:
    # servirà dopo per aggiungere gli spazi necessari
    # ad allineare a destra le righe specchiate

    lunghezza_massima = 0
    for riga in righe_etichetta:
        if lunghezza_massima < len(riga):
            lunghezza_massima = len(riga)

    etichetta_specchiata = ""

    for riga in righe_etichetta:
        # 3 modi per specchiare una riga

        # modo 1: ciclo for con reversed ed append su stringa

        # riga_specchiata = ""
        # for carattere in reversed(riga):
        #     riga_specchiata += carattere

        # modo 2: ciclo for e prepend su stringa

        # riga_specchiata = ""
        # for carattere in riga:
        #     riga_specchiata = carattere + riga_specchiata

        # modo 3: slicing

        riga_specchiata = riga[::-1]

        # occorre aggiungere un accapo dopo ogni riga meno l'ultima

        # soluzione: aggiungere l'accapo prima di appendere una riga
        # se in etichetta_specchiata è già stato messo del testo,
        # perché sono state già elaborate delle righe
        if etichetta_specchiata != "":
            etichetta_specchiata += "\n"

        etichetta_specchiata += " " * (lunghezza_massima - len(riga)) + riga_specchiata

        # in alternativa, si può aggiungere un accapo dopo ogni riga
        # (avendo eliminato l'if di sopra)...
        #etichetta_specchiata += riga_specchiata + "\n"

    return etichetta_specchiata
    # ... nel caso in cui si sia seguito l'approccio alternativo
    # per gli accapo, occorre eliminare l'accapo inserito dopo
    # l'ultima riga
    # Lo svantaggio di questo approccio è che si aggiunge qualcosa
    # per poi toglierlo, senza che ciò abbia semplificato molto
    # l'algoritmo
    #return etichetta_specchiata.rstrip()

# ESERCIZIO N. 2
# Si è nella fase vaccinale ed occorre monitorare le quantità di vaccino presenti in magazzino
# al fine di organizzare adeguatamente la distribuzione.
# Le varie postazioni vaccinali mandano giornalmente un file contenente righe che indicano
# chi ha ricevuto il vaccino, quale e quale lotto.
# Le righe del file hanno il seguente aspetto:
#   LCCMNP00, AstraM, 4677839
# Si vuole costruire una funzione che faccia il resoconto giornaliero della consumazione
#        secondoEsercizio(NomeFile)
# Il resoconto deve produrre una lista di coppie ordinate lessicograficamente
# dove ogni coppia è:
# (vaccino, dosierogate)


def secondoEsercizio(NomeFile):
    registro_dosi = {}
    # un altro modo per inizializzare un dictionary vuoto
    # registro_dosi = dict()

    with open(NomeFile, "r") as resoconto:
        for riga in resoconto:
            riga = riga.rstrip()  # eliminare il \n (in realtà, qualsiasi spazio) che può trovarsi alla fine della riga
            componenti_riga = riga.split(",")
            vaccino = componenti_riga[1].strip()

            if vaccino in registro_dosi:
                registro_dosi[vaccino] += 1
                #registro_dosi[vaccino] = registro_dosi[vaccino] + 1
            else:
                registro_dosi[vaccino] = 1

    # lista_uscita = []
    # for vaccino in registro_dosi:
    #     coppia = (vaccino, registro_dosi[vaccino])
    #     lista_uscita.append(coppia)
    # lista_uscita.sort()

    lista_uscita = sorted(registro_dosi.items())

    return lista_uscita

# ESERCIZIO N. 3
# Siamo in un laboratorio in cui si sta studiando il DNA del virus,
# ci viene richiesto di produrre una funzione che conti il numero
# di volte in cui sottosequenze di DNA sono presenti nella sequenza
# di base.
#
# La funzione ha il seguente aspetto:
#     terzoEsercizio(DNA_Virus,SottosequenzeDaCercare)
# dove:
#     - DNA_Virus è il DNA del virus
#     - SottosequenzeDaCercare è una lista di sequenze da cercare
# e l'output dovrà essere:
#      - una lista di coppie (sottosequenza,NumeroApparizioni)
#        ordinata come la lista SottosequenzeDaCercare
# Esempio
#   DNA_Virus = "GATTAGA"
#   SottosequenzeDaCercare = ["AGA","GA","TA"]
#   output = [("AGA",1),("GA",2),("TA",1)]
#
#   input = "abcdE"
#   output = (4,1,0)
#
#   input = "ABC dE"
#   output = (1,4,1)
# Chiarimento: Gli spazie sono classificati come caratteri speciali.

def terzoEsercizio(DNA_Virus,SottosequenzeDaCercare):
    #   INSERIRE LA VOSTRA SOLUZIONE
    return []

# ESERCIZIO N. 4
# Si vuole aiutare la ricerca scientifica costruendo una funzione di similitudine
# del patrimonio genetico tra virus.
# Date due sequenze genetiche la similitudine viene calcolata come la lunghezza della
# sottosequenza in comune tra le due sequenze.
# Si costruisca una funzione:
#    quartoEsercizio(s1, s2)
# che restituisca la lunghezza della sottosequenza in comune più lunga.



def quartoEsercizio(s1, s2):
    # SCRIVERE QUI LA VOSTRA SOLUZIONE
    return 0



# ESERCIZIO N. 5
# Nell'ambito del piano vaccinale, si vuole fornire agli operatori sanitari un sistema di controllo
# del contenuto delle fialette.
# Come è noto una fialetta contiene più dosi di vaccino.
# Si vuole dunque fornire la definizione della classe
#      Fialetta(contenutoInMl,doseInMl)
# che abbia i seguenti metodi.

class Fialetta:
    # contenutoInMl è il contenuto della fialetta
    # doseInMl è la misura della dose che deve essere somministrata
    def __init__(self, contenutoInMl,doseInMl):
        self.boh = 0

    # indica il numero di dosi possibili in una filetta
    def numeroDosi(self):
        return self.boh

    # indica se la fialetta ha ancora dosi. Fornisce True se ha dosi e False altrimenti.
    def haDosi(self):
        return False

    # Toglie una dose dalla fialetta.
    def estraiDose(self):
        self.boh = 0

    # ritorna la quantità di vaccino rimasto nella fialetta.
    def rimanenza(self):
        return 0

# Esercizio 6:
#
# Domanda teorica :
#
# Si descriva l'algoritmo di ordinamento di merge sort e se ne calcoli la complessità temporale

# Si inserisca la risposta in questa stringa:

risposta_teorica = "RISPONDERE QUI"


#### ESEMPIO DI VALUTAZIONE ----

def main():
    test_primo_esercizio = [("Vaccino: MioVaccino\nLotto:   12345","oniccaVoiM :oniccaV\n     54321   :ottoL"),
                            ("Vaccino: AlexNet\nData di produzione: 20/10/2020\nLotto: 9882","              teNxelA :oniccaV\n0202/01/02 :enoizudorp id ataD\n                   2889 :ottoL")]

    test_secondo_esercizio = [
        ("PrimoGiorno.txt", [('AstraM', 13), ('KAIS', 4), ('MioK', 9)]),
        ("SecondoGiorno.txt", [('AstraM', 9), ('KAIS', 2), ('MioK', 7)])]

    test_terzo_esercizio = [("GATTAGA", ["GA","TA","ATTA"], [("GA", 2), ("TA", 1), ("ATTA", 1)]),
                            ("GGGATAGGTAAGAAAAGT",["GTA","AA","GT","AAGGAG"],[("GTA", 1), ("AA", 4), ("GT", 2), ("AAGGAG", 0)])]

    test_quarto_esercizio = [("GATTACA","GAATTACG",5),("GGGAGGTAG","TTTAGGAGCATT",4)]
    test_quinto_esercizio = [[1, 3], [1, 2]]

    primo_sorpassa_test_di_base = True
    secondo_sorpassa_test_di_base = True
    terzo_sorpassa_test_di_base = True
    quarto_sorpassa_test_di_base = True
    quinto_sorpassa_test_di_base = True

    esercizi_corretti = 0

    for (input1, expected_output) in test_primo_esercizio:
        output = primoEsercizio(input1)
        if output != expected_output:
            print("PRIMO ESERCIZIO\n------------------------\nERRORE\n" +
                  ">"  + str(output) + "<" +
                  "\nnon è quanto richiesto come output per input \n>" + str(input1) + "<" +
                  "\ndovrebbe invece essere così:\n" + ">"+ str(
                expected_output )+ "<")
            primo_sorpassa_test_di_base = False
    if (primo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input1, expected_output) in test_secondo_esercizio:
        output = secondoEsercizio(input1)
        if output != expected_output:
            print("\n\nSECONDO ESERCIZIO\n------------------------\nERRORE\n" + str(
                output) + "\n non è quanto richiesto come output per input \n" + str(
                input1) + "\ndovrebbe invece essere così:\n" + str(expected_output))
            secondo_sorpassa_test_di_base = False
    if (secondo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input_s1, input_s2, expected_output) in test_terzo_esercizio:
        output = terzoEsercizio(input_s1, input_s2)

        if output != expected_output:
            print("\n\nTERZO ESERCIZIO\n------------------------\nERRORE\n" + str(
                output) + "\nnon sembra essere giusto rispetto all'input\n" + str(
                input_s1) + "\n" +
                  str(input_s2) + "\ndovrebbe invece essere così:\n" + str(expected_output))
            terzo_sorpassa_test_di_base = False
    if (terzo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input_1, input_2, expected_output) in test_quarto_esercizio:
        output = quartoEsercizio(input_1, input_2)
        if output != expected_output:
            print("QUARTO ESERCIZIO\n------------------------\nERRORE\n" + str(
                output) + "\nnon è quanto richiesto per gli input \n" + str(input_1) +"\n"+ str(
                input_2)  + "\ndovrebbe invece essere così:\n" + str(
                expected_output))
            quarto_sorpassa_test_di_base = False
    if (quarto_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    a = Fialetta(9, 2)
    conta_dosi = 0
    while a.haDosi():
        conta_dosi += 1
        a.estraiDose()
    rimanenza = a.rimanenza()

    quinto_sorpassa_test_di_base = (rimanenza == 1 and conta_dosi == 4)

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
