# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property


@dataclasses.dataclass
class BotoSesManager:
    env_name: str


@dataclasses.dataclass
class BotoSessionFactory:
    default_env_name: str = dataclasses.field(default="sbx")

    def get_workload_bsm(self, env_name: str) -> BotoSesManager:
        return BotoSesManager(env_name)

    @cached_property
    def bsm(self) -> BotoSesManager:
        return self.get_workload_bsm(env_name=self.default_env_name)


boto_ses_factory = BotoSessionFactory()
bsm = boto_ses_factory.bsm
