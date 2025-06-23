def main_min(arr):
    smallest = arr[0]
    for number in arr:
        if number < smallest:
            smallest = number
        return main_min

def max_min(arr):
       tallest = arr[0]
       for number in arr:
            if number > tallest:
                 tallest = number
                 return max_min