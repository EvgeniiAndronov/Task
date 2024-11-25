from methodsBook import *

class Book:
    def __init__(self, id, title, author, year, status):
        self.id: str = id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: bool = status


    def show_book(self):
        print(f"Название: {self.title}\nАвтор: {self.author}\nГод выпуска: {self.year}\nСтатус: {'В наличии' if self.status else 'Выдана'}")

