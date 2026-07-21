def get_age():
    age = input("Enter your age: ").strip()

    if not age.isdigit():
        print("Please enter a valid numeric age.")
        return

    age = int(age)
    print(f"Next year you'll be {age+1}.")

get_age()