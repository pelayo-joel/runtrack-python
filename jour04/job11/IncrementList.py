def IncrementList(newList):
    for i in range(0, len(newList)):
        newList[i] += 1
    return newList

L = [7, 11, 42, 39, 2]
print(L)
print(IncrementList(L))