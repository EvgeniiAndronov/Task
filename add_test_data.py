import json

def save_test_data():
    data = [
        {
        "id": "1234567890",
        "title": "C/C++",
        "author": "B. Straustrup",
        "year": 2000,
        "status": True
    }, {
        "id": "2345678901",
        "title": "Delphy 7",
        "author": "E. Trompton",
        "year": 1999,
        "status": False
    }, {
        "id": "3456789012",
        "title": "Harry Potter",
        "author": "J. Rouling",
        "year": 1998,
        "status": True
    }
    ]
    with open('data.json', 'w') as file:
        json.dump(data, file)