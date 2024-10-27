# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

# __user__ friendly string to be provided to the user 

# __repr__ is used for debugging purposes, more for developpers 
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price


    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: use the __repr__ method to return an obj representation
    # This helps debuggin make easier 
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1) # before __str__: <__main__.Book object at 0x100d7f850>
print(b2) # before __str__: <__main__.Book object at 0x100d7fa50>
print(str(b1))
print(repr(b2))