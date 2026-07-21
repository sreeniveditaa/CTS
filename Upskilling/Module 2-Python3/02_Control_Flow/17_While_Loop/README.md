# Exercise 17 - While Loop

## Objective
Use a condition-based loop with validation, a function, and formatted output.

## Task
Count down from 5 to 1 using a `while` loop.

## Instructions
- Use a function.
- Validate the count value.
- Use `while count > 0:`.
- Print the count at each step.
- Decrease the count using `count -= 1`.

## Project Structure

- `Exercise_17.py` - Python source code
- `17_output.png` - Program output screenshot

## Code

```python
def countdown(count):
    if not isinstance(count, int):
        print("Count must be an integer.")
        return

    if count<=0:
        print("Count must be greater than 0.")
        return

    print("Countdown:")

    while count > 0:
        print(count)
        count -= 1


count = 5

countdown(count)
```

## Expected Output

```
Countdown:
5
4
3
2
1
```