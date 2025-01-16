from dataclasses import dataclass
from env import *

import os
import json


@dataclass
class Config:
    app_name: str = "HoYoCenter"
    user_name: str = "用户"
    theme: str = "auto"

    def to_dict(self):
        return self.__dict__

    def update(self, config: dict):
        for k, v in config.items():
            setattr(self, k, v)
