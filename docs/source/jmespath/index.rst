Jmespath - query language for JSON
==============================================================================
用命令行处理过 JSON 的开发者几乎都知道大名鼎鼎的 JSON 命令行处理工具 `JQ <https://github.com/jqlang/jq>`. JQ 是 2013 年发布的.

而 Jmespath 是 2013 年发布的一个和 JQ 类似的 JSON 处理工具, 功能也非常强大, 但是没有 JQ 那么有名气. 但是强大之处在于 Jmespath 在主流编程语言几乎都有实现, 其中以 Python 的实现最佳, 最流行. 换言之你可以在 Python 中用 Jmespath 处理原生字典数据结构, 对于其他语言也类似. Jmespath 的作者是一个 AWS 的资深工程师 James Saryerwinnie (越南裔), 他同时也是 AWS Lambda 框架 Chalice 的作者. Jmespath 同时也是 AWS 内部流行的, 以及 AWS CLI 的 JSON 处理语言的内部实现.

如果你要对 JSON 数据进行处理, 可能 JQ 会更强. 而如果你主要是从 JSON 中提取数据, 那么 Jmespath 非常适合.

Reference:

- PyPI: https://pypi.org/project/jmespath/
- GitHub: https://github.com/jmespath/jmespath.py
- Doc: https://jmespath.org/

.. autotoctree::
    :maxdepth: 1
