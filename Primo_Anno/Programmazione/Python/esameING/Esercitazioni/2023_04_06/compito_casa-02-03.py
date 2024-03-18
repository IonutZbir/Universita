numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
numero3 = int(input("Inserisci il terzo numero: "))

if numero1 < numero2 < numero3:
    print("increasing")
elif numero1 > numero2 > numero3:
    print("decreasing")
else:
    print("neither")
