# Exercise 4 - Float Precision

## Objective
Handle floating-point arithmetic with functions, validation, and formatted output.

## Task
Calculate the net salary after tax and display the result with two decimal places.

## Instructions
- Use `salary = 75000.5` and `tax_rate = 0.18`.
- Use a function.
- Validate salary and tax rate.
- Use variables.
- Format the output to 2 decimal places.

## Project Structure

- `Exercise_04.py` - Python source code
- `04_output.png` - Program output screenshot

## Code

```python
def calculate_salary(salary, tax_rate):
    
    if salary <= 0:
        print("Salary must be greater than 0.")
        return

    if not (0 <= tax_rate <= 1):
        print("Tax rate must be between 0 and 1.")
        return

    net_salary = salary-(salary*tax_rate)

    print(f"Salary: ₹{salary:.2f}")
    print(f"Tax Rate: {tax_rate*100:.0f}%")
    print(f"Net Salary: ₹{net_salary:.2f}")


salary = 75000.5
tax_rate = 0.18

calculate_salary(salary, tax_rate)
```

## Expected Output

```
Gross Salary: ₹75000.50
Tax Rate: 18%
Net Salary: ₹61500.41
```