def assign_grade(score):
    if not isinstance(score, (int, float)):
        print("Score must be a number.")
        return

    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        return

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    else:
        grade = "C"

    print(f"Score : {score}")
    print(f"Grade : {grade}")

    if grade == "A":
        print("Excellent!")
    elif grade == "B":
        print("Good!")
    else:
        print("Get better!")

score = 88

assign_grade(score)