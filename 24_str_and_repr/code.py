class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # def __str__(self) -> str:
        # return f"My name is {self.name}, I am {self.age} years old."
    
    def __repr__(self) -> str:
        return f"<Person({self.name}, {self.age})>"
        
bob = Person("Bob", 35)
print(bob)