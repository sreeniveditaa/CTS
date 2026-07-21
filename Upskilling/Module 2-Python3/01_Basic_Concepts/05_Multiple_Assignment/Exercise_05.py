def display(coordinates):
    
    if not isinstance(coordinates, tuple):
        print("Coordinates must be a tuple.")
        return

    if len(coordinates) != 2:
        print("Coordinates must contain exactly two values.")
        return

    x, y = coordinates

    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")

coordinates = (10, 20)

display(coordinates)