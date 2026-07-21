# Exercise 28 - Write to File

## Objective
Create and write to a text file using a function with clean structure.

## Task
Save a greeting message into a text file.

## Instructions
- Use a function.
- Open a file in write mode.
- Write `"Hello World"` into the file.
- Print confirmation message.

## Project Structure

- `Exercise_28.py` - Python source code
- `message.txt` - Output file created by program
- `28_output.png` - Program output screenshot

## Code

```python
def write_message():
    file = open("message.txt", "w")
    file.write("Hello World")
    file.close()
    print("File written successfully")

write_message()
```

## Expected Output

```
File written successfully
```