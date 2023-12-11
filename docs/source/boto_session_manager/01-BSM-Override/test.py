# -*- coding: utf-8 -*-

from pylib import boto_ses

# ------------------------------------------------------------------------------
# 你可以在 import 业务逻辑代码之前 (注意必须 import 之前, 不然很多逻辑会不可控)
# 使用下面的代码来替换 cached property
#
# 如果正常使用业务代码 (comment out 这个代码块), 输出结果为:
# === app code ===
# boto_ses_factory.bsm = BotoSesManager(env_name='prd')
# bsm = BotoSesManager(env_name='prd')
#
# 如果使用下面的代码块, 输出结果为:
# === app code ===
# boto_ses_factory.bsm = BotoSesManager(env_name='sbx')
# bsm = BotoSesManager(env_name='sbx')
# ------------------------------------------------------------------------------
# cached_property 的本质是一个特殊属性, 你可以用 del 来删除它, 然后通过修改这个 cached_property
# 的工厂函数逻辑中所使用的变量的值, 然后再调用一次这个 cached_property, 之后就是新的值了.
del boto_ses.boto_ses_factory.bsm
boto_ses.boto_ses_factory.default_env_name = "prd"
# 而 bsm 本质上是一个模块级别的 variable, 是一个 mutable 的 singleton,
# 你只要 import 这个模块, 然后用 ${module_name}.${variable_name} 的方式来修改它的值就可以了.
boto_ses.bsm = boto_ses.boto_ses_factory.get_workload_bsm(env_name="prd")

# ------------------------------------------------------------------------------
# 调用业务逻辑代码
# ------------------------------------------------------------------------------
print("=== app code ===")
from pylib.app_code import print_boto_ses_factory_bsm, print_bsm

print_boto_ses_factory_bsm()
print_bsm()
