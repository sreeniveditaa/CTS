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