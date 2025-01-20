from tkinter import messagebox
import httpx
import random
import zipfile
import shutil
import os
import tempfile
from env import app_dir, dirs

base_url_list = ["https://cn-nb1.rains3.com/hoyocenter/"]
base_url = random.choice(base_url_list)


def need_update():
    url = base_url + "version.txt"
    rep = int(httpx.get(url).text)
    version_path = os.path.join(dirs.user_config_dir, "version.txt")
    if not os.path.exists(version_path):
        return True
    else:
        with open(version_path, "r") as f:
            ver = int(f.read())
    print(ver, rep)
    if rep > ver:  # type: ignore
        return True
    return False


def download():
    url = base_url + "resources.zip"
    shutil.rmtree(os.path.join(app_dir, "dist", "resources"), ignore_errors=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        with httpx.stream("GET", url) as rep:
            with open(os.path.join(tmpdir, "resources.zip"), "wb") as f:
                for chunk in rep.iter_bytes():
                    f.write(chunk)

        with zipfile.ZipFile(os.path.join(tmpdir, "resources.zip"), "r") as zip_ref:
            os.makedirs(os.path.join(app_dir, "dist", "resources"), exist_ok=True)
            zip_ref.extractall(os.path.join(app_dir, "dist", "resources"))

    ver = int(httpx.get(base_url + "version.txt").text)
    with open(os.path.join(dirs.user_config_dir, "version.txt"), "w") as f:
        f.write(str(ver))


def main():
    if need_update():
        r = messagebox.showinfo("资源更新", "检测到有资源更新，点击下载...")
        download()
        messagebox.showinfo("资源更新", "更新完成")

    else:
        pass
