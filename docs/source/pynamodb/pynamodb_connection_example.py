# -*- coding: utf-8 -*-

"""
本文详细的讲解一下, 在使用 PynamoDB 的 API 的时候, 底层到底是如何决定用哪个 boto3 session
跟 AWS 通信的. 在很多其他 ORM 框架中, 例如 SQLAlchemy, mongoengine 中, 都允许你显式滴创建
数据库连接对象, 然后用上下文管理器 ``with`` 来决定执行一个代码块的时候到底用哪个连接对象.
如果不显示制定, 你也可以在全局设置一个默认的连接对象, 这样就不用每次都显式指定了.

.. note::

    **请仔细阅读这一段, 了解 PynamoDB 中的 Connection 的设计缺陷**

    在 PynamoDB 中, 这个设计是不合格的. PynamoDB 无法让你显式指定用哪个连接对象. 所以在实际使用
    时就会发生你以为你在操作这个 AWS Account, 但其实 PynamoDB 却在和另一个 AWS Account 通信的情况.
    而官方文档中只介绍了如何创建全局的 Connection, 这个 Connection 一旦设定, 对于一个 Table
    的全部的操作就会一直用这个 Connection. 这是因为 PynamoDB 把跟 Connection 作为一个属性
    跟 Table class 对象 (不是实例) 绑定在一起. 一旦绑定就再也不会变了. 而这个绑定的动作是当你
    尝试运行任何需要跟 AWS 通信时的 API 时发生的, PynamoDB 会尝试检查 ``Model._connection``
    属性, 如果没检查到则会创建一个新的 Connection 对象并一直用下去. 只要你对这个 Table ORM Class
    进行操作, 就永远是这个 Connection, 无法切换到其他 Connection.

所以当你需要把一个 ORM Model 底层的 connection 对象切换到其他 AWS Account 时, 正确的做法是
先用 ``bsm = boto_session_manager.BotoSesManager(...)`` 创建一个新的 boto3 session,
然后把 ``Model._connection = None`` 属性设为 None,
然后用 ``Model.Meta.region = bsm.aws_region`` 来设定新的 region,
然后调用一次 ``Model.create_table()`` API 来触发 PynamoDB 重新创建一个新的 Connection 对象.
之后就会一直是这个 connection 了.
"""


from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.connection import Connection
from pynamodb.constants import PAY_PER_REQUEST_BILLING_MODE
from boto_session_manager import BotoSesManager


class Item(Model):
    class Meta:
        table_name = "pynamodb_connection_example_key_value_items"
        region = "us-east-1"
        billing_mode = PAY_PER_REQUEST_BILLING_MODE

    key = UnicodeAttribute(hash_key=True)
    value = NumberAttribute()


bsm1 = BotoSesManager(profile_name="bmt_app_dev_us_east_1", region_name="us-east-1")
bsm2 = BotoSesManager(profile_name="bmt_app_dev_us_east_1", region_name="us-east-2")

# ------------------------------------------------------------------------------
# This won't work
# ------------------------------------------------------------------------------
# with bsm1.awscli():
#     Item.Meta.region = bsm1.aws_region
#     conn = Connection()
#     Item.create_table(wait=True)  # expect to create table in us-east-1
#
# with bsm2.awscli():
#     Item.Meta.region = bsm2.aws_region
#     conn = Connection()
#     Item.create_table(wait=True)  # expect to create table in us-east-2

# ------------------------------------------------------------------------------
# This would work, but rely on the private attribute _connection
# ------------------------------------------------------------------------------
# with bsm1.awscli():
#     Item._connection = None
#     Item.Meta.region = bsm1.aws_region
#     conn = Connection()
#     Item.create_table(wait=True)  # expect to create table in us-east-1
#
# with bsm2.awscli():
#     Item._connection = None
#     Item.Meta.region = bsm2.aws_region
#     conn = Connection()
#     Item.create_table(wait=True)  # expect to create table in us-east-2

# ------------------------------------------------------------------------------
# 你的 default profile 是一个, 而你的 bsm 对象是另一个, 你希望 PynamoDB 的所有操作都用
# 这个 bsm 对象的 session. 例如:
# The default profile is bmt_app_devops_us_east_1, however, we want to use us-east-2
#
# 这种情况下你需要用 with bsm2.awscli(): 来重置所有 ORM class 的 _connection 属性
# 然后运行一次 create_table() API 来触发 Table class 重新创建一个新的 Connection 对象.
# 之后你就不需要 Context manager 了, 因为 Table class 会一直用这个新的 Connection 对象.
#
# 目前我还不知道为什么用 _get_connection() API 来触发 Table class 重新创建一个新的 Connection 对象.
# 并不 work, 但是用 create_table() API 就 work 了. 这意味着每次启动程序都要检查一次 table
# 存不存在, 这样会有性能浪费. 但是这是目前我找到的唯一的方法.
# ------------------------------------------------------------------------------
# with bsm2.awscli():
#     Item._connection = None
#     Item.Meta.region = bsm2.aws_region
#     conn = Connection()
#     Item.create_table(wait=True)  # expect to create table in us-east-2
#
# item = Item(key="foo", value=123)
# item.save()
