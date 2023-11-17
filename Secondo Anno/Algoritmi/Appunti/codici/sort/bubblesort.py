def bubbleSort(a):
    for i in range(len(a) - 1):
        j = 0
        while j < len(a) - 1 - i:
            if a[j] > a[j+1]:
                x = a[j]
                a[j] = a[j+1]
                a[j+1] = x
            j += 1
    return a

def bubbleSort2(a):
    for i in range(len(a) - 1):
        j = 0
        while j < len(a) - 1 - i:
            if a[j] > a[j+1]:
                x = a[j]
                a[j] = a[j+1]
                a[j+1] = x
            j += 1
    return a
a = [3, 2, 5, 4 ,1]

print(bubbleSort(a))
