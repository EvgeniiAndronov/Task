import json

def save_test_data():
    data = [
        {
        "id": "1234567890",
        "title": "title",
        "author": "author",
        "year": 2000,
        "status": True
    }, {
        "id": "2345678901",
        "title": "test",
        "author": "test",
        "year": 1999,
        "status": False
    }, {
        "id": "3456789012",
        "title": "Harry Potter",
        "author": "Rouling",
        "year": 1998,
        "status": True
    }
    ]
    with open('data.json', 'w') as file:
        json.dump(data, file)