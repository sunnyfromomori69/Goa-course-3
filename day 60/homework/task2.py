class Library:
    def __init__(self, books, secret_code):
        self._books = books
        self.__secretCode = secret_code

    @staticmethod
    def calculate_fine(days_late, rate_per_day):
        return days_late * rate_per_day


lib = Library(["Book A", "Book B"], "XYZ123")

print("Books:", lib._books)
print("Late fee:", Library.calculate_fine(5, 2))