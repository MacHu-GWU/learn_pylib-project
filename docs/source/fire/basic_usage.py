# -*- coding: utf-8 -*-

import typing as T
import fire


def main(
    name,
    is_kid: T.Optional[bool] = False,
    age: T.Optional[int] = 18,
):
    """
    this is main function

    this is description

    - sentence 1
    - sentence 2
    - sentence 3
    """
    print(f"name = {name}")
    print(f"is_kid = {is_kid}")
    print(f"age = {age}")


if __name__ == "__main__":
    fire.Fire(main)
