import httpx
from jsonrpcserver import method, Success, Result, Error
from typing import Optional
from base64 import b64encode


def rep2dict(rep: httpx.Response):
    """
    将httpx.Response对象转换为字典，方便查看和处理响应信息。

    Args:
        rep (httpx.Response): HTTP响应对象。

    Returns:
        Dict[str, Any]: 包含响应信息的字典。
    """
    if rep is None:
        raise ValueError("响应对象不能为空")

    try:
        j = rep.json()
    except ValueError:
        j = None

    content = rep.content
    encoded_content = b64encode(content).decode("utf-8") if content else ""

    return {
        "status_code": rep.status_code,
        "headers": dict(rep.headers),
        "content": encoded_content,
        "json": j,
    }


@method(name="requests.get")
async def get(
    url: str, params: Optional[dict] = None, headers: Optional[dict] = None
) -> Result:
    """发送GET请求
    Args:
        url (str): URL
        params (dict, optional): 参数. Defaults to None.
        headers (dict, optional): 头部. Defaults to None.
    Returns:
        Result: 响应
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params, headers=headers)
        except httpx.RequestError as e:
            return Error(code=500, message=str(e))
        return Success(rep2dict(response))


@method(name="requests.post")
async def post(
    url: str,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, params=params, headers=headers, json=data)
        except httpx.RequestError as e:
            return Error(code=500, message=str(e))
        return Success(rep2dict(response))


@method(name="requests.req")
async def req(
    method: str,
    url: str,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method, url, params=params, headers=headers, json=data
            )
        except httpx.RequestError as e:
            return Error(code=500, message=str(e))
        return Success(rep2dict(response))
