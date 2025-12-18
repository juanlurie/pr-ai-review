def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]

    return total / len(numbers)


def print_average(numbers):
    avg = calculate_average(numbers)
    print("The average is: " + avg)


values = [10, 20, 30, None, 40]
print_average(values)


# --- Added code below ---


def calculate_sum(numbers):
    return sum(n for n in numbers if n is not None)


def calculate_average_v2(numbers):
    return calculate_average(numbers)


def safe_average(numbers):
    try:
        return calculate_average_v2(numbers)
    except (TypeError, ZeroDivisionError):
        return 0


def print_stats(numbers):
    filtered = [n for n in numbers if n is not None]
    if not filtered:
        print("No valid numbers to process")
        return
    print("Sum:", calculate_sum(filtered))
    print("Average:", safe_average(filtered))
    print("Count:", len(filtered))
    print("Max:", max(filtered))
    print("Min:", min(filtered))


print_stats(values)


unused_values = [1, 2, 3]


def debug_print(data):
    if data == None:
        print("No data")
    else:
        print("Data:", data)
