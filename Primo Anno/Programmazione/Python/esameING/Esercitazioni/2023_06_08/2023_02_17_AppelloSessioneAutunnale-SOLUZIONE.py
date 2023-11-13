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



##           PRIMA DI COMINCIARE
#    SCARICARE QUESTO FILE SUL DESKTOP E CAMBIARGLI IL NOME
#
#           [NUMERO_MATRICOLA].py
#
# dove [NUMERO_MATRICOLA] è il vostro numero di matricola
#
# ESEMPIO : 00713042.py
#
##           TASSATIVO:
#
#             lavorare SEMPRE in QUESTO file
#
##           TASSATIVO:
# Prima di cominciare, eseguire il codice a vuoto e osservare la riga di valutazione finale
# e le stampe che vengono fornite
#
# ogni tanto eseguire il codice per vedere se porta alla valutazione automatica
##
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
#  Si vuole costruire un sistema per aiutare gli organizzatori di Sanromolo, il Festival della Musica Romanesca.


def compito(comando,input):
    if comando == "sostituire qui il testo del comando":
        output = funzione_di_prova(input) # sostituire qui la funzione da richiamare per quel comando
    elif comando == "sostituire qui il testo del comando":
        output = funzione_di_prova(input) # sostituire qui la funzione da richiamare per quel comando
    #Per i successivi esercizi svolti, inserire le 2 righe precedenti per gli altri comandi
    if comando == "impagina classifica":
        output = impagina_classifica(input)
    elif comando == "conteggio voti":
        output = conteggio_voti(input)
    elif comando == "valuta scaletta":
        output = valuta_scaletta(input)
    elif comando == "concorrenti che si apprezzano col tempo":
        output = concorrenti_apprezzati_con_eta(input)
    else:
        output = False
    return output

def funzione_di_prova(input):
    return None

# Naturalmente dovrete liberamente definire una funzione per ogni comando.
# Tale funzione dovrà essere richiamata dalla funzione compito(comando,input)
# quando riceve la stringa del comando


# ESERCIZIO N. 1
# per il comando
#        "impagina classifica"
# data in input la classifica che è una lista di concorrenti (Voti,NomeConcorrente) deve restituire una stringa in cui
# la classifica sia impaginata come negli esempi seguenti.
#
# Suggerimento: La funzione "str" può essere usata per convertire un intero in una stringa: str(123) = '123'
#
# esempio di input:
# [(100, 'aventino'), (70, 'esquilino'), (30, 'celio')]
# Output:
# 'voti concorrente\n
#  ----------------\n
#  100     aventino\n
#  70     esquilino\n
#  30         celio\n'
#
# esempio di input:
# [(10000, 'esquilino'), (5000, 'aventino')]
# Output:
# 'voti  concorrente\n
#  -----------------\n
#  10000   esquilino\n
#  5000     aventino\n'

