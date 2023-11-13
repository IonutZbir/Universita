def prima_occorrenza(s1, s2):
    """
    Trova la prima occorrenza della stringa s2 all'interno della stringa s1

    :param s1: stringa nella quale effettuare la ricerca
    :type s1: str
    :param s2: stringa da cercare
    :type s2: str
    :return l'indice della prima occorrenza di s2 in s1; oppure, -1 se non c'è alcuna occorrenza
    :rtype: int
    """

    indice = 0
    trovato = False
    while not trovato and indice <= len(s1) - len(s2):
        if s1.startswith(s2, indice):
            trovato = True
        else:
            indice += 1

    if trovato:
        return indice
    else:
        return -1


def ultima_occorrenza(s1, s2):
    """
    Trova la prima occorrenza della stringa s2 all'interno della stringa s1

    :param s1: stringa nella quale effettuare la ricerca
    :type s1: str
    :param s2: stringa da cercare
    :type s2: str
    :return l'indice della prima occorrenza di s2 in s1; oppure, -1 se non c'è alcuna occorrenza
    :rtype: int
    """

    indice = len(s1) - len(s2)
    trovato = False
    while not trovato and indice >= 0:
        if s1.startswith(s2, indice):
            trovato = True
        else:
            indice -= 1

    if trovato:
        return indice
    else:
        return -1


def controlla_tutti_caratteri(s1, s2):
    """
    Controlla che tutti i caratteri in s1 occorrano in s2 e che s1 abbia almeno un carattere
    :param s1: stringa in cui effettuare il controllo
    :type s1: str
    :param s2: stringa che definisce tutti e soli i caratteri ammessi
    :type s2: str
    :return: `True` se e solo se tutti i caratteri in s1 occorrono in s2 e s1 ha almeno lunghezza 1
    :rtype: bool
    """

    soddisfa_condizione = len(s1) > 0
    indice = 0
    while soddisfa_condizione and indice < len(s1):
        carattere = s1[indice]
        if carattere not in s2:
            soddisfa_condizione = False
        indice += 1

    return soddisfa_condizione

