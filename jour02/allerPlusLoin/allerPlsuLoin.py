import math

def Triangle(a, b, c):
    if (a + b >= c) and (a + c >= b) and (c + b >= a):
        #Triangle equilateral
        if a == b == c:
            return "Triangle equilateral"

        #Triangle isoceles
        elif (a == b != c) or (a == c != b) or (c == b != a):
            #Triangle isoceles et rectangle
            if (int(math.sqrt(a*a)) == int(math.sqrt(b*b + c*c))) or (int(math.sqrt(c*c)) == int(math.sqrt(b*b + a*a))) or int(math.sqrt((b*b)) == int(math.sqrt(a*a + c*c))):
                return "Triangle isoceles et rectangle"
            else:
                return "Triangle isoceles"
        
        #Triangle rectangle
        elif (a*a == b*b + c*c) or (c*c == b*b + a*a) or (b*b == a*a + c*c):
            return "Triangle rectangle"
            
        else:
            return "Triangle quelconque"
    else:
        return "Not a triangle"

print(Triangle(int(input()), int(input()), int(input())))