def add_expense(expenses, expense):
    if not isinstance(expenses, list):
        print("Error: Expenses must be a list.")
        return

    if not isinstance(expense, (int, float)):
        print("Error: Expense must be a number.")
        return

    if expense <= 0:
        print("Error: Expense must be greater than 0.")
        return
    expenses.append(expense)

    print("Updated Expenses List:")
    print(expenses)

expenses = [100, 250, 75]
new_expense = 150
add_expense(expenses, new_expense)