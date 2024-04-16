# -*- coding: utf-8 -*-

import typing as T
from pathlib import Path
from diskcache import Cache
from pyairtable import Api
from rich import print as rprint

cache = Cache(str(Path.home().joinpath(".projects", "pyairtable", ".cache")))

path_pac = Path.home().joinpath(".projects", "pyairtable", "pac")
TOKEN = path_pac.read_text().strip()
api = Api(TOKEN)

base_name = "Prompt Engineer"
_key = "Prompt Engineer base id"
prompt_engineer_base_id = cache.get(_key)
if prompt_engineer_base_id is None:
    res = api.bases()
    for base in res:
        if base.name == base_name:
            prompt_engineer_base_id = base.id
            cache.set(_key, prompt_engineer_base_id)
            break
    if prompt_engineer_base_id is None:
        raise ValueError(f"Can not find base with name {base_name}")

prompt_engineer_base = api.base(base_id=prompt_engineer_base_id)
_key = "prompt engineer base tables"
table_mapper: T.Dict[str, str] = cache.get(_key)
if table_mapper is None:
    table_mapper = {}
    for table in prompt_engineer_base.tables():
        table_mapper[table.name] = table.id
    cache.set(_key, table_mapper)

tb = api.table(prompt_engineer_base_id, table_mapper["Prompt"])
for record in tb.all():
    print(record)
