from random import randint

def Swap(newList):
    tmp = newList[0]
    newList[0] = newList[len(newList)-1]
    newList[len(newList)-1] = tmp
    return newList

myList = []
for i in range(randint(0, 10)):
    myList.append(randint(0, 10))

print(myList)
print(Swap(myList))