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