import re
import os
import shutil
from tempfile import template

pattern = r'version\s*=\s*"(\d+\.\d+\.\d+)"'
version = re.search(pattern, open("../../pyproject.toml", "r").read()).group(1)  # type: ignore


def get_directory_size(directory):
    """
    计算指定目录的总大小（包括子目录中的文件）。

    :param directory: 要计算大小的目录路径
    :return: 目录的总大小（以字节为单位）
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


if not os.path.exists("../../dist"):
    print("程序暂未打包")
    exit()

print("正在复制")
shutil.copytree("../../dist/", "src/opt/", dirs_exist_ok=True)
shutil.copy("../desktop.desktop", "src/usr/share/HoYoCenter.desktop")
shutil.copy("../../images/icon.png", "src/usr/share/icons/HoYoCenter.png")
os.remove("src/opt/HoYoCenter.zip")
print("正在修改权限")
os.chmod("src/opt/HoYoCenter", 0o755)

print("正在生成 control")
with open("src/DEBIAN/control_t", "r") as f:
    template = f.read()

with open("src/DEBIAN/control", "w") as f:
    template = template.replace("__VERSION__", version)
    template = template.replace(
        "__SIZE__", str(int(get_directory_size("src/opt/") / 1024))
    )
    f.write(template)

print("正在打包")
os.chdir("src")
os.system(f"dpkg-deb --build . ../hoyocenter_{version}_amd64.deb")
os.chdir("..")
