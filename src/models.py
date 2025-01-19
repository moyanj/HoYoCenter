import aiofiles
import ujson
from easydict import EasyDict


def merge_dict(dict1, dict2):
    """
    合并两个字典，支持递归合并嵌套字典和列表类型的值。

    Args:
        dict1 (Dict[str, Any]): 原始字典
        dict2 (Dict[str, Any]): 要合并的字典

    Returns:
        Dict[str, Any]: 合并后的字典

    Raises:
        TypeError: 如果dict1或dict2不是字典类型
    """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Both inputs must be dictionaries")

    for key, value in dict2.items():
        if key in dict1:
            dict1_data = dict1[key]

            if isinstance(dict1_data, dict) and isinstance(value, dict):
                dict1_data = merge_dict(dict1_data, value)
            elif isinstance(dict1_data, list) and isinstance(value, list):
                dict1_data.extend(value)
            else:
                dict1_data = value
            dict1[key] = dict1_data
        else:
            dict1[key] = value

    return dict1


class BetterDict(EasyDict):
    def __str__(self) -> str:
        return ujson.dumps(self.__dict__, indent=4, ensure_ascii=False)

    async def __save__(self, path: str):
        async with aiofiles.open(path, "w") as f:
            await f.write(str(self))


class Config(BetterDict):
    def __init__(self, conf: dict):
        base = {
            "theme": "auto",
            "user_name": "用户",
            "language": "zh-cn",
            "game": {
                "ys": {
                    "enable": False,
                    "uid": "",
                },
                "sr": {
                    "enable": False,
                    "uid": "",
                },
            },
            "user": {
                "name": "",
                "uid": "",
                "ltoken_v1": "",
                "ltoken_v2": "",
                "game_token": "",
                "mid": "",
                "cookie_token": "",
                "fp": "",
            },
            "init": False,
        }
        base = merge_dict(base, conf)
        super().__init__(base)
