def greetings(name="noble stranger"):

    if not isinstance(name, str):
        print("Error: argument must be a string!")
    else:
        print(f"Hello, {name}!")

if __name__ == "__main__":
    user_input = input("Enter a name (or leave empty for default): ")

    if user_input.strip() == "":
        greetings()
    else:
        greetings(user_input)