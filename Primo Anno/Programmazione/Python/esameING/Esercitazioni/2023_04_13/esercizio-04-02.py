def farfallese(frase):
    """
    Traduce una parola o frase dalla lingua italiana al farfallese: ogni vocale è raddoppiata con interposta una f

    :param frase: la parola o frase da tradurre
    :return: la traduzione in farfallese della parola o frase in ingresso
    """
    frase_tradotta = ""
    for c in frase:
        if vocale(c):
            frase_tradotta = frase_tradotta + c + "f" + c
        else:
            frase_tradotta = frase_tradotta + c

    return frase_tradotta


def vocale(carattere):
    """
    Restituisce True se il carattere passato è una vocale

    :param carattere:
    :return: True se il carattere passato è una vocale
    """
    return carattere.lower() in "aeiou"


print(farfallese("parola"))
