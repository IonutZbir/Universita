numero_tazzine = int(input("Inserire numero di tazzine di caffè: "))
numero_brioche = int(input("Inserire numero brioche: "))

numero_clienti_servibili = max(numero_tazzine, numero_brioche)

print("Numero massimo di clienti che si possono servire:", numero_clienti_servibili)
