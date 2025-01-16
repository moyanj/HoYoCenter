from jsonrpcserver import method, Result, Success, Error
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
async def update_config(data: dict):
    config.update(data)


@method(name="log.info")
async def log_info(msg: str):
    log.info(msg)


@method(name="log.warning")
async def log_warning(msg: str):
    log.warning(msg)


@method(name="log.error")
async def log_error(msg: str):
    log.error(msg)


@method(name="log.debug")
async def log_debug(msg: str):
    log.debug(msg)
