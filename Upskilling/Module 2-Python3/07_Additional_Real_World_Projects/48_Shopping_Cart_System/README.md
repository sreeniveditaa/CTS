# Exercise 48 - Shopping Cart System

## Objective

Use classes, lists, control flow, and the math module to build a simple shopping cart system.

## Task

Perform complete cart operations and print a receipt with GST.

## Instructions

- Create a `CartItem` class with price and quantity.
- Create a `ShoppingCart` class with:
  - Add item
  - Remove item
  - Calculate total
- Apply 18% GST.
- Print the final receipt.

## Project Structure

- `Exercise_48.py` - Python source code
- `48_output.png` - Program output screenshot

## Code

```python
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item.price <= 0 or item.quantity <= 0:
            print("Invalid item details.")
            return
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def print_receipt(self):
        subtotal = self.calculate_total()
        gst = subtotal * 0.18
        total = subtotal + gst

        print("===== Shopping Receipt =====")

        for item in self.items:
            print(
                f"{item.name} | ₹{item.price:.2f} x {item.quantity} = ₹{item.total_price():.2f}"
            )

        print(f"\nSubtotal : ₹{subtotal:.2f}")
        print(f"GST (18%): ₹{gst:.2f}")
        print(f"Grand Total: ₹{total:.2f}")


cart = ShoppingCart()

cart.add_item(CartItem("Keyboard", 1200, 1))
cart.add_item(CartItem("Mouse", 650, 2))
cart.add_item(CartItem("Headphones", 2500, 1))

cart.remove_item("Mouse")

cart.print_receipt()
```

## Expected Output

```
===== Shopping Receipt =====
Keyboard | ₹1200.00 x 1 = ₹1200.00
Headphones | ₹2500.00 x 1 = ₹2500.00

Subtotal : ₹3700.00
GST (18%): ₹666.00
Grand Total: ₹4366.00
```