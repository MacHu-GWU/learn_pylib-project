# -*- coding: utf-8 -*-

"""
Terminal 是有光标的. 从你的界面的左上角起就是光标的位置. 但一般你的光标的起始位置是你的 Shell
界面的输入框处. Terminal 有很多方法可以用来移动光标, 注意, 移动光标并不会改变字符. 这些方法
都需要被 ``print(..., end="")`` 然后 ``sys.stdout.flush()`` 之后才能在 Terminal 上看到
效果.

下面我们给出了一个让光标上下左右移动, 并用 home 回到左上角, 然后用 move_xy 定位到具体位置的例子.
"""

import time
import sys
import blessed

term = blessed.Terminal()
print("hello world")
print("apple banana")
print("blessed is awesome")
time.sleep(1)

print(term.move_up, end="")
sys.stdout.flush()
time.sleep(1)

print(term.move_up(2), end="")
sys.stdout.flush()
time.sleep(1)

print(term.move_right, end="")
sys.stdout.flush()
time.sleep(1)

print(term.move_right(3), end="")
sys.stdout.flush()
time.sleep(1)

print(term.move_left(1), end="")
sys.stdout.flush()
time.sleep(1)

print(term.move_left(3), end="")
sys.stdout.flush()
time.sleep(1)

print(term.move_down, end="")
sys.stdout.flush()
time.sleep(1)

print(term.move_down(2), end="")
sys.stdout.flush()
time.sleep(1)

print(term.home, end="")
sys.stdout.flush()
time.sleep(1)

print(term.move_xy(3, 3), end="")
sys.stdout.flush()
time.sleep(1)
