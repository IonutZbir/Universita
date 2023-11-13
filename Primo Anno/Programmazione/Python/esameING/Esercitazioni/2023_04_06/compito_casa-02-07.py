giorno = int(input("Inserisci Giorno: "))
mese = int(input("Inserisci Mese: "))

if 1 <= mese <= 12 and 1 <= giorno <= 31:
    if mese == 1 or mese == 2 or mese == 3:
        stagione = "Inverno"
    elif mese == 4 or mese == 5 or mese == 6:
        stagione = "Primavera"
    elif mese == 7 or mese == 8 or mese == 9:
        stagione = "Estate"
    elif mese == 10 or mese == 11 or mese == 12:
        stagione = "Autunno"

    if mese % 3 == 0 and giorno >= 21:
        if stagione == "Inverno":
            stagione = "Primavera"
        elif stagione == "Primavera":
            stagione = "Estate"
        elif stagione == "Estate":
            stagione = "Autunno"
        else:
            stagione = "Inverno"

    print("Stagione:", stagione)
else:
    print("Inserire giorno e mese correttamente ;)")