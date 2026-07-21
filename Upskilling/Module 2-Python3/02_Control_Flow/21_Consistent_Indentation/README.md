# Exercise 21 - Consistent Indentation

## Objective
Demonstrate clean, consistent indentation using a nested `if` statement inside a function.

## Task
Print `"Nested"` when both conditions are `True`.

## Instructions
- Use a function.
- Apply exactly 4 spaces per indentation level.
- Use nested `if` statements.
- Print `"Nested"`.
- Print a confirmation message.

## Project Structure

- `Exercise_21.py` - Python source code
- `21_output.png` - Program output screenshot

## Code

```python
def check_conditions(condition1, condition2):
    if condition1:
        if condition2:
            print("Nested")

    print("Indentation applied successfully.")

condition1 = True
condition2 = True

check_conditions(condition1, condition2)
```

## Expected Output

```
Nested
Indentation applied successfully.
```