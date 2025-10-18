def create_range(start, end):
    numbers = []
    i = start
    while i <= end:
        numbers.append(i)
        i += 1
    return numbers

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
