def sum_odd_numbers(range_size):
    if not isinstance(range_size, int):
        print("Error: Range size must be an integer.")
        return

    if range_size <= 0:
        print("Error: Range size must be greater than 0.")
        return

    total = 0

    for i in range(range_size):
        if i % 2 == 0:
            continue

        total += i

    print(f"Sum of Odd Numbers: {total}")

range_size = 10
sum_odd_numbers(range_size)