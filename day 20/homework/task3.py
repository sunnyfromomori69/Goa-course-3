user_number = int(input("enter the num: "))

while user_number is range(100):
    if user_number < 0:
        print("even and negative")
        user_number+2
else:
    print("Odd and negative")