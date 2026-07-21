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