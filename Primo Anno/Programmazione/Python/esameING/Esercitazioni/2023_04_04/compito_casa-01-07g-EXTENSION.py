# Questa soluzione mostra come usando i cicli sia possibile
# gestire una piramide di altezza qualsiasi

altezza_piramide = int(input("Altezza della piramide: "))
base_piramide = (altezza_piramide - 1) * 2 + 1
immagine = ""
i = 0
while i < altezza_piramide:
    immagine += ("*" * (2 * i + 1)).center(base_piramide, " ") + "\n"
    i += 1

print(immagine)
