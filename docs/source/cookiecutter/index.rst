.. _py-cookiecutter:

asciinema - Terminal session recorder
==============================================================================
Library to record terminal session and playback.

- PyPI: https://pypi.org/project/cookiecutter/
- GitHub: https://github.com/cookiecutter/cookiecutter
- Doc: https://cookiecutter.readthedocs.io/en/stable/


Overview
------------------------------------------------------------------------------


Best Practice
------------------------------------------------------------------------------


如何让一个变量跟随着另一个变量的变化而变化？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
例如你有一个变量是 project_name, 值是 my_project 这样的 snakecase 的形式. 你想要另一个变量 project_name_slug, 值是 my-project 这样的 slugify 的形式. 这里有几种做法:

1. 凡是你要用 ``{{ cookiecutter.package_name_slug }}`` 的地方都用 ``{{ cookiecutter.package_name | slugify }}`` 替代, 这是利用了 Cookiecutter 自带的 Jinja2 Extension, 在 Jinja2 render 的过程中进行的替换. 换言之你使用文件名的模板语言来实现了这个计算逻辑.
2. 你在 cookiecutter.json 中放两个 project_name, package_name_slug 变量. 但是你不用命令行来创建项目, 而是用脚本.


虽然 Jinja 很强大