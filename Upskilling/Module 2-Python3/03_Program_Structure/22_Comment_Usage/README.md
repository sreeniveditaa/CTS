# Exercise 22 - Comment Usage

## Objective
Show proper documentation using meaningful comments and a function.

## Task
Add explanatory comments and print the total salary.

## Instructions
- Use clear comments.
- Use a function.
- Define base and bonus salary.
- Calculate total salary.
- Print the result.

## Project Structure

- `Exercise_22.py` - Python source code
- `22_output.png` - Program output screenshot

## Code

```python
#Function Definition
def calculate_salary():
    #Store known values in variables
    base_salary = 50000
    bonus = 10000
    #Compure the total salary
    total_salary = base_salary + bonus
    #Print results
    print(f"Total Salary: {total_salary}")

#Call the defined function
calculate_salary()
```

## Expected Output

```
Total Salary: 60000
```