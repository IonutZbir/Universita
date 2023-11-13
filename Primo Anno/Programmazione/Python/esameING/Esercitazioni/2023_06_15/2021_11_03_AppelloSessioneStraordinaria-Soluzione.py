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
# Cambiare estenzione del file da .py a .doc e caricarlo nell'apposito spazio del modulo
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
# - un esercizio globale che comprente esercizi da 1 a 4
# - un esercizio sulle classi (esercizio 5)
# - un esercizio teorico (esercizio 6)


#     Esercizio globale
#
# Siamo nelle stanze dei servizi segreti e dobbiamo aiutare lo stato a
# badare alla sicurezza nazionale. I servizi ci daranno alcuni comandi
# e alcuni input che noi dovremo trattare attraverso la funzione compito.

def compito(comando,input):
    if comando == "prova1":
        output = funzione_di_prova(input)
    elif comando == "prova2":
        output = funzione_di_prova(input)
    elif comando == "trova bersaglio":
        output = trova_bersaglio(input)
    elif comando == "codifica messaggio":
        output = codifica_messaggio(input)
    elif comando == "analizza accessi telefonici":
        output = analizza_accessi_telefonici(input)
    elif comando == "determina se non dice la verità":
        output = non_dice_verita(input)
    else:
        output = None
    return output

def funzione_di_prova(input):
    return None

# Naturalmente dovrete liberamente definire una funzione per ogni comando.
# Tale funzione dovrà essere richiamata dalla funzione compito(comando,output)
# quando riceve la stringa del comando


# ESERCIZIO N. 1
# per il comando
#        "trova bersaglio"
# si vuole generare una funzione
# che prende una mappa rettangolare definita con dei caratteri e
# e restituisce la posizione del bersaglio indicato con *
# nella mappa in termini di riga e colonna. La numerazione inizia da 1
#
# esempio di input:
#  "BAC
#   BAC
#   B*C
#   BAC"
# deve dare questo output
# (3,2)

def trova_bersaglio(input):
    righe = input.split("\n")
    # non devo eliminare l'ultima riga,
    # perché in questo caso l'immagine
    # non termina con un \n

    for i in range(len(righe)):  # itero sulle righe
        for j in range(len(righe[i])):  # per ciascuna, riga itero sui caratteri della stessa
            # se il carattere è "*", allora restituisco una tupla contenente le coordinate
            if righe[i][j] == "*":
                return i + 1, j + 1

    return None

    # in alternativa
    # x = 0
    # y = 0
    # for i in range(len(righe)):  # itero sulle righe
    #     for j in range(len(righe[i])):  # per ciascuna, riga itero sui caratteri della stessa
    #         # se il carattere è "*", allora restituisco una tupla contenente le coordinate
    #         if righe[i][j] == "*":
    #             x = i + 1
    #             y = j + 1
    #
    # return x, y

#
#
# ESERCIZIO N. 2
# per il comando
#        "codifica messaggio"
# si vuole generare una funzione che prenda in input un messaggio e restituisca in output il messaggio codificato
# dove la codifica prevede che ogni lettera sia sostituita con la successiva nell'alfabeto tranne la z
# che deve essere sostituita con la a
# esempio di input:
#  "zanzotto"
# deve dare questo output
#  "aboapuup"

def codifica_messaggio(input):
    output = ""
    for carattere in input:
        output += codifica_carattere(carattere)

    return output


import string

def codifica_carattere(carattere):
    # determino se si tratta di una lettera minuscola oppure di una
    # maiuscola. Altrimenti, restituisco il carattere non codificato
    # necessario per essere riusata dell'esercizio sulle classi
    if carattere in string.ascii_lowercase:
        alfabeto = string.ascii_lowercase
    elif carattere in string.ascii_uppercase:
        alfabeto = string.ascii_uppercase
    else:
        return carattere

    # trovo la posizione nell'alfabeto
    indice_carattere = alfabeto.index(carattere)
    # determino il carattere cifrato scorrendo di uno l'indice
    # e usando l'operatore di resto per tornare a zero
    # quando raggiungo la fine
    indice_carattere_codificato = (indice_carattere + 1) % len(alfabeto)

    return alfabeto[indice_carattere_codificato]

    # si poteva risolvere alternativamente usando le funzioni ord() e chr()
    # sfruttando un'espressione tipo quella che segue:

    # chr(((ord(x) - ord("a")) + 1) % (ord("z") - ord("a") + 1) + ord("a"))

    # dove x è una variabile che contiene la lettera (minuscola) da
    # convertire.
    # Si può usare "a" <= x <= "z" per vedere se x è una lettera
    # minuscola.

#
# ESERCIZIO N. 3
# per il comando:
#      "analizza accessi telefonici"
# si ha a disposizione un file di testo dove ogni riga rappresenta il numero chiamato, il numero chiamante e l'orario.
# Si vuole sapere quale numero è stato chiamato da più numeri diversi.
# L'input è il file e l'output il numero chiamato di più. A parità di numero di chiamate, viene restituito il numero più basso.
#
# Dato il file la tripla:
# "2021_11_04_prova.txt"
# e dato il contenuto del file:
# 33421102020 33421202020 15:00
# 33421102020 33431202020 15:03
# 33421102020 33431202020 15:34
# 33421102021 33431202020 15:04
# 33421102021 33431202020 15:08
# l'output è:
# "33421102020"

