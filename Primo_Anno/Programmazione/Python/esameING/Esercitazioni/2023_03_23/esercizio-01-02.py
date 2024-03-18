m = int(input("Inserire il numero di file: "))
n = int(input("Inserire il numero di mele in ciascuna fila: "))
mele_totali = int(input("Inserire il numero di mele totale: "))

capienza_cassetta = m * n
cassette_riempite = mele_totali // capienza_cassetta
print("Cassette riempite:", cassette_riempite)
