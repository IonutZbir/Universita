# ATTENZIONE!
# ATTENZIONE!
# ATTENZIONE!
# ATTENZIONE!
# ATTENZIONE!
# Questa soluzione NON è buona.
# Nella version c vedremo come scrivere la condizione in maniera più semplice
# Notate, infatti, che l'elenco di tutti le maiuscole è lungo ed è facile
# dimenticarsene qualcuna o aggiungere altri caratteri indesiderati!
# Si può fare una considerazione simile anche per la condizione riguardante
# la parte numerica.

targa = input("Inserire targa: ")

if len(targa) != 7:
    targa_valida = False
else:
    i = 0
    targa_valida = True
    while i < len(targa) and targa_valida:
        c = targa[i]

        if i < 2:
            targa_valida = c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif i < 5:
            targa_valida = c in "0123456789"
        else:
            targa_valida = c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        i += 1

if targa_valida:
    print("Targa valida")
else:
    print("Targa non valida")
