functools - Higher-order functions and operations on callable objects
==============================================================================
functools 是 Python 标准库中对于函数式编程的支持. 因为函数在 Python 中是 first class object, 本身也是对象, 也可以被当做参数传递. 所以就衍生出了很多技巧.

- Doc: https://docs.python.org/3/library/functools.html


cached_property
------------------------------------------------------------------------------
这是在 3.8 之后才加入的. 用于解决 ``@property`` 装饰器包装的方法每次调用都要重新计算的问题.

.. dropdown:: Example: remove cached property cache.

    .. literalinclude:: ./cached_property_remove_cache.py
       :language: python
       :linenos:

Reference:

- https://docs.python.org/3/library/functools.html#functools.cached_property
