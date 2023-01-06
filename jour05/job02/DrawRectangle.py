def DrawRectangle():
    width = int(input("Width : "))
    height = int(input("Height : "))

    i = 0
    while i < height:
        j = 0
        while j < width:
            if j == 0:
                print("|", end = "")
            elif j == width-1:
                print("|")
            elif i == 0 or i == height-1:
                print("-", end = "")
            else:
                print(" ", end = "")
            j += 1
        i += 1

DrawRectangle()
