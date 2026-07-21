import json
def add_grade(gradebook, student, grade):
    if not (0 <= grade <= 100):
        print("Invalid grade.")
        return

    if student not in gradebook:
        gradebook[student] = []

    gradebook[student].append(grade)


def calculate_gpa(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def save_data(gradebook, filename):
    with open(filename, "w") as file:
        json.dump(gradebook, file, indent=4)

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

def class_average(gradebook):
    all_grades = []

    for grades in gradebook.values():
        all_grades.extend(grades)

    if not all_grades:
        return 0

    return sum(all_grades) / len(all_grades)


gradebook = {}

add_grade(gradebook, "Alice", 85)
add_grade(gradebook, "Alice", 90)
add_grade(gradebook, "Bob", 78)
add_grade(gradebook, "Bob", 82)
add_grade(gradebook, "Charlie", 95)

save_data(gradebook, "grades.json")

gradebook = load_data("grades.json")

print("Student GPAs")

for student, grades in gradebook.items():
    print(f"{student}: {calculate_gpa(grades):.2f}")

print(f"\nClass Average: {class_average(gradebook):.2f}")