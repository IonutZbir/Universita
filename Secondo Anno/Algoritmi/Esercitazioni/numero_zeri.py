def n_zeri(arr):
    i = 0
    j = len(arr) - 1
    z = 0
    u = 0
    while i <= j:
        if arr[i] == 0:
            z += 1
        if arr[j] == 1:
            u += 1
        print(f"i: {i}, j: {j}, z: {z}, u: {u}")
        i += 1
        j -= 1
    
    if z == u:
        return i - 1
    return -1

a = [1, 1, 0, 0, 0, 1, 1, 1]
print(n_zeri(a))
