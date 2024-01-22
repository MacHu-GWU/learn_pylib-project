# -*- coding: utf-8 -*-

from module_a import A
from module_b import B

a = A(name="alice")
b = B(name="bob")

print(f"{a.to_b() = }")
print(f"{A.from_b(b) = }")
print(f"{b.to_a() = }")
print(f"{B.from_a(a) = }")
