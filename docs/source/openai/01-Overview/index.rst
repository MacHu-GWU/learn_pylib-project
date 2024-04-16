Openai Python Overview
==============================================================================
OpenAI 作为一个公司, 它的核心 API 是一个跟编程语言无关的 Rest API. 而这套 API 最全的文档也是在官网上, 针对 RestAPI 来写的. 由于 AI 领域 Python 是最常用的语言, 所以 OpenAI 也提供了 Python 的 SDK. 相比之下 Python SDK 的文档主要着重于一些如果做某一类事情这样的示例, 而不是事无巨细的介绍所有的 API 的输入参数和输出数据结构. 所以如果你想要了解 OpenAI 的 API 的细节, 还是需要参考官方的 RestAPI 文档.


Models
------------------------------------------------------------------------------
在 `Models <https://platform.openai.com/docs/models>`_ 这篇官方文档中你能看到所有支持的文档, 以及它们的 identifier (用于 API 调用的参数)


Capabilities
------------------------------------------------------------------------------
按照 OpenAI 模型的能力, 可以分为下面几类功能, 每一个功能都是一个不同的 Endpoint. 每一个功能下都有专门对应的文档.

- `Text generation <https://platform.openai.com/docs/guides/text-generation>`_: 也是最常用的功能, 用来生成文本. 我们常用的用于对话, 生成文章, 生成代码等功能都属于这一类.
- `Function calling <https://platform.openai.com/docs/guides/function-calling>`_: 用来调用函数, 生成代码.


Links
------------------------------------------------------------------------------
- `OpenAI 官方文档 <https://platform.openai.com/docs/api-reference/introduction>`_
- `OpenAI Python README <https://github.com/openai/openai-python/blob/main/api.md>`_
