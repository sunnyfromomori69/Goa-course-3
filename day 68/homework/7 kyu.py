def series_sum(n):
    total = 0
    for i in range(1, n+1):
        total += 1 / (3*i - 2)
    return "{:.2f}".format(total)
# Sum of the first nth term of Series

def check_exam(arr1, arr2):
    total = 0
    for correct, answer in zip(arr1, arr2):
        if answer == correct:
            total += 4
        elif answer == "":
            total += 0
        else:
            total -= 1
    return max(total, 0)
# Check the exam

def remove_duplicate_words(s):
    seen = set()
    result = []
    for word in s.split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)

# Remove duplicate words