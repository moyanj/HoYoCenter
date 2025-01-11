from dataclasses import dataclass
from easydict import EasyDict


@dataclass
class Config:
    app_name: str = "HoYoCenter"
    user_name: str = "用户"

    def to_dict(self):
        return self.__dict__
