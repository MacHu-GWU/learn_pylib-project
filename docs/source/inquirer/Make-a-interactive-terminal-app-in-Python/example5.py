# -*- coding: utf-8 -*-

"""
Run this in terminal.

在本例中, 我们用两种方法实现了类似进度条的效果. 一种是用 sys.stdout.write, 另一种是用 print 函数.
两者的原理都是用 ``\r`` 回到行首, 然后重新打印该行内容, 并且一直不换行.
"""

import sys
import time

for i in range(1, 1+3):
    sys.stdout.write(f"\r{i}th iteration")
    sys.stdout.flush()
    time.sleep(1)
print("")

for i in range(1, 1+3):
    print(f"\r{i}th iteration", end="")
    time.sleep(1)
print("")