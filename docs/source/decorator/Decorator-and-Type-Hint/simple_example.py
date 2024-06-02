# -*- coding: utf-8 -*-

import decorator


@decorator.decorator
def before_and_after(func, *args, **kwargs):
    print(f"--- before {func} ---")
    result = func(*args, **kwargs)
    print(f"--- after {func} ---")
    return result


class User:
    @before_and_after
    def say_hello_method(self, name: str):
        print(f"say_hello_method: Hello {name}")

    @property
    @before_and_after
    def greeting_property(self):
        print(f"greeting: Greeting")
        return None

    @classmethod
    @before_and_after
    def say_hello_classmethod(cls, name: str):
        print(f"say_hello_classmethod: Hello {name}")

    @staticmethod
    @before_and_after
    def say_hello_staticmethod(name: str):
        print(f"say_hello_staticmethod: Hello {name}")


@before_and_after
def add_two(first: int, second: int) -> int:
    return first + second


user = User()

# 这些 typehint 在 PyCharm 2024 中都没有问题
user.say_hello_method(name="Alice")
_ = user.greeting_property
User.say_hello_classmethod(name="Bob")
User.say_hello_staticmethod(name="Charlie")
assert add_two(first=1, second=2) == 3
