# -*- coding: utf-8 -*-

"""
测试 eos (end of screen) 的效果.

- clear_eos: end of screen, 清除从光标往后的所有屏幕, 光标的位置是在两个字符中间的,
    而光标后面如果有字符那么这个字符也会被清除. 注意, 清除内容并不会导致光标移动.
"""

import sys
import time
import blessed

t = blessed.Terminal()

print("line1")
print("line2")
print("line3")
time.sleep(1)

print(t.move_up(2), end="")
print(t.move_right(2), end="")
sys.stdout.flush()
time.sleep(1)

print(t.clear_eos, end="")
sys.stdout.flush()
time.sleep(1)
