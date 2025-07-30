"https://www.codewars.com/kata/54edbc7200b811e956000556/train/python"
# Counting sheep...
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s is True:
            count += 1
    return count