.. _py-readchar:

readchar - Read keyboard events
==============================================================================
Library to easily read single chars and keystrokes.

- PyPI: https://pypi.org/project/readchar/
- GitHub: https://github.com/magmax/python-readchar
- Doc: https://github.com/magmax/python-readchar


基础用法
------------------------------------------------------------------------------
.. literalinclude:: example_1.py
   :language: python
   :linenos:


缓存用户的输入并只在需要的时候进行处理
------------------------------------------------------------------------------
.. literalinclude:: example_2.py
   :language: python
   :linenos:


仅当用户一段时间都没有新的输入才进行处理
------------------------------------------------------------------------------
.. literalinclude:: example_3.py
   :language: python
   :linenos:


当处理用户最新的输入时自动杀死之前的处理进程
------------------------------------------------------------------------------
.. literalinclude:: example_4.py
   :language: python
   :linenos:


Key Code
------------------------------------------------------------------------------
如果你查看 readchar 的源码, 你会发现有的按键的 key code 很奇怪. 例如:

.. code-block:: python

    CTRL_I = TAB
    CTRL_J = LF
    DELETE = SUPR

这是因为一些历史原因键盘的按键码就是这样的. readchar 的处理是正确的, 不要怀疑.
