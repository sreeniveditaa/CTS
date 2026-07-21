# Exercise 19 - Continue Statement

## Objective
Use the `continue` statement to skip even numbers with a function, validation, and formatted output.

## Task
Sum only the odd numbers in a given range.

## Instructions
- Use a function.
- Validate the range.
- Loop with `range(10)`.
- Skip even numbers using `continue`.
- Accumulate only odd numbers.

## Project Structure

- `Exercise_19.py` - Python source code
- `19_output.png` - Program output screenshot

## Code

```python
def sum_odd_numbers(range_size):
    if not isinstance(range_size, int):
        print("Error: Range size must be an integer.")
        return

    if range_size <= 0:
        print("Error: Range size must be greater than 0.")
        return

    total = 0

    for i in range(range_size):
        if i % 2 == 0:
            continue

        total += i

    print(f"Sum of Odd Numbers: {total}")

range_size = 10
sum_odd_numbers(range_size)
```

## Expected Output

```
Sum of Odd Numbers: 25
```