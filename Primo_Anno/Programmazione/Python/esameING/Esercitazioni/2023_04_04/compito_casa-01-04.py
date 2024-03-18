from math import sqrt

a = float(input("Inserire la lunghezza del primo cateto: "))
b = float(input("Inserire la lunghezza del secondo cateto: "))
c = sqrt(a**2 + b**2)
print("La lunghezza dell'ipotenusa è %.2f" % c)
