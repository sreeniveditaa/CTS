def print_numbers(count):
    if not isinstance(count, int):
        print("Count must be an integer.")
        return

    if count <= 0:
        print("Count must be greater than 0.")
        return

    print("Numbers from 1 to 5:")

    for i in range(5):
        print(i + 1)

count = 5
print_numbers(count)