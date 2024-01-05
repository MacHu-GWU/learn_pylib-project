tenacity - Retry Library
==============================================================================
Tenacity is a general-purpose retrying library to simplify the task of adding retry behavior to just about anything.

- PyPI: https://pypi.org/project/tenacity/
- GitHub: https://github.com/jd/tenacity
- Doc: https://tenacity.readthedocs.io/en/latest/


Exponential Backoff
------------------------------------------------------------------------------
Wait 1 se before first retry, then wait 2, 4, 8 seconds before second, third, fourth retry. Stop if the third retry failed (we made 4 attempts in total).

.. literalinclude:: ./test_exponential_backoff.py
   :language: python
   :linenos:

Output::

    ------ 1 th, elapsed 0.0001 seconds ------
    ❌ Failed
    ------ 2 th, elapsed 1.0057 seconds ------
    ❌ Failed
    ------ 3 th, elapsed 3.0094 seconds ------
    ❌ Failed
    ------ 4 th, elapsed 7.0147 seconds ------
    ❌ Failed
    raise RetryError, no more retry

    Traceback (most recent call last):
      File "/Users/sanhehu/Documents/GitHub/learn_pylib-project/docs/source/tenacity/test_exponential_backoff.py", line 39, in <module>
        print(f"original error: {e.last_attempt.result()!r}")
      File "/Users/sanhehu/.pyenv/versions/3.8.13/lib/python3.8/concurrent/futures/_base.py", line 437, in result
        return self.__get_result()
      File "/Users/sanhehu/.pyenv/versions/3.8.13/lib/python3.8/concurrent/futures/_base.py", line 389, in __get_result
        raise self._exception
      File "/Users/sanhehu/Documents/GitHub/learn_pylib-project/.venv/lib/python3.8/site-packages/tenacity/__init__.py", line 382, in __call__
        result = fn(*args, **kwargs)
      File "/Users/sanhehu/Documents/GitHub/learn_pylib-project/docs/source/tenacity/test_exponential_backoff.py", line 31, in run_task
        raise TaskError("random error")
    __main__.TaskError: random error

    Process finished with exit code 1
