# Exercise 14 - If-Elif-Else

## Objective
Use a multi-way decision with functions, validation, and structured output.

## Task
Assign a grade based on the score.

## Instructions
- Use a function.
- Validate the score.
- Use the variable `score = 88`.
- Print grade `A`, `B`, or `C`.
- Add slight enhancements over the basic version.

## Project Structure

- `Exercise_14.py` - Python source code
- `14_output.png` - Program output screenshot

## Code

```python
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
```

## Expected Output

```
Score : 88
Grade : B
Good!
```