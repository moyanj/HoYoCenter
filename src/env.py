import sys
import json
import os
from loguru import logger as log
from easydict import EasyDict
from platformdirs import PlatformDirs
from models import State, Config

from typing import Any

__all__ = ["DEBUG", "URLS", "dirs", "is_linux", "log", "app_dir", "state", "config"]

DEBUG = True if "--debug" in sys.argv else False  # 是否为调试模式
URLS: Any = EasyDict(json.load(open("data/urls.json", encoding="utf-8")))  # 所有URL

is_linux = sys.platform == "linux"

dirs = PlatformDirs("HoYoCenter", ensure_exists=True)  # 平台目录
state = State()  # 状态
app_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

if os.path.exists(os.path.join(dirs.user_config_dir, "config.json")):
    config_fp = open(
        os.path.join(dirs.user_config_dir, "config.json"), encoding="utf-8"
    )
else:
    config_fp = open(
        os.path.join(dirs.user_config_dir, "config.json"), "w+", encoding="utf-8"
    )
    config_fp.write("{}")
    config_fp.seek(0)

config = Config(**json.load(config_fp))  # 配置文件

log_format = (
    "{time:YYYY-MM-DD HH:mm:ss.SSS} | "
    "{level: <8} | "
    "{process.name}:{process.id} | "
    "{name}:{function}:{line} | "
    "{message}"
)

# 添加文件记录器
log.add(
    os.path.join(dirs.user_log_dir, "HoYoCenter.log"),
    level="INFO",
    format=log_format,
    enqueue=True,
    rotation="10 MB",
)
print("日志文件路径：", os.path.join(dirs.user_log_dir, "HoYoCenter.log"))
