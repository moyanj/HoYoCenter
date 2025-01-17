import aiofiles
import ujson


class BetterDict:

    def __init__(self, data: dict) -> None:
        self.update(data)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        return self.__dict__.get(key)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def update(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                self.__dict__[key] = value

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def __delattr__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __str__(self):
        return ujson.dumps(self.__dict__, ensure_ascii=False, indent=4)

    def __repr__(self):
        return f"BetterDict({self.__dict__})"

    async def __save__(self, path: str):
        async with aiofiles.open(path, "w") as f:
            await f.write(str(self))


class Config(BetterDict):
    user_name: str = "用户"
    theme: str = "auto"
    init: bool = False
