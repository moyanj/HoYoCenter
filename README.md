<h1 align="center">
  <img src="https://cdn.jsdelivr.net/gh/moyanj/HoYoCenter/images/icon.png" width="64px" height="64px">
  <br>
  <a href="https://github.com/moyanj/HoYoCenter"> 
    HoYoCenter
  </a>
</h1>
<p align="center">
    <a target="_blank" href="https://github.com/moyanj"><img src="https://img.shields.io/badge/github-moyanj-brightgreen.svg"/></a>&nbsp; 
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/Code%20Style-black-000000.svg"/></a> 
    <a target="_blank" href="https://img.shields.io/badge/License-BSD-brightgreen.svg"><img src="https://img.shields.io/badge/License-BSD-brightgreen.svg" /></a>&nbsp;
    <a target="_blank" href="https://img.shields.io/github/languages/top/moyanj/HoYoCenter.svg"><img src="https://img.shields.io/github/languages/top/moyanj/HoYoCenter.svg" /></a>&nbsp;
    <a target="_blank" href="https://img.shields.io/github/commit-activity/t/moyanj/HoYoCenter"><img src="https://img.shields.io/github/commit-activity/t/moyanj/HoYoCenter" /></a>&nbsp;
</p>
<p align="center">
  此存储库包含了<strong>HoYoCenter</strong>的源代码。<strong>HoYoCenter</strong>是一个跨平台的<a href="https://www.mihoyo.com">米哈游</a>系列游戏数据查询工具。
</p>

<p align="center">
<a href="#介绍">介绍</a> &nbsp;&bull;&nbsp;
<a href="#安装">安装</a> &nbsp;&bull;&nbsp;
 <a href="/dev">开发文档</a>
</p>

# 介绍

HoYoCenter 是一个跨平台的米哈游系列游戏数据查询工具，支持以下游戏：

- 崩坏：星穹铁道
- 原神
- 绝区零

# 安装

下载[最新 releases 版本](https://github.com/moyanj/HoYoCenter/releases/latest)

下载[最新开发版本](https://github.com/moyanj/HoYoCenter/actions/workflows/debug.yml)（可能无法正常运行）

## 安装说明

- 目前预打包仅支持 x86_64 架构的 Windows，Linux 平台（Windows 需要 Windows 10 及以上版本）。
- ArchLinux 系用户现只支持从源代码运行。
- Linux 平台请确保您的系统中已安装`libwebkit2gtk-3.0`或`libwebkit2gtk-4.0`。
- Windows 平台请确保您的系统中已安装`Microsoft Edge WebView2`（[下载地址](https://developer.microsoft.com/zh-cn/microsoft-edge/webview2/)）。

## 运行说明

- 如果你下载了 zip 程序压缩包，请解压后双击打开`HoYoCenter.exe`（或者`HoYoCenter`）即可运行。
- 如果你下载了源代码，请参见下文的开发说明。

# 开发

## 环境要求

- Python 3.10
- Node.js 22

## 安装依赖

```bash
pip install uv
uv pip install -r pyproject.toml
cd web
pnpm install # 或者 npm install
```

## 运行

debug 模式

```bash
cd web
pnpm dev
# 另开启一个终端
cd src
python main.py --debug
```

## 打包

```bash
python build.py
```

# 特别感谢

- [OpenAI](https://openai.com/)
- [Microsoft](https://www.microsoft.com/)
- [GitHub](https://github.com/)
- [清华大学](https://github.com/THUDM)
- [UIGF organization](https://uigf.org)
- [EnkaAPI](https://enka.network/)

# 特定的原神项目

- [Snap.Hutao](https://hut.ao)
- [Genshin.Launcher.Plus](https://github.com/DawnFz/Genshin.Launcher.Plus)
- [Starward](https://github.com/Scighost/Starward)

# 使用的技术栈

## 后端

- [fastapi](https://github.com/tiangolo/fastapi)（服务器框架）
- [pywebview](https://github.com/r0x0r/pywebview)（显示页面）
- [pyinstaller](https://github.com/pyinstaller/pyinstaller)（打包 EXE）

## 前端

- [Vue](https://vuejs.org/)（前端 JS 框架）
- [Elment Plus](https://element-plus.org/)（前端 UI 框架）
- [TypeScript](https://www.typescriptlang.org/)
- [Vite](https://vitejs.dev/)
