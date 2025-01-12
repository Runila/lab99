class Book:
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        if self.year is None:
            return f"{self.title} -- книга написанная автором {self.author}"
        else:
            return f"{self.title} -- книга написанная автором {self.author} и опубликованная в  {self.title}."


book = Book("Пикни́к на обо́чине", " Братья Стругацкие")
book_2 = Book("Пикни́к на обо́чине", "Братья Стругацкие",year=1972)
print(book_2.get_info())