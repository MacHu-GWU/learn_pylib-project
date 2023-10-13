# -*- coding: utf-8 -*-

"""
Run this in terminal.

和前面的例子中把 1, 2, 3 依次打印出来不同, 在本例中, 我们希望将 1, 2, 3 在一瞬间同时打印出来.
每隔 1 秒钟, 我们会用 sys.stdout.write 方法将字符写入 buffer, 注意这里我们是没有换行符的.
然后再在最后写入一个换行符来触发 flush. 所以最后的结果就是 (| 是用来表示光标所在位置)::

    123
    |
"""

import sys
import time

for i in range(1, 1 + 3):
    sys.stdout.write(f"{i}")
    time.sleep(1)
sys.stdout.write("\n")