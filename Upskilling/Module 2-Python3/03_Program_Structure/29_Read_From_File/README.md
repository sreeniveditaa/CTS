# Exercise 29 - Read from File

## Objective
Read text from a file using a function with basic error handling.

## Task
Open a text file and display its contents.

## Instructions
- Use a function.
- Open file in read mode.
- Read full content using `read()`.
- Print file content.
- Handle missing file gracefully.

## Project Structure

- `Exercise_29.py` - Python source code
- `message.txt` - Input file
- `29_output.png` - Program output screenshot

## Code

```python
def read_message():
    try:
        file = open("message.txt", "r")
        content = file.read()
        file.close()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("Error: File not found")

read_message()
```

## Expected Output

```
File Content:
Hello World
```