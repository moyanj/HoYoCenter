import subprocess
import os
import shutil
import sys
import zipfile
import json
import time
import re

NPM = "pnpm"
PYTHON = "python"

pattern = r'version\s*=\s*"(\d+\.\d+\.\d+)"'


def clean_build():
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")


def make_zip():
    zip = zipfile.ZipFile("dist/HoYoCenter.zip", "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk("dist/HoYoCenter"):
        fpath = path.replace("dist/HoYoCenter", "")

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))

    zip.close()


def make_build_info():
    return {
        "version": re.search(pattern, open("pyproject.toml", "r").read()).group(1),  # type: ignore
        "commit": subprocess.check_output("git rev-parse HEAD", shell=True)
        .decode("utf-8")
        .strip(),
        "branch": subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True)
        .decode("utf-8")
        .strip(),
        "python": ".".join(
            [str(sys.version_info.major), str(sys.version_info.minor), str(sys.version_info.micro)]  # type: ignore
        ),
        "platform": sys.platform,
        "args": sys.argv[1:],
        "build_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    }


def build_web():
    os.chdir("web")
    subprocess.run(f"{NPM} run build-only", shell=True, check=True)
    os.chdir("..")


def build_server():
    os.chdir("src")
    subprocess.run(
        f"pyinstaller main.py --workpath ../build --distpath ../dist --windowed --specpath ../build --name HoYoCenter --icon ../images/icon.ico --uac-admin --clean --noconfirm",
        shell=True,
        check=True,
    )
    os.chdir("..")


def copy_data():

    shutil.copytree("web/dist", "dist/HoYoCenter/dist", dirs_exist_ok=True)
    with open("dist/HoYoCenter/build_info.json", "w") as f:
        json.dump(make_build_info(), f)


def main():
    clean_build()
    if "no-web" not in sys.argv:
        build_web()
    build_server()
    copy_data()
    if "no-zip" not in sys.argv:
        make_zip()


if __name__ == "__main__":
    main()
