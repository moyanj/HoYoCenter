import httpx
from jsonrpcserver import method, Success, Result, Error
from typing import Optional


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
        response = await client.get(url, params=params, headers=headers)
        return Success(response.json())


@method(name="requests.post")
async def post(
    url: str,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, params=params, headers=headers, json=data)
        return Success(response.json())


@method(name="requests.req")
async def req(
    method: str,
    url: str,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method, url, params=params, headers=headers, json=data
        )
        return Success(response.json())
