# -*- coding: utf-8 -*-

from learn_pylib import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_pylib.tests import run_cov_test

    run_cov_test(__file__, "learn_pylib.api", preview=False)
