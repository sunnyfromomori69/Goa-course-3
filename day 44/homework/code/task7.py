"https://www.codewars.com/kata/56747fd5cb988479af000028/train/python"

# Get the Middle Character

def get_middle(s):
    l = len(s)
    if l % 2 == 0:
        return s[l//2 - 1] + s[l//2]
    else:
        return s[l//2]