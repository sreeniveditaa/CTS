# Exercise 54 - Inventory Manager

## Objective

Use classes, inheritance, dictionaries, and sets to manage warehouse inventory.

## Task

Track products, stock levels, and generate low-stock alerts.

## Instructions

- Create a `Product` base class.
- Create `Perishable` and `Electronics` classes inheriting from `Product`.
- Track stock levels using a dictionary.
- Use a set to identify low-stock items.
- Print an inventory summary.

## Project Structure

- `Exercise_54.py` - Python source code
- `54_output.png` - Program output screenshot

## Code

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


class Perishable(Product):
    def __init__(self, name, stock, expiry_date):
        super().__init__(name, stock)
        self.expiry_date = expiry_date


class Electronics(Product):
    def __init__(self, name, stock, warranty):
        super().__init__(name, stock)
        self.warranty = warranty


inventory = {}

inventory["Milk"] = Perishable("Milk", 5, "2026-07-15")
inventory["Bread"] = Perishable("Bread", 2, "2026-07-02")
inventory["Laptop"] = Electronics("Laptop", 10, "2 Years")
inventory["Mouse"] = Electronics("Mouse", 3, "1 Year")

low_stock = {
    name for name, product in inventory.items()
    if product.stock < 5
}

print("Inventory Summary")

for name, product in inventory.items():
    print(f"{name}: {product.stock} units")

print("\nLow Stock Alerts")

if low_stock:
    for item in sorted(low_stock):
        print(item)
else:
    print("No low stock items.")
```

## Expected Output

```
Inventory Summary
Milk: 5 units
Bread: 2 units
Laptop: 10 units
Mouse: 3 units

Low Stock Alerts
Bread
Mouse
```