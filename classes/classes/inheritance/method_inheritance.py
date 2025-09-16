class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def book_info(self):
        print(f"{self.title} is authored by {self.author}")

class Fiction(Book):
    def __init__(self, author, title, publisher):
        super().__init__(author, title)
        self.publisher = publisher

    def book_info(self):
        print(f"{self.title} is authored by {self.author} and published by {self.publisher}")

    def invoke_base_class_method(self):
        super().book_info()

silva_book = Fiction("Daniel Silva", "Prince of Fire", "Berkley")
silva_book.book_info()
silva_book.invoke_base_class_method()