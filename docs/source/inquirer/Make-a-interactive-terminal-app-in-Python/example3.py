# -*- coding: utf-8 -*-

"""
Run this in terminal.

在本例中我们希望用 print 函数实现和前面的例子一样的结果. 可以看到 ``print(i, end="")`` 的效果
和 ``sys.stdout.write(f"{i}")`` 是一样的.
"""

import time

for i in range(1, 1 + 3):
    print(i, end="")
    time.sleep(1)
print("")