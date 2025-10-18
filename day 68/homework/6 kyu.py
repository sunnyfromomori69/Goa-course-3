def unique_in_order(sequence):
    result = []
    for item in sequence:
        if not result or result[-1] != item:
            result.append(item)
    return result

# Unique In Order

def tribonacci(signature, n):
    result = signature[:n]
    while len(result) < n:
        result.append(sum(result[-3:]))
    return result

# Tribonacci Sequence

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
# Find the unique number