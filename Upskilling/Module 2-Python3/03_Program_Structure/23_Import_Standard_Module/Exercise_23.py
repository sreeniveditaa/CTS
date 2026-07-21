import math

def circle_area(radius):
    if not isinstance(radius, (int, float)):
        print("Error: Radius must be a number.")
        return

    if radius<=0:
        print("Error: Radius must be greater than 0.")
        return

    area=math.pi*radius**2
    print(f"Area of Circle: {area:.2f}")

radius = 7
circle_area(radius)