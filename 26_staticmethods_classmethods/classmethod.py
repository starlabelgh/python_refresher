class Book:
    TYPES = ("hardcover", "paperback")
    
    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"<Book: {self.name}, Type: {self.book_type}, Weighing: {self.weight}>"

book = Book("Harry Potter", "hardcover", 1500)  
print(book)