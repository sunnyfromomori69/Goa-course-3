"https://www.codewars.com/kata/56606694ec01347ce800001b/train/python"
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

"https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python"
def find_next_square(n):
    root = n ** 0.5
    if root == int(root):
        return int((root + 1) ** 2)
    else:
        return -1
    
"https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python"
def binary_array_to_number(arr):
    result = ""
    for bit in arr:
        result += str(bit)
    return int(result, 2)

"https://www.codewars.com/kata/5949481f86420f59480000e7/train/python"
def odd_or_even(arr):
    total = sum(arr)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"