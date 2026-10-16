class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  def info(self):
    return f'Книга - {self.title}, Автор - {self.author}, Год - {self.year}'

  def __str__(self):
    return self.info()

  def __eq__(self, other):
    return isinstance(other, Book) and self.tetle == other.title

  @property
  def age(self):
    return datatime.now().year - self.year

  @classmethod
  def from_string(cls, data):
     title, author, year = data.split(';')
     return cls(title, author, int(year))

book_cats = Book('Путешествия котов', 'Лорд де Кот', 2000)
print(book_cats.info())


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format
    def info(self):
        return f'Книга - {self.title}, Автор - {self.author}, Год - {self.year} формат - {self.format}'
ebook_dogs = Ebook('Путешествия собак', 'Лорд де Пёс', 2002, 'Электронный')

print(ebook_dogs.info())