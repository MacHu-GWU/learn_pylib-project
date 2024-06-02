BSM Override
==============================================================================
Keywords: boto session manager, bsm, ses

我们有如下代码结构::

    /pylib
        /__init__.py
        /boto_ses.py
        /app_code.py
    test.py

在 ``boto_ses.py`` 中, 我们有一个 ``BotoSessionFactory`` 类, 它有一个方法 ``get_workload_bsm`` 能获得指定的 environment 的 boto session 对象.

它还有一个 cached_property ``BotoSessionFactory.bsm``, 它一旦被调用过一次, 那它的值就再也不会被改变了. 这个对象是一个 shortcut, 用来获得最常用的 boto session 对象.

并且为了方便使用, 我们把 ``boto_ses_factory.bsm`` 的值赋值给了一个变量 ``bsm``.

.. literalinclude:: ./pylib/boto_ses.py
   :language: python
   :linenos:

在 ``app_code.py`` 的业务逻辑代码中, 我们会 ``import boto_ses`` 并引用 ``boto_ses_factory.bsm`` 和 ``bsm`` 这两个变量.

.. literalinclude:: ./pylib/app_code.py
   :language: python
   :linenos:

**现在问题来了**, 我们在开发过程中为了方便测试有这个需求, 我们需要能有临时将这个 bsm 的对象替换为指向另一个 environment 的对象. 但是业务逻辑代码已经引用了这个变量, 并且这个变量已经被缓存了. 我们该怎么做呢?

请阅读下面的测试代码中的解决方案以及注释.

.. literalinclude:: ./test.py
   :language: python
   :linenos:
