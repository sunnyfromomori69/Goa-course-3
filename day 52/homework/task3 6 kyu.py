def alphabet_position(text):
    text = text.lower()  # make all letters lowercase
    result = []
    for char in text:
        if char.isalpha():  # only letters
            result.append(str(ord(char) - ord('a') + 1))
    return ' '.join(result)