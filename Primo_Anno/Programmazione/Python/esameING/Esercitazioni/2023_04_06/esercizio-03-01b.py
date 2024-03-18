parola = input("Inserire una parola: ")

for lunghezza_sottostringa in range(1, len(parola) + 1):
    for i in range(len(parola) - lunghezza_sottostringa + 1):
        print(parola[i:i + lunghezza_sottostringa])
