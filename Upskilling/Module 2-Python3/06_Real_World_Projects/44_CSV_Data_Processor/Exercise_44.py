import csv

def analyze_employee_data(filename):
    try:
        employees = []
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Salary"] = int(row["Salary"])
                employees.append(row)

        if not employees:
            print("Error: No employee data found.")
            return
        high_salary_employees = [
            employee for employee in employees
            if employee["Salary"] > 50000
        ]
        average_salary = sum(
            employee["Salary"] for employee in employees
        ) / len(employees)

        print("Employees with Salary > 50000")
        for employee in high_salary_employees:
            print(f"{employee['Name']} - {employee['Salary']}")

        print(f"\nAverage Salary: {average_salary:.2f}")

    except FileNotFoundError:
        print("Error: employees.csv not found.")
    except ValueError:
        print("Error: Invalid salary data.")


analyze_employee_data("employees.csv")