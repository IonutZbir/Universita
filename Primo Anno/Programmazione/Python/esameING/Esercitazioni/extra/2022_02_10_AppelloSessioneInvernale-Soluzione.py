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
## TASSATIVO:  lavorare SEMPRE in QUESTO file
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
# Si vogliono aiutare i professori a svolgere gli esami nella maniera meno pesante,
# pertanto si vogliono fornire delle funzioni che li aiutino nella varie attività
# correlate all'esame.

def compito(comando,input):
    if comando == "prova1":
        output = funzione_di_prova(input)
    elif comando == "prova2":
        output = funzione_di_prova(input)
    elif comando == "ordina studenti":
        output = ordina_studenti(input)
    elif comando == "ordina studenti per voto":
        output = ordina_studenti_per_voto(input)
    elif comando == "correggi compito":
        output = correggi_compito(input)
    elif comando == "trova e-mail":
        output = trova_email(input)
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
#        "ordina studenti"
# si vuole realizzare una funzione che ordini gli studenti per cognome.
# La funzione prende in input una lista di studenti in una stringa
# e restituisce una lista di studenti ordinati per cognome.
# Gli studenti sono indicati con nome e cognome  e sono separati nella lista da ;
#
# esempio di input:
#  "Mario Rossi; Giovanni Bianchi; Elena Marroni; Pina Iavoni"
# deve dare questo output
#  "Giovanni Bianchi; Pina Iavoni; Elena Marroni; Mario Rossi"
#

def ordina_studenti(input):
    lista_studenti = input.split("; ")  # uso "; " come delimitatore per rimuovereanche lo spazio dopo il punto e virgola
    # attenzione: il codice di cui sopra non funzionerebbe se il numero di spazi dopo il punto e virgola fosse variabile

    # Soluzione più corta usando il parametro "key" del metodo "sort" per ordinare rispetto
    # al cognome, che viene estratto con una funzione ausiliare

    # lista_studenti.sort(key=estrai_cognome)
    # return "; ".join(lista_studenti)

    # Soluzione più estesa: converto la lista di studenti in una lista di tuple
    # (cognome, nome completo). Ordinando quest'ultima (lessicograficamente),
    # le tuple sono dapprima ordinate per cognome, come richiesto. Infine,
    # genero nuovamente una lista di nomi completi a partire dalle tuple ordinate

    lista_studenti_temp = []

    for nome_completo in lista_studenti:
        _, cognome = nome_completo.split()
        tupla = (cognome, nome_completo)
        lista_studenti_temp.append(tupla)

    lista_studenti_temp.sort()

    risultato = ""
    for _, nome_completo in lista_studenti_temp:
        if risultato != "":
            risultato += "; "

        risultato += nome_completo

    return risultato


def estrai_cognome(nome_completo):
    _, cognome = nome_completo.split()
    return cognome

# ESERCIZIO N. 2
# per il comando
#        "ordina studenti per voto"
# Lo studente ha 5 esercizi, ciascun esercizio avrà un voto
# e il voto totale è la somma dei voti degli esercizi.
# Si vuole ordinare gli studenti in maniera decrescente rispetto al voto totale.
# L'input è una lista di studenti con i rispettivi voti
# e l'output è la lista degli stessi studenti ordinata in maniera decrescente rispetto al voto finale .
#
# esempio di input:
#  [("mario",1,2,3,4,5),("dario",2,2,3,4,5),("gina",2,2,2,2,2)]
# deve dare questo output
#  [("dario",2,2,3,4,5),("mario",1,2,3,4,5),("gina",2,2,2,2,2)]


def ordina_studenti_per_voto(input):
    # Sto usando la versione abbreviata per ordinare rispetto al voto
    # In alternativa, si sarebbe potuto (come visto nell'esercizio
    # precedente) creare una lista di tuple il cui primo elemento è
    # il voto totale e il secondo elemento è il record

    # Inoltre, uso il parametro "reverse" per ordinare in senso
    # decrescente (True)
    return sorted(input, key=calcola_voto, reverse=True)


def calcola_voto(record_studente):
    voti = record_studente[1:]  # escludo l'elemento d'indice zero che è il nome
    return sum(voti)

#
# ESERCIZIO N. 3
# per il comando:
#      "correggi compito"
# Si presume che un compito corretto chiuda ed apra le parentesi in modo corretto.
# Quindi deve dire se le parentesi sono bilanciate in una stringa di parentesi.
# Se sono bilanciate, dirà True altrimenti dirà False
#
# Esempio:
# input:
# (())()()
# output: True
#
# input:
# (())())
# output: False


def correggi_compito(input):
    # itero sulla stringa aprendo e chiudendo le parentesi tonde:
    # mi fermo appena trovo una parentesi chiusa non bilanciata
    # e alla fine controllo che tutte le parentesi siano state chiuse
    # Nota: sto assumendo che non ci siano caratteri diversi da ( e )
    indice = 0
    numero_parentesi_aperte = 0
    while numero_parentesi_aperte >= 0 and indice < len(input):
        carattere = input[indice]

        if carattere == "(":
            numero_parentesi_aperte += 1
        else:  # carattere == ")"
            numero_parentesi_aperte -= 1

        indice += 1

    # Si noti che il ciclo termina appena numero_parentesi_aperte < 0, cioè appena si è trovata
    # una parentesi (chiusa) non bilanciata. Altrimenti, una successiva parentesi aperta avrebbe
    # riportato il contatore a zero nascondendo l'errore.

    return numero_parentesi_aperte == 0

