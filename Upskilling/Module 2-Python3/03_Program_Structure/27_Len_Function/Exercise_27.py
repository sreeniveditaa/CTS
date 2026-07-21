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