def safe_divide(a, b):
    try:
        result = a/b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

a = 10
b = 0
safe_divide(a, b)