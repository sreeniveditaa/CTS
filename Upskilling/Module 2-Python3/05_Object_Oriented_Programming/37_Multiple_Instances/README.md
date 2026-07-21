# Exercise 37 - Multiple Instances

## Objective
Create multiple objects from a class and access their attributes.

## Task
Create an employee roster using multiple instances of a class.

## Instructions
- Define a class with `__init__`.
- Create multiple objects (instances).
- Add a method to display employee information.
- Print employee names.

## Project Structure

- `Exercise_37.py` - Python source code
- `37_output.png` - Program output screenshot

## Code

```python
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_info(self):
        print(f"Employee: {self.name} | Department: {self.department}")


emp1 = Employee("Alice", "HR")
emp2 = Employee("Bob", "IT")
emp3 = Employee("Charlie", "Finance")

employees = [emp1, emp2, emp3]

for employee in employees:
    employee.display_info()
```

## Expected Output

```
Employee: Alice | Department: HR
Employee: Bob | Department: IT
Employee: Charlie | Department: Finance
```