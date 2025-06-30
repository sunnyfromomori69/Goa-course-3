"https://www.codewars.com/kata/515e271a311df0350d00000f/train/python"
#Square(n) Sum
def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total