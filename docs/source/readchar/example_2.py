# -*- coding: utf-8 -*-

"""
Buffer the input keys and process then when ENTER is pressed.

有的时候我们希望用户完成一系列输入之后再进行处理, 这时我们就需要一个 buffer 来缓存用户的输入.
然后判断是否对用户的输入进行处理. 在这个例子中我们使用了一个 list 来作为 buffer, 并当用户按下
Enter 键后才对 buffer 中的内容进行处理.
"""

import typing as T

import readchar


def process_entered(entered: T.List[str]):
    keys = "".join(entered)
    print(f"processed entered keys: {keys}")
    print("done")


def is_need_process(entered: T.List[str], last_key: str) -> bool:
    return last_key == readchar.key.ENTER


def main():
    entered = list()
    print("pleas enter your input and press ENTER to process it.")
    while 1:
        key = readchar.readkey()
        print(f"pressed: {key!r}")
        entered.append(key)
        if is_need_process(entered, key):
            process_entered(entered)
            entered.clear()
            print("pleas enter your input and press ENTER to process it.")


if __name__ == "__main__":
    main()
