
numbers = set()


numbers.add(3)  
numbers.add(6)

numbers.remove(3)  
numbers.remove(6)


numbers.add(2)
numbers.add(4)


even_numbers = {2, 4, 6, 8}


combined = numbers.union(even_numbers)
print("Union:", combined)  


common = numbers.intersection(even_numbers)

print("Intersection:", common)  

diff = numbers.difference(even_numbers)
print("Difference:", diff)  

print("numbers:", numbers)
print("even_numbers:", even_numbers)
