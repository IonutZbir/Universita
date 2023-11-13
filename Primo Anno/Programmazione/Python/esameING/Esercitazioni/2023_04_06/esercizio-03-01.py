parola = input("Inserire una parola: ")

lunghezza_sottostringa = 1
while lunghezza_sottostringa <= len(parola):
    i = 0
    while i + lunghezza_sottostringa <= len(parola):
        print(parola[i:i + lunghezza_sottostringa])
        i += 1
    lunghezza_sottostringa += 1
