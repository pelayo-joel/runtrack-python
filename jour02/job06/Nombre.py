def nombre(num):
    if num < 0:
        return "negatif"
    elif num > 0:
        return "positif"
    else:
        return "null"

myNum = int(input("I'll determine if it's positive or negative : ")) 
print(nombre(myNum))