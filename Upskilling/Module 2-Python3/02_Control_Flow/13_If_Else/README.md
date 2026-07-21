# Exercise 13 - If-Else

## Objective
Use a two-way decision with functions, validation, and formatted output.

## Task
Check whether a number is even or odd.

## Instructions
- Use a function.
- Validate the input.
- Use the variable `num = 8`.
- Print `Even` or `Odd`.

## Project Structure

- `Exercise_13.py` - Python source code
- `13_output.png` - Program output screenshot

## Code

```python
def check_even_odd(num):
    if not isinstance(num, int):
        print("Error: Input must be an integer.")
        return

    if num%2==0:
        print(f"Number: {num}")
        print("Result: Even")
    else:
        print(f"Number: {num}")
        print("Result: Odd")

num = 8

check_even_odd(num)
```

## Expected Output

```
Number: 8
Result: Even
```