# Exercise 43 - Configuration Manager

## Objective

Use classes, inheritance, dictionaries, and file I/O to manage application configuration.

## Task

Create a configurable system that loads database settings from a file.

## Instructions

- Create a base `Config` class.
- Create a `DatabaseConfig` class inheriting from `Config`.
- Use the `configparser` module.
- Load settings from `db.ini`.
- Validate all required keys.

## Project Structure

- `Exercise_43.py` - Python source code
- `db.ini` - Database configuration file
- `43_output.png` - Program output screenshot

## Code

```python
import configparser


class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()

    def load(self):
        self.config.read(self.filename)


class DatabaseConfig(Config):
    def display_settings(self):
        required_keys = ["host", "port", "username", "password", "database"]

        if "DATABASE" not in self.config:
            print("Error: DATABASE section not found.")
            return

        database = self.config["DATABASE"]

        for key in required_keys:
            if key not in database:
                print(f"Error: Missing required key '{key}'.")
                return

        print("Database Configuration")
        print(f"Host: {database['host']}")
        print(f"Port: {database['port']}")
        print(f"Username: {database['username']}")
        print(f"Password: {database['password']}")
        print(f"Database: {database['database']}")


db_config = DatabaseConfig("db.ini")
db_config.load()
db_config.display_settings()
```

## Expected Output

```
Database Configuration
Host: localhost
Port: 3306
Username: admin
Password: pass123
Database: employee_db
```