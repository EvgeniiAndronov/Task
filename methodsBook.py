import json
import random
import string
from book import *

# Добавление книги, на вход dict с полями класса книги
def add_book(book) -> None:
    try:
        with open('data.json', 'r+') as file:
            data = json.load(file)
            book["id"]: str = generate_random_id()

            data.append(book)
            file.seek(0)
            json.dump(data, file)
    except FileNotFoundError:
        with open('data.json', 'w') as file:
            book["id"] = generate_random_id()
            json.dump([book], file)
    except FileExistsError:
        print("Файл уже обрабатывается")
    except Exception as e:
        print(e)
        print("Непредвиденная ошибка! Попробуйте снова.")

# генерирование случайного id дял книги, 10 строковых символов
def generate_random_id() -> str:
    letters_and_digits = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(letters_and_digits) for _ in range(10))
    return random_id

# Удаление книги, на вход строка, где написан id книги
def delete_book(book_id) -> None:
    try:
        with open('data.json', 'r+') as file:
            data = json.load(file)
            update_data = [obj for obj in data if obj["id"] != book_id]
            # for obj in data:
            #     print(f"-{book_id}-\n-{obj['id']}-")
            #     if obj["id"] != book_id:
            #         print(f"{obj['id']}-")
            #         update_data.append(obj)

            file.seek(0)
            json.dump(update_data, file, sort_keys=True)
            file.truncate()
    except FileNotFoundError:
        print("Файл не найден! Создайте первую запись.")
    except Exception as e:
        print("Непредвиденная ошибка обработки")

# поиск книги, на вход аргумент поиска(название, автор или год), а так же тип параметра поиска(title, author, year), вернет список dict
def find_books(parametr, typ) -> [dict]:
    data_to_ret = []
    try:
        with open('data.json', 'r') as file:
            if typ == "year":
                try:
                    parametr = int(parametr)
                except ValueError:
                    print("Введены некорректные данные")
                    return [{"id": "empty",
                            "title": "empty",
                            "author": "empty",
                            "year": 2000,
                            "status": False
                            }]
            data = json.load(file)
            for obj in data:
                if obj[f"{typ}"] == parametr:
                    data_to_ret.append(obj)
        return data_to_ret
    except FileNotFoundError:
        print("Файл не найден! Создайте первую запись.")
    except ValueError:
        print("Ошибка введенных данных.")
    except Exception as e:
        print("Непредвиденная ошибка обработки")

def all_books() -> list:
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data

# Изменение состояния книги, на вход идут id книги и новый статус в формате bool
def change_book_status(book_id, new_status) -> None:
    try:
        with open('data.json', 'r+') as file:
            data = json.load(file)
            for obj in data:
                if obj["id"] == book_id:
                   obj["status"] = new_status

            file.seek(0)
            json.dump(data, file)
    except FileNotFoundError:
        print("Файл не найден! Создайте первую запись.")
    except ValueError:
        print("Ошибка введенных данных.")
    except Exception as e:
        print("Непредвиденная ошибка обработки")

