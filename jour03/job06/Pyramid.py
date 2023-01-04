def AlphabeticalPyramid():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    n = 0
    while n <= len(alphabet):
        print(alphabet[:n])
        n += 1
    
AlphabeticalPyramid()