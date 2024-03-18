def trovaVarchi(labirinto):
    """
    Trova i varchi lungo il perimetro di un labirinto
    :param labirinto: un labirinto rappresentato come una matrice m x n di caratteri
    :return: una lista di varchi lungo il perimetro di un labirinto, ciascuno rappresentato come una lista [i, j]
             dove i è il numero di riga e j è il numero di colonna
    """
    varchi = []

    larghezza = len(labirinto[0])
    lunghezza = len(labirinto)

    for i in range(larghezza):
        # varchi lungo il lato superiore
        if labirinto[0][i] == " ":
            varchi.append([0, i])

        # varchi lungo il lato inferiore
        if labirinto[lunghezza - 1][i] == " ":
            varchi.append([lunghezza - 1, i])

    # varchi lungo i lati verticali
    for j in range(lunghezza):
        # ... lungo il lato sinistro
        if labirinto[j][0] == " ":
            varchi.append([j, 0])

        # ... lungo il lato destro
        if labirinto[j][larghezza - 1] == " ":
            varchi.append([j, larghezza - 1])

    return varchi


def trovaUscita(labirinto, posizione, uscita):
    """
    Trova un percorso verso l'uscita partendo dalla posizione corrente
    :param labirinto: una matrice che rappresenta il labirinto. Viene modifica dalla funzione (es. aggiunta di punti
                      nelle celle sul cammino corrente
    :param posizione: posizione corrente
    :param uscita: posizione dell'uscita
    :return: True se e solo se è stata trovato un cammino verso l'uscita
    """
    i = posizione[0]
    j = posizione[1]

    if labirinto[i][j] != " ":
        return False

    labirinto[i][j] = "."

    stampaImmagine(labirinto)

    if posizione == uscita:
        return True

    nuovePosizioni = calcolaNuovePosizioni(labirinto, posizione)

    for prossimaPosizione in nuovePosizioni:
        r = trovaUscita(labirinto, prossimaPosizione, uscita)

        if r:
            return True

    labirinto[i][j] = " "

    stampaImmagine(labirinto)

    return False


def calcolaNuovePosizioni(labirinto, posizione):
    """
    Restituisce una lista i cui elementi sono le posizioni (non occupate da muri) che possono essere raggiunte con una
    mossa dalla posizione corrente
    :param labirinto: una matrice che rappresenta il labirinto
    :param posizione: posizione corrente
    :return: lista delle posizioni raggiungibili
    """
    i = posizione[0]
    j = posizione[1]

    nuovePosizioni = list()

    if i > 0:
        aggiungiPosizioneSenzaMuri(labirinto, i - 1, j, nuovePosizioni)

    if i < len(labirinto) - 1:
        aggiungiPosizioneSenzaMuri(labirinto, i + 1, j, nuovePosizioni)

    if j > 0:
        aggiungiPosizioneSenzaMuri(labirinto, i, j - 1, nuovePosizioni)

    if j < len(labirinto[0]) - 1:
        aggiungiPosizioneSenzaMuri(labirinto, i, j + 1, nuovePosizioni)

    return nuovePosizioni


def aggiungiPosizioneSenzaMuri(labrinto, i, j, listaPosizioni):
    """
    Aggiunge la posizione (i, j) alla lista passata, se quella posizione non è occupata da un muro (rappresentato da un
    asterisco)

    :param labrinto: una matrice che rappresenta il labirinto
    :param i: riga associata alla nuova posizione
    :param j: colonna associata alla nuova posizione
    :param listaPosizioni: lista di posizioni
    """
    if labrinto[i][j] != "*":
        listaPosizioni.append([i, j])


def leggiImmagine(immagine):
    """
    Legge un'immagine rappresentata come una stringa (formata da n riga ciascuna contente m caratteri e terminata dal
    carattere di nuova riga) e la trasforma in una matrice di caratteri m x n (eliminando i caratteri di nuova riga e
    l'ultima riga vuota)
    :param immagine: una stringa che rappresenta un'immagine
    :return: una matrice m x n contente i caratteri di cui si compone l'immagine
    """
    righe = immagine.split("\n")
    righe.pop(-1)
    for i in range(len(righe)):
        righe[i] = list(righe[i])
    return righe


def stampaImmagine(matrice):
    """
    Stampa un'immagine rappresenta come matrice di caratteri
    :param matrice: una matrice di caratteri
    """
    for r in matrice:
        print("".join(r))
    print()


def main():
    immagineLabirinto = \
        "* *******\n" + \
        "*     * *\n" + \
        "* *** * *\n" + \
        "*   *   *\n" + \
        "* * *** *\n" + \
        "* * *   *\n" + \
        "*   * ***\n" + \
        "***** * *\n" + \
        "*       *\n" + \
        "******* *\n"

    labirinto = leggiImmagine(immagineLabirinto)

    varchi = trovaVarchi(labirinto)

    if len(varchi) != 2:
        print("Numero di varchi scorretto:", varchi)
        return

    print("Varchi: ")
    print(varchi)

    scelta = int(input("Da quale iniziare? (1 o 2): "))
    if scelta == 1:
        ingresso = varchi[0]
        uscita = varchi[1]
    else:
        ingresso = varchi[1]
        uscita = varchi[0]

    uscita_trovata = trovaUscita(labirinto, ingresso, uscita)
    if uscita_trovata:
        print("== Uscita trovata ==")
    else:
        print("== Uscita non trovata ==")

main()


