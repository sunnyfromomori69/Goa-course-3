"https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python"
# Is it a palindrome?
def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    return False