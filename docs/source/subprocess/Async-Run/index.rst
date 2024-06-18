Run subprocess asynchronously
==============================================================================
默认情况下 `subprocess.run() <https://docs.python.org/3/library/subprocess.html#subprocess.run>`_ 是 sync 模式. 也就是一条命令执行完毕后才会执行下一条命令. 但是有时候我们需要异步执行多条命令, 这时候我们可以使用 `subprocess.Popen() <https://docs.python.org/3/library/subprocess.html#subprocess.Popen>`_ 来实现.

例如在下面的例子中我们有两个脚本, 分别是 sleep 5 秒和 10 秒.

.. dropdown:: script1.py

    .. literalinclude:: ./script1.py
       :language: python
       :linenos:

.. dropdown:: script2.py

    .. literalinclude:: ./script2.py
       :language: python
       :linenos:

我们可以用下面的脚本来异步执行这两个脚本. 总共花费了 10 秒钟.

.. dropdown:: subprocess_run_async_mode_example.py

    .. literalinclude:: ./subprocess_run_async_mode_example.py
       :language: python
       :linenos:

还是用 ``subprocess_run_async_mode_example.py`` 脚本, 但是我们换成下面两个 script, 其中一个会运行到一半抛出异常. 你可以看到由于是异步执行, 所以另一个脚本还是会继续执行.

.. dropdown:: script3.py

    .. literalinclude:: ./script3.py
       :language: python
       :linenos:

.. dropdown:: script4.py

    .. literalinclude:: ./script4.py
       :language: python
       :linenos:
