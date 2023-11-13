s1 = input("Inserire una stringa: ")
s2 = input("Inserire la stringa da cercare: ")

i = 0
while i <= len(s1) - len(s2):
    corrispondenti = True

    if s1[i:i+len(s2)] == s2:
        print(i)

    i += 1