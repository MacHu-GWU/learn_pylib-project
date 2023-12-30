# -*- coding: utf-8 -*-

"""
我有一个 :class:`MyItem` 类. 是所有跟 Item 相关的类的基类, 并且用户可以扩展这个类.
我还有一个 :class:`MyClass` 的类. 大部分的参数和方法都是返回一个 :class:`MyItem` 的实例.

我如何允许用户扩展 MyClass 和 MyItem 并且还能获得正确的类型提示呢?

答案是用 `TypeVar <https://docs.python.org/3/library/typing.html#typing.TypeVar>`_ + `Generic <https://docs.python.org/3/library/typing.html#typing.Generic>`_.

本实现是将 MyItem 的子类的类型作为一个 Generic 参数在定义 MyClass 的子类时传入.
"""

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
item.say_hi()  # 能够正确提示
