# -*- coding: utf-8 -*-

"""

"""

import typing as T
import fire


class App:
    def __call__(self, version: T.Optional[bool] = False):
        if version:
            print("0.0.1")
        else:
            print("app")

    def config(self):
        print("app config")

    def run(self):
        print("app run")


if __name__ == "__main__":
    fire.Fire(App)
