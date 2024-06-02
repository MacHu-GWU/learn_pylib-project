# -*- coding: utf-8 -*-

from typing import Generator, ContextManager

# 你如果用 contextlib, 怎么弄 type hint 都不对
# from contextlib import contextmanager
# 你如果用 decorator, 用 typing.ContextManager[...] 就可以了
from decorator import contextmanager


class Session:
    def __init__(self):
        self.is_live = False

    def start(self):
        self.is_live = True

    def close(self):
        self.is_live = False

    def execute(self, msg):
        print(f"execute: {msg}")

    def error(self):
        raise ValueError("something wrong!")


class Connection:
    @contextmanager
    def session1(self) -> ContextManager[Session]:
        """
        Working
        """
        session = Session()
        try:
            session.start()
            yield session
        finally:
            session.close()

    @contextmanager
    def session2(self) -> Generator[Session, None, None]:
        """
        Not working
        """
        session = Session()
        try:
            session.start()
            yield session
        finally:
            session.close()

    @contextmanager
    def session3(self):
        """
        Not working
        """
        session = Session()
        try:
            session.start()
            yield session
        finally:
            session.close()


conn = Connection()

with conn.session1() as ses:
    assert ses.is_live is True
    ses.execute("1")
assert ses.is_live is False

with conn.session2() as ses:
    assert ses.is_live is True
    ses.execute("1")
assert ses.is_live is False

with conn.session3() as ses:
    assert ses.is_live is True
    ses.execute("1")
assert ses.is_live is False
