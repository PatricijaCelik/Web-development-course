number1 = int(input("Enter first number: "))
operation = input("Enter an arithmetic operation: ")
number2 = int(input("Enter second number: "))

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("You did not enter the correct arithmetic operation.")