def impagina_classifica(input):
    # la tabella deve avere due colonne, separate al centro come se ci fosse un bordo verticale, che però nello specifico
    # è costituito da una striscia verticale di spazi

    # calcolare la larghezza di ciascuna colonna, cercando l'elemento più lungo (inclusa l'intestazione)

    # rispetto alla soluzione vista a lezione, ho tolto "max" dal nome delle variabili: non si tratta della larghezza
    # massima ma proprio della larghezza di una colonna, che a sua volta è calcolata come il massimo della lunghezza
    # degli elementi nella colonna

    larghezza_prima_colonna = len('voti')
    larghezza_seconda_colonna = len('concorrente')
    for voti, nome_concorrente in input:
        lunghezza_voti = len(str(voti))
        if lunghezza_voti > larghezza_prima_colonna:
            larghezza_prima_colonna = lunghezza_voti

        lunghezza_nome = len(nome_concorrente)
        if lunghezza_nome > larghezza_seconda_colonna:
            larghezza_seconda_colonna = lunghezza_nome

    # Nel ciclo for sovrastante viene usato il "variable unpacking" in modo tale, iterando su una lista i cui elementi
    # sono coppie, posso scompattare ciascuna coppia, assegnandone le componenti a due variabili distinte.
    # In alternativa:
    # for coppia in input:
    #     voti = coppia[0]
    #     nome_concorrente = coppia[1]
    #     ...


    # Il numero di spazi è pari alla differenza tra la lunghezza di un valore e la larghezza della colonna:
    # ciò va considerato per entrambe le colonne.
    # Inoltre va aggiunto uno spazio per il separatore delle colonne

    output = "voti" + " " * (larghezza_prima_colonna
                             - len("voti")
                             + larghezza_seconda_colonna
                             - len("concorrente") + 1) + "concorrente" + "\n"

    output += "-" * (larghezza_prima_colonna +
                     larghezza_seconda_colonna + 1) + "\n"

    for (voti, nome_concorrente) in input:
        output += str(voti) + " " * (larghezza_prima_colonna
                                     - len(str(voti))
                                     + larghezza_seconda_colonna
                                     - len(nome_concorrente) + 1) + nome_concorrente + "\n"

    return output

# ESERCIZIO N. 2
# per il comando
#        "conteggio voti"
# dato in input l'elenco dei voti deve produrre la classifica come lista di concorrenti (Voti, NomeConcorrente)
# In caso di ex-equo l'ordine in classifica è arbitrario
# esempio di input:
# ['esquilino', 'celio', 'aventino', 'esquilino', 'aventino', 'celio', 'aventino', 'esquilino', 'aventino', 'aventino']
# Output:
# [(5, 'aventino'),(3, 'esquilino'), (2, 'celio')]
def conteggio_voti(input):
    voti_concorrente = dict()
    for concorrente_votato in input:
        if concorrente_votato in voti_concorrente:
            voti_concorrente[concorrente_votato] += 1
        else:
            voti_concorrente[concorrente_votato] = 1

    risultato = []
    # for item in votiConcorrente.items():
    #     concorrente = item[0]
    #     voti = item[1]
    #     risultato.append((voti, concorrente))

    # produco la lista in output
    for concorrente in voti_concorrente:
        voti = voti_concorrente[concorrente]
        coppia = (voti, concorrente)
        risultato.append(coppia)

    # occorre ordinarla in maniera decrescente rispetto ai voti: si ricordi che le tuple contenute nella lista sono
    # confrontate un po' come le stringhe a partire dal primo elemento, quindi dai voti

    # primo approccio: ordino in maniera decrescente
    risultato.sort(reverse=True)  # si ricordi che sort() ordina la lista in-place
    # oppure,
    # risultato = sorted(risultato, reverse=True)  # si ricordi che sorted() restituisce una nuova lista

    # secondo approccio: ordinare in maniera crescente e poi invertire
    #risultato.sort()  # oppure, risultato = sorted(risultato)
    #risultato.reverse()  # oppure, risultato = risultato[::-1]

    return risultato
#
# ESERCIZIO N. 3
# per il comando
#        "valuta scaletta"
# dato in input il nome di un file contenente la scaletta della kermesse come righe ciascuna delle quali è del tipo
# nome-concorrente,strumento1,strumento2,strumento3,...
# si vuole determinare la "noiosità" della scaletta, andando a sommare per ciascun concorrente un contributo pari alla
# frazione degli strumenti che sono stati usati anche dal concorrente precedente
#
# esempio di input:
# 'scaletta1.txt'
# Output:
# 0.25
#
# esempio di input:
# 'scaletta2.txt'
# Output:
# 0.75

