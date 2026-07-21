def find_common_skills(skills1, skills2):
    if not isinstance(skills1, set) or not isinstance(skills2, set):
        print("Error: Both inputs must be sets.")
        return

    common_skills = skills1 & skills2

    if common_skills:
        print("Common Skills:")
        for skill in sorted(common_skills):
            print(skill)
    else:
        print("No common skills found.")

employee1 = {"Python", "SQL", "Java"}
employee2 = {"Python", "C++", "SQL"}
find_common_skills(employee1, employee2)