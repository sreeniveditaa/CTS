def area_rectangle(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        print("Error: Inputs must be numbers.")
        return None

    if length <= 0 or width <= 0:
        print("Error: Length and width must be greater than 0.")
        return None

    return length*width


result=area_rectangle(5, 3)

if result is not None:
    print(f"Area: {result}")