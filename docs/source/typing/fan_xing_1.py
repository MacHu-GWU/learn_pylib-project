# -*- coding: utf-8 -*-

"""
我们有一个函数 :func:`func`, 它的参数和返回值都是 BaseModel 的实例. 那如果我要扩展 BaseModel,
同时在不修改 ``func()`` 函数的情况下如何同时保留正确的类型提示呢?

本例是一个错误示范.
"""


class BaseModel:
    def base_model_method(self):
        print("base_model_method")


def func(
    model: BaseModel,
) -> BaseModel:
    """
    这个函数接受的参数是 :class:`BaseModel` 的子类，返回值也是 :class:`BaseModel` 的子类.
    """
    return model


class MyModel(BaseModel):
    def my_model_method(self):
        print("my_model_method")


model_out = func(MyModel())
model_out.my_model_method() # 无法正确提示
