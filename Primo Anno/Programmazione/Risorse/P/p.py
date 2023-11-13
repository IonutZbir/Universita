
a = ["a", "c", "d", "r", "f"]
c = 0
for x, y in zip(a[:-1], a[1:]):
    c += 1 if x < y else 0
    #print(x, y)



k = 2
j = 1
a = [1, 2, 3, 4]
b = ["ciao", "mamma", "tf", "cacca"]
a[k] = b
print(a)
c = a[:]
c[k][j] = 1
print(c)
a[j] = 'one'
print(a)
print(a[k][j])
print(c[k][j])