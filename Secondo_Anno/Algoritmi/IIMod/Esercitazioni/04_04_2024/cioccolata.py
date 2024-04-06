def cioccolata(G, L):
    # G è una lista, nella quale, in ciascuna posizione i = 0, 1, ..., L + 1, G[i] è il profitto per un pezzo di cioccolata lungo i.
    L += 1
    OPT = [0] * L

    for j in range(1, L):
        max = 0
        for k in range(j):
            mk = G[j - k] + OPT[k]
            if max < mk:
                max = mk
        OPT[j] = max
    print(OPT)
    return OPT[L - 1]


G = [0, 6, 10, 20, 21, 25, 27, 30]

k = cioccolata(G, 7)
print(k)
