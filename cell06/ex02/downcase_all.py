def downcase_it(text):
 
    return text.lower()


if __name__ == "__main__":
    user_input = input("Enter a word or phrase (or leave empty): ")

    if user_input.strip() == "":
        print("none")
    else:
        result = downcase_it(user_input)
        print("Lowercase result:", result)