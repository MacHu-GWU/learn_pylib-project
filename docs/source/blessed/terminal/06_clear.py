# -*- coding: utf-8 -*-

"""
Blessed 有四个跟清除 Terminal 屏幕相关的命令:

- clear: 清除整个屏幕.
- clear_eol: end of line, 光标所在的行从光标往左边的全部内容. 光标的位置是在两个字符中间的,
    而光标后面如果有字符那么这个字符也会被清除. 注意, 清除内容并不会导致光标移动.
- clear_bol: begin of line, 光标所在的行从光标往右边的全部内容. 光标的位置是在两个字符中间的,
    而光标后面如果有字符那么这个字符也会被清除. 注意, 清除内容并不会导致光标移动.
- clear_eos: end of screen, 清除从光标往后的所有屏幕, 光标的位置是在两个字符中间的,
    而光标后面如果有字符那么这个字符也会被清除. 注意, 清除内容并不会导致光标移动.

这个例子展示了 clear 的效果.
"""

import time
import blessed

t = blessed.Terminal()

print("line1")
time.sleep(1)

print("line2")
time.sleep(1)

print(t.clear())
time.sleep(1)

print("line3")
time.sleep(1)

print("line4")
time.sleep(1)

print(t.clear())
time.sleep(1)
