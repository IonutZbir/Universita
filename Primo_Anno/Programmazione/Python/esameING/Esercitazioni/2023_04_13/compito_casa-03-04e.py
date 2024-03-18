s1 = input("Inserire una stringa: ")
s2 = input("Inserire la stringa da cercare: ")

i = 0
while i != -1:
    i = s1.find(s2, i)
    if i != -1:
        print(i)
        i += 1

