# -*- coding: utf-8 -*-

"""
现代的 Terminal 会有一些高级功能, 例如闪烁. 但不是所有的 Terminal 都有这些功能. 例如在
PyCharm 自带的 terminal 中就不能 blink. blessed 可以允许你用函数使用这些功能, 但如果
Terminal 不支持这些功能, 则会自动降级将其变为普通字符串. 这样你就不需要为了兼容不同的 Terminal
而写不同的代码了.
"""

import time
import blessed

term = blessed.Terminal()
print(term.blink("Insert System disk into drive A:"))
time.sleep(3)