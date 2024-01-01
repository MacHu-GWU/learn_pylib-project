Subprocess with sudo
==============================================================================
使用 Python 来代替 Bash 脚本可以更好的控制逻辑判断和字符串. 但是有的命令是需要 sudo 权限的. 那么我们怎么能让 Python 脚本中的 ``subprocess.run()`` 命令能精确的以我们想要的用户, 例如 sudo (root 用户) 和普通用户来执行命令呢?

- `sudo manual <https://man7.org/linux/man-pages/man8/sudo.8.html>`_
