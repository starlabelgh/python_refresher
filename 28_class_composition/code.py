class BookShelf:
    def __init__(self, quantity) -> None:
        self.quantity = quantity
        
    def __str__(self) -> str:
        return f"BookShelf with {self.quantity} books."
    
shelf = BookShelf(300)

print(shelf)


class Book(BookShelf):
    def __init__(self, name, quantity) -> None:
        super().__init__(quantity)
        self.name = name
        
    def __str__(self) -> str:
        return super().__str__()