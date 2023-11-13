s1 = input("Inserire una stringa: ")
s2 = input("Inserire la stringa da cercare: ")

i = 0
while i <= len(s1) - len(s2):

    if s1.startswith(s2, i):
        print(i)

    i += 1
