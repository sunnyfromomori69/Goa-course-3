def factorial(int):
    result = 1
    for i in range(1, int + 1):
        result *= i
    return result

print(factorial(5))