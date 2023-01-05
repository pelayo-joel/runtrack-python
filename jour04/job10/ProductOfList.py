def ProductOfList(newList):
    product = 1
    for i in range(0, len(newList)):
        if newList[i] >= 25 and newList[i] <= 90:
            product *= newList[i]
    return product

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(ProductOfList(L))