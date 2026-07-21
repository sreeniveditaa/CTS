# Exercise 50 - Backup Utility

## Objective

Use file operations, modules, sets, and error handling to build a smart backup tool.

## Task

Copy files to a backup folder while skipping duplicates and logging operations.

## Instructions

- Use the `shutil` module.
- Copy files while skipping duplicates using a set.
- Handle `FileNotFoundError` and `PermissionError`.
- Log all operations to `backup.log`.

## Project Structure

- `Exercise_50.py` - Python source code
- `source/` - Source files
- `backup/` - Backup folder (created automatically)
- `backup.log` - Operation log
- `50_output.png` - Program output screenshot

## Code

```python
import os
import shutil


def backup_files(source_folder, backup_folder):
    copied_files = set()

    os.makedirs(backup_folder, exist_ok=True)

    try:
        with open("backup.log", "a") as log:
            for file_name in os.listdir(source_folder):
                source_path = os.path.join(source_folder, file_name)
                backup_path = os.path.join(backup_folder, file_name)

                if file_name in copied_files or os.path.exists(backup_path):
                    message = f"Skipped duplicate: {file_name}"
                    print(message)
                    log.write(message + "\n")
                    continue

                shutil.copy2(source_path, backup_path)
                copied_files.add(file_name)

                message = f"Copied: {file_name}"
                print(message)
                log.write(message + "\n")

    except FileNotFoundError:
        print("Error: Source folder not found.")
    except PermissionError:
        print("Error: Permission denied while copying files.")


backup_files("source", "backup")
```

## Expected Output

```
Copied: file1.txt
Copied: file2.txt
Copied: file3.txt
```

On subsequent runs:

```
Skipped duplicate: file1.txt
Skipped duplicate: file2.txt
Skipped duplicate: file3.txt
```