Disable Capture Standard Output in Pytest
==============================================================================
在 pytest 中, 如果你直接用 ``pytest`` 命令运行测试, pytest 会自动捕获标准输出和标准错误. 所谓捕获就是将 ``print`` 出来的东西保存到一个字节流中, 而不是打印出来. 通常我们想要看 ``print`` 的内容的话就是用 ``pytest -s`` 参数指定不捕获标准输出, 等效于 ``pytest --capture=no``. 但这样做只能把所有的 ``print`` 的内容打开. 有没有一种方法能够在代码中精细控制哪一段代码显式 print, 哪一段不显示呢? 答案是有的, 你只要用 ``capsys`` 这个 `fixture <https://docs.pytest.org/en/latest/explanation/fixtures.html>`_ 就可以了. 请参考下面的例子:

.. dropdown:: test_all.py

    .. literalinclude:: ./tests/test_all.py
       :language: python
       :linenos:


Reference
------------------------------------------------------------------------------
- `Accessing captured output from a test function <https://docs.pytest.org/en/latest/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function>`_
