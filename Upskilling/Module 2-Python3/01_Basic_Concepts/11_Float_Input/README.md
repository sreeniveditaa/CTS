# Exercise 11 - Float Input

## Objective
Handle decimal input with validation, a function, and formatted output.

## Task
Convert weight from kilograms to pounds.

## Instructions
- Use a function.
- Validate decimal input.
- Convert kilograms to pounds using `lbs = kg * 2.20462`.
- Print the weight in pounds.

## Project Structure

- `Exercise_11.py` - Python source code
- `11_output.png` - Program output screenshot

## Code

```python
def convert_weight():
    weight=input("Enter weight in kilograms: ").strip()
    kg=float(weight)

    if kg<=0:
        print("Weight must be greater than 0.")
        return

    lbs=kg*2.20462
    print(f"Weight in Pounds: {lbs:.2f} lbs")

convert_weight()
```

## Expected Output

```
Enter weight in kilograms: 51.5
Weight in Pounds: 113.54 lbs
```