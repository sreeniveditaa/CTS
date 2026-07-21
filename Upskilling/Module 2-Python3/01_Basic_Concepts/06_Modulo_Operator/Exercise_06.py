def check(number):
    if not isinstance(number, int):
        print("Input must be an integer.")
        return
    
    if number%2==0:
        print(f"Number: {number}")
        print("Result: Even")
    else:
        print(f"Number: {number}")
        print("Result: Odd")

number = 17
check(number)