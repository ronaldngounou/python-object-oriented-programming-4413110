# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

# We made the monolithic class to have different classes responsible for each feature

class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price

        self.author = author 

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)
    
    def get_book_pagecount(self):
        result = 0 
        for chapter in self.chapters:
            result += chapter.pagecount 
        return result 

class Author:
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname 
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter: 
    def __init__(self, name, pagecount):
        self.name = name 
        self.pagecount = pagecount

author = Author("Leo", "Tolstoy")

b1 = Book("War and Peace", 39.0, author)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
print(b1.get_book_pagecount())