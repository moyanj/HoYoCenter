from sanic import Blueprint, Request

bp = Blueprint("login", url_prefix="/login")


@bp.route("/")
async def login(request: Request):
    return "login"
