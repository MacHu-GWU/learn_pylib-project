Make a interactive terminal app in Python
==============================================================================
`Inquirer <https://github.com/magmax/python-inquirer>`_ 是一个在命令行界面中提供交互式的 User Input / Output 的 Python 库. 通过这个开源项目, 我们可以学习到如何在 Python 中实现一个交互式的命令行工具的关键技术. 本文详细的探讨一下该技术.


print, sys.stdout.write 和 sys.stdout.flush
------------------------------------------------------------------------------
用命令行作为 UI 的核心是管理在 Terminal 中显式的字符串. 所以我们要理解将字符串打印到屏幕上的原理.

- 系统中有一个 ``sys.stdout`` 的字节流, 可以储存 "将要" 打印到终端上的字符串.
- ``sys.stdout.write`` 的作用是是将字符串写入到 ``sys.stdout`` 字节流的 buffer 但不打印. 但如果字符串中有换行符 ``\n``, 则会自动把字符串的所有内容打印到终端.
- 而 ``sys.stdout.flush`` 的作用则是将 ``sys.stdout`` 字节流的 buffer 中的内容打印到终端上.
- 而我们常用的 ``print`` 函数的作用本质上是将多个参数转化成字符串, 并且用分隔符分隔 (print 是有一个 ``sep`` 参数的, 默认是空格), 然后在最后用换行符换行 (print 是有一个 ``end`` 参数的, 默认是 ``\n`` 换行符).

我们来看下面几个例子加强理解, **请仔细阅读代码中的注释**.

.. literalinclude:: ./example1.py
   :language: python
   :linenos:

.. literalinclude:: ./example2.py
   :language: python
   :linenos:

.. literalinclude:: ./example3.py
   :language: python
   :linenos:

.. literalinclude:: ./example4.py
   :language: python
   :linenos:

还有一个很重要的知识点是 ``\n`` 和 ``\r`` 的区别. ``\n`` 是换行符, 会让光标移到下一行的行首. 而 ``\r`` 是回车符, 会让光标移到本行的行首, 注意, ``\r`` 回到行首的. ``\r`` 是在不换行的情况下, 刷新当前行已经打印出的内容的核心技巧, 其本质就是将光标移到行首并重新打印. 请看下面的例子.

.. literalinclude:: ./example5.py
   :language: python
   :linenos:

.. literalinclude:: ./example6.py
   :language: python
   :linenos:


Terminal
------------------------------------------------------------------------------
Terminal 作为 UI 的载体, 它有界面大小, 光标位置等各种概念. 我们需要充分了解 Terminal 的工作原理才能构建出正确的 UI.

在 Python 中有一个库 `blessed <https://github.com/jquast/blessed>`_ 可以让用户轻松构建 Terminal App. 请阅读 :ref:`这个博文 <py-blessed>` 详细了解 Terminal 的相关知识.


Render
------------------------------------------------------------------------------
我们掌握了 ``sys.stdout.write`` / ``sys.stdout.flush`` 和 ``blessed`` 库之后, 就可以开始学习交互式 Terminal App 的核心原理了.

一个 Terminal App 的界面是由字符组成的, 而这个界面又是被一个叫做 render (渲染器) 的组件渲染出来的. 当用户用键盘进行输入, 并捕获到一些快捷键命令之后, App 中的数据就会发生改变, 渲染器就要负责将这些改变渲染出来, 显示在屏幕上. 而前面学到的知识本质上是在介绍 **如何渲染**.