# -*- coding: utf-8 -*-

"""
我们有一个类 :class:`BaseContainer`, 它的大部分参数和返回值有的是 BaseModel 的实例,
有的是 BaseModel 的类本身. 那如果我要扩展 BaseModel, 同时在不修改 ``BaseContainer`` 类
的情况下如何同时保留正确的类型提示呢?

这是一个错误实现. 很多人会以为将类本身作为参数传入 ``__init__`` 中就可以了. 很遗憾, 这是 IDE
的功能的一部分, 强如 PyCharm 也无法正确提示.
"""

import typing as T


class BaseModel:
    def base_model_method(self):
        print("base_model_method")


T_BASE_MODEL = T.TypeVar("T_BASE_MODEL", bound=BaseModel)


class BaseContainer:
    """
    这个类的初始化函数接受的参数是 :class:`BaseModel` 的子类的类, 不是实例.
    get() 方法的返回值是 :class:`BaseModel` 的子类的实例.
    """

    def __init__(self, model_class: T.Type[T_BASE_MODEL]):
        self.model_class = model_class

    def get(self) -> T_BASE_MODEL:
        return self.model_class()


class MyModel(BaseModel):
    def my_model_method(self):
        print("my_model_method")


model_out = BaseContainer(BaseModel).get()
model_out.base_model_method()  # 能够正确提示

model_out = BaseContainer(MyModel).get()
model_out.my_model_method()  # 如何参数是子类则不能正确提示
