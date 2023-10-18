# -*- coding: utf-8 -*-

"""
这是一个更高级的用法. 通常我们每按下一个键的时候就希望后台对输入的内容进行处理并反馈, 但是这个
处理过程可能耗时较长. 而用户如果继续输入了新的内容, 我们就应该让之前的处理过程停止, 并开始处理新的
输入.

在这个例子中我们实现了一个丢筛子游戏. 每当用户按下任意字母键的时候就会随机生成一个 1-1000 之间的
数字. 每次丢筛子的耗时大约为 3 秒, 如果在这 3 秒内用户再次按下任意字母键, 则会重新丢筛子, 且
之前的丢筛子的线程会被杀死. 如果最新一次的丢筛子过了 3 秒成功结束, 而用户期间没有按下任意字母键,
则会打印出用户按下的数字以及丢出的结果.
"""

import typing as T
import random
import multiprocessing

import readchar


def toss(key: str) -> T.Optional[T.Tuple[str, int]]:
    """
    The real long-running job.

    Takes around 3 - 4 seconds
    """
    # st = time.time()
    print(f"toss dice using key: {key}")
    a_list = list(range(1000000))
    for _ in range(10):
        random.shuffle(a_list)
    value = random.randint(1, 1000)
    print(f"  the key {key} gives you {value}")
    # print(time.time() - st)
    return key, value


def main():
    process: T.Optional[multiprocessing.Process] = None
    while True:
        key = readchar.readchar()
        # if this is not the first entered key, we should terminate the existing process
        if process is not None:
            process.terminate()  # Terminate the process immediately
            process.join()  # Wait for the old process to finish
        # we create a new process to run the job anyway
        process = multiprocessing.Process(
            target=toss,
            args=(key,),
        )
        process.start()


if __name__ == "__main__":
    main()
