def almeno_un_pari(lista):
    incontrato_pari = False
    indice = 0
    while not incontrato_pari and indice < len(lista):
        if lista[indice] % 2 == 0:
            incontrato_pari = True
        indice += 1
    return incontrato_pari


def esegui_caso_di_prova(lista):
    print(lista, "--->", almeno_un_pari(lista))


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
