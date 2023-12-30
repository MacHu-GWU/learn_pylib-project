# -*- coding: utf-8 -*-

"""
我们有一个类 :class:`BaseContainer`, 它的大部分参数和返回值有的是 BaseModel 的实例,
有的是 BaseModel 的类本身. 那如果我要扩展 BaseModel, 同时在不修改 ``BaseContainer`` 类
的情况下如何同时保留正确的类型提示呢? 这个例子和前一个例子的唯一区别是这个类是一个 dataclass.

答案是用 `TypeVar <https://docs.python.org/3/library/typing.html#typing.TypeVar>`_ + `Generic <https://docs.python.org/3/library/typing.html#typing.Generic>`_.

这是一个正确实现.
"""

import typing as T
import dataclasses


@dataclasses.dataclass
class BaseModel:
    def base_model_method(self):
        print("base_model_method")


T_BASE_MODEL = T.TypeVar("T_BASE_MODEL", bound=BaseModel)


@dataclasses.dataclass
class BaseContainer(T.Generic[T_BASE_MODEL]):
    """
    这个类的初始化函数接受的参数是 :class:`BaseModel` 的子类的类, 不是实例.
    get() 方法的返回值是 :class:`BaseModel` 的子类的实例.
    """

    model_class: T.Type[T_BASE_MODEL] = dataclasses.field()

    def get(self) -> T_BASE_MODEL:
        return self.model_class()


class MyModel(BaseModel):
    def my_model_method(self):
        print("my_model_method")


class MyContainer(BaseContainer[MyModel]):
    pass


model_out = MyContainer(MyModel).get()
model_out.my_model_method()  # 能够正确提示
