def countdown(count):
    if not isinstance(count, int):
        print("Count must be an integer.")
        return

    if count<=0:
        print("Count must be greater than 0.")
        return

    print("Countdown:")

    while count > 0:
        print(count)
        count -= 1

count = 5
countdown(count)