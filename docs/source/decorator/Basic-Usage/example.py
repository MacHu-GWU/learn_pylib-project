# -*- coding: utf-8 -*-

from decorator import decorator


@decorator
def before_and_after(func, *args, **kwargs):
    print("before")
    result = func(*args, **kwargs)
    print("after")
    return result


@before_and_after
def my_func():
    message = "hello world"
    print(message)
    return


print("--- test my_func() ---")
my_func()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @before_and_after
    def say_hello(self):
        print(f"Hello from {self.first_name}")

    # when stacking with other decorator,
    # use decorator made by ``decorator`` library first
    @property
    @before_and_after
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"full name is {full_name}")
        return full_name


alice = User(first_name="alice", last_name="boon")

print("--- test Alice.say_hello() ---")
alice.say_hello()

print("--- test Alice.full_name() ---")
alice.full_name
