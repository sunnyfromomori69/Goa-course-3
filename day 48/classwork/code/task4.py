"https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python"
#Mumbling 
def accum(s):
    result = ""
    i = 0

    for letter in s:
        big = letter.upper()
        small = letter.lower()
        group = big + small * i

        if i == 0:
            result = group
        else:
            result = result + "-" + group

        i = i + 1

    return result