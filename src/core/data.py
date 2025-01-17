from jsonrpcserver import method, Result, Success, Error
import os
import utils
from env import *


@method(name="data.config")
async def get_config():
    return Success(config.__dict__)


@method(name="data.urls")
async def get_urls():
    return Success(URLS)


@method(name="data.build_info")
async def get_build_info():
    return Success(build_info)


@method(name="data.update_config")
async def update_config(data: dict, save: bool = True):
    config._update(data)
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
