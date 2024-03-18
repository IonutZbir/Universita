numero = int(input("Inserisci un intero positivo fino a 3999: "))

unita = numero % 10
decine = (numero // 10) % 10
centinaia = (numero // 100) % 10
migliaia = numero // 1000

unitaStringa = ""
if unita < 4:
    unitaStringa = "I" * unita
elif unita == 4:
    unitaStringa = "IV"
elif unita < 9:
    unitaStringa = "V" + ("I" * (unita - 5))
else:
    unitaStringa = "IX"

decineStringa = ""
if decine < 4:
    decineStringa = "X" * decine
elif decine == 4:
    decineStringa = "XL"
elif decine < 9:
    decineStringa = "L" + ("X" * (decine - 5))
else:
    decineStringa = "XC"

centinaiaStringa = ""
if centinaia < 4:
    centinaiaStringa = "C" * centinaia
elif centinaia == 4:
    centinaiaStringa = "CD"
elif centinaia < 9:
    centinaiaStringa = "D" + ("C" * (centinaia - 5))
else:
    centinaiaStringa = "CM"

migliaiaStringa = "M" * migliaia

print(migliaiaStringa + centinaiaStringa + decineStringa + unitaStringa)
