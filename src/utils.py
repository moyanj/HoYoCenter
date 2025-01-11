import sys
import subprocess
import socket
import os
import json
from sanic.response import JSONResponse
from env import *


def restart():
    if DEBUG:
        command = " ".join(sys.argv)
        command = "python " + command
    else:
        command = " ".join(sys.argv)
    subprocess.Popen(command)
    sys.exit()


def get_free_port():
    base = 49152  # 从动态端口范围开始
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex(("127.0.0.1", base))
        if res != 0:  # 如果连接失败，说明端口空闲
            return base
        base += 1
        if base > 65535:  # 超过最大端口号范围，重新从起始端口开始
            base = 49152


def clear_console():
    if is_linux:
        os.system("clear")
    else:
        os.system("cls")


def Rest(msg: str = "OK", status_code: int = 200, data=None):
    """Rest

    Keyword Arguments:
        msg -- 消息 (default: {"OK"})
        status_code -- 状态码 (default: {200})
        data -- 数据 (default: {None})

    Returns:
        处理后的返回字符串
    """
    ret_dict = {"msg": msg, "code": status_code, "data": data}
    retStr = json.dumps(ret_dict, indent=4, ensure_ascii=False)
    req = JSONResponse(retStr)
    req.status = status_code
    req.headers["Content-Type"] = "application/json; charset=utf-8"

    return req


def patch_web_log(record):
    record["name"] = "Web"
    record["function"] = "js_function"
    record["line"] = -1
    return record
