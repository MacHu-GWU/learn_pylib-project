# -*- coding: utf-8 -*-

import random
from datetime import datetime
from tenacity import retry, wait_exponential, stop_after_attempt, RetryError


class Counter:
    def __init__(self):
        self.i = 0


counter = Counter()
start = datetime.now()


class TaskError(Exception):
    pass


def before_func(arg1):
    print(f"before_func {arg1 = }")


def after_func(arg1):
    print(f"after_func {arg1 = }")


@retry(
    wait=wait_exponential(multiplier=1, exp_base=2, min=0, max=30),
    stop=stop_after_attempt(4),
    before=before_func,
    after=after_func,
)
def run_task():
    counter.i += 1
    now = datetime.now()
    elapsed = f"{(now - start).total_seconds():.4f}"
    print(f"------ {counter.i} th, elapsed {elapsed} seconds ------")
    if random.randint(1, 100) <= 100:
        print("❌ Failed")
        raise TaskError("random error")
    else:
        print("✅ Succeeded")


try:
    run_task()
except RetryError as e:
    print(f"raise RetryError, no more retry")
    print(f"original error: {e.last_attempt.result()!r}")
