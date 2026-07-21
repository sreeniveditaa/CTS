# Exercise 24 - All Import

## Objective
Use `from module import *` along with simple utility usage inside a function.

## Task
Import everything from a standard module and use a few functions.

## Instructions
- Use `from math import *`.
- Use a function.
- Validate input.
- Demonstrate usage of `sqrt`, `pow`, and `pi`.
- Print results.

## Project Structure

- `Exercise_24.py` - Python source code
- `24_output.png` - Program output screenshot

## Code

```python
from math import *
def math_operations(value):
    if not isinstance(value, (int, float)):
        print("Input must be a number.")
        return

    if value <= 0:
        print("Value must be greater than 0.")
        return

    square_root = sqrt(value)
    power_value = pow(value, 2)

    print(f"Value: {value}")
    print(f"Square Root: {square_root:.2f}")
    print(f"Power (square): {power_value}")
    print(f"Pi Value: {pi:.5f}")

value = 16
math_operations(value)
```

## Expected Output

```
Value: 16
Square Root: 4.00
Power (square): 256
Pi Value: 3.14159
```