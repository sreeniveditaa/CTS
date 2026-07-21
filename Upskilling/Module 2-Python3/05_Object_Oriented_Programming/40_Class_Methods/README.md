# Exercise 40 - Class Methods

## Objective
Use a class method as a factory to create objects from a formatted string.

## Task
Create an Employee object from a string like `"Shubh,75000"`.

## Instructions
- Use `@classmethod`.
- Parse string input.
- Convert salary to an integer.
- Return a new object using `cls`.
- Print employee details.

## Project Structure

- `Exercise_40.py`
- `40_output.png`
## Code
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))

    def display(self):
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")


employee = Employee.from_string("Shubh,75000")
employee.display()
```
## Expected Output

```
Employee: Shubh
Salary: 75000
```