# -*- coding: utf-8 -*-

"""
Read a single keypress from the user.

这是 readchar 的基础用法, 在一个无限循环中不断读取用户输入的字符, 然后根据用户的输入做出相应的处理.
在我们这个例子中, 我们只是简单的打印出用户输入的字符.
"""

import readchar


def main():
    while 1:
        print("before")
        key = readchar.readkey()  # this is like input() but returns the key pressed
        print(f"pressed {key!r}")
        print("after")


if __name__ == "__main__":
    main()
