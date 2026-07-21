# Exercise 9 - Basic Input

## Objective
Read and validate user input using a function and formatted output.

## Task
Get the user's name and display a greeting message.

## Instructions
- Use a function.
- Validate empty input.
- Use `input()`.
- Print a greeting message.

## Project Structure

- `Exercise_09.py` - Python source code
- `09_output.png` - Output screenshot

## Code

```python
def greet_user():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    print(f"Hello, {name}! Welcome.")

greet_user()
```

## Expected Output

```
Enter your name: Cynthia
Hello, Cynthia! Welcome.
```