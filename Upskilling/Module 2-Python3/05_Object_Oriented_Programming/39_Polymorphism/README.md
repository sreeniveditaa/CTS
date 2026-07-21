# Exercise 39 - Polymorphism

## Objective
Demonstrate polymorphism using method overriding.

## Task
Show different behaviors of the same `work()` method for different employee types.

## Instructions
- Create a base class.
- Override the method in child classes.
- Store objects in a list.
- Call the same method for all objects.
- Observe different outputs.

## Project Structure

- `Exercise_39.py`
- `39_output.png`

## Code

```python
class Employee:
    def work(self):
        print("Employee is working.")


class Developer(Employee):
    def work(self):
        print("Developer is writing code.")


class Manager(Employee):
    def work(self):
        print("Manager is managing the team.")


class Tester(Employee):
    def work(self):
        print("Tester is testing the application.")


employees = [Developer(), Manager(), Tester()]

for employee in employees:
    employee.work()
```

## Expected Output

```
Developer is writing code.
Manager is managing the team.
Tester is testing the application.
```