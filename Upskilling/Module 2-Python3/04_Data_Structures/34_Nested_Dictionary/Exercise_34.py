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