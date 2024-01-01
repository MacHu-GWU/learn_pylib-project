.. _py-twine:

Twine - Utilities for interacting with PyPI
==============================================================================
Twine is a utility for publishing Python packages on PyPI.

It provides build system independent uploads of source and binary distribution artifacts for both new and existing projects.

- PyPI: https://pypi.org/project/twine/
- GitHub: https://github.com/pypa/twine/
- Doc: https://twine.readthedocs.io/en/stable/


About Twine
------------------------------------------------------------------------------
Twine 是 Python 官方维护的包上传工具. 在很早以前, 官方是用 distutils 包配合 ``setup.py`` 文件来发布包的. 后来为了顺应社区发展以及提升用户便利性, 官方发布了 Twine 这个工具, 也成为了事实上的新标准.


PyPI Requires MFA from 2024-01-01
------------------------------------------------------------------------------
从 2024-01-01 起, PyPI 要求所有用户必须开启 MFA 才能上传 PyPI 包. 在这之后, 如果你要继续用 twine 来上传包, 你需要在 https://pypi.org/manage/account/token/ 生成一个 API token, 并配置好 ``${HOME}/.pypirc`` 文件. 文件内容长这个样子:

.. code-block:: ini

    [pypi]
      username = __token__
      password = pypi-a1b2c3d4...

- `Enforcement of 2FA for upload.pypi.org begins today <https://blog.pypi.org/posts/2023-06-01-2fa-enforcement-for-upload/>`_
