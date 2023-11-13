# Questa soluzione mostra come usando i cicli sia possibile
# gestire una piramide di altezza qualsiasi

altezza_piramide = int(input("Altezza della piramide: "))
immagine = ""
i = 0
while i < altezza_piramide:
    immagine += " " * (altezza_piramide - i - 1) + \
                "*" * (2 * i + 1) + \
                " " * (altezza_piramide - i - 1) + \
                "\n"
    i += 1

print(immagine)
