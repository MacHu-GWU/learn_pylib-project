# -*- coding: utf-8 -*-

"""
term.height, term.width 属性本质是一个函数, 可以动态获取 terminal 的高度和宽度.
"""

import blessed

term = blessed.Terminal()
print(f"height = {term.height}, width = {term.width}")
