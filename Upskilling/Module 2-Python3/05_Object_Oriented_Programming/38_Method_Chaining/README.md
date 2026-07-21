# Exercise 38 - Method Chaining

## Objective
Demonstrate method chaining by returning `self` from methods.

## Task
Create an employee object, set salary, apply raise, and display the final salary.

## Instructions
- Create a class.
- Methods should return `self`.
- Use method chaining.
- Add basic validation.
- Print the final salary.

## Project Structure

- `Exercise_38.py`
- `38_output.png`

## Code 
```python
class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        if salary <= 0:
            print("Invalid salary.")
            return self
        self.salary = salary
        return self

    def apply_raise(self, amount):
        if amount < 0:
            print("Invalid raise amount.")
            return self
        self.salary += amount
        return self

    def display(self):
        print(f"Employee: {self.name}")
        print(f"Final Salary: {self.salary}")
        return self


employee = Employee("Cynthia")
employee.set_salary(50000).apply_raise(5000).display()
```

## Expected Output

```
Employee: Cynthia
Final Salary: 55000
```