# -*- coding: utf-8 -*-

"""
term.height, term.width 属性本质是一个函数, 可以动态获取 terminal 的高度和宽度.
你试试看在 Terminal 中运行这个程序, 并不断改变 Terminal 的大小, 你会看到输出的值也会不同.
"""

import time
import blessed

term = blessed.Terminal()

for _ in range(10):
    time.sleep(1)
    print(f"height = {term.height}, width = {term.width}")
