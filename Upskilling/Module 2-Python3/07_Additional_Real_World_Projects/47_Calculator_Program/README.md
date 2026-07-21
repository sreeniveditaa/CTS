# Exercise 47 - Complete Calculator Program

## Objective

Combine input, functions, and error handling.

## Task

Build a robust calculator that supports addition, subtraction, multiplication, and division.

## Instructions

- Create a function `calculate(a, b, op)` handling `+`, `-`, `*`, `/`.
- Use `input()` for numbers and operation.
- Handle `ZeroDivisionError`.
- Display the result neatly.

## Project Structure

- `Exercise_47.py` - Python source code
- `47_output.png` - Program output screenshot

## Code

```python
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
```

## Sample Output

```
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): +
Result: 15.0
```