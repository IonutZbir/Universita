def arricchisci_matrice(matrice):
    """
    Data una matrice m x n, restituisce una nuova matrice (m + 1) x (n + 1) in cui sono state aggiunte:
     * una nuova riga in fondo che contiene la somma di tutte le righe
     * una nuova colonna a destra che contiene la somma di tutte le colonne

    :param matrice: una matrice m x n
    :type matrice: list[list[int]]
    :return: una matrice (m + 1) x (n + 1)
    :rtype: list[list[int]]
    """
    m = len(matrice)
    n = len(matrice[0])

    somma_righe = [0] * (n + 1)

    risultato = []

    for i in range(m):
        riga = matrice[i]
        somma_riga_corrente= sum(riga)
        nuova_riga = riga + [somma_riga_corrente]
        for j in range(len(nuova_riga)):
            somma_righe[j] += nuova_riga[j]

        risultato.append(nuova_riga)

    risultato.append(somma_righe)

    return risultato


def main():
    print(arricchisci_matrice([[1, 2, 3], [4, 5, 6]]))


main()
