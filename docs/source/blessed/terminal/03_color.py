# -*- coding: utf-8 -*-

"""
term.number_of_colors 可以获取当前 terminal 支持的颜色数量. 一般的 terminal 都支持 256,
高级的 terminal 例如 Mac 上的 iTerm 支持 16 位颜色.

blessed 的牛逼之处在于在使用颜色的时候, 如果指定的颜色在当前 terminal 不支持, 它会自动找到
最近的所支持的颜色而不会报错.
"""

import blessed

term = blessed.Terminal()
print(f"number_of_colors = {term.number_of_colors}")

print(term.red("hello"))
