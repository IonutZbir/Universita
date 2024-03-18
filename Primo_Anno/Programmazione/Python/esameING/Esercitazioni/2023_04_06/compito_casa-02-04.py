numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
numero3 = int(input("Inserisci il terzo numero: "))

if numero1 > numero2:  # (3?) .. 2 .. (3?) .. 1 ..(?3)
    if numero3 > numero1:  # 2 1 3
        print(numero2, numero1, numero3)
    else:  # (3?) .. 2 .. (3?) .. 1
        if numero2 > numero3:  # 3 2 1
            print(numero3, numero2, numero1)
        else:  # 2 3 1
            print(numero2, numero3, numero1)
else:  # (?3) .. 1 .. (?3) .. 2 .. (?3)
    if numero2 > numero3:  # (?3) .. 1 .. (?3) .. 2
        if numero1 > numero3:  # 3 1 2
            print(numero3, numero1, numero2)
        else:  # 1 3 2
            print(numero1, numero3, numero2)
    else:  # 1 2 3
        print(numero1, numero2, numero3)