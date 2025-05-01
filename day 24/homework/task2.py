words = ["apple", "banana", "cherry", "date", "elderberry"]
reversed_words = words[::-1]

counter = 0
for word in (reversed_words):
    if counter % 2 == 1:
        print(word)
    counter += 1