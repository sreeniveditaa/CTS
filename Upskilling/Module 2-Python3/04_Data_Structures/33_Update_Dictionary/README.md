# Exercise 33 - Update Dictionary

## Objective
Perform bulk dictionary updates using a function with basic validation.

## Task
Merge employee details from two dictionaries.

## Instructions
- Use a function.
- Validate dictionary inputs.
- Use `.update()`.
- Print the updated employee data.

## Project Structure

- `Exercise_33.py` - Python source code
- `33_output.png` - Program output screenshot

## Code

```python
def update_employee_data(employee1, employee2):
    if not isinstance(employee1, dict) or not isinstance(employee2, dict):
        print("Error: Both inputs must be dictionaries.")
        return

    employee1.update(employee2)
    print("Updated Employee Data:")
    print(employee1)

employee_data = {"Name": "Alice","Age": 28}
new_details = {"Department": "IT","Salary": 65000}
update_employee_data(employee_data, new_details)
```

## Expected Output

```
Updated Employee Data:
{'Name': 'Alice', 'Age': 28, 'Department': 'IT', 'Salary': 65000}
```