def display_coordinates(coordinates):
    if not isinstance(coordinates, tuple):
        print("Error: Coordinates must be a tuple.")
        return

    if len(coordinates) != 2:
        print("Error: Coordinates must contain exactly two values.")
        return

    x, y = coordinates
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Error: Coordinate values must be numeric.")
        return

    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")

coordinates = (15, 30)
display_coordinates(coordinates)