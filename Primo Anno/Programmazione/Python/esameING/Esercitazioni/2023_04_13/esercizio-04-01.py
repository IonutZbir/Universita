def numero_romano(numero):
    """
    Restituisce la rappresentazione di un numero intero positivo secondo la numerazione romana

    :param numero: numero da convertire
    :type numero: int
    :return: la rappresentazione del numero nella rappresentazione romana
    :rtype str
    """
    unita = numero % 10
    decine = (numero // 10) % 10
    centinaia = (numero // 100) % 10
    migliaia = numero // 1000

    return "M" * migliaia + cifra_romana(centinaia, "C", "D", "M") + cifra_romana(decine, "X", "L", "C") + cifra_romana(unita, "I", "V", "X")


def cifra_romana(n, simbolo_uno, simbolo_cinque, simbolo_dieci):
    """
    Restituisce la rappresentazione di una cifra (i.e. un numero non negativo strettamente minore di 10) nella numerazione
    romana

    :param n: cifra da convertire
    :type n: int
    :param simbolo_uno: cifra romana per l'unità
    :type simbolo_uno: str
    :param simbolo_cinque: cifra romana per il cinque
    :type simbolo_cinque: str
    :param simbolo_dieci: cifra romana per il dieci
    :type simbolo_dieci: str
    :return:
    :rtype str
    """
    risultato = ""

    if n < 4:
        risultato = simbolo_uno * n
    elif n == 4:
        risultato = simbolo_uno + simbolo_cinque
    elif n < 9:
        risultato = simbolo_cinque + (simbolo_uno * (n - 5))
    else:
        risultato = simbolo_uno + simbolo_dieci

    return risultato


def leggi_intero_compreso_tra(minimo, massimo):
    """
    Legge un numero intero compreso tra `min` e `max`.

    :param minimo: valore minimo accettabile
    :param massimo: valore massimo accettabile
    :return: il valore letto
    """
    input_valido = False
    while not input_valido:
        numero = int(input("Inserisci un intero tra %d e %d: " % (minimo, massimo)))
        if numero < minimo or numero > massimo:
            print("Errore: il numero inserito è fuori dall'intervallo consentito")
        else:
            input_valido = True
    return numero


def main():
    numero = leggi_intero_compreso_tra(1, 3999)
    print(numero_romano(numero))


main()
