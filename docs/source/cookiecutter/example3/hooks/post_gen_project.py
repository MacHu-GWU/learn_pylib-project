# -*- coding: utf-8 -*-

from pathlib import Path

dir_project_root = Path.cwd()

license = "{{ cookiecutter.license }}"
license_mapping = {
    "MIT": "MIT License content",
    "GPL": "GPL License content",
}
path_license = dir_project_root.joinpath("LICENSE.txt")
path_license.write_text(license_mapping[license], encoding="utf-8")
