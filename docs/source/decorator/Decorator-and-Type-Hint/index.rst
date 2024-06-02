decorator - Decorator and Type Hint
==============================================================================
在自己不用库实现 decorator 的时候, 一个很常见的问题就是你 wrap 之后的函数的 __name__, __doc__, 以及 type hint 之类的东西会乱掉. 由于我认为 decorator 是目前写装饰器最优秀的库, 这个文档测试了当你使用 decorator 的库的时候, 在各种情况下 type hint 是否能正常工作.

.. dropdown:: simple_example.py

    .. literalinclude:: ./simple_example.py
       :language: python
       :linenos:

.. dropdown:: context_manager_example.py

    .. literalinclude:: ./context_manager_example.py
       :language: python
       :linenos:
