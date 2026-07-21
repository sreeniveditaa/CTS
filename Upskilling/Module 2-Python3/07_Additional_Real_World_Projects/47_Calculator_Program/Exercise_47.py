def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operation (+, -, *, /): ")

    result = calculate(num1, num2, operator)

    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid numeric values.")