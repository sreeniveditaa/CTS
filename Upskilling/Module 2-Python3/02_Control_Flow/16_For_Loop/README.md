# Exercise 16 - For Loop Basics

## Objective
Iterate a fixed number of times with a function, validation, and formatted output.

## Task
Print numbers from 1 to 5 using `range()`.

## Instructions
- Use a function.
- Validate the loop count.
- Use `for i in range(5)`.
- Print numbers `1` to `5`.

## Project Structure

- `Exercise_16.py` - Python source code
- `16_output.png` - Program output screenshot

## Code

```python
def print_numbers(count):
    if not isinstance(count, int):
        print("Error: Count must be an integer.")
        return

    if count <= 0:
        print("Error: Count must be greater than 0.")
        return

    print("Numbers from 1 to 5:")

    for i in range(5):
        print(i + 1)


count = 5

print_numbers(count)
```

## Expected Output

```
Numbers from 1 to 5:
1
2
3
4
5
```