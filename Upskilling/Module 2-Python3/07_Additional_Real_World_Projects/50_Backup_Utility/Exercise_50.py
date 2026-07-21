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