import sys
import json
import os
from loguru import logger as log
from platformdirs import PlatformDirs
from models import Config

from typing import Any

__all__ = [
    "DEBUG",
    "dirs",
    "is_linux",
    "log",
    "app_dir",
    "config",
    "build_info",
]

DEBUG = True if "--debug" in sys.argv else False  # 是否为调试模式
app_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

try:
    build_info = json.load(
        open(os.path.join(app_dir, "build_info.json"), encoding="utf-8")
    )
except:
    build_info = {
        "version": "DEBUG",
        "commit": "__debug__",
        "branch": "main",
        "python": "3",
        "platform": "debug",
        "args": [],
        "build_time": "__debug__",
    }

is_linux = sys.platform == "linux"

dirs = PlatformDirs("HoYoCenter", ensure_exists=True)  # 平台目录

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

config = Config(json.load(config_fp))  # 配置文件

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
log.debug("日志文件路径：", os.path.join(dirs.user_log_dir, "HoYoCenter.log"))
