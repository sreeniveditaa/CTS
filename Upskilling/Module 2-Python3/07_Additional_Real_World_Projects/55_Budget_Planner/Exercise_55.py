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