from flask import (
    Flask,
    request,
    send_from_directory,
    render_template,
    redirect,
)  # Flask
from utils import Rest
import utils
import logging
from env import *  # 所有全局变量

logs = logging.getLogger("werkzeug")
logs.disabled = True

# 初始化Flask
app = Flask("HoYoCenter-Server")


# 404错误
@app.errorhandler(404)
def error_404(e):
    return Rest("页面不存在", 404)


# 顶级错误处理器
@app.errorhandler(Exception)
def error_500(e):
    return Rest("未知错误", 500, data=str(e))


# 输出日志
@app.after_request
def after_request(response):
    # 获取状态码
    status_code = response.status_code
    # log
    log.info(
        f"{request.method} {request.path}{'?' if request.query_string else ''}{request.query_string.decode()} {status_code}"
    )
    return response


@app.route("/")
def index():
    # 返回主页
    return send_from_directory(app_dir + "/dist/", "index.html")


@app.route("/app/config")
def app_config():
    return Rest("获取配置成功", 200, data=config)


@app.route("/log")
def add_log():
    with log.contextualize(name="Web", function="js_function", line=-1):
        log.patch(utils.patch_web_log).log(request.args.get("type"), request.args.get("msg"))  # type: ignore
    return Rest()


@app.route("/static/<path:filename>")
def static_file(filename):
    return send_from_directory(app_dir + "/static/", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6553, debug=True)
