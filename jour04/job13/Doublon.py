def Doublon(newList):
    length = 0
    i = 0
    for content in newList:
        length += 1

    while i < length:
        j = i + 1
        while j < length:
            if newList[j] == newList[i]:
                del newList[j]
                length -= 1
                break
            j += 1
        i += 1
    return newList

myList = [10,20,30,20,10,50,60,40,80,50,40]
print(myList)
print(Doublon(myList))