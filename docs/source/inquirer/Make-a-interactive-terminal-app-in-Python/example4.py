# -*- coding: utf-8 -*-

"""
Run this in terminal.

在本例中, 我们希望看一下当我们给 ``sys.stdout.write`` 的字符串中包含换行符是什么结果.
结果和我们预测的一样, alice 和 bob 是同时出来的, 之间没有间隔::

    start! you will see 'hello' in 1 sec
    hello
    you just saw 'hello', then you will see 'alice' and 'bob' (in new line) in 1 sec
    alice
    bob
"""

import sys
import time

print("start! you will see 'hello' in 1 sec")

sys.stdout.write(f"hello")
time.sleep(1)
sys.stdout.flush()

time.sleep(1)
print("")
print("you just saw 'hello', then you will see 'alice' and 'bob' (in new line) in 1 sec")
time.sleep(1)

sys.stdout.write(f"alice\nbob\n")
time.sleep(1)
sys.stdout.flush()