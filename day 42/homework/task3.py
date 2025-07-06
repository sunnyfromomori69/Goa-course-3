student = {
    "name": "Anna",
    "hobby": "reading",
    "height": 165,
    "weight": 55
}

student_name = student.get("name")
print("Name:", student_name)  

removed_height = student.pop("height")
print("Removed height:", removed_height)  


print("Updated student dictionary:", student)
