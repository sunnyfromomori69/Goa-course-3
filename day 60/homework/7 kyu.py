def get_sum(a, b):
    if a == b:
        return a
    lower, upper = (a, b) if a < b else (b, a)
    count = upper - lower + 1
    return (lower + upper) * count // 2

# 2

def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))

# 3
def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

# 4
def sum_digits(n):
    n = abs(n)
    total = 0
    for digit in str(n):
        total += int(digit)
    return total