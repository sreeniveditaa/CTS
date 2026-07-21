# Exercise 8 - Min/Max Functions

## Objective
Use the built-in `min()` and `max()` functions with validation, a function, and structured output.

## Task
Find the highest and lowest salary in a list.

## Instructions
- Use a function.
- Validate the salary list.
- Compute the minimum and maximum salary.
- Print the results.
- Use the list `[50000, 75000, 62000, 95000]`.

## Project Structure

- `Exercise_08.py` - Python source code
- `08_output.png` - Program output screenshot

## Code

```python
def min_max(salaries):
    if not isinstance(salaries, list) or len(salaries) == 0:
        print("Salary list cannot be empty.")
        return

    lowest = min(salaries)
    highest = max(salaries)

    print("Salary List: ", salaries)
    print(f"Lowest Salary : ₹{lowest}")
    print(f"Highest Salary: ₹{highest}")


salaries = [50000, 75000, 62000, 95000]

min_max(salaries)
```

## Expected Output

```
Salary List: [50000, 75000, 62000, 95000]
Lowest Salary: ₹50000
Highest Salary: ₹95000
```