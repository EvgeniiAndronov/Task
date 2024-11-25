from add_test_data import save_test_data
from methodsBook import *
from book import *


# Взаимодействуя с пользователем, добавляем книгу
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

# Взаимодействуя с пользователем, удаляем книгу
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

# Вспомогательный метод, определение поискового преоритета
def new_type(parametr) -> str:
    if parametr == "1":
        return "title"
    if parametr == "2":
        return "author"
    if parametr == "3":
        return "year"

# Взаимодействуя с пользователем, ищем книгу или книги
def user_find_book() -> None:
    try:
        print("1. Название книги\n2. Автор книги\n3. Год выпуска")
        typ = str(input("Введите параметр поиска книги: "))

        type_to_check = new_type(typ)

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

# Взаимодействуя с пользователем, отображаем все книги
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

# Вспомогательный метод определения смены статуса
def descriptor_user_data_status_book(status) -> bool:
    if status == "1":
        return False

    if status == "2":
        return True

# Взаимодействуя с пользователем, изменяем статус книги
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





list_command = """
    1. Добавление книги.
    2. Удаление книги.
    3. Поиск книги.
    4. Отображение всех книг.
    5. Изменение статуса книги(есть в наличии или нет).
    
    0. Завершение работы программы.
"""

helloMessage = f"""
    Привет! Это система управления библиотекой.
    Вот что она умеет делать:
"""

choose_option = "Выберете действие(введите номер действия): "

def main():
    flag = True
    print(helloMessage)
    while flag:
        print(list_command)
        option = str(input(choose_option))
        if option == "1":
            user_add_book()
        if option == "2":
            user_del_book()
        if option == "3":
            user_find_book()
        if option == "4":
            user_watch_all_book()
        if option == "5":
            user_change_status_book()
        if option == "0":
            flag = False


if __name__ == "__main__":
    # main()
    save_test_data()