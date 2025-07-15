"https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python"
#Jaden Casing Strings
def to_jaden_case(string):
    words = string.split()      
    i = 0
    while i < len(words):
        words[i] = words[i].capitalize()  
        i += 1
    return ' '.join(words)       
