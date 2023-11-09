# -*- coding: utf-8 -*-

import typing as T

T_ITEM = T.TypeVar("T_ITEM")


class MyClass(T.Generic[T_ITEM]):
    def __init__(self, item_type: T.Type[T_ITEM]):
        self.item_type = item_type

    def get_item(self) -> T_ITEM:
        return None


class MyItem:
    def say_hi(self):
        print("say hi")


my_class = MyClass(MyItem)
item = my_class.get_item()
item.say_hi()