Python Library For PDF
==============================================================================
因为 PyMuPDF 是一个 Python 库, 在深入了解 PyMuPDF 之前, 我希望能了解一下 Python 社区一共有哪些 PDF 相关的库. 由于我们时间有限, 所以希望选择最有价值的来学习.

.. note::

    下面的信息记录于 2023-11-10 日.

- PyPDF2: 老牌项目.
    - PyPI: https://pypi.org/project/PyPDF2/
    - GitHub: https://github.com/py-pdf/pypdf
    - 首次发布时间: 2012-08-06
    - 最近一次更新时间: 2022-12-22
    - GitHub Stars: 6.6k
    - License: BSD, free software
    - 依赖: 无, 它是纯 Python 实现.
- PyMuPDF: open source only, need to buy license for commercial project. 全面且强大, 基于 C++ 写的  `MuPDF <https://mupdf.com/>`_. 但是 Python 包自带用的是预编译的 MuPDF binary, 所以无需 yum, apt install. 美中不足就是商用需要 License.
    - PyPI: https://pypi.org/project/PyMuPDF/
    - GitHub: https://github.com/pymupdf/PyMuPDF
    - 首次发布时间: 2016-08-21
    - 最近一次更新时间: 2023-11-06
    - GitHub Stars: 3.1k
    - License: GNU AFFERO GPL 3.0, 商用需要买 License
    - 依赖: 无, 它是基于 C++ 实现, 然后 Python 只是 Binding, C++ 的源码包含在了包里.
- pdfminer: MIT.
    - PyPI: https://pypi.org/project/pdfminer.six/
    - GitHub: https://github.com/pdfminer/pdfminer.six
    - 首次发布时间: 2014-09-15
    - 最近一次更新时间: 2022-11-05
    - GitHub Stars: 4.9k
    - License: MIT
    - 依赖: 无, 它是纯 Python 实现.
- `pdf2image <https://pypi.org/project/pdf2image/>`_: open source, free. 功能很简单, 将 PDF 转化为 Image 图片, 底层用的是 `popper <https://poppler.freedesktop.org/>`_ 这个 PDF Render 工具. 需要用 yum, apt install CLI 之后才能使用.
- `Aspose.pdf <https://pypi.org/project/aspose-pdf/>`_: 一个用 .Net 开发的商用文档处理工具. 支持非常多富格式文档, 其中就支持 PDF. 价格很贵, 但是功能和性能绝对牛逼. 唯一遗憾是必须是 Windows 环境.
    - `aspose.PDF <https://products.aspose.com/pdf/>`_

另外, `The PDF Format <https://pypdf.readthedocs.io/en/latest/dev/pdf-format.html>`_ 这篇文档介绍了 PDF 文件格式的底层数据结构, 非常值得一读.

**结论**

- 个人使用建议 PyPDF2 和 pdfminer.
- 商用选择 PyMuPDF 或 aspose
