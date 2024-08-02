.. _py-dynamodb-json:

dynamodb-json - DynamoDB Json encoder
==============================================================================
DynamoDB JSON util to load and dump strings of Dynamodb JSON format to python object and vise-versa.

- PyPI: https://pypi.org/project/dynamodb-json/
- GitHub: https://github.com/Alonreznik/dynamodb-json


Overview
------------------------------------------------------------------------------
DynamoDB JSON 是 Amazon DynamoDB 数据库的内部存储格式, 类似于 JSON. 不过它在此之上用 JSON 构建了一套类型系统 (这里有个 `例子 <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.Format.html#S3DataImport.Requesting.Formats.DDBJson>`_)

比如 Python 中的 ``{"name": "Alice"}``, DynamoDB JSON 中就是 ``{"name": {"S": "Alice"}}``. 这个 ``"S"`` 就是用来表示类型的.

``dynamodb-json`` 这个库可以帮我们做到在普通 Python 字典和 DynamoDB JSON 之间的转换. 这个库的底层用了 ``boto3.dynamodb.types.TypeSerializer`` 这个能把 Python 对象转化成 DynamoDB 对象的类. 所以它依赖于 boto3. 我个人认为这种序列化工具应该尽量保持轻量, 没有依赖. 不过这个库的功能确实很实用, 所以我还是推荐使用.

还有一个库 ``pynamodb`` 也能做到这一点, 不过它需要先定义一个类, 比较的麻烦.


Example
------------------------------------------------------------------------------
.. dropdown:: example.py

    .. literalinclude:: ./example.py
       :language: python
       :linenos:
