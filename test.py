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
