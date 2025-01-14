class Sensore:
    def __init__(self, misurazione, categoria):
        self.misurazione = misurazione
        self.categoria = categoria

s1 = Sensore(23.4, "temp")
s2 = Sensore(26.4, "temp")
s3 = Sensore(8, "umd")

sensori = {s1, s2, s3}


def maxMisurazione(categoria):
    # Prima fase: creo un dizionario del tipo: {"temp": [s1, s2], "umd": [s3]}
    categorie = {}
    for s in sensori:
        cat = s.categoria
        if cat in categorie:
            categorie[cat].append(s)
        else:
            categorie[cat] = [s]
    
    #  Seconda fase: calcolo la massima misurazione di una categoria
    categoriaDaMisurare = categorie[categoria]
    m = 0
    for sensore in categoriaDaMisurare:
        if sensore.misurazione > m:
            m = sensore.misurazione
    return m

print(maxMisurazione("temp"))

       
    