def valuta_scaletta(input):
    valutazione = 0.0

    # si sarebbe potuto pensare che il primo artista andasse gestito differentemente, perché non c'è un artista che lo
    # precede per fare il confronto.
    # In realtà, si può vedere che il processo generico usato per gestire un artista "nel mezzo" funziona anche per il
    # primo artista, assumendo semplicemente che per il primo artista gli strumenti precedenti siano l'insieme vuoto:
    # facendo i calcoli si vede che il contributo del primo artista è sempre zero.

    strumenti_precedenti = set()

    with open(input, "r") as f:
        for record in f:
            record = record.rstrip()  # elimino il \n alla fine, se c'è
            # devo togliere il primo elemento, cioè il nome dell'artista
            #campi = record.split(",")
            #strumenti = campi[1:]
            #insieme_strumenti = set(strumenti)

            # col metodo pop() evito una copia
            #campi = record.split(",")
            #campi.pop(0)
            #insieme_strumenti = set(campi)

            # a sinistra abbiamo solo due variabili mentre a destra abbiamo una lista di vari elementi (almeno uno che è il nome del concorrente):
            # - il primo elemento viene assegnato alla variabile _, di solito usata per indicare un valore ignorato
            # - i restanti elementi sono collezionati in una lista che viene assegnata alla variabile strumenti (che si noti è stata preceduta da un asterisco)
            _, *strumenti = record.split(",")
            insieme_strumenti = set(strumenti)

            # ho usato i set in modo tale da poter calcolare facilmente gli strumenti comuni attraverso l'intersezione
            valutazione += len(insieme_strumenti.intersection(strumenti_precedenti)) / len(insieme_strumenti)

            # al termine di ciascuna iterazione, prima di passare all'artista successivo, gli strumenti usati dall'artista
            # corrente sono assegnati alla variabile che contiene gli strumenti usati dall'artista precedente
            strumenti_precedenti = insieme_strumenti

    return valutazione

# ESERCIZIO N. 4
# per il comando:
#      "concorrenti che si apprezzano col tempo"
# data in input la distribuzione demografica dei voti ricevuti da ciascun concorrente come lista dei voti ottenuti, rispettivamente, da giovani, adulti
# e anziani, si restituiscano quei concorrenti che sono apprezzati con l'età, vale a dire che i voti ricevuti da ciascuna
# fascia demografica sono maggiori di quelli delle fasce demografiche più giovani
# esempio di input:
# [('aventino', (100, 15, 60)),('celio', (70, 80, 100)),('esquilino', (10, 70, 40)), ('palatino', (20, 20, 45))]
# Output:
#  {'celio'}
#
# esempio di input:
# [('aventino', (100, 150, 160)),('celio', (70, 80, 100)),('esquilino', (10, 70, 40)), ('palatino', (20, 25, 45))]
# Output:
#  {'aventino','celio', 'palatino'}

def concorrenti_apprezzati_con_eta(input):
    risultato = set()

    # for dati_concorrente in input:
    #     concorrente = dati_concorrente[0]
    #     voti = dati_concorrente[1]
    #     voti_giovani = voti[0]
    #     voti_adulti = voti[1]
    #     voti_anziani = voti[2]
    #     if voti_giovani < voti_adulti < voti_anziani:
    #         risultato.add(concorrente)

    # Esempio di unpacking più complesso
    for concorrente, (voti_giovani, voti_adulti, voti_anziani) in input:
        if voti_giovani < voti_adulti < voti_anziani:
            risultato.add(concorrente)

    return risultato

# ESERCIZIO 5
# Si vuole creare una classe che gestisca i voti.
class GestoreVoti:

    def __init__(self):
        self._votiConcorrenti = dict()

    def registraVoto(self, concorrente):
        if concorrente in self._votiConcorrenti:
            self._votiConcorrenti[concorrente] += 1
        else:
            self._votiConcorrenti[concorrente] = 1

    # restituisce il concorrente che ha vinto la kermesse musicale
    def vincitore(self):
        # vincitore = ""
        # voto_massimo = 0
        # for concorrente in self._votiConcorrenti:
        #     voti_concorrente = self._votiConcorrenti[concorrente]
        #     if voti_concorrente >= voto_massimo:
        #         voto_massimo = voti_concorrente
        #         vincitore = concorrente
        #
        # return vincitore

        return max(self._votiConcorrenti.keys(), key=self._votiConcorrenti.get) # sto passando il riferimento al metodo get dello specifico dizionario usato da questo oggetto

