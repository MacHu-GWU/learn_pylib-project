.. _py-flask-restless-ng:

Flask-Restless-NG - Flask and Sqlalchemy based RESTful API
==============================================================================
Flask-Restless provides simple generation of ReSTful APIs for database models defined using SQLAlchemy (or Flask-SQLAlchemy). The generated APIs satisfy the requirements of the JSON API specification.

- PyPI: https://pypi.org/project/Flask-Restless-NG/
- GitHub: https://github.com/mrevutskyi/flask-restless-ng
- Doc: https://flask-restless-ng.readthedocs.io/en/latest/


Overview
------------------------------------------------------------------------------
到 2024-06 我写这篇文章位置, RestAPI 的标准, 以及如何对后端资源在数据库中的抽象进行操作的标准已经很成熟了. flask-restless-ng 就是一个基于 Flask 和 Sqlalchemy 的 RestAPI 生成器. 通过简单的配置, 就可以生成符合 JSON API 规范的 RestAPI. 你无需为每一个 ORM Model 实现 CRUD 所对应的函数. 你只需要定义号 ORM Model 以及 Relationship 既可.

这个项目的前身是 `Flask-Restless <https://pypi.org/project/Flask-Restless/>`_ (这种方式已经在 2015 年就很成熟了), 不过这个项目从 2015 年就不再维护了, 直到 2020 年社区有人 fork 了然后接手了, 目前这个项目已经有了新的生命, 也就是 Flask-Restless-NG.


Table of Content
------------------------------------------------------------------------------
.. autotoctree::
    :maxdepth: 1
