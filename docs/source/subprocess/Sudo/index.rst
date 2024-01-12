Subprocess with sudo
==============================================================================
使用 Python 来代替 Bash 脚本可以更好的控制逻辑判断和字符串. 但是有的命令是需要 sudo 权限的. 那么我们怎么能让 Python 脚本中的 ``subprocess.run()`` 命令能精确的以我们想要的用户, 例如 sudo (root 用户) 和普通用户来执行命令呢?

假如你有一个自动化工作, 需要分别运行两个脚本, 一个是用普通用户, 一个是用 root 用户:

.. code-block:: python

    # content of my main.py
    import subprocess

    # 这是要用 user 来运行的
    subprocess.run(["~/.pyenv/shims/python", "my_script_1.py"])

    # 这是要用 root 来运行的
    subprocess.run(["/usr/bin/python3", "my_script_2.py"])

这时候你无论是用 ``python main.py`` 还是用 ``sudo python main.py``, 都会用同一个设置运行两个脚本. 正确的做法应该是你用 ``sudo python main.py`` 来运行. 但是 ``main.py`` 里的内容需要变一下. 其原理就是你永远用 root 来运行你的入口脚本, 但是对于里面脚本再调用脚本, 凡是要用到 root 的地方就不变, 凡是要用到 user 的地方就用 ``sudo -H -u your_username`` 来运行.

.. code-block:: python

    # content of my main.py
    import subprocess

    # 这是要用 user 来运行的
    subprocess.run([
        "sudo",
        "-H",
        "-u",
        "ubuntu",
        "~/.pyenv/shims/python",
        "my_script_1.py",
    ])

    # 这是要用 root 来运行的
    subprocess.run(["/usr/bin/python3", "my_script_2.py"])


Reference

- `sudo manual <https://man7.org/linux/man-pages/man8/sudo.8.html>`_
