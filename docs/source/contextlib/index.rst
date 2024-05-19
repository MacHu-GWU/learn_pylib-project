Contextlib - Data Classes
==============================================================================
在 Python 中上下文管理器 (context) 语法 ``with context_manager_constructor(...) as obj:`` 语法是一个非常强大的语言特性, 也是一种非常优雅的资源管理方式. 官方标准库 ``contextlib`` 提供了一些工具函数, 用于简化上下文管理器的创建.

- Doc: https://docs.python.org/3/library/contextlib.html



contextmanager
------------------------------------------------------------------------------
.. dropdown:: test_contextmanager_1.py

    .. literalinclude:: ./test_contextmanager_1.py
       :language: python
       :linenos:

.. dropdown:: test_contextmanager_2.py

    .. literalinclude:: ./test_contextmanager_2.py
       :language: python
       :linenos:

.. dropdown:: test_contextmanager_3.py

    .. literalinclude:: ./test_contextmanager_3.py
       :language: python
       :linenos:
