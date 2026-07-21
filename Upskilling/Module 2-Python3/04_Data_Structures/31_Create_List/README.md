o# Exercise 31 - Create List

## Objective
Initialize a list with basic validation, a function, and clean output.

## Task
Create a shopping cart list and display the items.

## Instructions
- Use a function.
- Validate the list items.
- Initialize the list with values `[100, 250, 75]`.
- Print the cart contents.

## Project Structure

- `Exercise_31.py` - Python source code
- `31_output.png` - Program output screenshot

## Code

```python
def display_cart(cart):
    if not isinstance(cart, list):
        print("Error: Cart must be a list.")
        return

    if not cart:
        print("Error: Cart is empty.")
        return

    if not all(isinstance(item, (int, float)) for item in cart):
        print("Error: Cart contains invalid items.")
        return

    print("Shopping Cart Contents:")

    for item in cart:
        print(item)

cart = [100, 250, 75]
display_cart(cart)
```

## Expected Output

```
Shopping Cart Contents:
100
250
75
```