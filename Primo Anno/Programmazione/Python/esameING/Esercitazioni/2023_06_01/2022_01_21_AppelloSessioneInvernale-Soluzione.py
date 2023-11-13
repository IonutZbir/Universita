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
    elif comando == "valuta magazzino":
        output = valuta_magazzino(input)
    elif comando == "valuta soddisfazione":
        output = valuta_soddisfazione(input)
    elif comando == "analizza ordini":
        output = analizza_ordini(input)
    elif comando == "cibo bilanciato":
        output = cibo_bilanciato(input)
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

# Genera l'istogramma dal basso verso l'alto, decrementando la quantità di ciascun cibo
# mano a mano che viene generato l'istogramma

def valuta_magazzino(input):
    quantita_cibo = {}
    totale_cibo = 0
    for cibo in input:
        # se il cibo non è stato visto prima, assegna 0 al relativo contatore
        if cibo not in quantita_cibo:
            quantita_cibo[cibo] = 0
        # in ogni caso, incrementa il contatore
        quantita_cibo[cibo] += 1
        # quantità totale di cibo; equivale alla lunghezza della stringa di input
        totale_cibo += 1

    output = ""

    # L'istogramma viene generato da basso, riga per riga, prependendo ciascuna riga
    # all'output generato in precedenza.
    # Per ciascuna riga, se la quantità di cibo è positiva, inserisce il cibo e decrementa
    # la sua quantità e il totale; altrimenti, inserisce uno spazio.


    # finché c'è cibo da dove inserire nell'istogramma...
    while totale_cibo > 0:  # in alternativa, si può testare che c'è almeno un cibo con quantità positiva
        # ...genera una nuova riga
        riga = ""
        for cibo in sorted(quantita_cibo):
            # se di un cibo ce ne è ancora, inserisce il cibo e decrementa i vari contatori
            if quantita_cibo[cibo] > 0:
                quantita_cibo[cibo] -= 1
                totale_cibo -= 1
                riga += cibo
            else: # altrimenti inserisce uno spazio
                riga += " "
        # prepende la nuova riga all'output (quindi, sopra le righe generate in precedenza),
        # inserendo se necessario un \n
        if output != "":
            output = "\n" + output
        output = riga + output

    return output

# Genera l'istogramma dall'alto al basso, confrontando la quantità di ciascun cibo
# con livelli progressivamente più bassi

# def valuta_magazzino(input):
#     quantita_cibo = {}
#     totale_cibo = 0
#     for cibo in input:
#         # se il cibo non è stato visto prima, assegna 1 al relativo contatore
#         if cibo not in quantita_cibo:
#             quantita_cibo[cibo] = 1
#         else:
#             quantita_cibo[cibo] += 1  # altrimenti, incrementa il contatore
#
#     # calcola l'altezza massima delle colonne
#     altezza_massima = max(quantita_cibo.values())
#
#     # Genera l'istogramma dall'alto verso il basso, considerando livelli via via più bassi
#     # fino a uno. Per un dato livello, se il livello è minore o uguale alla quantità di cibo,
#     # aggiunge il cibo nella riga, altrimenti inserisce uno spazio
#
#     output = ""
#     for livello in range(altezza_massima, 0, -1):
#         for cibo in sorted(quantita_cibo):
#             if livello <= quantita_cibo[cibo]:
#                 output += cibo
#             else:
#                 output += " "
#         # qui, ho deciso d'inserire il \n dopo aver aggiunto una riga
#         # salvo che non sia l'ultima
#         if livello > 1:
#             output += "\n"
#
#     return output

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

def valuta_soddisfazione(input):
    # itera sulle parole alla ricerca di una parola che esprime soddisfazione
    risultato = False
    # si poteva usare un ciclo while per terminare l'iterazione
    # non appena risultato == True
    for parola in input.split():
        if esprime_soddisfazione(parola):
            risultato = True
    return risultato


def esprime_soddisfazione(parola):
    numero_doppie = 0
    i = 0
    while i < len(parola) - 1 and numero_doppie < 2:
        if parola[i] == parola[i + 1]:
            numero_doppie += 1
        i += 1

    # Siccome il ciclo while soprastante viene interrotto appena trova due doppie,
    # questo controllo esprime in realtà "almeno 2". Se dal ciclo while
    # si toglie la seconda condizione (potendolo quindi sostituire con un for),
    # la condizione sottostante esprime "esattamente 2"
    return numero_doppie == 2
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

def analizza_ordini(input):
    prodotti_da_ordinare = set()
    with open(input, "r") as f:
        for riga in f:
            prodotto, quantita_desiderata, quantita_disponibile = riga.rstrip("\n").split(" ")

            if int(quantita_desiderata) > int(quantita_disponibile):
                prodotti_da_ordinare.add(prodotto)

    return prodotti_da_ordinare

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

def cibo_bilanciato(input):
    quantita_proteine = 0
    quantita_zuccheri = 0

    for cibo in input:
        if cibo in "aeiou":
            quantita_proteine += 1
        else:
            quantita_zuccheri += 1

    return quantita_proteine == 2 * quantita_zuccheri

# ESERCIZIO N. 5
# si vuole definire una classe Cibo che
class Cibo:
#  - memorizzi il nome del cibo
#       a = Cibo("hamburger")
    def __init__(self, nome):
        # questa informazione non viene usata nell'implementazione della classe e pertanto non è necessario includerla
        # nello stato come attributo
        # self._nome = nome
        self._ingredienti = set()

# aggiunge un ingrediente
#
#       a.aggiungi("pane")
    def aggiungi(self, ingrediente):
        self._ingredienti.add(ingrediente)

# rimuove un ingrediente se c'è
#
#       a.rimuovi("pane")
    def rimuovi(self, ingrediente):
        self._ingredienti.discard(ingrediente)

# verifichi se c'è un ingrediente
#
#       a.verifica("pane")
    def verifica(self, ingrediente):
        return ingrediente in self._ingredienti


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
