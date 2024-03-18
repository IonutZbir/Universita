a = [1, 2, 3, 4, 5]
b = ['ciao', 'mamma', 'papa', 'sorella', 'fratello']
# / div float
# // div int

n = 5
k = 4
j = 3

a[k] = b
c = a[:]
c[k][j] = 1 # modifico anche b in a, b è un alias non una copia
a[j] = 'one'
print(a)
print(c)
print(c[k][j], a[k][j])

d = {1: 10, '2': 2}
print(d.get(2, 10.2))

print(2 + 's')