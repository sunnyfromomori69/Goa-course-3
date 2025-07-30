"https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python"
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
"https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python"
def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

"https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python"
def fake_bin(x):
    result = ""
    for digit in x:
        if int(digit) < 5:
            result += '0'
        else:
            result += '1'
    return result

"https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python"
def reverse_seq(n):
    return list(range(n, 0, -1))

"https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python"
def count_sheep(n):
    result = ""
    for i in range(1, n + 1):
        result += f"{i} sheep..."
    return result

"https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python"
def remove_exclamation_marks(s):
    return s.replace('!', '')

"https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python"
def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)