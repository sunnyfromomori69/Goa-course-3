"https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python"
# Highest and Lowest
def high_and_low(numbers):
    numbers_array = numbers.split()

    int_numbers = []
    for number in numbers_array:
        int_numbers.append(int(number))

    high = max(int_numbers)
    low = min(int_numbers)

    return str(high) + " " + str(low)