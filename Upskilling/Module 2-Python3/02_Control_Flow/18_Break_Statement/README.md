# Exercise 18 - Break Statement

## Objective
Use a break statement to exit a loop early with a function, validation, and clean output.

## Task
Find and print the first even number in a given range.

## Instructions
- Use a function.
- Validate the range size.
- Loop with `for i in range(...)`.
- Use the modulo (`%`) operator to check if a number is even.
- Use `break` once the first even number is found.

## Project Structure

- `Exercise_18.py` - Python source code
- `18_output.png` - Program output screenshot

## Code

```python
def find_first_even(range_size):
    if not isinstance(range_size, int):
        print("Range size must be an integer.")
        return

    if range_size <= 0:
        print("Range size must be greater than 0.")
        return

    for i in range(range_size):
        if i % 2 == 0:
            print(f"First Even Number: {i}")
            break

range_size = 10

find_first_even(range_size)
```

## Expected Output

```
First Even Number: 0
```