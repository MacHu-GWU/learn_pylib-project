# -*- coding: utf-8 -*-


def test_all(capsys):
    print("You should NOT see this")
    with capsys.disabled():
        print("You should see this")
    print("You should NOT see this")
