class publisher:
    def __init__(self,name):
        self.name=name
class book(publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
class python(book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price=price
        self.pages=pages
    def display(self):
        print(f"Publisher: {self.name}") 
        print(f"Title: {self.title}") 
        print(f"Author: {self.author}") 
        print(f"Price: {self.price}") 
        print(f"Number of Pages: {self.pages}")

python_book = python("O'Reilly Media", "Learning Python", "Mark Lutz", 45.99, 1594) 
python_book.display()