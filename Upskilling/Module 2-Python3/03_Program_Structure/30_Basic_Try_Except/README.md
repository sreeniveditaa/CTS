# Exercise 30 - Basic Try-Except

## Objective
Catch simple runtime errors using `try-except` with a function and clear output.

## Task
Safely divide two numbers and handle division-by-zero errors.

## Instructions
- Use a function.
- Use `try-except`.
- Handle `ZeroDivisionError`.
- Print result or error message.

## Project Structure

- `Exercise_30.py` - Python source code
- `30_output.png` - Program output screenshot

## Code

```python
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

a = 10
b = 0
safe_divide(a, b)
```

## Expected Output

```
Error: Cannot divide by zero
```