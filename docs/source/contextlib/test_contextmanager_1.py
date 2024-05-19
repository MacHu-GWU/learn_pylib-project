# -*- coding: utf-8 -*-

"""
这个例子展示了 contextmanager 的基本用法. 如果你用它来装饰一个简单函数, 那么这个函数的入参和
yield 的值的 type hint 都会正常工作.
"""

import contextlib


class User:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.name}")


@contextlib.contextmanager
def start(name: str):
    try:
        print("Start")
        user = User(name=name)
        yield user
        print("Happy End")
    except Exception as e:
        print(f"Exception: {e}")
        raise e
    finally:
        print("Finally")


# type hint in ``start()`` is working fine
with start(name="Alice") as user:
    # type hint in ``user`` is working fine
    user.say_hello()

"""
Output:

Start
Hello, I am Alice
Happy End
Finally
"""

# type hint in ``start()`` is working fine
with start(name="Alice") as user:
    # type hint in ``user`` is working fine
    user.say_hello()
    raise ValueError("Something went wrong")

"""
Output:

Start
Hello, I am Alice
Exception: Something went wrong
Finally
Traceback (most recent call last):
  File "/path/to/learn_pylib-project/docs/source/contextlib/test_contextmanager_1.py", line 42, in <module>
    raise ValueError("Something went wrong")
ValueError: Something went wrong
"""
