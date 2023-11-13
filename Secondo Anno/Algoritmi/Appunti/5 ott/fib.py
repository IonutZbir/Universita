def fib2(n):
    if n<= 2:
        return 1
    return fib2(n-1) + fib2(n-2)

def fib3(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]

def fib4(n):
    a,b,c = 1, 1,1
    for i in range(2, n):
        c = a + b
        b = a
        a = c
    return c

def fib5(n):
    m = [[1, 0], [0, 1]]
    for i in range(1, n):
        m = matrixProduct(m, [[1,1],[1,0]])
    return m[0][0]

def fib6(n):
    a = [[1, 1], [1, 0]]
    m = matrixPower(a, n-1)
    return m[0][0]

def matrixProduct(m1, m2):
    # 2x2 matrix
    m = [[0, 0], [0, 0]]
    for i in range(2): # 16 operazione
        for j in range(2):
            for k in range(2):
                m[i][j] += m1[i][k] * m2[k][j]
    return m

def matrixPower(a, k):
    if k == 0:
        return [[1, 0], [0, 1]]
    else: 
        m = matrixPower(a, int(k/2))
        m = matrixProduct(m ,m)
    if k % 2 != 0:
        m = matrixProduct(m, a)
    return m