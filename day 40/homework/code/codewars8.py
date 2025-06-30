"https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python"
# Shortest Word
def find_short(s):
    words = s.split()
    shortest = len(words[0])
    for word in words:
        if len(word) < shortest:
            shortest = len(word)
    return shortest