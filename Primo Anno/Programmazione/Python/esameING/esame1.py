#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE
#                 ATTENZIONE --- LEGGERE PRIMA DI COMINCIARE


# Riempire le stringhe con il vostro nome, cognome e matricola
nome = "Ionut"  # LASCIARE UNA STRINGA
cognome = "Zbirciog"  # LASCIARE UNA STRINGA
matricola = "0308984"  # LASCIARE UNA STRINGA


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
#
#   NON SI PUO' USARE:
#         - conoscenza proveniente da persone che stanno facendo l'appello con voi
#         - aiuti esterni di qualsiasi genere forniti da persone a vario titolo
#         - ChatGPT o altro sistema d'intelligenza artificiale in grado di svolgere
#           gli esercizi al posto vostro o aiutarvi sostanzialmente a farlo
#
#
#    Se, a nostro insindacabile giudizio, due compiti sono troppo simili e
#    non hanno la FONTE indicata e provabile, saranno annullati
#
#
# =================================================================================================


# PRIMA DI COMINCIARE
#    SCARICARE QUESTO FILE SUL DESKTOP E CAMBIARGLI IL NOME
#
#           [NUMERO_MATRICOLA].py
#
# dove [NUMERO_MATRICOLA] è il vostro numero di matricola
#
# ESEMPIO : 00713042.py
#
# TASSATIVO:
#
#             lavorare SEMPRE in QUESTO file
#
# TASSATIVO:
# Prima di cominciare, eseguire il codice a vuoto e osservare la riga di valutazione finale
# e le stampe che vengono fornite
#
# ogni tanto eseguire il codice per vedere se porta alla valutazione automatica
##
#
#
#                              *TASSATIVO*
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
#  Si vuole scrivere un sistema a supporto di coloro che si cimentano dietro ai fornelli

def compito(comando, input):
    if comando == 'cucchiai':
        output = cucchiai(input)
    elif comando == 'rispetta tempi di cottura':
        output = rispetta_tempi_di_cottura(input)
    elif comando == 'valuta dieta':
        output = valuta_dieta(input)
    elif comando == 'conta calorie':
        output = conta_calorie(input)
    else:
        output = False
    return output


