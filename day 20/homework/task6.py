"""7) მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)"""


vowels = "aeiouAEIOU"
sentence = input("Enter a sentence: ")

vowel_count = 0
consonant_count = 0
length = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1
    elif char not in vowels and char != " ":
        consonant_count += 1
    length += 1

print(f"Vowels in total: {vowel_count}")
print(f"Consonants in total: {consonant_count}")
print(f"Sentence length: {length}")