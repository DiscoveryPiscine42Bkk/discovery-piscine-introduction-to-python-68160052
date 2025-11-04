def shrink(text):

    print(text[:8])


def shout(text):

    print(text.upper())


if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")

    print("Shrink function output:")
    shrink(user_input)

    print("Shout function output:")
    shout(user_input)
