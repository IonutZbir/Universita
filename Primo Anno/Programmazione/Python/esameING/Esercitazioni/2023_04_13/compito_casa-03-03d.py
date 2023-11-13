from sys import exit

a = int(input("Inserire un numero dispari: "))
if a < 0 or a % 2 == 0:
    exit("Errore: non hai inserito un numero dispari")

b = int(input("Inserire un numero dispari maggiore o uguale al precedente: "))
if b < 0 or b % 2 == 0 or b < a:
    exit("Errore: non hai inserito un numero dispari maggiore o uguale a %d" % a)

somma = 0
for numero in range(a, b + 1, 2):
    somma = somma + numero

print(somma)
