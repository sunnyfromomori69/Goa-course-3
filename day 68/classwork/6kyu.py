def to_camel_case(text):
    parts = text.replace('-', '_').split('_')
    result = parts[0]

    for i in range(1, len(parts)):
        word = parts[i]
        result += word[0].upper() + word[1:]

    return result