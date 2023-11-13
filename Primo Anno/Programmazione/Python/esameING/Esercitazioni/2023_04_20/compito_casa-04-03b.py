def almeno3x(parola):
    """
    Stampa se la parola in ingresso contiene almeno 3 x tra l'inizio e la fine

    :param parola: la parola in cui effettuare la ricerca
    """

    numero_x = 0
    indice1 = 0
    while indice1 < len(parola) and parola[indice1] == "x":
        numero_x += 1
        indice1 += 1

    indice2 = len(parola) - 1
    while indice2 > indice1 and parola[indice2] == "x":
        numero_x += 1
        indice2 -= 1

    if numero_x >= 3:
        print("La parola '%s' contiene almeno 3 x tra l'inizio e la fine" % parola)
    else:
        print("La parola '%s' non contiene almeno 3 x tra l'inizio e la fine" % parola)


almeno3x("x.......xx")
almeno3x("xxxx...  ")
almeno3x("xx...x")
almeno3x("xxx")
almeno3x("x......x")
almeno3x("....x....")
almeno3x("....xxx....")
almeno3x("..x.x.x..")
almeno3x("xx")
almeno3x("x")
almeno3x("")