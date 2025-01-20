import httpx
import subprocess
import zipfile
import os
import shutil

# 定义资源链接
hutao_res_url = "https://static-tiny.snapgenshin.cn/zip/{}.zip"
character_data_url = "https://github.com/EnkaNetwork/API-docs/raw/refs/heads/master/store/characters.json"
star_rail_repo_url = "https://ghproxy.cn/https://github.com/Mar-7th/StarRailRes.git"

# 定义资源列表
hutao_res_list = ["AvatarIcon", "IconElement"]


# 定义临时目录
tmpdir = "./resources"
ys_tmpdir = os.path.join(tmpdir, "Genshin")
sr_tmpdir = os.path.join(tmpdir, "StarRail")
git_tmpdir = ".tmp"


# 创建目录
def create_directories():
    print("正在创建目录...")
    shutil.rmtree(tmpdir, ignore_errors=True)
    os.makedirs(ys_tmpdir, exist_ok=True)
    os.makedirs(sr_tmpdir, exist_ok=True)
    os.makedirs(git_tmpdir, exist_ok=True)
    print("目录创建完成。")


# 下载原神资源
def download_ys():
    print("开始下载原神资源...")
    for name in hutao_res_list:
        url = hutao_res_url.format(name)
        print(f"正在下载 {name} 从 {url}")
        with httpx.Client(timeout=20) as client:
            with client.stream("GET", url) as response:
                with open(f"{name}.zip", "wb") as f:
                    for chunk in response.iter_bytes():
                        f.write(chunk)
        with zipfile.ZipFile(f"{name}.zip", "r") as zip_ref:
            zip_ref.extractall(os.path.join(ys_tmpdir, name))
        os.remove(f"{name}.zip")
    print("原神资源下载完成。")


def download_ys_info():
    print("开始下载原神角色信息...")
    if os.path.exists(os.path.join(git_tmpdir, "GenshinInfo")):
        print("原神角色信息已存在，跳过下载。")
    else:
        subprocess.run(
            f"git clone --filter=blob:none --sparse https://github.com/DGP-Studio/Snap.Metadata {git_tmpdir}/GenshinInfo",
            shell=True,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        os.chdir(os.path.join(git_tmpdir, "GenshinInfo"))
        subprocess.run(
            "git sparse-checkout add Genshin/CHS/",
            shell=True,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        os.chdir("../..")
    shutil.copytree(
        os.path.join(git_tmpdir, "GenshinInfo", "Genshin", "CHS"),
        os.path.join(ys_tmpdir, "Infomation"),
    )


# 准备原神角色图标
def prepare_AvatarIcon():
    print("正在准备原神角色图标...")
    try:
        os.remove(os.path.join(ys_tmpdir, "AvatarIcon", "Snap.png"))
    except FileNotFoundError:
        pass

    for i in os.listdir(os.path.join(ys_tmpdir, "AvatarIcon")):
        if (
            i.startswith("UI_AvatarIcon_Side_")
            or i.endswith("_TT.png")
            or "Costume" in i
            or i.startswith("UI_AvatarIcon_Paimon")
        ):
            try:
                os.remove(os.path.join(ys_tmpdir, "AvatarIcon", i))
            except FileNotFoundError:
                pass

    character_data = httpx.get(character_data_url, follow_redirects=True).json()
    for k, v in character_data.items():
        file = v["SideIconName"].replace("Side_", "")
        try:
            shutil.move(
                os.path.join(ys_tmpdir, "AvatarIcon", file + ".png"),
                os.path.join(ys_tmpdir, "AvatarIcon", f"{k}.png"),
            )
        except Exception:
            pass
    print("原神角色图标准备完成。")


# 下载星穹铁道资源
def download_sr():
    print("开始下载星穹铁道资源...")
    if os.path.exists(os.path.join(git_tmpdir, "StarRailRes")):
        print("星穹铁道资源已存在，跳过下载。")
        return

    subprocess.run(
        f"git clone --filter=blob:none --sparse {star_rail_repo_url} {git_tmpdir}/StarRailRes",
        shell=True,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    os.chdir(os.path.join(git_tmpdir, "StarRailRes"))
    subprocess.run(
        "git sparse-checkout add image/character_preview/",
        shell=True,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    subprocess.run(
        "git sparse-checkout add icon/element/",
        shell=True,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    subprocess.run(
        "git sparse-checkout add index_min/cn/",
        shell=True,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    os.chdir("../..")  # 返回上一级目录
    print("星穹铁道资源下载完成。")


# 准备星穹铁道资源
def prepare_sr():
    print("正在准备星穹铁道资源...")
    shutil.copytree(
        os.path.join(git_tmpdir, "StarRailRes", "image", "character_preview"),
        os.path.join(sr_tmpdir, "CharacterIcon"),
    )
    shutil.copytree(
        os.path.join(git_tmpdir, "StarRailRes", "icon", "element"),
        os.path.join(sr_tmpdir, "ElementIcon"),
    )
    shutil.copytree(
        os.path.join(git_tmpdir, "StarRailRes", "index_min", "cn"),
        os.path.join(sr_tmpdir, "Infomation"),
    )
    print("星穹铁道资源准备完成。")


# 主程序
if __name__ == "__main__":
    create_directories()
    download_ys()
    prepare_AvatarIcon()
    download_ys_info()
    download_sr()
    prepare_sr()
