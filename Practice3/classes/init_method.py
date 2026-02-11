class Book:
    def __init__(self, title, author):
        """Инициализация свойств объекта через конструктор."""
        self.title = title
        self.author = author

my_book = Book("1984", "George Orwell")
print(f"Книга: {my_book.title}, Автор: {my_book.author}")