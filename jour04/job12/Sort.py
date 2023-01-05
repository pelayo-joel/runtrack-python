from random import randint
#randint is only used to generate our lists randomly, it is not used for anything else than that

def LengthOf(newList):
    length = 0
    for content in newList:
        length += 1
    return length

#Quicksort algorithm
"""The most basic one where you simply check while going through your list if there is any number in the list that is inferior and swap it with yourself
Depending on the length of the list, this algorithm might not be the most efficient if not the least (O(n^2)), still very efficient for short lists)"""
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
    
#Bubble sort algorithm
""":D"""
def BubbleSort(newList):
    i = 1

    while i < LengthOf(newList):
        j = 0
        while j < LengthOf(newList):
            
            j += 1
        i += 1
    return None

#Merge sort algorithm
"""The idea here is to split the list until we're left with a list of length 2 which makes the sorting task pretty easy, then we merge them back together, hence the name
This algorithm is pretty efficient when it's dealing with very large lists (O(n*log n)), not so efficient for short lists)"""
def MergeSort(newList):
    length = LengthOf(newList)
    if length < 2:
        return newList

    sortedList = []
    splitPoint = int(length / 2)
    rightSide = MergeSort(newList[splitPoint:])
    leftSide = MergeSort(newList[:splitPoint])

    i, j= 0, 0
    while i < LengthOf(leftSide) and j < LengthOf(rightSide):
        if leftSide[i] < rightSide[j]:
            sortedList += [leftSide[i]]
            i += 1
        else:
            sortedList += [rightSide[j]]
            j += 1

    while i < LengthOf(leftSide):
        sortedList += [leftSide[i]]
        i += 1
    while j < LengthOf(rightSide):
        sortedList += [rightSide[j]]
        j += 1

    return sortedList


#Generate random lists to sort
mySmallList = []
i, j, k = 0, 0, 0
while i < randint(0, 10):
    mySmallList += [randint(0, 10)]
    i += 1

myMediumList = []
while j < randint(20, 50):
    myMediumList += [randint(0, 50)]
    j += 1

myLargeList = []
while k < randint(50, 100):
    myLargeList += [randint(0, 100)]
    k += 1

#Compare generated list with sorted one using different algorithms
print(f"Small list : {mySmallList}\nQuicksort algorithm : {Quicksort(mySmallList)}\n")
print(f"Medium list : {myMediumList}\nBubble Sort algorithm : {BubbleSort(myMediumList)}\n")
print(f"Large list : {myLargeList}\nMerge Sort algorithm : {MergeSort(myLargeList)}")