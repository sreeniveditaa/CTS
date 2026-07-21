# Exercise 35 - Create Tuple

## Objective
Use an immutable tuple with a function and basic validation.

## Task
Store fixed coordinates and display them.

## Instructions
- Use a tuple.
- Use a function.
- Validate coordinate values.
- Print coordinates in a readable format.

## Project Structure

- `Exercise_35.py` - Python source code
- `35_output.png` - Program output screenshot

## Code

```python
def display_coordinates(coordinates):
    if not isinstance(coordinates, tuple):
        print("Error: Coordinates must be a tuple.")
        return

    if len(coordinates) != 2:
        print("Error: Coordinates must contain exactly two values.")
        return

    x, y = coordinates
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Error: Coordinate values must be numeric.")
        return

    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")

coordinates = (15, 30)
display_coordinates(coordinates)
```

## Expected Output

```
X Coordinate: 15
Y Coordinate: 30
```