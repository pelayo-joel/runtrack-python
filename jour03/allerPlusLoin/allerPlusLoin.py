def Palindrome(toReverse):
    n = len(toReverse) - 1
    reversed = ""
    while n >= 0:
        reversed += toReverse[n]
        n -= 1
    
    print(reversed)

Palindrome("nikana")