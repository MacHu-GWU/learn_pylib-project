# -*- coding: utf-8 -*-

from dynamodb_json import json_util
from rich import print as rprint

py_data = {
    "id": 1,
    "name": "Alice",
    "age": 25,
    "weight": 94.7,
    "bio": {
        "dob": "1990-01-01",
        "address": "123 Main St.",
        "hometown": None,
    },
    "relationships": [
        {"name": "Bob", "relation": "friend"},
        {"name": "Charlie", "relation": "father"},
    ],
}

s = json_util.dumps(py_data)
rprint(f"{type(s) = }")  # str
print(s)
"""
{"id": {"N": "1"}, "name": {"S": "Alice"}, "age": {"N": "25"}, "weight": {"N": "94.7"}, "bio": {"M": {"dob": {"S": "1990-01-01"}, "address": {"S": "123 Main St."}, "hometown": {"NULL": true}}}, "relationships": {"L": [{"M": {"name": {"S": "Bob"}, "relation": {"S": "friend"}}}, {"M": {"name": {"S": "Charlie"}, "relation": {"S": "father"}}}]}}
"""

d = json_util.dumps(py_data, as_dict=True)
rprint(f"{type(d) = }")  # dict
rprint(d)  #
"""
{
    'id': {'N': '1'},
    'name': {'S': 'Alice'},
    'age': {'N': '25'},
    'weight': {'N': '94.7'},
    'bio': {
        'M': {
            'dob': {'S': '1990-01-01'},
            'address': {'S': '123 Main St.'},
            'hometown': {'NULL': True}
        }
    },
    'relationships': {
        'L': [
            {'M': {'name': {'S': 'Bob'}, 'relation': {'S': 'friend'}}},
            {'M': {'name': {'S': 'Charlie'}, 'relation': {'S': 'father'}}}
        ]
    }
}
"""

res = json_util.loads(s)
rprint(f"{type(res) = }")  # dict
rprint(res)  # dict
"""
{
    'id': 1,
    'name': 'Alice',
    'age': 25,
    'weight': 94.7,
    'bio': {'dob': '1990-01-01', 'address': '123 Main St.', 'hometown': None},
    'relationships': [
        {'name': 'Bob', 'relation': 'friend'},
        {'name': 'Charlie', 'relation': 'father'}
    ]
}
"""

res = json_util.loads(d)
rprint(f"{type(res) = }")  # dict
rprint(res)  # dict
"""
{
    'id': 1,
    'name': 'Alice',
    'age': 25,
    'weight': 94.7,
    'bio': {'dob': '1990-01-01', 'address': '123 Main St.', 'hometown': None},
    'relationships': [
        {'name': 'Bob', 'relation': 'friend'},
        {'name': 'Charlie', 'relation': 'father'}
    ]
}
"""
