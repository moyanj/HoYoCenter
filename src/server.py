from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from jsonrpcserver import async_dispatch
import uvicorn
from utils import Rest
from env import *  # 所有全局变量
import ujson

import core

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
    response: Response = await call_next(request)
    if request.url.path != "/log":
        log.info(
            f"{request.method} {request.url.path}{'?' if request.query_params else ''}{request.query_params} {response.status_code}"
        )
    return response


@app.get("/")
async def index():
    # 返回主页
    return FileResponse(path=app_dir + "/dist/" + "index.html")


@app.route("/api", methods=["POST"])
async def api(request: Request):
    # 处理JSON-RPC请求
    response = await async_dispatch(
        await request.body(), serializer=ujson.dumps, deserializer=ujson.loads
    )
    return Response(response)


# 挂载静态文件目录
app.mount("/", StaticFiles(directory=app_dir + "/dist", check_dir=False), name="dist")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=6553, reload=True)
