import aiofiles
import ujson


class BetterDict:
    """
    更好的字典

    Attributes:
        __dict (dict):原始字典
    """

    def __init__(self, conf: dict):
        self.__dict = conf
        self._update()

    def __getattr__(self, name):
        if name in self.__dict:
            return self.__dict[name]
        else:
            raise AttributeError(f"BetterDict has no attribute '{name}'")

    def __setattr__(self, name, value):

        if isinstance(value, dict):
            value = BetterDict(value)
        elif isinstance(value, list):
            value = [
                BetterDict(item) if isinstance(item, dict) else item for item in value
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
            conf (dict):要更新的字典
        """
        if conf:
            self.__dict = conf

        for key, value in self.__dict.items():
            self.__setattr__(key, value)

    async def __save__(self, path: str):
        async with aiofiles.open(path, "w") as f:
            await f.write(str(self))


class Config(BetterDict):
    user_name: str = "用户"
    theme: str = "auto"
    init: bool = False