def cucchiai(input):
    quantita, unita = input.split()
    quantita = int(quantita)

    if unita == "g":
        quantita_grammi = quantita
    elif unita == "kg":
        quantita_grammi = quantita * 1000
    elif unita == "hg":
        quantita_grammi = quantita * 100

    massimo_cucchiai = (quantita_grammi // 100) * 5
    return massimo_cucchiai


def rispetta_tempi_di_cottura(input):
    ingredienti = input.split(',')
    ingredienti_tempi = []

    # Analisi dell'input per ottenere una lista di ingredienti con i relativi tempi di cottura
    for ingrediente in ingredienti:
        nome, tempo = ingrediente.split(':')
        ingredienti_tempi.append((nome, int(tempo)))

    # Ordinamento degli ingredienti in base al tempo di cottura
    ingredienti_tempi = sorted(ingredienti_tempi, key=lambda x: x[1])

    # Generazione della sequenza di istruzioni
    sequenza = ""
    lun = len(ingredienti_tempi)
    for i in range(lun):
        ingrediente = ingredienti_tempi[lun-1-i][0]
        tempo_cottura = ingredienti_tempi[lun-1-i][1]

        if i > 0:
            tempo = abs(tempo_cottura - ingredienti_tempi[lun-i][1])
            if tempo > 1:
                end = "i"
            else:
                end = "o"
            sequenza += "dopo " + str(tempo) + " minut" + end + ", "

        sequenza += "inserire " + str(ingrediente) + "\n"
    sequenza = sequenza[:-1]
    return sequenza

def valuta_dieta(file):
    File = open(file, 'r')
    dict_comuni = {}
    output = set()
    for row in File:
        piatti = row.split(',')[1:]
        for piatto in piatti:
            if piatto.endswith('\n'):
                piatto = piatto.split('\n')[0]
            if piatto not in dict_comuni:
                dict_comuni[piatto] = 1
            else:
                dict_comuni[piatto] += 1
    File.close()
    maxP = max(dict_comuni.values())
    
    for key in dict_comuni:
        if dict_comuni[key] == maxP:
            output.add(key)
    return output


def conta_calorie(s):
    # Data una stringa composta dai simboli C, P e G a indicare rispettivamente le unità di carboidrati, proteine e grassi
    # di cui si compone un pasto.
    # Sapendo che un'unità di grassi apporta 10 calorie, il doppio dell'apporto di proteine o zuccheri, si vuole determinare
    # l'apporto calorico complessivo, sapendo però che se un'unità di zuccheri è adiacente a un'unità di proteine,
    # nel metabolizzarle l'organismo produce il 20% in più di energia. Si noti che ogni unità di nutrienti può essere considerata
    # adiacente soltanto a un'altra unità (si veda secondo esempio).
    # test_quarto_esercizio = [("CCGP", 25), ("CPCG", 27), ("CGPC", 27)]
    calorie = 0
    len_str = len(s)
    for x in range(len_str):
        if s[x] == 'C':
            calorie += 5
            if x > 0 and x<len_str and (s[x - 1] == "P" or s[x + 1] == "P") :
                calorie += 2
        elif s[x] == 'P':
            calorie += 5
        elif s[x] == 'G':
            calorie += 10
    return calorie

# Naturalmente dovrete liberamente definire una funzione per ogni comando.
# Tale funzione dovrà essere richiamata dalla funzione compito(comando,input)
# quando riceve la stringa del comando


# ESERCIZIO N. 1
# per il comando
#        "cucchiai"
#
# Sappiamo che 5 cucchiai da cucina equivalgono a un etto di farina.
# Determinare il massimo numero di cucchiai che non eccede un dato quantitativo
# di farina espresso in grammi, chili o etti.
#
# Dato in input:
# "110 g"
# si deve rispondere:
# 5
#
# Dato in input:
# "2 hg"
# si deve rispondere:
# 10
#
# Dato in input:
# "1 kg"
# si deve rispondere:
# 50

# ESERCIZIO N. 2
# per il comando
#        "rispetta tempi di cottura"
# Dati gli ingredienti di una ricetta con il relativo tempo di cottura in minuti,
# produrre una sequenza d'istruzioni per inserirli in cottura in modo che
# tutti gli ingredienti siano cotti al punto giusto.
# Per semplicità, si assuma che non ci siano due ingredienti con lo stesso tempo di cottura.
#
# Esempio di input:
# "riso:15,patate:10,fagioli:20,carote:5,orzo:14"
# Output:
# "inserire fagioli\n
#  dopo 5 minuti, inserire riso\n
#  dopo 1 minuto, inserire orzo\n
#  dopo 4 minuti, inserire patate\n
#  dopo 5 minuti, inserire carote"
#
# Nota: prestare attenzione al fatto che il tempo di cottura è dato come una stringa
# invece che come un intero


#
# ESERCIZIO N. 3
# per il comando
#        "valuta dieta"
#
# Dato in input il nome di un file le cui righe descrivono i piatti serviti in giorni diversi,
# si vuole determinare i piatti più comuni.
#
# Esempio di input:
# 'pasti1.txt'
# Output:
# {"pasta"}
#
# Esempio di input:
# 'pasti2.txt'
# Output:
# {"fagioli", "insalata"}


# ESERCIZIO N. 4
# per il comando:
#      "conta calorie"
#
# Data una stringa composta dai simboli C, P e G a indicare rispettivamente le unità di carboidrati, proteine e grassi
# di cui si compone un pasto.
# Sapendo che un'unità di grassi apporta 10 calorie, il doppio dell'apporto di proteine o zuccheri, si vuole determinare
# l'apporto calorico complessivo, sapendo però che se un'unità di zuccheri è adiacente a un'unità di proteine,
# nel metabolizzarle l'organismo produce il 20% in più di energia. Si noti che ogni unità di nutrienti può essere considerata
# adiacente soltanto a un'altra unità (si veda secondo esempio).
#
# Esempio:
#
# "CCGP" -> 25
# "CPCG" -> 27


# ESERCIZIO 5
# Si vuole creare una classe che gestisca un menu.
class Menu:

    # Costruisce un menu avente un certo nome
    def __init__(self, nome_menu):
        self.name = nome_menu
        self.menu = []

    # Aggiunge un piatto al menu
    def aggiungi_piatto(self, piatto):
        self.menu.append(piatto)

    # Restituisce una stringa che rappresenta il menu costituita dalle seguenti righe:
    # * la prima riga contiene il nome del menu (e.s. pranzo del lunedì) e, nel caso, tra parentesi tonde
    #   l'indicazione del fatto che il menu è "vegano" oppure "vegetariano"
    # * i piatti su righe separate nell'ordine in cui sono stati inseriti
    #
    # Per esempio:
    # "menu della domenica (vegano)\n
    #  pasta al sugo vegetale\n
    #  uovo fritto"
    def stampa_menu(self):
        isVegan = True
        isVeget = True
        piatti = ""
        for piatto in self.menu:
            isVegan = isVegan and piatto.adatto_vegani()
            isVeget = isVeget and piatto.adatto_vegetariani()
            piatti += piatto.name + "\n"
                
        output = ""
        if isVegan:
            output += self.name + " (vegano)\n"
        elif isVeget:
            output += self.name + " (vegetariano)\n"
        else: 
            output += self.name + "\n"
        
        output += piatti[:-1]
        #print(output + "\n")
        return output

class Piatto:

    # costruisce un piatto dato il suo nome e la lista degli ingredienti
    def __init__(self, nome_piatto, ingredienti):
        self.name = nome_piatto
        self.ingredienti = ingredienti

    # un piatto è adatto ai vegetariani se non contiene carne né pesce
    def adatto_vegetariani(self):
        return "carne" not in self.ingredienti and "pesce" not in self.ingredienti

    # un piatto è adatto ai vegani se è adatto ai vegetariani e non contiene neanche miele, latte, burro, uova né formaggio
    def adatto_vegani(self):
        bad_ing = ["miele", "latte", "burro", "uova", "formaggio"]
        veg = True
        for x in bad_ing:
            if x in self.ingredienti:
                veg = False
        return self.adatto_vegetariani() and veg

    def nome_piatto(self):
        return self.name

# Esercizio 6:
#
# Domanda teorica:
#
# Si commenti l'affermazione il Sistema Operativo rende simili macchine differenti.
#
# Si inserisca la risposta in questa stringa:


risposta_teorica = ""

# ESEMPIO DI VALUTAZIONE ----


def main():

    comando1 = "cucchiai"
    test_primo_esercizio = [("110 g", 5), ("2 hg", 10), ("1 kg", 50)]

    comando2 = "rispetta tempi di cottura"
    test_secondo_esercizio = [("riso:15,patate:10,fagioli:20,carote:5,orzo:14",
                               "inserire fagioli\ndopo 5 minuti, inserire riso\ndopo 1 minuto, inserire orzo\ndopo 4 minuti, inserire patate\ndopo 5 minuti, inserire carote")]

    comando3 = "valuta dieta"
    test_terzo_esercizio = [
        ('piatti1.txt', {"pasta"}), ('piatti2.txt', {"insalata", "fagioli"})]

    comando4 = "conta calorie"
    test_quarto_esercizio = [("CCGP", 25), ("CPCG", 27), ("CGPC", 27)]

    primo_sorpassa_test_di_base = True
    secondo_sorpassa_test_di_base = True
    terzo_sorpassa_test_di_base = True
    quarto_sorpassa_test_di_base = True
    quinto_sorpassa_test_di_base = True

    esercizi_corretti = 0

    for (input1, expected_output) in test_primo_esercizio:
        comando = comando1
        output = compito(comando, input1)
        if output != expected_output:
            print("PRIMO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" +
                  ">" + str(output) + "<" +
                  "\nnon è quanto richiesto come output per input \n>" + str(input1) + "<" +
                  "\ndovrebbe invece essere così:\n" + ">" + str(
                      expected_output) + "<")
            primo_sorpassa_test_di_base = False
    if (primo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input1, expected_output) in test_secondo_esercizio:
        comando = comando2
        output = compito(comando, input1)
        if output != expected_output:
            print("SECONDO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" +
                  str(output) + "\n non è quanto richiesto come output per input \n" +
                  str(input1) + "\ndovrebbe invece essere così:\n" + str(expected_output))
            secondo_sorpassa_test_di_base = False
    if (secondo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input1, expected_output) in test_terzo_esercizio:
        comando = comando3
        output = compito(comando, input1)

        if output != expected_output:
            print("\n\nTERZO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" + str(
                output) + "\nnon sembra essere giusto rispetto all'input\n" + str(
                input1) + "\ndovrebbe invece essere così:\n" + str(expected_output))
            terzo_sorpassa_test_di_base = False
    if (terzo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input1, expected_output) in test_quarto_esercizio:
        comando = comando4
        output = compito(comando, input1)
        if output != expected_output:
            print("QUARTO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" + str(
                output) + "\nnon è quanto richiesto per gli input \n" + str(input1) +
                "\ndovrebbe invece essere così:\n" + str(expected_output))
            quarto_sorpassa_test_di_base = False
    if (quarto_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    gestoreMenu = Menu("menu della domenica")
    gestoreMenu.aggiungi_piatto(Piatto("pasta al sugo vegetale", [
                                "passata", "sale", "olio", "carota", "cipolla", "sedano"]))

    quinto_sorpassa_test_di_base = quinto_sorpassa_test_di_base and gestoreMenu.stampa_menu() == "menu della domenica (vegano)\npasta al sugo vegetale"

    gestoreMenu.aggiungi_piatto(
        Piatto("uovo fritto", ["uova", "sale", "olio"]))

    quinto_sorpassa_test_di_base = quinto_sorpassa_test_di_base and gestoreMenu.stampa_menu(
    ) == "menu della domenica (vegetariano)\npasta al sugo vegetale\nuovo fritto"

    gestoreMenu.aggiungi_piatto(Piatto("bistecca", ["carne"]))

    quinto_sorpassa_test_di_base = quinto_sorpassa_test_di_base and gestoreMenu.stampa_menu(
    ) == "menu della domenica\npasta al sugo vegetale\nuovo fritto\nbistecca"

    gestoreMenu.aggiungi_piatto(Piatto("carote", ["carote"]))

    quinto_sorpassa_test_di_base = quinto_sorpassa_test_di_base and gestoreMenu.stampa_menu(
    ) == "menu della domenica\npasta al sugo vegetale\nuovo fritto\nbistecca\ncarote"

    
    if not quinto_sorpassa_test_di_base:
        print("\n\n\nESERCIZIO CLASSI\n\n\nPer esercizio delle classi, non corretto\n")

    if (quinto_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    print("\n\n\n\n **               ^ ^ ^                **")
    print(" **               | | |                **")
    print(" **      eventuali errori sopra        **\n")

    print(
        " ** CONTROLLARE LA RIGA DI VALUTAZIONE **\n Il numero di esercizi che passano il test di correttezza è ",
        esercizi_corretti, end=" ")
    print(" quindi NON puoi consegnare" if esercizi_corretti <
          2 else ".  Consegna il compito!")
    print(" Riga valutazione: " + nome + ":" + cognome + ":" + matricola + ":" + str(
        primo_sorpassa_test_di_base) + ":" + str(secondo_sorpassa_test_di_base) + ":" + str(
        terzo_sorpassa_test_di_base), ":" + str(quarto_sorpassa_test_di_base), ":" + str(quinto_sorpassa_test_di_base),
        ":", risposta_teorica)


main()
