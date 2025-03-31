# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from pathlib import Path
from cookiecutter.main import cookiecutter


@dataclasses.dataclass
class Context:
    package_name: str = dataclasses.field()

    # --- Derived
    package_name_slug: str = dataclasses.field(init=False)

    def __post_init__(self):
        self.package_name_slug = self.package_name.replace("_", "-")

    def to_dict(self) -> dict[str, T.Any]:
        return dataclasses.asdict(self)


dir_here = Path(__file__).absolute().parent
context = Context(
    package_name="my_package",
)
cookiecutter(
    template=f"{dir_here}",
    no_input=True,
    extra_context=context.to_dict(),
)
