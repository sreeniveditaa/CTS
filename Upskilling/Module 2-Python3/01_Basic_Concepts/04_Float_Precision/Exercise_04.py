def calculate_salary(salary, tax_rate):
    
    if salary <= 0:
        print("Salary must be greater than 0.")
        return

    if not (0 <= tax_rate <= 1):
        print("Tax rate must be between 0 and 1.")
        return

    net_salary = salary-(salary*tax_rate)

    print(f"Salary: ₹{salary:.2f}")
    print(f"Tax Rate: {tax_rate*100:.0f}%")
    print(f"Net Salary: ₹{net_salary:.2f}")


salary = 75000.5
tax_rate = 0.18

calculate_salary(salary, tax_rate)