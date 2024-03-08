# -*- coding: utf-8 -*-

import parse

template = "[id={id}][name={name}]"
data = {"id": "id-1", "name": "Alice"}

text = template.format(**data)
assert text == "[id=id-1][name=Alice]"

# access key value pairs
res = parse.parse(template, text)
assert res.named == data

# text doesn't match template
res = parse.parse(template, "id = id-1, name = alice")
assert res is None
