def Length100():
    n = 0
    while n <= 100:
        if n == 26 or n == 37 or n == 88:
            n += 1
            continue
        print(n)
        n += 1
    
Length100()