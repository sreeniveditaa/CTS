def min_max(salaries):
    if not isinstance(salaries, list) or len(salaries) == 0:
        print("Salary list cannot be empty.")
        return

    lowest = min(salaries)
    highest = max(salaries)

    print("Salary List: ", salaries)
    print(f"Lowest Salary: ₹{lowest}")
    print(f"Highest Salary: ₹{highest}")


salaries = [50000, 75000, 62000, 95000]

min_max(salaries)