"https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python"
# Regex validate PIN code
def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False

    for char in pin:
        if char < '0' or char > '9':
            return False

    return True