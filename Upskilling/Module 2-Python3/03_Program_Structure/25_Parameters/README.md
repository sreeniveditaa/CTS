# Exercise 25 - Parameters

## Objective
Pass arguments into a function with validation and structured output.

## Task
Create a function that adds two numbers and prints the result.

## Instructions
- Use a function with parameters.
- Validate inputs.
- Return the sum.
- Print the result of `add(5, 3)`.

## Project Structure

- `Exercise_25.py` - Python source code
- `25_output.png` - Program output screenshot

## Code

```python
def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Inputs must be numbers.")
        return

    return a+b

result=add_numbers(5, 3)
print(f"Sum: {result}")
```

## Expected Output

```
Sum: 8
```