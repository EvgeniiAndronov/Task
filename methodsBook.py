import json
import random
import string



def add_book(book):
    try:
        with open('data.json', 'r+') as file:
            data = json.load(file)
            print(data)
            book["id"] = generate_random_id()

            data.append(book)
            file.seek(0)
            json.dump(data, file)
    except Exception:
        with open('data.json', 'w') as file:
            book["id"] = generate_random_id()
            json.dump([book], file)

def generate_random_id() -> str:
    letters_and_digits = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(letters_and_digits) for i in range(10))
    return random_id

def delete_book(book_id):
    with open('data.json', 'r+') as file:
        data = json.load(file)
        update_data = [obj for obj in data if obj["id"] != book_id]
        # for obj in data:
        #     print(f"-{book_id}-\n-{obj['id']}-")
        #     if obj["id"] != book_id:
        #         print(f"{obj['id']}-")
        #         update_data.append(obj)

        file.seek(0)
        json.dump(update_data, file)
        file.truncate()
