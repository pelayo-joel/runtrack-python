def PasCompris(rndWord):
    forbiddenChar = "êéèàçùëûôöâä!@#$%^^&*()_-=+{]}[':;/?.>,<\|1234567890"
    newWord = [*rndWord]

    i = 0
    while i < len(rndWord):
        j = len(rndWord) - 1
        if rndWord[i] == " " or rndWord[i] in forbiddenChar or rndWord[i].isupper():
            return print("Invalid character : only lowercase characters are accepted")
        while j > 0 and newWord[j] > newWord[j - 1]:
            tmp = newWord[j]
            newWord[j] = newWord[j-1]
            newWord[j-1] = tmp
            break
        i += 1

    return "".join(newWord)

myWord = "abcde"
print(PasCompris(myWord))