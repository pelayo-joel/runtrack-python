import random

def L5(newList):
    print(newList[1])
    newList[3] = newList[3-1] + newList[3+1]
    print(newList[len(newList)-1])

L = []
for i in range(5):
    L.append(random.randint(0, 10))

print(L)
L5(L)