# -*- coding: utf-8 -*-

"""
测试 eol (end of line), bol (begin of line) 的效果.

- clear_eol: end of line, 光标所在的行从光标往左边的全部内容. 光标的位置是在两个字符中间的,
    而光标后面如果有字符那么这个字符也会被清除. 注意, 清除内容并不会导致光标移动.
- clear_bol: begin of line, 光标所在的行从光标往右边的全部内容. 光标的位置是在两个字符中间的,
    而光标后面如果有字符那么这个字符也会被清除. 注意, 清除内容并不会导致光标移动.
"""

import sys
import time
import blessed

t = blessed.Terminal()

print("line1")
print("line2")
time.sleep(1)

print(t.move_up, end="")
print(t.move_right(2), end="")
sys.stdout.flush()
time.sleep(1)

print(t.clear_eol, end="")
sys.stdout.flush()
time.sleep(1)

print(t.move_up, end="")
sys.stdout.flush()
time.sleep(1)

print(t.clear_bol, end="")
sys.stdout.flush()
time.sleep(1)