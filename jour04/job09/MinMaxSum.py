def MinMaxSum(newList):
    listMin = newList[0]
    listMax = newList[0]
    for i in range(0, len(newList)):
        if listMin > newList[i]:
            listMin = newList[i]
        if listMax < newList[i]:
            listMax = newList[i]
    print(listMin, listMax)
    return listMin + listMax


L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print(MinMaxSum(L))