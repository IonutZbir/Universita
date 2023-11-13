def lista_numeri_dispari(n):
    """
    Restituisce una lista contenente i primi n numeri dispari
    :param n: indica quanti numeri dispari restituire
    :type n: int
    :return: una lista contenente i primi n numeri dispari
    :rtype: list[int]
    """

    risultato = []

    for i in range(n):
        risultato.append(2 * i + 1)

    return risultato

