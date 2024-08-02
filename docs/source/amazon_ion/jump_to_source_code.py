# -*- coding: utf-8 -*-

import amazon.ion.simpleion as ion
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

text = ion.dumps(py_data, binary=False)
data = ion.loads(text, value_model=ion.IonPyValueModel.STRUCT_AS_STD_DICT)
print(data)
