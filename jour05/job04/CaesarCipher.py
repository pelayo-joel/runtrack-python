def CaesarCipherSpeUp(message, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    speChar = "êéèàçùëûôöâä!@#$%^^&*()_-=+{]}[':;/?.>,<\|1234567890"
    deciphered = ""
    beUp = 1
    beSpe = 2

    i = 0
    while i < len(message):
        j = 0
        while j < len(alphabet):
            if message[i].lower() == alphabet[j]:
                deciphered += alphabet[(j+n) % len(alphabet)]
            if message[i].lower() == alphabet[j] and i == beUp:
                deciphered += alphabet[(j+n+2) % len(alphabet)].upper()
                beUp += 2
            if message[i].lower() == alphabet[j] and i == beSpe:
                deciphered += speChar[(j+n+3) % len(speChar)]
                beSpe += 2
            j += 1
        i += 1

    return deciphered

def CaesarCipher(message, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    deciphered = ""

    i = 0
    while i < len(message):
        j = 0
        while j < len(alphabet):
            if message[i].lower() == alphabet[j]:
                deciphered += alphabet[(j+n) % len(alphabet)]
            j += 1
        i += 1

    return deciphered

myMessage = input("Your message : ")
mySubKey = int(input("Your sub-key : "))
print(f"With fixed key (all lowercase) : {CaesarCipher(myMessage, mySubKey)}")
print(f"Fixed (with seemingly random uppercase/special char) : {CaesarCipherSpeUp(myMessage, mySubKey)}")