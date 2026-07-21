from math import *
def math_operations(value):
    if not isinstance(value, (int, float)):
        print("Input must be a number.")
        return

    if value <= 0:
        print("Value must be greater than 0.")
        return

    square_root = sqrt(value)
    power_value = pow(value, 2)

    print(f"Value: {value}")
    print(f"Square Root: {square_root:.2f}")
    print(f"Power (square): {power_value}")
    print(f"Pi Value: {pi:.5f}")

value = 16
math_operations(value)