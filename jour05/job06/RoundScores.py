from random import randint

def RoundScores(newList):
    i = 0
    while i < len(newList):
        if newList[i] < (5 * round(newList[i]/5)):
            newList[i] = (5 * round(newList[i]/5))
        i += 1

    return newList
            

scoreList = []
i = 0
while i < randint(10, 100):
    scoreList += [randint(0, 100)]
    i += 1

print(scoreList)
print(RoundScores(scoreList))

