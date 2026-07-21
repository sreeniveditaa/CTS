# Exercise 26 - Multiple Parameters

## Objective
Handle multiple arguments in a function with validation and formatted output.

## Task
Calculate the area of a rectangle using length and width.

## Instructions
- Use a function that accepts two arguments.
- Validate the numbers.
- Calculate and return the area.
- Print `area(5, 3)`.

## Project Structure

- `Exercise_26.py` - Python source code
- `26_output.png` - Program output screenshot

## Code

```python
def area_rectangle(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        print("Error: Inputs must be numbers.")
        return None

    if length <= 0 or width <= 0:
        print("Error: Length and width must be greater than 0.")
        return None

    return length*width


result=area_rectangle(5, 3)

if result is not None:
    print(f"Area: {result}")
```

## Expected Output

```
Area: 15
```