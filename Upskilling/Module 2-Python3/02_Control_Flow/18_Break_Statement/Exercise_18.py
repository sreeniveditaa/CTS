def find_first_even(range_size):
    if not isinstance(range_size, int):
        print("Error: Range size must be an integer.")
        return

    if range_size <= 0:
        print("Error: Range size must be greater than 0.")
        return

    for i in range(range_size):
        if i % 2 == 0:
            print(f"First Even Number: {i}")
            break

range_size = 10
find_first_even(range_size)