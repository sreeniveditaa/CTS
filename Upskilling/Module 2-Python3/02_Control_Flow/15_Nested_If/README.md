# Exercise 15 - Nested If

## Objective
Use nested conditions with a function, basic validation, and formatted output.

## Task
Validate a username and password using nested `if` statements.

## Instructions
- Use a function.
- Validate blank inputs.
- Use nested `if` statements for username and password validation.
- Use the variables:
  - `user = "admin"`
  - `pwd = "pass123"`

## Project Structure

- `Exercise_15.py` - Python source code
- `15_output.png` - Program output screenshot

## Code

```python
def validate_login(user, pwd):
    if not user.strip() or not pwd.strip():
        print("Error: Username and password cannot be empty.")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("Invalid Username")

user = "admin"
pwd = "pass123"

validate_login(user, pwd)
```

## Expected Output

```
Login Successful
```