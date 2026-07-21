import csv
from datetime import datetime

def analyze_expenses(filename):
    try:
        current_month = datetime.now().month
        current_year = datetime.now().year
        category_totals = {}

        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense_date = datetime.strptime(row["Date"], "%Y-%m-%d")
                if (
                    expense_date.month == current_month
                    and expense_date.year == current_year
                ):
                    amount = float(row["Amount"])
                    category = row["Category"]

                    category_totals[category] = (
                        category_totals.get(category, 0) + amount
                    )

        if not category_totals:
            print("No expenses found for the current month.")
            return

        print("Current Month Expense Summary")

        for category, total in category_totals.items():
            print(f"{category}: {total:.2f}")

    except FileNotFoundError:
        print("Error: expenses.csv not found.")
    except ValueError:
        print("Error: Invalid data in expenses.csv.")

analyze_expenses("expenses.csv")