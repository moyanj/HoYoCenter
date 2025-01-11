from sanic import Sanic, Request, json, file
from sanic.exceptions import NotFound, SanicException
from sanic_cors import CORS
from utils import Rest
import utils
import logging
import uvloop

from env import *  # 所有全局变量

uvloop.install()
Sanic.start_method = "fork"
Sanic.START_METHOD_SET = True

logs = logging.getLogger("sanic")
logs.disabled = True

# 初始化Sanic
app = Sanic("HoYoCenter-Server")
CORS(app)


# 404错误
@app.exception(NotFound)
def error_404(request: Request, e):
    return Rest("页面不存在", 404)


# 顶级错误处理器
@app.exception(SanicException)
def error_500(request: Request, e):
    return Rest("未知错误", 500, data=str(e))


# 输出日志
@app.after_server_start
async def after_request(app, loop):
    async def log_response(request, response):
        # 获取状态码
        status_code = response.status
        # log
        log.info(
            f"{request.method} {request.path}{'?' if request.query_string else ''}{request.query_string} {status_code}"
        )

    app.ctx.log_response = log_response


@app.middleware("response")
async def log_response_middleware(request, response):
    await app.ctx.log_response(request, response)


@app.route("/")
async def index(request: Request):
    # 返回主页
    return await file(app_dir + "/dist/" + "index.html")


@app.route("/app/config")
async def app_config(request: Request):
    return Rest("获取配置成功", 200, data=config.to_dict())


@app.route("/log")
async def add_log(request: Request):
    with log.contextualize(name="Web", function="js_function", line=-1):
        log.patch(utils.patch_web_log).log(request.args.get("type"), request.args.get("msg"))  # type: ignore
    return Rest()


@app.route("/static/<filename:path>")
async def static_file(request: Request, filename):
    return await file(app_dir + "/static/" + filename)


@app.route("/<filename:path>")
async def dist_file(request: Request, filename):
    return await file(app_dir + "/dist/" + filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6553, debug=True)
