# -*- coding: utf-8 -*-

"""
这个例子展示了 contextmanager 和 classmethod 一起使用时的用法. @classmethod 必须在上面.
由于标准库实现的时候还没有 type hint, 这个函数的入参和 yield 的值的 type hint 都 **不会** 正常工作.
"""

import typing as T
import contextlib


class User:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.name}")

    @classmethod
    @contextlib.contextmanager
    def start(cls, name: str) -> T.Generator["User", None, None]:
        try:
            print("Start")
            user = cls(name=name)
            yield user
            print("Happy End")
        except Exception as e:
            print(f"Exception: {e}")
            raise e
        finally:
            print("Finally")


# type hint in ``start()`` is NOT working fine in PyCharm
with User.start(name="Alice") as user:
    # type hint in ``user`` is NOT working fine in PyCharm
    user.say_hello()

"""
Output:

Start
Hello, I am Alice
Happy End
Finally
"""
