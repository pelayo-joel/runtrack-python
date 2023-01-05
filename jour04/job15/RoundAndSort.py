def LengthOf(newList):
    length = 0
    for content in newList:
        length += 1
    return length

def Quicksort(newList):
    i = 0
    while i < LengthOf(newList):
        j = 0
        while j < LengthOf(newList):
            if newList[i] < newList[j]:
                tmp = newList[i]
                newList[i] = newList[j]
                newList[j] = tmp
            j += 1
        i += 1
    return newList



def RoundThenSort(newList):
    i = 0
    while i < LengthOf(newList):
        newList[i] = int(newList[i])
        i += 1
    return Quicksort(newList)

myList = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(RoundThenSort(myList))