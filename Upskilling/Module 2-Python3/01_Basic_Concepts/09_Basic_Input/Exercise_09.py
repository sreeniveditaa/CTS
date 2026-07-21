def greet_user():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    print(f"Hello, {name}! Welcome.")

greet_user()