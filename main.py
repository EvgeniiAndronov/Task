import json
from methodsBook import *
from add_test_data import *

class Book:
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def add_book(self):
        book = {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

        add_book(book)

    def find_book(self):
        pass

    def change_status_book(self):
        pass

def user_add_book():
    try:
        title = str(input("Введите название книги: "))
        author = str(input("Введите автора книги: "))
        year = int(input("Введите год выпуска книги"))
        book = Book(title, author, year, year, True)
        book.add_book()
        print("Книга успешно добавлена!")
    except ValueError:
        print("Ввели некорректные данные, попробуйте еще раз")

def user_del_book():
    try:
        id = str(input("Введите id книги: "))
        delete_book(id)

    except ValueError:
        print("Ввели некорректные данные, попробуйте еще раз.")
    except Exception:
        print("Что-то пошло не так! Попробуйте еще раз.")


#
# save_test_data()
# user_del_book()



# book = Book(
#     id="s",
#     title="Title",
#     author="Author",
#     year=2004,
#     status=True
# )
#
# book.add_book()

