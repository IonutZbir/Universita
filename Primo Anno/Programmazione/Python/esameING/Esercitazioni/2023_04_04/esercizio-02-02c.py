# ATTENZIONE!
# ATTENZIONE!
# ATTENZIONE!
# ATTENZIONE!
# ATTENZIONE!
# Questa soluzione NON è buona.
# Nella version c vedremo come scrivere la condizione in maniera più semplice
# Notate, infatti, che l'elenco di tutti le maiuscole è lungo ed è facile
# dimenticarsene qualcuno!

targa = input("Inserire targa: ")

if len(targa) != 7:
    targa_valida = False
else:
    i = 0
    targa_valida = True
    while i < len(targa) and targa_valida:
        c = targa[i]

        if i < 2:
            targa_valida = "A" <= c <= "Z"
        elif i < 5:
            targa_valida = "0" <= c <= "9"
        else:
            targa_valida = "A" <= c <= "Z"

        i += 1

if targa_valida:
    print("Targa valida")
else:
    print("Targa non valida")
