def nWord(n, sentence):#nword :)
    newSentence = ""
    length = 0
    i = 0
    for content in sentence:
        length += 1

    count = 0
    pointer = 0
    while i < length:
        if count <= n+1 and sentence[i] == " ":
            pointer = i
            count = 0
        elif sentence[i] == " ":
            newSentence = newSentence + sentence[pointer:i]
            pointer = i
            count = 0
        elif i == length-1:
            newSentence = newSentence + sentence[pointer:length]
        count += 1
        i += 1
    return newSentence

print(nWord(3, " La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"))