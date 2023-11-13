numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
numero3 = int(input("Inserisci il terzo numero: "))

if numero1 > numero2:
    if numero1 > numero3:
        massimo = numero1
    else:
        massimo = numero3
else:
    if numero2 > numero3:
        massimo = numero2
    else:
        massimo = numero3

print("Il massimo è ", massimo)
