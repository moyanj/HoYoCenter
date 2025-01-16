from fastapi import FastAPI, Request, HTTPException, File, UploadFile, Depends
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger
import uvicorn
import logging
from utils import Rest
import utils
from env import *  # 所有全局变量

# 配置日志
logging.getLogger("uvicorn").disabled = True
logs = logging.getLogger("fastapi")
# logs.disabled = True

# 初始化FastAPI
app = FastAPI(title="HoYoCenter-Server")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


# 404错误
@app.exception_handler(404)
async def error_404(request: Request, exc: HTTPException):
    return Rest("页面不存在", 404)


# 顶级错误处理器
@app.exception_handler(HTTPException)
async def error_500(request: Request, exc: HTTPException):
    return Rest("未知错误", 500, data=str(exc.detail))


# 输出日志
@app.middleware("http")
async def log_request(request: Request, call_next):
    response = await call_next(request)
    if request.url.path != "/log":
        logger.info(
            f"{request.method} {request.url.path}{'?' if request.query_params else ''}{request.query_params} {response.status_code}"
        )
    return response


@app.get("/")
async def index():
    # 返回主页
    return FileResponse(path=app_dir + "/dist/" + "index.html")


@app.route("/app/config", methods=["GET", "POST"])
async def app_config(request: Request):
    if request.method == "POST":
        config.update(await request.json())
        utils.save_config()
    return Rest("获取配置成功", 200, data=config.to_dict())


@app.get("/log")
async def add_log(request: Request):
    with log.contextualize(name="Web", function="js_function", line=-1):
        log.patch(utils.patch_web_log).log(request.query_params.get("type"), request.query_params.get("msg"))  # type: ignore
    return Rest()


# 挂载静态文件目录
app.mount(
    "/static",
    StaticFiles(directory=app_dir + "/static", check_dir=False),
    name="static",
)
app.mount("/", StaticFiles(directory=app_dir + "/dist", check_dir=False), name="dist")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6553)
