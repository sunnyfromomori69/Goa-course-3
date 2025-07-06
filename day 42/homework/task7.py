def update_and_remove(dictionary):
    dictionary.update({"age": 14})
    removed_item = dictionary.popitem()
    print("Updated dictionary:", dictionary)
    print("Removed item:", removed_item)
    return dictionary, removed_item
