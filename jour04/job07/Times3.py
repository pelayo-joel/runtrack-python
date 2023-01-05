def Times3(newList):
    count3 = 0
    for i in range(0, len(newList)):
        if newList[i] % 3 == 0:
            count3 += 1
    return count3

L = [8, 24,48,2,16]
print(Times3(L))