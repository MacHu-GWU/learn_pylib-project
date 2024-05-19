# -*- coding: utf-8 -*-

"""
这个例子展示了 contextmanager 和 classmethod 一起使用时的用法. @classmethod 必须在上面.
社区有一个库 `decorator <https://pypi.org/project/decorator/>`_ 对标准库做了一些改进,
如果你使用的是 ``decorator.contextmanager`` 那么这个函数的入参和 yield 的值的 type hint 都 **会** 正常工作.
"""

from decorator import contextmanager


class User:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.name}")

    @classmethod
    @contextmanager
    def start(cls, name: str):  # 无需显式使用 ``-> T.Generator["User", None, None]``
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


# type hint in ``start()`` is working fine in PyCharm
with User.start(name="Alice") as user:
    user.say_hello()  # type hint in ``user`` is working fine in PyCharm

"""
Output:

Start
Hello, I am Alice
Happy End
Finally
"""
