# -*- coding: utf-8 -*-

"""
Only process the input when the user stopped typing for a while.

在很多桌面 App 的设计中, 通常都会有用户在输入框中不断输入内容, 然后就会有即时的反馈. 但是当用户
打字很快的时候, 我们并不需要每输入一个字符就立刻进行处理. 一般我们会将用户的输入缓存起来, 然后
当用户停止输入了一段时间后 (一般是几百毫秒), 我们再对用户的输入进行处理.

这里注意要使用 ``time.time()`` 来获取系统时间, 而不是 CPU 时间.
"""

import typing as T
import time

import readchar


def process_entered(entered: T.List[str]):
    keys = "".join(entered)
    print(f"processed entered keys: {keys}")


def main():
    wait_time = 1.0
    entered = list()
    start_time: T.Optional[float] = None  # when the user started typing
    while 1:
        key = readchar.readkey()
        entered.append(key)
        if start_time is None:
            start_time = time.time()
            event_time = start_time
        else:
            event_time = time.time()
        print(f"pressed: {key!r}, process time {event_time}")
        if event_time - start_time > wait_time:
            process_entered(entered)
            start_time = None
            entered.clear()


if __name__ == "__main__":
    main()