# Esercizio 6:
#
# Domanda teorica:
#
# Si descriva il concetto di complessità temporale di un algoritmo
#
# Si inserisca la risposta in questa stringa:

risposta_teorica = "ciao " \
                   "mondo"

#### ESEMPIO DI VALUTAZIONE ----

def main():

    comando1 = "impagina classifica"
    test_primo_esercizio = [([(100, 'aventino'), (70, 'esquilino'), (30, 'celio')], 'voti concorrente\n----------------\n100     aventino\n70     esquilino\n30         celio\n'),
                            ([(10000, 'esquilino'), (5000, 'aventino')], 'voti  concorrente\n-----------------\n10000   esquilino\n5000     aventino\n')]

    comando2 = "conteggio voti"
    test_secondo_esercizio = [(['esquilino', 'celio', 'aventino', 'esquilino', 'aventino', 'celio', 'aventino', 'esquilino', 'aventino', 'aventino'], [(5, 'aventino'),(3, 'esquilino'), (2, 'celio')])]


    comando3 = "valuta scaletta"

    test_terzo_esercizio = [('scaletta1.txt', 0.25), ('scaletta2.txt', 0.75)]

    comando4 = "concorrenti che si apprezzano col tempo"

    test_quarto_esercizio = [([('aventino', (100, 15, 60)),('celio', (70, 80, 100)),('esquilino', (10, 70, 40)), ('palatino', (20, 20, 45))], {'celio'}),
                             ([('aventino', (100, 150, 160)),('celio', (70, 80, 100)),('esquilino', (10, 70, 40)), ('palatino', (20, 25, 45))], {'aventino','celio', 'palatino'}),
                             ([('aventino', (100, 150, 90)),('celio', (100, 90, 90))], set())]


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
            print("SECONDO ESERCIZIO\ncomando: " + comando + "------------------------\nERRORE\n" +
                  str(output) + "\n non è quanto richiesto come output per input \n" +
                  str(input1) + "\ndovrebbe invece essere così:\n" + str(expected_output))
            secondo_sorpassa_test_di_base = False
    if (secondo_sorpassa_test_di_base):
        esercizi_corretti = esercizi_corretti + 1

    for (input1, expected_output) in test_terzo_esercizio:
        comando = comando3
        output = compito(comando,input1)

        if abs(output - expected_output) > 0.0001:
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

    gestoreVoti = GestoreVoti()
    gestoreVoti.registraVoto('aventino')

    quinto_sorpassa_test_di_base = quinto_sorpassa_test_di_base and gestoreVoti.vincitore() == 'aventino'

    gestoreVoti.registraVoto('aventino')
    gestoreVoti.registraVoto('celio')

    quinto_sorpassa_test_di_base = quinto_sorpassa_test_di_base and gestoreVoti.vincitore() == 'aventino'

    gestoreVoti.registraVoto('celio')
    gestoreVoti.registraVoto('celio')

    quinto_sorpassa_test_di_base = quinto_sorpassa_test_di_base and gestoreVoti.vincitore() == 'celio'

    gestoreVoti.registraVoto('aventino')
    gestoreVoti.registraVoto('aventino')
    gestoreVoti.registraVoto('esquilino')

    quinto_sorpassa_test_di_base = quinto_sorpassa_test_di_base and gestoreVoti.vincitore() == 'aventino'

    if not quinto_sorpassa_test_di_base:
        print("\n\n\nESERCIZIO CLASSI\n\n\nPer esercizio delle classi, non corretto\n")


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
