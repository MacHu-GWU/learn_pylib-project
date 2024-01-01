# -*- coding: utf-8 -*-

"""
精确控制 subprocess.run 以 sudo 或是普通用户的方式运行命令.
"""

import subprocess
from pathlib import Path

dir_home = Path.home()
print(f"{dir_home = }")

args = [
    f"sudo",
    "-H",
    "-u",
    "ubuntu",
]


# p = Path("/usr/local/bin/subprocess-test/test.txt")
# args = ["echo", "hello", ">", f"{p}"]
# subprocess.run(args, check=True)
# content = p.read_text()
# print(f"Succeeded! content = {content!r}")
