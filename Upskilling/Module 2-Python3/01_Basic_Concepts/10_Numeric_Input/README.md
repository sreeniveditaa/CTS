# Exercise 10 - Numeric Input

## Objective
Convert user input to a number with validation, a function, and formatted output.

## Task
Ask the user for their age, validate the input, convert it to an integer, and display their age next year.

## Instructions
- Use a function.
- Validate numeric input.
- Convert the input using `int()`.
- Print `"Next year you'll be <age + 1>"`.

## Project Structure

- `Exercise_10.py` - Python source code
- `10_output.png` - Program output screenshot

## Code

```python
def get_age():
    age = input("Enter your age: ").strip()

    if not age.isdigit():
        print("Please enter a valid numeric age.")
        return

    age = int(age)
    print(f"Next year you'll be {age+1}.")

get_age()
```

## Expected Output

```
Enter your age: 21
Next year you'll be 22.
```