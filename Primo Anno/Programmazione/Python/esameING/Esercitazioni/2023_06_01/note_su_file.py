#
# Per accedere a un file, occorre averne il nome (se si trova nella "current working directory":
# in PyCharm la cartella dove si trova il file .py eseguito) oppure il suo path (assoluto oppure
# relativo alla current working directory) nel caso di file che si trovano fuori dalla "current
# working directory".

nome_file = "2022_01_21_prova.txt"

# 1. aprire il file. La funzione "open" restituisce un oggetto che rappresenta un accesso a un file,
#    includendo informazioni quali la "posizione corrente" nel file, detta "file pointer".
f = open(nome_file, "r")
# 2. fare qualcosa con il file
# ...
# 3. chiudere il file
f.close()

# La chiusura di un file è importante: finché un file è aperto, esso rimane associato al processo
# che sta eseguendo il programma, consumando risorse (limitate dal sistema operativo), mentre il sistema
# operativo potrebbe far rispettare dei vincoli (es., Windows non permette di cancellare un file aperto)
# Inoltre, le scritture su un file potrebbero essere "bufferizzate" dalla libreria Python e differite/raggruppate per
# ottimizzare l'accesso al file. Alla chiusura di un file, l'informazione ancora contenuta nel buffer
# viene scritta.
# A seconda dell'implementazione di Python, tutti i file sono comunque chiusi al termine del programma oppure quando
# non sono più "raggiungibili" (semplificando, non ci sono variabili, attributi, etc... che fanno riferimento
# a questi oggetti). In realtà, ciò potrebbe non avvenire in caso di certi crash "gravi" (non una semplice eccezione),
# che determinano la terminazione immediata del processo che esegue il programma Python.
# Si noti che il sistema operativo chiude comunque i file aperti associati a un processo che ha eseguito un programma
# Python. Tuttavia, essendo situato a un livello logico più basso, il sistema operativo non invocherà le procedure di
# svuotamento dei buffer implementati a livello di libreria Python.

# Il codice soprastante per accedere a un file è soggetto al fatto che se il codice al punto 2) solleva un'eccezione
# (tipo ciò che accade quando si accede a un indice non valido di una lista), la chiusura 3) non viene invocata (esplicitamente)

# Meglio usare il costrutto "with". Esso chiude un file in automatico appena termina il blocco di codice a
# esso associato (anche in presenza di eccezioni).

# Per approfondire, si suggerisce di leggere questo riferimento: https://realpython.com/why-close-file-python/

# Per approfondire il discorso della lettura/scrittura di file si suggerisce questo riferimento:
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# Apre un file in sola lettura. Se il file non esiste, viene lanciata l'eccezione FileNotFoundError
with open(nome_file, "r") as f:
    pass  # al posto di "pass", inserire del codice che lavora sul file

print("- primo test ----")
# Il secondo argomento ("r") indica la modalità di apertura (in questo caso, in sola lettura).
# Si noti che per impostazione predefinita, i file sono aperti in sola lettura e modalità testo.
# La modalità testo implica che i byte letti dal file sono convertiti in stringhe usando un
# encoding (dipendente dalla piattaforma, a meno di non specificarne uno) e viceversa quando viene
# scritta una stringa, essa viene convertita in byte usando un encoding. In maniera simile, il
# delimitatore di riga del sistema operativo \n (su Unix) e \r\n (su Windows) viene convertito in
# \n (anche questo comportamento può essere variato)
with open(nome_file, "r") as f:
    # Legge tutto il contenuto del file in una stringa.
    # Il problema è che non possiamo leggere in questo modo file più grandi della memoria
    # disponibile (si noti che, in genere, la memoria di massa è molto più capiente della
    # memoria RAM e che spesso i file possono essere molti grandi)
    testo = f.read()
    print(testo)

print("- secondo test ----")

