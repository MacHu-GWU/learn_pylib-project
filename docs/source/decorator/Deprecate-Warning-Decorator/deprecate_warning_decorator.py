# -*- coding: utf-8 -*-

"""
在维护一个开源项目时, 随着版本的推进, 很多旧的 API 会不推荐使用了, 但是为了兼容性, 一般维护着
不会粗暴的将这个 API 删除. 正确的做法是实现一个新的 API 来取代这个 API, 然后在旧的 API 上
加上 PendingDeprecationWarning, 让开发者自己看到这个 API 以后要准备被 deprecate 了.
然后在 1 - 2 个版本时间后, 再在旧的 API 上加上 DeprecationWarning, 让旧的 API 依然能够工作,
但是明确说明什么时候这个 API 会被彻底删除, 并且提示用户使用新的 API. 再经过再经过 1 - 2 个
版本时间后, 再将旧的 API 删除.

这种做法在 Python 中一般由装饰器实现.
"""

import warnings
from decorator import decorator


@decorator
def mark_pending_deprecation(func, *args, **kwargs):
    """
    这个不是给最终用户看的, 这个是给开发者自己看的.
    """
    warnings.warn(
        f"{func.__name__} will be deprecated soon, it will be marked as deprecated from A.B.C",
        PendingDeprecationWarning,
    )
    result = func(*args, **kwargs)
    return result


@decorator
def mark_deprecation(func, *args, **kwargs):
    """
    这是给最终用户看的, 提示用户使用新的 API.
    """
    warnings.warn(
        f"{func.__name__} is deprecated, it will be deleted from X.Y.Z, "
        f"you should use 'this' API instead",
        DeprecationWarning,
    )
    result = func(*args, **kwargs)
    return result


@mark_pending_deprecation
def my_func(name: str):
    print(f"Hello {name} from my_func")


class Model:
    @mark_pending_deprecation
    def __init__(self, name: str):
        print("Construct an instance of class Model")
        self.name = name

    @mark_pending_deprecation
    def my_method(self):
        print(f"Hello {self.name} from Model.my_method")

    @property
    @mark_pending_deprecation
    def my_property(self):
        print(f"Hello {self.name} from Model.my_property")
        return None

    @classmethod
    @mark_deprecation
    def my_classmethod(cls, name: str):
        print(f"Hello {name} from Model.my_classmethod")

    @staticmethod
    @mark_deprecation
    def my_staticmethod(name: str):
        print(f"Hello {name} from Model.my_staticmethod")


if __name__ == "__main__":
    """
    打印的结果如下:
    
    Hello Alice from my_func
    Construct an instance of class Model
    Hello Alice from Model.my_method
    Hello Alice from Model.my_property
    Hello Alice from Model.my_classmethod
    Hello Alice from Model.my_staticmethod
    /path/to/learn_pylib-project/docs/source/decorator/Deprecate-Warning-Decorator/deprecate_warning_decorator.py:36: DeprecationWarning: my_classmethod is deprecated, it will be deleted from X.Y.Z, you should use 'this' API instead
      warnings.warn(
    /path/to/learn_pylib-project/docs/source/decorator/Deprecate-Warning-Decorator/deprecate_warning_decorator.py:36: DeprecationWarning: my_staticmethod is deprecated, it will be deleted from X.Y.Z, you should use 'this' API instead
      warnings.warn(
    """
    my_func(name="Alice")

    model = Model(name="Alice")
    model.my_method()
    _ = model.my_property
    Model.my_classmethod(name="Alice")
    Model.my_staticmethod(name="Alice")
