def lista_in_ordine_crescente(lista):
    lista_ordinata = True
    i = 0
    while lista_ordinata and i < len(lista) - 1:
        if not lista[i] < lista[i+1]:
            lista_ordinata = False
        i += 1
    return lista_ordinata


def esegui_caso_di_prova(lista):
    print(lista, "-->", end=" ")
    print(lista_in_ordine_crescente(lista))


def main():
    print(lista_in_ordine_crescente([]))
    print(lista_in_ordine_crescente([1]))
    print(lista_in_ordine_crescente([1, 2]))
    print(lista_in_ordine_crescente([1, 2, 3]))
    print("----")
    print(lista_in_ordine_crescente([2, 1, 3]))
    print(lista_in_ordine_crescente([1, 1, 2]))
    print(lista_in_ordine_crescente([1, 2, 2]))


main()
