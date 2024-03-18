s1 = input("Inserire una stringa: ")
s2 = input("Inserire la stringa da cercare: ")

i = 0
while i <= len(s1) - len(s2):
    corrispondenti = True
    j = 0
    while corrispondenti and j < len(s2):
        if s1[i + j] != s2[j]:
            corrispondenti = False
        j += 1
    if corrispondenti:
        print(i)

    i += 1