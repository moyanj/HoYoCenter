from jsonrpcserver import method, Result, Success, Error
import os
import utils
import hashlib
import base64
import platform
from env import *
import webview


@method(name="data.config")
async def get_config():
    return Success(config.__dict__)


@method(name="data.build_info")
async def get_build_info():
    return Success(build_info)


@method(name="data.update_config")
async def update_config(data: dict, save: bool = True):
    config.update(data)
    if save:
        await config.__save__(os.path.join(dirs.user_config_dir, "config.json"))
    return Success()


def base_log(level: str, msg: str):
    log.patch(utils.patch_web_log).log(level, msg)


@method(name="log.info")
async def log_info(msg: str):
    base_log("INFO", msg)
    return Success()


@method(name="log.warning")
async def log_warning(msg: str):
    base_log("WARNING", msg)
    return Success()


@method(name="log.error")
async def log_error(msg: str):
    base_log("ERROR", msg)
    return Success()


@method(name="log.debug")
async def log_debug(msg: str):
    base_log("DEBUG", msg)
    return Success()


@method(name="data.device_id")
async def get_device_id():
    # 获取系统信息
    system_name = platform.platform()
    system_version = platform.release()
    computer_name = platform.node()
    computer_system = platform.system()
    computer_bit = platform.architecture()[0]
    cpu_count = os.cpu_count()  # 使用os模块获取CPU核心数
    username = os.getlogin()  # 获取当前登录的用户名
    cpu_arch = platform.machine()

    # 构造设备ID字符串
    deviceid = (
        system_name
        + "_"
        + system_version
        + "_"
        + computer_name
        + "_"
        + computer_system
        + "_"
        + computer_bit
        + "_"
        + str(cpu_count)
        + "_"
        + username
        + "_"
        + cpu_arch
    )

    # 对设备ID进行SHA-256哈希
    hash_id = hashlib.sha256(deviceid.encode("utf-8")).digest()
    big_hash_id = base64.b85encode(hash_id).decode()  # 转换为大写

    return Success(big_hash_id)


@method(name="data.open_url")
async def open_url(url: str):
    window = webview.create_window("", url)
    webview.start(window)
    return Success()
