.. _py-typing:

typing
==============================================================================
Python 在 3.5 开始全面拥抱类型系统, 以 `typing <https://docs.python.org/3/library/typing.html>`_ 这个标准库的方式提供. 这个系统是可选的.

除了标准库, 还有两个社区维护的库也很重要:

- `typing <https://pypi.org/project/typing/>`_, 跟标准库同名的库, 用于在 < 3.5 的 Python 中支持类型标注系统.
- `typing-extensions <https://pypi.org/project/typing-extensions/>`_, 用于在低版本的 Python 中获得高版本 Python 中的官方 typing 标准库的特性. 例如在 3.8 后引入了 ``TypedDict``, 如果你想在 Python 3.5 中用这个功能就可以用这个库.


Generics 泛型
------------------------------------------------------------------------------
.. literalinclude:: fan_xing_1.py
   :language: python
   :linenos:

.. literalinclude:: fan_xing_2.py
   :language: python
   :linenos:

.. literalinclude:: fan_xing_3.py
   :language: python
   :linenos:

.. literalinclude:: fan_xing_4.py
   :language: python
   :linenos:

.. literalinclude:: fan_xing_5.py
   :language: python
   :linenos:

.. literalinclude:: fan_xing_6.py
   :language: python
   :linenos:

.. literalinclude:: generic_by_parameter.py
   :language: python
   :linenos:

.. literalinclude:: generic_by_subclass.py
   :language: python
   :linenos:


Mixin 模式
------------------------------------------------------------------------------
.. literalinclude:: mixin_pattern.py
   :language: python
   :linenos:
