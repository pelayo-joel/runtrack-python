def DiagonalInRectangle():
    height = int(input("Height : ")) + 1
    width = height

    i = 0
    diagonal = width - 1
    while i < height:
        j = 0
        while j < width:
            if (j == width-1 and i == height-1) or (j == width-1 and i == 0):
                print("+")
            elif (j == 0 and i == 0) or (j == 0 and i == height-1):
                print("+", end="")
            elif j == 0:
                print("|", end = "")
            elif j == width-1:
                print("|")
            elif j == diagonal:
                print(" ", end="")
            elif i == 0 or i == height-1:
                print("-", end = "")
            else:
                print("#", end = "")
            j += 1
        if i != 0 or i != height-1:
            diagonal -= 1
        i += 1

DiagonalInRectangle()