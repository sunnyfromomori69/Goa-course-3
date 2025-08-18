def my_decorator(func):
    def wrapper():
        print("Calling the function...")
        result = func()  
        print("Function has been called.")
        return result
    return wrapper



my_decorator
def greet():
    return "Hello World"


print(greet())

# 3) შექმენით decorator ფუნქცია, რომელიც თავისთავად შექმნის wrapper ფუნქციას და დააბრუენბს მას. აიღეთ მარტივი greet ფუნქცია რომელიც აბრუნებს "Hello World"-ს და გამოიძახეთ მიანიჭეთ მას decorator. საბოლოოდ გამოიძახეთ greet ფუნქცია