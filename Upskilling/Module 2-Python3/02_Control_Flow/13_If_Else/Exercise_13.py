def check_even_odd(num):
    if not isinstance(num, int):
        print("Error: Input must be an integer.")
        return

    if num%2==0:
        print(f"Number: {num}")
        print("Result: Even")
    else:
        print(f"Number: {num}")
        print("Result: Odd")

num = 8

check_even_odd(num)