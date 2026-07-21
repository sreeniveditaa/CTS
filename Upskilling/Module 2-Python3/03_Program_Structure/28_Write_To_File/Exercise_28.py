def write_message():
    file = open("message.txt", "w")
    file.write("Hello World")
    file.close()
    print("File written successfully")

write_message()