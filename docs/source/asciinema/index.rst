.. _py-asciinema:

asciinema - Terminal session recorder
==============================================================================
Library to record terminal session and playback.

- PyPI: https://pypi.org/project/asciinema/
- GitHub: https://github.com/asciinema/asciinema
- Doc: https://asciinema.org/
- Website: https://asciinema.org/


Overview
------------------------------------------------------------------------------
asciinema 是一个能把 Terminal session 记录下来并重新播放的 Python 库. 它的原理是将 Terminal 的输出保存文纯文本格式 (相比 GIF 等基于图像的格式来说, 体积要小太多了), 然后再用这个库来播放. 它不仅可以记录 Terminal 中的交互式的输入输出, 就算你进入到一个 Vim 的 editor 内之后的情况也能记录下来, 强大得恐怖如斯.

同时 https://asciinema.org/ 是一个提供终端录制的网站. 你可以将 asciinema 生成的录像上传到这个网站并分享给其他人, 或是嵌入到博客, HTML, Markdown, Restructured Text 中.


How to Use
------------------------------------------------------------------------------


Record and Play on Local
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
本节我们介绍如何在本地使用这个命令行工具.

**首先, 你要用 Python 安装这个库**

.. code-block:: bash

    pip install asciinema # you need Python3.7+

**然后, 你就可以开始录制了**

你可以用下面的命令来开始录制.

.. code-block:: bash

    asciinema rec ${filename}

其中 ``${filename}`` 是你要保存的录像文件名. 例如 example.cast.

.. code-block:: bash

    asciinema rec example.cast

按回车后就会进入到录制模式, 你可以用 Ctrl + D 跳出录制.

如果这个文件名已经存在, 你可以用 ``--overwrite`` 参数来覆盖它.

.. code-block:: bash

    asciinema rec --overwrite example.cast

举例, 我们想记录一个简单的命令行交互过程:

.. code-block:: bash

    $ echo Hello
    Hello

**录制完毕后, 你就可以播放了**

录制完毕后你就会看到 ``example.cast`` 文件了. 你可以用 ``asciinema play`` 命令来播放它.

.. code-block:: bash

    asciinema play example.cast


Upload Your Record to asciinema.org
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
注:

    本节内容来自于官方文档 https://asciinema.org/docs/usage

**注册 asciinema.org 账号**

首先你先要登录 https://asciinema.org/. 这个网站是用 passwordless + email 的方式登录的. 你的用户名就是你的 email. 你输入 email 后它会给你发一个带链接的邮件.

**将本地机器跟 asciinema.org 账号关联起来**

对于每一台新电脑上的新用户, 你需要运行一次 ``asciinema auth`` 命令将你的本地电脑跟已经登录过的 https://asciinema.org/ 上的 profile 关联起来. 它会在本地生成一个 ``${HOME}/.config/asciinema/install-id`` 文件, 里面的内容是一个 token. 而你在网站上查看你的 profile 的时候也能看到这个 token 已经被关联了.

.. code-block:: bash

    asciinema auth

**上传录像**

在这之后就能用 ``asciinema uplode ${filename}`` 命令将其上传到网站上了.

.. code-block:: bash

    asciinema upload example.cast


Embed your Record to HTML, Markdown, Restructured Text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
你执行完 ``asciinema upload`` 命令后就会出现一个链接可以在网站上查看你的录像. 你还可以登录你的 https://asciinema.org/ 账号后在你的 Profile 菜单里找到你所有上传的录像.

例如我们前面的 ``echo hello`` 的例子的 `录像地址在这里 <https://asciinema.org/a/oXF6Ykpxv7UqR4bcq2lJNX2RD>`_.

如果你想要将其嵌入到文档中, 你可以点击 ``Share`` 按钮. 里面比较重要的有:

1. HTML: 你可以直接嵌入到 HTML 中.
2. Markdown: 里面有两个链接, ``*.svg`` 是你的图像网址, 另一个则是在网站上预览的链接.

如果你要嵌入到 Restructured Text, 你可以用下面的语法实现 (记得把 record_id 替换成你自己的).

.. image:: https://asciinema.org/a/oXF6Ykpxv7UqR4bcq2lJNX2RD.svg
    :target: https://asciinema.org/a/oXF6Ykpxv7UqR4bcq2lJNX2RD
