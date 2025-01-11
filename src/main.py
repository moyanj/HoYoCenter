import webview
import click
from server import app as flask
from env import *
from tkinter import messagebox
import os
import requests
import utils
from multiprocessing import Process

# 渲染引擎字典
engine_dict = {"edge": "edgechromium", "ie": "mshtml", "gtk": "gtk", "qt": "qt"}


def has_webview():
    import winreg

    try:
        winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\EdgeWebView\\BLBeacon", 0, winreg.KEY_READ)  # type: ignore
    except:
        return False
    return True


def install_webview():
    if DEBUG or is_linux:
        return
    if has_webview():
        return
    messagebox.showwarning("警告", "未安装Microsoft Edge WebView2")
    # 是否安装Microsoft Edge WebView2
    if messagebox.askyesno("提示", "是否安装Microsoft Edge WebView2?"):
        req = requests.get(URLS.webview)
        WebViewDownloadPath = os.path.join(
            dirs.user_cache_dir, "MicrosoftEdgeWebView2.exe"
        )
        with open(WebViewDownloadPath, "wb") as f:
            f.write(req.content)
        os.system(WebViewDownloadPath)

        utils.restart()


def run_server(debug):
    port = utils.get_free_port()
    t = Process(
        target=flask.run,
        kwargs={"host": "127.0.0.1", "port": port, "debug": debug},
        name="HoYoCenter-Server",
    )
    t.start()
    return f"http://127.0.0.1:{port}/", t


# 创建WebView窗口
@click.command()
@click.option("--debug", is_flag=True, help="是否开启调试模式")
@click.option("--width", default=1280, help="宽度")
@click.option("--height", default=720, help="高度")
@click.option("--minimized", is_flag=True, help="最小化")
@click.option("--engine", default="edge", help="webview引擎")
def main(debug, width, height, minimized, engine):
    """主函数

    Arguments:
        略
    """
    # 判断是否为正确的渲染引擎
    if engine not in engine_dict.keys():
        messagebox.showerror("错误", "请输入正确的引擎！")
        exit()

    install_webview()

    # 判断是否启动服务器
    url, t = run_server(debug)

    window_args = {
        "title": "HoYoCenter",
        "width": width,
        "height": height,
        "minimized": minimized,
        "url": url,
    }

    start_args = {
        "user_agent": "HoYoCenter-WebView/1.1.0",
        "gui": engine_dict[engine],
        "storage_path": os.path.join(dirs.user_data_dir, "Web"),
    }

    # 以Debug模式启动
    if debug:
        window_args.update(
            {
                "title": "HoYoCenter-Debug",
                "text_select": True,
                "url": "http://localhost:5173/",
            }
        )

    print("HoYoCenter-Server URL:", url)
    webview.create_window(**window_args)
    webview.start(**start_args)  #  type: ignore 启动WebView

    # 强制结束服务器
    t.terminate()
    t.join()


if __name__ == "__main__":
    main()
