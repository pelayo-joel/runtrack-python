def SumOfTimes2(newList):
    sum2 = 0
    for i in range(0, len(newList)):
        if newList[i] % 2 == 0:
            sum2 += newList[i]
    return sum2

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
print(SumOfTimes2(L))