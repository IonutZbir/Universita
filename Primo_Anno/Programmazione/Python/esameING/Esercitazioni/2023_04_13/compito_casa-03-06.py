s1 = input("Inserire una stringa: ")

s2 = ""
for i in range(0, len(s1)):
    if i != 0 and i % 3 == 0:
        s2 = "," + s2

    s2 = s1[-i - 1] + s2

print(s2)
