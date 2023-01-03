def calcule(num1, num2, operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2
        case _:
            return "Invalid operator"

myNum1 = int(input("First integer : "))
myNum2 = int(input("Second integer : "))
myOperator = input("Operator : ")

print(calcule(myNum1, myNum2, myOperator))