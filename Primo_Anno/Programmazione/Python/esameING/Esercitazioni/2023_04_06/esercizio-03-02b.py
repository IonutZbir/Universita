from sys import exit

numero = int(input("Inserire un intero non negativo: "))

if numero < 0:
    exit("Errore: numero negativo")

numeroFormattato = ""

while numero >= 1000:
    gruppo = numero % 1000
    numeroFormattato = "," + str(gruppo).rjust(3, "0") + numeroFormattato
    numero //= 1000

numeroFormattato = str(numero) + numeroFormattato

print(numeroFormattato)
