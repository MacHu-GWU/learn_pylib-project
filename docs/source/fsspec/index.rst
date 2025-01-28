.. _py-fsspec:

fsspec - A specification that python filesystems should adhere to.
==============================================================================
在 Python 中有 `File Objects <https://docs.python.org/3/c-api/file.html>`_ 的概念, 提供了一套通用的接口来对类似文件的对象进行 IO. 在云时代, 很多存储都被转移到了云端, 而每个云厂商各自为政提供不同的 API 让学习成本变得很高. 所以社区里出现了 fsspec 项目, 用一套接口搞定所有的云存储.

- PyPI: https://pypi.org/project/fsspec/
- GitHub: https://github.com/fsspec/filesystem_spec/tree/master
- Doc: https://filesystem-spec.readthedocs.io/en/latest/index.html
