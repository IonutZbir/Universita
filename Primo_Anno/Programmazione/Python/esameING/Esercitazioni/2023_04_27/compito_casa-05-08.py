def tutti_pari(lista):
    risultato = True
    indice = 0
    while risultato and indice < len(lista):
        if lista[indice] % 2 != 0:
            risultato = False
        indice += 1
    return risultato


def esegui_caso_di_prova(lista):
    print(lista, "--->", tutti_pari(lista))


def main():
    esegui_caso_di_prova([])
    esegui_caso_di_prova([2])
    esegui_caso_di_prova([2, 4])
    esegui_caso_di_prova([1])
    esegui_caso_di_prova([2, 1])
    esegui_caso_di_prova([1, 2])
    esegui_caso_di_prova([1, 2, 1])
    esegui_caso_di_prova([2, 1, 2])


main()
