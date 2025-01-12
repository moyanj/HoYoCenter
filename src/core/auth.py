from typing import Optional
import hashlib
import time
import random


class Salt:
    K2 = "G1rXOpMLQS77VPWEGycOSxekCTZe2Q8M"
    LK2 = "sd1e1gQJuvqBfZxas1oeAACXzbim5cge"
    VERSION = "2.80.1"

    X4 = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"
    X6 = "	t0qEgfub6cvueAPgR5m9aQWWVciEer7v"
    prod = "JwYDpKvLj6MrMqqYU6jTKF17KNO2PXoS"


def ds2(
    body: str = "",
    query: Optional[list[str]] = None,
    salt: str = Salt.X4,
):
    if query is None:
        squery = ""
    else:
        squery = "&".join(sorted(query))
    t = int(time.time())
    r = random.randint(100001, 200000)
    c = hashlib.md5(
        f"salt={salt}&t={t}&r={r}&b={body}&q={squery}".encode("utf-8")
    ).hexdigest()
    return f"{t},{r},{c}"


def ds1(salt: str = Salt.K2):
    lettersAndNumbers = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    t = int(time.time())
    r = "".join(random.choices(lettersAndNumbers, k=6))
    main = f"salt={salt}&t={t}&r={r}"
    c = hashlib.md5(main.encode("utf-8")).hexdigest()
    return f"{t},{r},{c}"
