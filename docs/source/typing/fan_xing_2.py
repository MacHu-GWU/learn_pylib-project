# -*- coding: utf-8 -*-

"""
我们有一个函数 :func:`func`, 它的参数和返回值都是 BaseModel 的实例. 那如果我要扩展 BaseModel,
同时在不修改 ``func()`` 函数的情况下如何同时保留正确的类型提示呢?

答案是在定义 func 的入参出参时使用 `TypeVar <https://docs.python.org/3/library/typing.html#typing.TypeVar>`_
泛型.
"""
import typing as T


class BaseModel:
    def base_model_method(self):
        print("base_model_method")


T_BASE_MODEL = T.TypeVar("T_BASE_MODEL", bound=BaseModel)


def func(
    model: T_BASE_MODEL,
) -> T_BASE_MODEL:
    """
    这个函数接受的参数是 :class:`BaseModel` 的子类，返回值也是 :class:`BaseModel` 的子类.
    """
    return model


class MyModel(BaseModel):
    def my_model_method(self):
        print("my_model_method")


model_out = func(MyModel())
model_out.my_model_method() # 能够正确提示
