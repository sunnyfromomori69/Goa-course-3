"https://www.codewars.com/kata/59a9919107157a45220000e1/train/python"
# Find all occurrences of an element in an array

def find_all(array, n):
    result =[]
    
    for index in range(len(array)):
        if array[index] == n:
            result.append(index)
            
    return result