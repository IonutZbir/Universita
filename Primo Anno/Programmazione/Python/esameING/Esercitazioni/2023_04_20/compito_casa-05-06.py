def lista_in_ordine_crescente(lista):
    if len(lista) <= 1:
        return True
    else:
        valore_precedente = lista[0]
        risultato = True
        i = 1
        while risultato and i < len(lista):
            valore_corrente = lista[i]
            if not valore_precedente < valore_corrente:
                risultato = False
            valore_precedente = valore_corrente
            i += 1

    return risultato


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
    print(lista_in_ordine_crescente([1, 1, 2]))


main()
