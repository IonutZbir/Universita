numero_telai = int(input("Inserire numero telai: "))
numero_ruote = int(input("Inserire numero ruote: "))

numero_biciclette = min(numero_telai, numero_ruote // 2)

print("Biciclette assemblabili:", numero_biciclette)
