"https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python"
# Reversed Words
def reverseWords(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)