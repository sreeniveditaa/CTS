def check_result(marks):
    if not isinstance(marks, (int, float)):
        print("Error: Marks must be a number.")
        return

    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100.")
        return

    if marks >= 50:
        print(f"Marks: {marks}")
        print("Result: Pass")
    else:
        print(f"Marks: {marks}")
        print("Result: Fail")

marks = 75

check_result(marks)