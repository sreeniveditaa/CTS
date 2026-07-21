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
