from sys import exit

numero = int(input("Inserire un intero positivo: "))
if numero < 0:
    exit("Errore: hai inserito un valore negativo")

somma = 0
while numero > 0:
    cifra = numero % 10
    if cifra % 2 == 1:
        somma += cifra
    numero //= 10

print(somma)
