# Exercise 12 - Simple If

## Objective
Use a basic conditional with a function, validation, and user interaction.

## Task
Check whether a student passes based on their marks.

## Instructions
- Use a function.
- Validate marks.
- Use the variable `marks = 75`.
- Print `Pass` or `Fail`.

## Project Structure

- `Exercise_12.py` - Python source code
- `12_output.png` - Program output screenshot

## Code

```python
def check_result(marks):
    if not isinstance(marks, (int, float)):
        print("Error: Marks must be a number.")
        return

    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100.")
        return

    if marks >= 50:
        print(f"Marks: {marks}")
        print("Result: Pass")
    else:
        print(f"Marks: {marks}")
        print("Result: Fail")

marks = 75

check_result(marks)
```

## Expected Output

```
Marks: 75
Result: Pass
```