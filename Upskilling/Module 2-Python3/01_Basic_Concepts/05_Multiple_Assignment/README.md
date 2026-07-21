# Exercise 5 - Multiple Assignment

## Objective
Use multiple assignment with basic validation, functions, and formatted output.

## Task
Unpack `(x, y)` coordinates and display them.

## Instructions
- Use a function.
- Validate the coordinates.
- Use multiple assignment.
- Print the coordinates.

## Project Structure

- `Exercise_05.py` - Python source code
- `05_output.png` - Output screenshot

## Code

```python
def display(coordinates):
    
    if not isinstance(coordinates, tuple):
        print("Coordinates must be a tuple.")
        return

    if len(coordinates) != 2:
        print("Coordinates must contain exactly two values.")
        return

    x, y = coordinates

    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")

coordinates = (10, 20)

display(coordinates)
```

## Expected Output

```
X Coordinate: 10
Y Coordinate: 20
```