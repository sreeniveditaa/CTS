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