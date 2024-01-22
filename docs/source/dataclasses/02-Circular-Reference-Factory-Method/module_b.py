# -*- coding: utf-8 -*-
# content of module_b.py

import typing as T
import dataclasses

if T.TYPE_CHECKING:
    from module_a import A


@dataclasses.dataclass
class B:
    name: str = dataclasses.field()

    def to_a(self) -> "A":
        from module_a import A

        return A(name=self.name)

    @classmethod
    def from_a(cls, a: "A"):
        return cls(name=a.name)
