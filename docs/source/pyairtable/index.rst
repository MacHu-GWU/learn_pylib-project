pyairtable - Airtable Python Client
==============================================================================
- PyPI: https://pypi.org/project/pyairtable/
- GitHub: https://github.com/gtalarico/pyairtable
- Doc: https://pyairtable.readthedocs.io/en/stable/getting-started.html
- Airtable API Doc: https://airtable.com/developers/web/api/introduction


Overview
------------------------------------------------------------------------------

一些 Developer 需要知道的点:

- `Authentication <https://airtable.com/developers/web/api/authentication>`_: Airflow 使用 personal access token 进行认证, 每个 token 都有对应的 scope 和权限.
- `Rate Limits <https://airtable.com/developers/web/api/rate-limits>`_: 每秒钟最多 50 个 request.
- `List records <https://airtable.com/developers/web/api/list-records>`_: 每个 page 最多 100 条记录.


Example
------------------------------------------------------------------------------
.. literalinclude:: ./test_pyairtable.py
   :language: python
   :linenos:
