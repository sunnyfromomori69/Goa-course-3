my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list) 


my_tuple = tuple(my_list)
print("Converted to tuple:", my_tuple)  # This prints the list as a tuple

# Convert the tuple back to a list using list()
new_list = list(my_tuple)
print("Converted back to list:", new_list)     #This prints the tuple converted back into a list