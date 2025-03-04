import math


lastNum: float
num1: float
num2: float
res: float

op: str = ""
operations: int = 0

VALID_OPERATIONS = ["+", "-", "*", "/", "^"]

def getOperation(number1: float, operator: str, number2: float) -> float:
    if operator not in VALID_OPERATIONS:
        return
    
    match operator:
        case "+":
            return addition(number1, number2)
        case "-":
            return subtraction(number1, number2)
        case "*":
            return multiplication(number1, number2)
        case "/":
            return division(number1, number2)
        case "^":
            return exponent(number1, number2)

def addition(*nums: tuple[float]) -> float:
    total = 0
    for num in nums:
        total += num
    return total

def subtraction(base: float, subtractant: float) -> float:
    return base - subtractant

def multiplication(base: float, power: float) -> float:
    return base * power


def division(numerator: float, denominator: float) -> float:
    value: float
    try:
        value = numerator / denominator
    except ZeroDivisionError:
        print("Division by zero error, returning zero")
        return 0
    return value

def exponent(base: float, power: float) -> float:
    return math.pow(base, power)

print("Welcome to the Python Calculator.")
print("What would you like to calculate?")
while True:
    useLastResult = False
    if operations > 0:
        useLastResult = input("Use last result as first number? y/n: ").lower().strip()
        if useLastResult == "y":
            useLastResult = True
        else:
            useLastResult = False
    
    if not useLastResult:
        while True:
            try:
                num1 = float(input("Enter a number: "))
                break
            except ValueError:
                pass
            print("Invalid input, ", end="")
    else:
        num1 = lastNum
    
    op = input("Enter an operation: ")
    while op not in VALID_OPERATIONS:
        print("Not a valid operation, valid operations are (+, -, *, /, ^)")
        op = input("Enter an operation:")
    
    while True:
        try:
            num2 = float(input("Enter a second number: "))
            break
        except ValueError:
            pass
        print("Invalid input, ", end="")

    res = getOperation(num1, op, num2)
    lastNum = res
    operations += 1
    print("Result:", res, "\n")
