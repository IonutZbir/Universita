def ruota_90_gradi_senso_orario(immagine):
    """
    Ruota un'immagine di 90 gradi in senso orario

    :param immagine: una immagine fatta di n x n caratteri disposti su n righe e n colonne. L'ultima riga ha un accapo
    :type immagine: str
    :return:
    :rtype: str
    """
    righe = immagine.split("\n")
    righe.pop()  # rimuove l'ultima riga vuota causata dall'ultimo accapo
    righe.reverse()

    risultato = ""

    n = len(righe)
    for j in range(n):
        for i in range(n):
            risultato += righe[i][j]
        risultato += "\n"

    return risultato


def main():
    immagine = "XXXXX\n..X..\n..X..\n..X..\n..X..\n"
    risultato = ruota_90_gradi_senso_orario(immagine)
    print(risultato)


main()
