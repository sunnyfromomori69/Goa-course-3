"https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python"
# Isograms
def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)