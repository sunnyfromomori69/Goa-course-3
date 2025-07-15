"https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python"
#Convert number to reversed array of digits
def digitize(n):
    s = str(n)
    r = s[::-1]
    result = []
    for digit in r:
        result.append(int(digit))
    return result