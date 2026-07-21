# Exercise 36 - Set Intersection

## Objective
Find common elements between two sets using a function and basic validation.

## Task
Identify common skills between two skill sets.

## Instructions
- Use sets.
- Use a function.
- Validate inputs.
- Find the intersection using `&`.
- Print the common skills.

## Project Structure

- `Exercise_36.py` - Python source code
- `36_output.png` - Program output screenshot

## Code

```python
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
```

## Expected Output

```
Common Skills:
Python
SQL
```