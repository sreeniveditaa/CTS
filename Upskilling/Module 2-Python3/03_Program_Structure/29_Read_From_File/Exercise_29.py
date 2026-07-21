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