# -*- coding: utf-8 -*-

"""
Simple sub command example.

- Class = top level command
- Method = sub command
"""

import typing as T
import fire


class App:
    """
    Top level command document.
    """
    def __call__(self, version: T.Optional[bool] = False):
        if version:
            print("0.0.1")
        else:
            print("app")

    def config(self):
        """
        "config" subcommand document
        """
        print("app config")

    def run(self):
        """
        "run" subcommand document
        """
        print("app run")


if __name__ == "__main__":
    fire.Fire(App())
