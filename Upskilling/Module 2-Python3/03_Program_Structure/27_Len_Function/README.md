# Exercise 27 - Len Function

## Objective
Use `len()` inside a function with basic validation and structured output.

## Task
Get the length of a given string.

## Instructions
- Use a function.
- Validate the string.
- Use `len(text)`.
- Print the length.

## Project Structure

- `Exercise_27.py` - Python source code
- `27_output.png` - Program output screenshot

## Code

```python
def get_length(text):
    if not isinstance(text, str):
        print("Error: Input must be a string.")
        return None

    if text.strip() == "":
        print("Error: String cannot be empty.")
        return None

    length=len(text)
    print(f"Text: {text}")
    print(f"Length: {length}")

text = "Python Programming"
get_length(text)
```

## Expected Output

```
Text: Python Programming
Length: 19
```