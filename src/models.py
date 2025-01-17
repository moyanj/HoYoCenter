import aiofiles
import ujson


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
        if isinstance(value, BetterDict):
            value = value.__dict
        if key in dict1:
            dict1_data = dict1[key]
            if isinstance(dict1_data, BetterDict):
                dict1_data = dict1_data.__dict

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


class BetterDict:
    """
    更好的字典

    Attributes:
        __dict (dict): 原始字典
    """

    def __init__(self, conf: dict):
        self.__dict = conf
        self._update()

    def __getattr__(self, name):
        if name == "_BetterDict__dict":
            return object.__getattribute__(self, name)
        if name in self.__dict:
            return self.__dict[name]
        else:
            raise AttributeError(f"'BetterDict' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        if name == "_BetterDict__dict":
            super().__setattr__(name, value)
        else:
            if isinstance(value, dict):
                value = BetterDict(value)
            elif isinstance(value, list):
                value = [
                    BetterDict(item) if isinstance(item, dict) else item
                    for item in value
                ]
            self.__dict[name] = value

    def __getitem__(self, name):
        return self.__getattr__(name)

    def __setitem__(self, name, value):
        self.__setattr__(name, value)

    def __len__(self):
        return len(self.__dict)

    def __str__(self):
        return ujson.dumps(self.__dict, indent=4, ensure_ascii=False)

    def __repr__(self):
        return str(self.__dict)

    def _update(self, conf=None):
        """
        更新字典内容

        Args:
            conf (dict): 要更新的字典
        """
        if conf:
            self.__dict = merge_dict(self.__dict, conf)
            for key, value in self.__dict.items():
                if isinstance(value, dict):
                    self.__dict[key] = BetterDict(value)
                elif isinstance(value, list):
                    self.__dict[key] = [
                        BetterDict(item) if isinstance(item, dict) else item
                        for item in value
                    ]

    async def save(self, path: str):
        async with aiofiles.open(path, "w") as f:
            await f.write(str(self))


class Config(BetterDict):
    def __init__(self, conf: dict):
        base = {
            "theme": "auto",
            "user_name": "用户",
            "game": {
                "ys": {
                    "enable": False,
                    "uid": "",
                },
                "sr": {
                    "enable": False,
                    "uid": "",
                },
                "zzz": {
                    "enable": False,
                    "uid": "",
                },
            },
            "user": {
                "name": "",
                "cookie": "",
                "uid": "",
                "ltoken_v1": "",
                "ltoken_v2": "",
                "stoken_v1": "",
                "stoken_v2": "",
                "game_token": "",
                "mid": "",
                "cookie_token": "",
                "fp": "",
            },
            "init": False,
        }
        base = merge_dict(base, conf)
        super().__init__(base)
