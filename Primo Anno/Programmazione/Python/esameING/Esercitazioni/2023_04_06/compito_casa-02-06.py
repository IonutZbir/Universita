numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
numero3 = int(input("Inserisci il terzo numero: "))

if numero1 == numero2 == numero3:
    print("all the same")
#elif numero1 != numero2 != numero3 != numero1:
elif numero1 != numero2 and numero1 != numero3 and numero2 != numero3:
    print("all different")
else:
    print("neither")
