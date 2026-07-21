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