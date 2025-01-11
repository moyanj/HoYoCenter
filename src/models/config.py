from dataclasses import dataclass
from easydict import EasyDict


@dataclass
class Config:
    def to_dict(self):
        return self.__dict__
