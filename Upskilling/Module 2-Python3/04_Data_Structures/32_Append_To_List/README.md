# Exercise 32 - Append to List

## Objective
Add a single item to a list using a function with validation.

## Task
Add a new expense to an existing expenses list.

## Instructions
- Use a function.
- Validate the expense amount.
- Use `.append()`.
- Print the updated expenses list.

## Project Structure

- `Exercise_32.py` - Python source code
- `32_output.png` - Program output screenshot

## Code

```python
def add_expense(expenses, expense):
    if not isinstance(expenses, list):
        print("Error: Expenses must be a list.")
        return

    if not isinstance(expense, (int, float)):
        print("Error: Expense must be a number.")
        return

    if expense <= 0:
        print("Error: Expense must be greater than 0.")
        return
    expenses.append(expense)

    print("Updated Expenses List:")
    print(expenses)

expenses = [100, 250, 75]
new_expense = 150
add_expense(expenses, new_expense)
```

## Expected Output

```
Updated Expenses List:
[100, 250, 75, 150]
```