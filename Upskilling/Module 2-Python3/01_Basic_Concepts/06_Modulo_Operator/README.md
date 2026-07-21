# Exercise 6 - Modulo Operator

## Objective
Use the modulo operator with a function, validation, and clean output.

## Task
Check whether a number is even or odd using the modulo (`%`) operator.

## Instructions
- Use a function.
- Validate the number.
- Compute the remainder.
- Print "Even" or "Odd".
- Use the variable `number = 17`.

## Project Structure

- `Exercise_06.py` - Python source code
- `06_output.png` - Output screenshot

## Code

```python
def check(number):
    if not isinstance(number, int):
        print("Input must be an integer.")
        return
    
    if number%2==0:
        print(f"Number: {number}")
        print("Result: Even")
    else:
        print(f"Number: {number}")
        print("Result: Odd")

number = 17
check(number)
```

## Expected Output

```
Number: 17
Result: Odd
```