from math import hypot

a = float(input("Inserire la lunghezza del primo cateto: "))
b = float(input("Inserire la lunghezza del secondo cateto: "))
c = hypot(a, b)
print("La lunghezza dell'ipotenusa è %.2f" % c)
