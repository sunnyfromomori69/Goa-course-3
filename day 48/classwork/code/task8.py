"https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python"
#Abbreviate a Two Word Name
def abbrev_name(name):
    first, second = name.split()
    return first[0].upper() + "." + second[0].upper()