def CaesarCipher(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    deciphered = ""

    i = 0
    while i < len(message):
        j = 0
        while j < len(alphabet):
            if message[i].lower() == alphabet[j]:
                deciphered += alphabet[(j+3) % len(alphabet)]
            j += 1
        i += 1

    return deciphered

myMessage = "MyCipher"
print(CaesarCipher(myMessage))