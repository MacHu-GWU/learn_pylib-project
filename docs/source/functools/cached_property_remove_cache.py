# -*- coding: utf-8 -*-

"""
Example: remove cached property cache.
"""

import dataclasses
from functools import cached_property


@dataclasses.dataclass
class Person:
    first_name: str
    last_name: str

    @cached_property
    def full_name(self):
        print("call full name")
        return f"{self.first_name} {self.last_name}"

    def reset_full_name_cache(self):
        try:
            del self.full_name
        except AttributeError:
            pass


p = Person("John", "Doe")
p.reset_full_name_cache()
print(p.full_name)
print(p.full_name)

p.reset_full_name_cache()
print(p.full_name)
