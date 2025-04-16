number = int(input("Enter the number: "))

while number in range(100):
    print(number)
    number += 2
    if number > 0:
        print("Positive.")
if number < 0:
    print("Negative")