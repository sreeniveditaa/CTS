import json

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Salary: {self.salary}"

def save_employees(employees, filename):
    data = {}
    for emp_id, employee in employees.items():
        data[emp_id] = {
            "name": employee.name,
            "salary": employee.salary
        }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_employees(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    employees = {}

    for emp_id, details in data.items():
        employees[emp_id] = Employee(
            emp_id,
            details["name"],
            details["salary"]
        )

    return employees


employees = {
    "E101": Employee("E101", "Alice", 65000),
    "E102": Employee("E102", "Bob", 72000),
    "E103": Employee("E103", "Charlie", 58000)
}

save_employees(employees, "emps.json")

loaded_employees = load_employees("emps.json")

print("Employee Records:")
for employee in loaded_employees.values():
    print(employee)