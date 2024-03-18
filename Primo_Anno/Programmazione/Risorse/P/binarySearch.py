def binarySearch(value, givenList):
    halfList = len(givenList) // 2
    if len(givenList) == 0:
        return False
    if value == givenList[halfList]:
        return True
    elif value < givenList[halfList]:
        newList = givenList[:halfList]
        return binarySearch(value, newList)
    else:
        newList = givenList[halfList + 1:]
        return binarySearch(value, newList)
        
        
def binarySearchNonRecursive(value, givenList):
    if len(givenList) == 0:
        return False
    start = 0
    end = len(givenList) - 1
    while start <= end:
        mid = (start + end) // 2
        if value == givenList[mid]:
            return True
        elif value > givenList[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binarySearchNonRecursive(13, lista))