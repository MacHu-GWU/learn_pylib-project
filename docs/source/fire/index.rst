.. _py-fire:

fire - Python CLI Tool
==============================================================================
Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.

- PyPI: https://pypi.org/project/fire/
- GitHub: https://github.com/google/python-fire
- Doc: https://github.com/google/python-fire/blob/master/docs/guide.md


Overview
------------------------------------------------------------------------------
Fire 是一个由 Google 的团队维护, 但是并不作为 Google 的产品的 Python 开源项目. 该项目 2014 年就发布了. 和大部分命令行框架不同的是, fire 可以将 Python 中的函数, 方法, 类直接转化为一个命令行工具, 而无需重新编写 Wrapper. 该项目是我见过的 Python 社区中的命令行工具中最简单, 最易用的一个. 虽然它不适合作为非常复杂的 CLI 工具的底层框架, 但是它几乎适用于 90% 的情况. 并且它没有任何外部依赖, 安装交付非常方便.


How it Work
------------------------------------------------------------------------------
任何 callable 的对象如果被 ``fire.Fire(callable_object)`` 包装, 那么这个对象就可以被当做命令行工具使用. 这个对象可以是函数, 类, 方法.

- callable 对象的参数就是命令行参数.
- callable 对象中的任何 mandatory 的参数会变成 CLI 的 mandatory 参数.
    - 你可以按照定义的顺序传入参数, 也可以下面四种方式中的任何一种传入参数 ``--arg_name value``, ``--arg_name=value``, ``--arg-name value``, ``--arg-name=value``. arg name 既可以用 underscore 也可以用 hyphen, 即时 Python 中的变量只能用 underscore. 你既可以用空格也可以用等号来分隔参数名和参数值.
- callable 对象中的任何 optional 的参数会变成 CLI 的 optional 参数. 如果你不指定, 那么 callable 对象中的默认参数值将会被使用.
- 如果你只指定了 ``--arg_name`` 但没有指定 value, 那么这个值将会被视为 True. 你可以在参数名前加 no 来传递一个 False, 例如 ``--noarg_name``.
- 传递某个 arg name 的时候不仅可以用 ``--arg_name``, 还可以用首字母简写 ``-a`` (其中 a 这里只是个例子, 实际取决于你的参数名)
- 如果你 fire 的对象是一个类, 那么类的方法将会被视为 sub command.
- 如果你 fire 的对象是一个类, 并且它的属性里是一些其他类的实例, 那么其他类将会被视为 sub command, 而其他类的方法将会被视为 sub command 的 sub command.
- fire 会自动根据参数和 doc string 生成 CLI 文档.
    - 根据参数是否可选以及它们的默认值会自动生成参数文档.
    - doc string 的第一行会被用作 command 的 name, 而剩下的部分则会被用作 command 的 description.


Examples
------------------------------------------------------------------------------


Basic Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: ./basic_usage.py
   :language: python
   :linenos:


Subcommand example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: ./subcommand_example1.py
   :language: python
   :linenos:


Subcommand example 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: ./subcommand_example2.py
   :language: python
   :linenos:
