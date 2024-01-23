# -*- coding: utf-8 -*-

import json
from pathlib import Path

import avro
import avro.schema
from avro.io import DatumReader, DatumWriter
from avro.datafile import DataFileReader, DataFileWriter


def save_schema():
    schema = {
        "namespace": "example.avro",
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "favorite_number", "type": ["int", "null"]},
            {"name": "favorite_color", "type": ["string", "null"]},
        ],
    }
    Path("user.avsc").write_text(json.dumps(schema, indent=4))


def load_schema() -> avro.schema.Schema:
    return avro.schema.parse(Path("user.avsc").read_text())


def write_data():
    schema = load_schema()
    data = [
        {"name": "Alyssa", "favorite_number": 256},
        {"name": "Ben", "favorite_number": 7, "favorite_color": "red"},
    ]
    with Path("users.avro").open("wb") as f:
        writer = DataFileWriter(f, DatumWriter(), schema)
        for record in data:
            writer.append(record)
        writer.close()


def read_data():
    with Path("users.avro").open("rb") as f:
        reader = DataFileReader(f, DatumReader())
        for user in reader:
            print(user)
        reader.close()


# save_schema()
# write_data()
# read_data()
