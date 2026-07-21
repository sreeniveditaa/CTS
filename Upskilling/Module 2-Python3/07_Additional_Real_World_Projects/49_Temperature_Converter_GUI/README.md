# Exercise 49 - Temperature Converter GUI

## Objective

Use classes, user input, modules, and formatted output.

## Task

Convert temperatures between Celsius, Fahrenheit, and Kelvin.

## Instructions

- Create a `Converter` class.
- Convert between Celsius, Fahrenheit, and Kelvin.
- Use an `input()` menu.
- Format output to two decimal places.
- Display results using the `tabulate` module.

## Project Structure

- `Exercise_49.py` - Python source code
- `49_output.png` - Program output screenshot

## Requirements

Install the tabulate module:

```bash
pip install tabulate
```

## Code

```python
from tabulate import tabulate


class Converter:
    def celsius_to_fahrenheit(self, c):
        return (c * 9 / 5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9

    def celsius_to_kelvin(self, c):
        return c + 273.15

    def kelvin_to_celsius(self, k):
        return k - 273.15

    def fahrenheit_to_kelvin(self, f):
        return self.celsius_to_kelvin(self.fahrenheit_to_celsius(f))

    def kelvin_to_fahrenheit(self, k):
        return self.celsius_to_fahrenheit(self.kelvin_to_celsius(k))


converter = Converter()

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = input("Enter your choice (1-6): ")
value = float(input("Enter temperature: "))

result = None
conversion = ""

if choice == "1":
    result = converter.celsius_to_fahrenheit(value)
    conversion = "Celsius → Fahrenheit"
elif choice == "2":
    result = converter.fahrenheit_to_celsius(value)
    conversion = "Fahrenheit → Celsius"
elif choice == "3":
    result = converter.celsius_to_kelvin(value)
    conversion = "Celsius → Kelvin"
elif choice == "4":
    result = converter.kelvin_to_celsius(value)
    conversion = "Kelvin → Celsius"
elif choice == "5":
    result = converter.fahrenheit_to_kelvin(value)
    conversion = "Fahrenheit → Kelvin"
elif choice == "6":
    result = converter.kelvin_to_fahrenheit(value)
    conversion = "Kelvin → Fahrenheit"
else:
    print("Invalid choice.")
    exit()

table = [[conversion, f"{value:.2f}", f"{result:.2f}"]]

print()
print(tabulate(table, headers=["Conversion", "Input", "Output"], tablefmt="grid"))
```

## Sample Output

```
Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
Enter your choice (1-6): 1
Enter temperature: 25

+-------------------------+---------+----------+
| Conversion              |   Input |   Output |
+=========================+=========+==========+
| Celsius → Fahrenheit    |   25.00 |    77.00 |
+-------------------------+---------+----------+
```