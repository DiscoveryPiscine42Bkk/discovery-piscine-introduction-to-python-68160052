def upcase_it(text):

    return text.upper()


if __name__ == "__main__":
    user_text = input("Enter a word or phrase: ")
    result = upcase_it(user_text)
    print("Uppercase result:", result)