s1 = input("Inserire una stringa: ")

s2 = ""
for carattere in s1:
    if len(s2) == 0 or s2[-1] != carattere:
        s2 += carattere

print(s2)
