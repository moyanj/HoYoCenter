import subprocess
import os
import shutil
import sys
import zipfile

NPM = "pnpm"
PYTHON = "python"


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


def build_web():
    os.chdir("web")
    subprocess.run(f"{NPM} run build", shell=True, check=True)
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
    shutil.copytree("src/data", "dist/HoYoCenter/data", dirs_exist_ok=True)


def main():
    clean_build()
    if "no-web" not in sys.argv:
        build_web()
    build_server()
    copy_data()
    make_zip()


if __name__ == "__main__":
    main()
