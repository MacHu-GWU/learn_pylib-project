# -*- coding: utf-8 -*-

import typing as T
import dataclasses

T_DATA_LIKE = T.Union[dict, "T_BASE_MODEL", None]


@dataclasses.dataclass
class BaseModel:
    def base_model_method(self):
        print("call base_model_method")

    @classmethod
    def from_dict(
        cls: T.Type["T_BASE_MODEL"],  # <=== 这里的关键是给 cls 也加上 TypeHint, 并且用 TypeVar 标注
        dct: T.Union[dict, "T_BASE_MODEL", None],
    ) -> T.Optional["T_BASE_MODEL"]:
        """
        Construct an instance from dataclass-like data.
        It could be a dictionary, an instance of this class, or None.
        """
        if isinstance(dct, dict):
            return cls(**dct)
        elif isinstance(dct, cls):
            return dct
        elif dct is None:
            return None
        else:
            raise TypeError

    @classmethod
    def from_list(
        cls: T.Type["T_BASE_MODEL"],  # <=== 这里的关键是给 cls 也加上 TypeHint, 并且用 TypeVar 标注
        list_of_dct_or_obj: T.Optional[T.List[T_DATA_LIKE]],
    ) -> T.Optional[T.List[T.Optional["T_BASE_MODEL"]]]:
        """
        Construct list of instance from list of dataclass-like data.
        It could be a dictionary, an instance of this class, or None.
        """
        if isinstance(list_of_dct_or_obj, list):
            return [cls.from_dict(item) for item in list_of_dct_or_obj]
        elif list_of_dct_or_obj is None:
            return None
        else:  # pragma: no cover
            raise TypeError


T_BASE_MODEL = T.TypeVar("T_BASE_MODEL", bound=BaseModel)


@dataclasses.dataclass
class MyModel(BaseModel):
    def my_model_method(self):
        print("call my_model_method")


my_model = MyModel.from_dict({})
my_model.base_model_method()  # type hint OK
my_model.my_model_method()  # type hint OK

my_model_list = MyModel.from_list([{}])
my_model = my_model_list[0]
my_model.base_model_method()  # type hint OK
my_model.my_model_method()  # type hint OK
