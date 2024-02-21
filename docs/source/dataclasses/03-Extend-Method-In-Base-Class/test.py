# -*- coding: utf-8 -*-


class BaseModel:
    def low_level_api(self, low_arg: str):
        pass

    def high_level_api(self, high_arg: str):
        self.low_level_api(high_arg)


class UserModel(BaseModel):
    def low_level_api(self, low_arg: str, new_arg: str):
        pass


user_model = UserModel()
user_model.high_level_api("high_arg")
