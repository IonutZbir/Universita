s1 = input("Inserire una stringa: ")

s2 = ""
for i in range(len(s1)):
    if i == 0 or s1[i] != s1[i - 1]:
        s2 += s1[i]

print(s2)
