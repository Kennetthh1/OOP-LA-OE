#la08
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book1 = Book("Kwento ko to", "Ako")
book2 = Book("His Into Her", "Maxine Lat Calibuso")
print(book1.title, book1.author)
print(book2.title, book2.author)
del book1.author
#print(book1.title, book1.author)
print(book2.title, book2.author)