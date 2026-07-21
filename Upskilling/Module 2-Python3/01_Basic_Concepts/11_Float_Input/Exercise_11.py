def convert_weight():
    weight=input("Enter weight in kilograms: ").strip()
    kg=float(weight)

    if kg<=0:
        print("Weight must be greater than 0.")
        return

    lbs=kg*2.20462
    print(f"Weight in Pounds: {lbs:.2f} lbs")

convert_weight()