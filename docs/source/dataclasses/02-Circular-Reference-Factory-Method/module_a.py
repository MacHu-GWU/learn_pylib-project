# -*- coding: utf-8 -*-
# content of module_a.py

import typing as T
import dataclasses

if T.TYPE_CHECKING:
    from module_b import B


@dataclasses.dataclass
class A:
    name: str = dataclasses.field()

    def to_b(self) -> "B":
        from module_b import B

        return B(name=self.name)

    @classmethod
    def from_b(cls, b: "B"):
        return cls(name=b.name)
