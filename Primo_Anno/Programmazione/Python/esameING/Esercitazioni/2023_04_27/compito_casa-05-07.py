def rimuovi_pari(lista):
    """
    Rimuove i numeri pari dalla lista in ingresso (in place)
    :param lista: una lista di numeri interi
    :type lista: list[int]
    """
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            lista.pop(i)
        else:
            i += 1

        # Nota: quando si cancella l'elemento corrente, non si deve aggiornare il contatore perché l'elemento successivo
        # andrà a occupare la posizione lasciata dell'elemento appena rimosso


def effettua_test(lista):
    print(lista, end=" --> ")
    rimuovi_pari(lista)
    print(lista)


def main():
    effettua_test([])
    effettua_test([1])
    effettua_test([2])
    effettua_test([1, 2, 3])
    effettua_test([1, 3, 2])
    effettua_test([2, 1, 3])


main()
