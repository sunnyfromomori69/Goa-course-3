def even_sum(border):
    total = 0
    for i in range(0, border + 1):
        if i % 2 == 0:  
            total += i
    return total
print(even_sum(10))
print(even_sum(7))   