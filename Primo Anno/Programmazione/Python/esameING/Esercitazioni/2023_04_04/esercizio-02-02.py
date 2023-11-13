targa = input("Inserire targa: ")

if len(targa) != 7:      # Se non è formata da 7 caratteri, una targa non è valida
    valida = False
else:                    # Altrimenti, scompongo la targa nelle sue 3 parti e le valido
    prima_parte = targa[:2]     # Primi due caratteri
    seconda_parte = targa[2:5]  # Successivo gruppo di 3 caratteri
    terza_parte = targa[5:]     # Ultimo gruppo (di 2 caratteri)

    # valido la prima parte
    prima_parte_valida = (prima_parte.isupper() and
                          prima_parte.isalpha() and
                          prima_parte.isascii())

    # valido la seconda parte
    seconda_parte_valida = seconda_parte.isdigit()
    
    # valido la terza parte
    terza_parte_valida = (terza_parte.isupper() and
                          terza_parte.isalpha() and
                          terza_parte.isascii())

    valida = prima_parte_valida and seconda_parte_valida and terza_parte_valida

if valida:
    print("Targa valida")
else:
    print("Targa non valida")
