class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


my_book = Book("The Knight in the Panther's Skin", "Shota Rustaveli", 600)
my_book.info()