def analizza_accessi_telefonici(input):
    # costruisco una mappa che associa a ogni
    # numero di telefono i numeri che lo hanno
    # chiamato
    registro_chiamate = {}
    with open(input, "r") as f:
        for linea in f:
            numero_chiamato, numero_chiamante, _ = linea.rstrip().split(" ")
            if numero_chiamato not in registro_chiamate:
                registro_chiamate[numero_chiamato] = set()
            registro_chiamate[numero_chiamato].add(numero_chiamante)

    risultato = ""
    chiamate = 0

    # itero sulle coppie chiave/valore nella mappa
    # e determino il numero che è stato chiamato
    # dal maggior numero di numeri e in caso di
    # parità, aggiorno solo se il nuovo massimo
    # candidato è lessicograficamente minore
    for numero_chiamato, numeri_chiamanti in registro_chiamate.items():
        if len(numeri_chiamanti) > chiamate or \
                (len(numeri_chiamanti) == chiamate and numero_chiamato < risultato):
            risultato = numero_chiamato
            chiamate = len(numeri_chiamanti)

    return risultato

#
#
# ESERCIZIO N. 4
# per il comando:
#      "determina se non dice la verità"
# Si è studiato un metodo infallibile per determinare se qualcuno non dice la verità.
# Si è osservato che chi non dice la verità usa nei suoi messaggi due vocali lo stesso numero di volte.
# Si costruica una funzione che prenda in input un messaggio e se la persona non sta dicendo la verità (True)
# o sta dicendo la verità (False)
#
# Input:
# "abate"
# Output:
# False
# Input:
# "abruzzo un caso"
# Output:
# True

def non_dice_verita(input):
    # costruisco una mappa che associa alle vocali
    # la loro frequenza (solo se maggiore di 0)
    frequenze = {}
    for carattere in input:
        if carattere in "aeiou":
            if carattere in frequenze:
                frequenze[carattere] += 1
            else:
                frequenze[carattere] = 1

    # costruisco una mappa "inversa" che associa
    # a ogni livello di frequenza l'insieme dei
    # numeri (potenzialmente più di uno) che hanno
    # quella frequenza
    caratteri_co_frequenti = dict()
    for carattere, frequenza in frequenze.items():
        if frequenza in caratteri_co_frequenti:
            caratteri_co_frequenti[frequenza].add(carattere)
        else:
            caratteri_co_frequenti[frequenza] = set([carattere])  # oppure { carattere }

    # vedo se c'è almeno un livello di frequenza con 2 o più
    # caratteri associati
    risultato = False
    for cofrequenti in caratteri_co_frequenti.values():
        if len(cofrequenti) >= 2:
            risultato = True

    # Si poteva ottimizzare nel caso migliore, osservando che non serve
    # davvero determinare tutti i caratteri con la stessa frequenza,
    # potendosi invece limitare a verificare che ce ne sia almeno una coppia

    return risultato

# ESERCIZIO N. 5
# si vuole definire una classe Messaggio che
class Messaggio:
#  - memorizzi il messaggop
#       a = Messaggio("il cane corre")
    def __init__(self, nome):
        self._messaggio = nome

#  modifichi il messaggio rimuovendo la prima occorrenza della parola sul testo
#       a.rimuovi("cane")
    def rimuovi(self, parola):
        tokens = self._messaggio.split()
        if parola in tokens:
            tokens.remove(parola)
        self._messaggio = " ".join(tokens)

#  - codifichi il messaggio memorizzato
# dove la codifica prevede che ogni lettera sia sostituita con la successiva nell'alfabeto tranne la z.
# Tutti i caratteri non alfabetici devono rimanere tali e quali.
# che deve essere sostituita con la a
    def codifica(self):
        output = ""
        for carattere in self._messaggio:
            output += codifica_carattere(carattere)

        return output

# Esercizio 6:
#
# Domanda teorica :
#
# Si descriva la complessità temporale e spaziale degli algoritmi

# Si inserisca la risposta in questa stringa:

risposta_teorica = "RISPONDERE QUI"


#### ESEMPIO DI VALUTAZIONE ----

def main():
    comando1 = "trova bersaglio"
    test_primo_esercizio = [("BAC\nBAC\nB*C\nBAC", (3, 2)),("BAC\nBAC\nBAC\nBA*", (4, 3))]
    comando2 = "codifica messaggio"
    test_secondo_esercizio = [("zanzotto", "aboapuup")]

    comando3 = "analizza accessi telefonici"
    test_terzo_esercizio = [("2021_11_04_prova.txt", "33421102020")]

    comando4 = "determina se non dice la verità"
    test_quarto_esercizio =  [("abate", False), ("abruzzo un caso",True)]


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

    a = Messaggio("il cane corre via")
    a.rimuovi("cane")
    m = a.codifica()
    #

    quinto_sorpassa_test_di_base = (m == "jm dpssf wjb")


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
