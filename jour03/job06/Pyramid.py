def AlphabeticalPyramid(alphabet):
    n = 0
    while n <= len(alphabet):
        print(alphabet[:n])
        n += 1
        alphabet = alphabet[n-1:]
    
alphabetPy = "abcdefghijklmnopqrstuvwxyz"
AlphabeticalPyramid(alphabetPy * 10)


#######---------Previous version---------#######

#def AlphabeticalPyramid():
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    n = 0
#    while n <= len(alphabet):
#        print(alphabet[:n])
#        n += 1
