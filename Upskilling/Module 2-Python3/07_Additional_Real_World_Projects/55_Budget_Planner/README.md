# Exercise 55 - Budget Planner

## Objective

Use classes, control flow, external modules, and visualization to track a monthly budget.

## Task

Create a monthly budget planner that tracks spending, alerts overspending, and visualizes data.

## Instructions

- Create a `Category` class with `limit` and `spent`.
- Input expenses using a loop.
- Use `matplotlib` for pie chart visualization.
- Alert when a category exceeds its budget.

## Project Structure

- `Exercise_55.py` - Python source code
- `55_output.png` - Program output screenshot

## Requirements

Install Matplotlib:

```bash
pip install matplotlib
```

## Code

```python
import matplotlib.pyplot as plt


class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount

    def is_over_budget(self):
        return self.spent > self.limit


categories = {
    "Food": Category("Food", 5000),
    "Transport": Category("Transport", 3000),
    "Entertainment": Category("Entertainment", 2000)
}

while True:
    category = input("Enter category (Food/Transport/Entertainment or done): ")

    if category.lower() == "done":
        break

    if category not in categories:
        print("Invalid category.")
        continue

    try:
        amount = float(input("Enter expense: "))
    except ValueError:
        print("Invalid amount.")
        continue

    categories[category].add_expense(amount)

print("\nMonthly Budget Summary")

labels = []
amounts = []

for category in categories.values():
    print(
        f"{category.name}: Spent ₹{category.spent:.2f} / Limit ₹{category.limit:.2f}"
    )

    if category.is_over_budget():
        print(f"Alert: {category.name} exceeded the budget!")

    labels.append(category.name)
    amounts.append(category.spent)

plt.figure(figsize=(6, 6))
plt.pie(amounts, labels=labels, autopct="%1.1f%%")
plt.title("Monthly Spending")
plt.show()
```

## Sample Output

```
Monthly Budget Summary
Food: Spent ₹5500.00 / Limit ₹5000.00
Alert: Food exceeded the budget!
Transport: Spent ₹1500.00 / Limit ₹3000.00
Entertainment: Spent ₹1200.00 / Limit ₹2000.00
```

The program also displays a pie chart representing the spending distribution.