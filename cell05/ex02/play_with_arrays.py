def play_with_arrays(numbers):
    filtered_numbers = [n for n in numbers if n > 5]

    result = [n + 2 for n in filtered_numbers]

    return filtered_numbers, result

if __name__ == "__main__":
    original = [2, 8, 9, 48, 8, 22, -12, 2]

    print(original)
    filtered, result = play_with_arrays(original)
    print(result)
