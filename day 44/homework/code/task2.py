"https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python"
#Calculate BMI
def bmi(weight, height):
    value = weight / (height ** 2)
    if value <= 18.5:
        return "Underweight"
    elif value <= 25.0:
        return "Normal"
    elif value <= 30.0:
        return "Overweight"
    else:
        return "Obese"