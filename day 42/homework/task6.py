animal = {
    "type": "dog",
    "name": "Bobby",
    "age": 5
}


animal_copy = animal.copy()
print("Original animal dictionary:", animal)
print("Copied animal dictionary:", animal_copy)

animal.clear()
animal_copy.clear()

print("Cleared original animal dictionary:", animal)
print("Cleared copied animal dictionary:", animal_copy)