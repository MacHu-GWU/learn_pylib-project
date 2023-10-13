# -*- coding: utf-8 -*-

"""
Run this in terminal.

在本例中, 我们展示了 ``\r`` 的实际效果, ``\r`` 只是将打印的光标回到了行首, 但是并不会清楚之前的内容.
这也是你第一次能看到 ``1th iteration`` 第二次却会看到 ``2th loopation`` 的原因, 因为
``2th loop`` 中的 loop 仅仅是覆盖了 iteration 的前面四个字符. ``3th end`` 同理.
"""

import time

print(f"\r1th iteration", end="")
time.sleep(1)
print(f"\r2th loop", end="")
time.sleep(1)
print(f"\r3th end", end="")
time.sleep(1)