# ESERCIZIO N. 4
# per il comando:
#      "trova e-mail"
# Si ha a disposizione una stringa in cui ogni riga contiene un potenziale indirizzo e-mail.
# Bisogna contare il numero di indirizzi e-mail ben formati.
#
# Input:
# "a@u.it
#  b@@@l
#  a@
#  j.l@u.lo"
# Output:
# 2

def trova_email(input):
    # suddivido la stringa in una lista di potenziali indirizzi email
    lista_email = input.split("\n")

    # Nota: non devo rimuovere l'ultimo elemento della lista, perché la stringa
    # di input non termina con \n

    # itero sulla lista incrementando un contatore ogni volta che
    # incontro un indirizzo e-mail valido
    contatore = 0
    for indirizzo_email in lista_email:
        if valida_email(indirizzo_email):
            contatore += 1

    return contatore


def valida_email(indirizzo_email):
    # per validare un'email

    # 1. suddivido intorno al @
    #    e verifico che ci siano esattamente due parti intorno
    componenti_email = indirizzo_email.split("@")

    if len(componenti_email) != 2:
        return False

    # 2. considero le due parti: username e dominio
    username = componenti_email[0]
    dominio = componenti_email[1]

    # 3. suddivido entrambi rispetto ai punti
    componenti_username = username.split(".")
    componenti_dominio = dominio.split(".")

    valido = True

    # 4. verifico che il dominio abbia almeno 2 parti (es. gmail.com)
    if len(componenti_dominio) < 2:
        valido = False

    # 5. verifico che la username sia formata da sole lettere alternate a punti
    if not componenti_solo_lettere_e_punti(componenti_username):
        valido = False

    # 6. verifico che il dominio sia formata da sole lettere alternate a punti

    if not componenti_solo_lettere_e_punti(componenti_dominio):
        valido = False

    return valido


# ESERCIZIO N. 5


def componenti_solo_lettere_e_punti(lista):
    # itero sugli elementi della lista alla ricerca di una componente
    # che non sia una stringa (non vuota) di sole lettere ASCII, cioè
    # a..z e A..Z
    valido = True
    i = 0
    while valido and i < len(lista):
        comp = lista[i]
        if not comp.isalpha() or not comp.isascii():  # isalpha() implica almeno un carattere
            valido = False
        i += 1
    return valido

# si vogliono realizzare due classi: Registro e Studente
# Registro conterrà Studenti.

class Studente:
    def __init__(self, nome, cognome):
        # Lascio gli attributi "pubblici" perché dovranno essere
        # acceduti dalla classe Registro.
        # In realtà, avrei potuti comunque rendere privati, visto
        # Python non impone realmente nessun vincolo di accesso.
        self.nome = nome
        self.cognome = cognome

# dove s è uno studente
    def stampa(self):
        return self.nome + " " + self.cognome

class Registro:
#  - il registro sia associato ad una classe
#       a = Registro("I C")
    def __init__(self, classe):
        self._classe = classe
        self._studenti = []

# aggiunge uno studente
#
#       a.aggiungi(s)
# dove s è uno studente
    def aggiungi(self, s):
        self._studenti.append(s)

# produce una stringa che è la stampa il registro,
# ovvero il nome della classe sulla prima riga e uno studente per riga
# ordinati per cognome ma stampati nome cognome
#
#       a.rimuovi("pane")
    def produciStringa(self):
        risultato = ""
        risultato += self._classe

        lista_temp = []

        for studente in self._studenti:
            lista_temp.append((studente.cognome, studente))

        lista_temp.sort()

        for _, studente in lista_temp:
            risultato += "\n" + studente.stampa()

        return risultato

# Esercizio 6:
#
# Domanda teorica :
#
# Si commenti la frase "la complessità temporale descrive la lunghezza dell'algoritmo"
#
# Si inserisca la risposta in questa stringa:

risposta_teorica = "RISPONDERE QUI"


#### ESEMPIO DI VALUTAZIONE ----

def main():

    comando1 = "ordina studenti"
    test_primo_esercizio = [("Mario Rossi; Giovanni Bianchi; Elena Marroni; Pina Iavoni", "Giovanni Bianchi; Pina Iavoni; Elena Marroni; Mario Rossi")]

    comando2 = "ordina studenti per voto"
    test_secondo_esercizio = [([("mario",1,2,3,4,5),("dario",2,2,3,4,5),("gina",2,2,2,2,2)], [("dario",2,2,3,4,5),("mario",1,2,3,4,5),("gina",2,2,2,2,2)])]

    comando3 = "correggi compito"
    test_terzo_esercizio = [("(())()()", True),(")(())()()(", False)]

    comando4 = "trova e-mail"
    test_quarto_esercizio =  [("a@u.it\nb@@@l\na@\nj.l@u.lo", 2)]


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

    r = Registro("V C")
    r.aggiungi(Studente("Mario","Rossi"))
    r.aggiungi(Studente("Giovanni","Bianchi"))
    r.aggiungi(Studente("Elena","Marroni"))
    r.aggiungi(Studente("Pina","Iavoni"))

    stringa_prodotta = r.produciStringa()
    stringa_attesa = "V C\nGiovanni Bianchi\nPina Iavoni\nElena Marroni\nMario Rossi"
    quinto_sorpassa_test_di_base = (stringa_prodotta == stringa_attesa)
    if not quinto_sorpassa_test_di_base:
        print("\n\n\nESERCIZIO CLASSI\n\n\nPer esercizio delle classi, mi attendo questo:\n"+stringa_attesa)


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
