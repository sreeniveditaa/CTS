def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Inputs must be numbers.")
        return
    return a+b

result=add_numbers(5, 3)
print(f"Sum: {result}")