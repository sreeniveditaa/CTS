# Exercise 23 - Import Standard Module

## Objective
Use the `math` module inside a function with validation and formatted output.

## Task
Calculate the area of a circle using `math.pi` and a given radius.

## Instructions
- Import the `math` module.
- Use a function.
- Validate the radius.
- Use formula: `area = math.pi × radius²`.
- Print area with 2 decimal places.

## Project Structure

- `Exercise_23.py` - Python source code
- `23_output.png` - Program output screenshot

## Code

```python
import math

def circle_area(radius):
    if not isinstance(radius, (int, float)):
        print("Error: Radius must be a number.")
        return

    if radius<=0:
        print("Error: Radius must be greater than 0.")
        return

    area=math.pi*radius**2
    print(f"Area of Circle: {area:.2f}")

radius = 7
circle_area(radius)
```

## Expected Output

```
Area of Circle: 153.94
```