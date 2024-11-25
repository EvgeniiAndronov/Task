import json
from methodsBook import *
from add_test_data import *
from book import *

def user_add_book() -> None:
    try:
        title = str(input("Введите название книги: "))
        author = str(input("Введите автора книги: "))
        year = int(input("Введите год выпуска книги: "))
        book = {
            "id": "none",
            "title": title,
            "author": author,
            "year": year,
            "status": True
        }
        add_book(book)
        print("Книга успешно добавлена!")
    except ValueError:
        print("Ввели некорректные данные, попробуйте еще раз")
    except TypeError:
        print("Ошибка введенных данных.")
    except Exception as e:
        print("Непредвиденная ошибка!")

def user_del_book() -> None:
    try:
        id = str(input("Введите id книги на удаление: "))
        delete_book(id)
    except ValueError:
        print("Ввели некорректные данные, попробуйте еще раз")
    except TypeError:
        print("Ошибка введенных данных.")
    except Exception as e:
        print("Непредвиденная ошибка!")


def new_type(parametr) -> str:
    if parametr == "1":
        return "title"
    if parametr == "2":
        return "author"
    if parametr == "3":
        return "year"


def user_find_book() -> None:
    try:
        print("1. Название книги\n2. Автор книги\n3. Год выпуска")
        typ = str(input("Введите параметр поиска книги: "))
        print(typ, "--------")
        type_to_check = new_type(typ)
        print(type_to_check, "--------")
        parametr = str(input("Введите параметр поиска: "))

        books: [dict] = find_books(parametr, type_to_check)

        for book in books:
            b: Book = Book(
                id=book.get("id"),
                title=book.get("title"),
                author=book.get("author"),
                year=book.get("year"),
                status=book.get("status")
            )
            print("\n")
            b.show_book()
            print("\n")
    except ValueError:
        print("Ввели некорректные данные, попробуйте еще раз")
    except TypeError:
        print("Ошибка введенных данных.")
    except Exception as e:
        print("Непредвиденная ошибка!")


def user_watch_all_book() -> None:
    try:
        data = all_books()
        for book in data:

            b: Book = Book(
                id=book.get("id"),
                title=book.get("title"),
                author=book.get("author"),
                year=book.get("year"),
                status=book.get("status")
            )
            print(f"-----{b.id}------")
            b.show_book()
            print("\n")

    except ValueError:
        print("Ввели некорректные данные, попробуйте еще раз")
    except TypeError:
        print("Ошибка введенных данных.")
    except Exception as e:
        print("Непредвиденная ошибка!")

def descriptor_user_data_status_book(status) -> bool:
    if status == "1":
        return False

    if status == "2":
        return True

def user_change_status_book() -> None:
    try:
        id = str(input("Введите id книги, у которой хотите изменить статус: "))
        book: [dict] = find_books(id, "id")[0]
        b: Book = Book(
            id=book.get("id"),
            title=book.get("title"),
            author=book.get("author"),
            year=book.get("year"),
            status=book.get("status")
        )
        b.show_book()
        status = str(input("Введите новый статус:\nЕсли хотите изменить статус на 'Выдана' - введите 1,\nесли хотите изменить статус на 'В наличии' - введите 2\n"))

        change_book_status(book.get("id"), descriptor_user_data_status_book(status))
        book_new: [dict] = find_books(id, "id")[0]
        b_new: Book = Book(
            id=book_new.get("id"),
            title=book_new.get("title"),
            author=book_new.get("author"),
            year=book_new.get("year"),
            status=book_new.get("status")
        )
        b_new.show_book()


    except ValueError:
        print("Ввели некорректные данные, попробуйте еще раз")
    except TypeError:
        print("Ошибка введенных данных.")
    except Exception as e:
        print("Непредвиденная ошибка!")

# # add test data
# save_test_data()
#
# print("all books------------------")
# user_watch_all_book()
#
# # save_test_data()
# print("del book--------------------")
# user_del_book()
#
# print("find book -------------------")
# user_find_book()
#
# print("change status book-----------")
# user_change_status_book()

# print("add book --------------------")
# user_add_book()