with open(nome_file, "r") as f:
    # legge al più 3 caratteri e avanza la posizione della prossima operazione di lettura/scrittura
    primi_cinque = f.read(3)
    secondi_cinque = f.read(3)

    print(primi_cinque, end="")  # il keyword argument end="" evita l'aggiunta di \n dopo la print
    print(secondi_cinque, end="")
    print()  # manda a capo
    # Restituisce la posizione della successiva operazione di lettura/scrittura.
    # In modalità testuale, è un valore "opaco" che non dovrebbe essere interpretato
    print(f.tell())

print("- terzo test ----")

with open(nome_file, "r") as f:
    # sto stampando tutto il file, leggendo a gruppi di 5 caratteri
    testo = f.read(5)
    while testo != "":
        print(testo, end="")
        testo = f.read(5)  # il metodo read() restituisce una stringa vuota quando si è arrivata alla fine del file

print("- quarto test ----")

with open(nome_file, "r") as f:
    righe = f.readlines()  # restituisce una lista i cui elementi sono le righe del file
    print(righe)
    # tutte le righe, tranne l'ultima se non finisce con un accapo, sono terminate da un accapo (\n)
    for riga in righe:
        riga = riga.rstrip()  # si noti che riga[:-1] non va bene, perché non è detto che l'ultima riga contenga uno spazio da rimuovere!
        print(repr(riga))

print("- quinto test ----")

with open(nome_file, "r") as f:
    riga = f.readline()  # legge una riga, restituisce "" se ha raggiunto la fine del file
    n = 0
    # per leggere una specifica riga, devo leggere tutte quelle precedenti
    riga_che_voglio = 2
    while riga != "" and n <= riga_che_voglio:
        print(n, repr(riga))
        riga = f.readline()
        n += 1

print("- sesto test ----")

with open(nome_file, "r") as f:
    for riga in f:
        print(repr(riga))

# apre un file in scrittura con troncamento (cioè eliminando il contenuto esistente)
# se il file non esiste, viene creato
with open("file_da_scrivere.txt", "w") as f:
    #f.write("ciao\n")  # il metodo write() non va a capo in automatico
    print("ciao", file=f)  # con il keyword argument file=f indichiamo alla print di scrivere su file

with open("file_da_scrivere.txt", "w") as f:
    print("mondo", file=f)

# nel file "file_da_scrivere.txt" troveremo solo la parola "mondo"

with open("file_da_scrivere2.txt", "w") as f:
    f.write("ciao ")

# Apre un file in scrittura aggiungendo alla fine del file se esiste.
# Se il file non esiste, viene creato

with open("file_da_scrivere2.txt", "a") as f:
    f.write("mondo!")

# nel file "file_da_scrivere2.txt" troveremo il testo "ciao mondo"

print("- settimo test ----")

import os

# "w+" indica che si vuole aprire in scrittura e lettura (troncando il file)
# "a+" serve a scrivere (sempre) alla del file, ma permettendo di leggere in altre posizioni
# "r+" apre il file in lettura e scrittura, fallendo se il file non esiste e non cancellando i dati esistenti
with open("file_da_scrivere3.txt", "w+") as f:
    f.write("ciao")
    # Siccome la prossima operazione è alla fine del file, non può essere letto nulla
    print("Lettura = ", repr(f.read(1)))
    # Riportiamo la posizione all'inizio del file
    f.seek(0, os.SEEK_SET)
    # Leggeremo la "c" che abbiamo scritto
    print("Lettura = ", repr(f.read(1)))
    # Su Windows, questa I viene comunque scritta dopo ciao, invece che al posto della "i"
    f.write("I")  # stiamo sovrascrivendo la i con una I maiuscola
    f.seek(0, os.SEEK_END)  # riportiamoci alla fine del file
    f.write("!")

    # Si noti che per i file aperti come testo, il metodo seek accetta i valori restituiti dal
    # metodo tell() relativi all'inizio del file e la coppia (0, os.SEEK_END) per spostarsi alla fine

    # In generale, per i file di testo è molto difficile lavorare con seek() e tell()

