def reverse_words(text):
    return ' '.join(text.split()[::-1])

2.
def remove_smallest(numbers):
    if not numbers:
        return []
    numbers_copy = numbers.copy()        
    numbers_copy.remove(min(numbers_copy)) 
    return numbers_copy

3.
def stray(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num
        
4.
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())