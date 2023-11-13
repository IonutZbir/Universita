s1 = input("Inserire una stringa: ")
s2 = input("Inserire la stringa da cercare: ")

for i in range(len(s1) - len(s2) + 1):

    if s1.startswith(s2, i):
        print(i)
