numero = int(input("Inserire un intero compreso tra 1 e 9: "))
pallottoliere = "|" + "0" * (10 - numero) + "-" * 10 + "0" * numero + "|"
print(pallottoliere)
