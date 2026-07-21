# Exercise 34 - Nested Dictionary

## Objective
Work with nested dictionaries using a function and basic validation.

## Task
Store department-wise employee data and retrieve a specific employee's salary.

## Instructions
- Use a nested dictionary.
- Use a function to fetch data.
- Validate department and employee name.
- Print the employee salary.

## Project Structure

- `Exercise_34.py` - Python source code
- `34_output.png` - Program output screenshot

## Code

```python
def get_employee_salary(data, department, employee):
    if department not in data:
        print("Error: Department not found.")
        return

    if employee not in data[department]:
        print("Error: Employee not found.")
        return

    salary = data[department][employee]["Salary"]

    print(f"Department: {department}")
    print(f"Employee: {employee}")
    print(f"Salary: {salary}")


employees = {
    "IT": {
        "Alice": {"Salary": 65000},
        "Bob": {"Salary": 70000}
    },
    "HR": {
        "Emma": {"Salary": 55000},
        "John": {"Salary": 60000}
    }
}

get_employee_salary(employees, "IT", "Bob")
```

## Expected Output

```
Department: IT
Employee: Bob
Salary: 70000
```