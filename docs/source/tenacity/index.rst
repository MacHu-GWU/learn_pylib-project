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
    ------ 2 th, elapsed 1.0028 seconds ------
    ❌ Failed
    ------ 3 th, elapsed 3.0081 seconds ------
    ❌ Failed
    ------ 4 th, elapsed 7.0103 seconds ------
    ❌ Failed
    raise RetryError, no more retry
