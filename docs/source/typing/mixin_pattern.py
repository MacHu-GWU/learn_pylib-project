# -*- coding: utf-8 -*-

"""
Mixin 模式是一个非常有用的设计模式. 你可以将一个类的方法分拆成很多个 Mixin 类. 然后在
主类中集成所有的 Mixin 类从而获得它们的方法. 使得代码更加清晰, 便于维护.

如果你想要在主类和 Mixin 类中都获得 type hint, 那么你需要在 Mixin 类中大部分的方法中的
``self: "主类"`` 都做上这样的类型提示.
"""

import typing as T
import dataclasses


@dataclasses.dataclass
class AppMixin:
    app_attr: str

    def app_method(self: "Config"):
        # type hint OK
        _ = self.deploy_attr
        print("app_method")


@dataclasses.dataclass
class DeployMixin:
    deploy_attr: str

    def deploy_method(self: "Config"):
        _ = self.app_attr
        print("deploy_method")


@dataclasses.dataclass
class ConstructorMixin:
    # type hint NOT OK
    @classmethod
    def new(
        cls: T.Type["Config"],
        app_attr: str,
        deploy_attr: str,
    ):
        return cls(
            app_attr=app_attr,
            deploy_attr=deploy_attr,
        )


@dataclasses.dataclass
class Config(
    AppMixin,
    DeployMixin,
    ConstructorMixin,
):
    pass


# type hint OK
config = Config.new(
    app_attr="app_attr",
    deploy_attr="deploy_attr",
)
print(config)

# type hint OK
config = Config(app_attr="app_attr", deploy_attr="deploy_attr")
print(config)
