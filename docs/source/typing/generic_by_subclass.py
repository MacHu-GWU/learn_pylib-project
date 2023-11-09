# -*- coding: utf-8 -*-

import typing as T

T_ITEM = T.TypeVar("T_ITEM")


class MyClass(T.Generic[T_ITEM]):
    def get_item(self) -> T_ITEM:
        return None


class MyItem:
    def say_hi(self):
        print("say hi")


class MyNewClass(MyClass[MyItem]):
    pass


my_new_class = MyNewClass()
item = my_new_class.get_item()
item.say_hi()
