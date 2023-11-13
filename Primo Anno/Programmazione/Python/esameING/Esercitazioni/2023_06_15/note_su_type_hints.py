class Animale:
    pass

# I due punti dopo i parametri e la freccia (->) dopo
# la lista dei parametri introducono rispettivamente
# un type hint per ciascun parametro e per il valore
# di ritorno

# È anche possibile annotare variabili locali ai metodi

# ...e molto altro ancora

def fun(a: int,
        b: float,
        c: str,
        d: list[str],
        e: tuple[int, float, str],
        f: tuple[str, list[tuple[int, int]]],
        g: Animale) -> str:
    return "Ciao"

# Il type hint può servirvi quando il tipo di una variabile
# non viene inferito da PyCharm e, di conseguenza, non viene
# è possibile fare autocompletamento.