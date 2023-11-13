def conta_pari_e_dispari(lista):
    """
    Restituisci il numero di pari e di dispari all'interno di una lista di interi
    :param lista: una lista di numero interi
    :type lista: list[int]
    :return: quanti pari e quanti dispari ci sono nella lista
    :rtype: tuple[int, int]
    """
    numero_pari = 0
    numero_dispari = 0

    for numero in lista:
        if numero % 2 == 0:
            numero_pari += 1
        else:
            numero_dispari += 1

    return numero_pari, numero_dispari


def main():
    print(conta_pari_e_dispari([10, 5, 6, 4, 2, 7]))


main()
