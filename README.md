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
<a href="#开发">开发文档</a>
</p>

# 介绍

HoYoCenter 是一个跨平台的米哈游系列游戏数据查询工具，支持以下游戏：

- 崩坏：星穹铁道
- 原神

它旨在为玩家提供一个便捷的工具，用于查询游戏数据、角色信息、装备详情等。通过简洁的界面和高效的后端处理，HoYoCenter 让玩家能够快速获取所需信息，提升游戏体验。

---

# 安装

## 下载

- 最新稳定版本：推荐从[GitHub Releases](https://github.com/moyanj/HoYoCenter/releases)下载最新稳定版本。

- 最新开发版本：如果需要最新功能，可以从[Github Actions](https://github.com/moyanj/HoYoCenter/actions/workflows/debug.yml)下载最新开发版本，但请注意开发版本可能包含未修复的错误。

## 安装说明

- 支持平台：目前预打包版本支持 x86_64 架构的 Windows 和 Linux 平台，从源码安装可以支持 Windows, Linux, MacOS

- Windows：需要 Windows 10 及以上版本。

- Linux：请确保系统中已安装`libwebkit2gtk-3.0`或`libwebkit2gtk-4.0`（Qt 版本无需此依赖）。

- Windows 平台：请确保系统中已安装[Microsoft Edge WebView2](https://developer.microsoft.com/zh-cn/microsoft-edge/webview2/)。

## 运行说明

如果你下载了 zip 程序压缩包：

1. 解压下载的文件。

2. 双击打开`HoYoCenter.exe`（Windows）或`HoYoCenter`（Linux）即可运行。

如果你下载了源代码，请参见下文的开发说明。

---

# 开发

## 环境要求

- Python：3.10 及以上版本。

- Node.js：22 版本。

## 安装依赖

```bash
# 安装 Python 依赖
pip install uv
uv pip install -r pyproject.toml

# 安装前端依赖
cd web
pnpm install  # 推荐使用 pnpm，也可以使用 npm install
```

## 运行

### Debug 模式:

1. 打开两个终端窗口。

2. 在第一个窗口运行前端开发服务器：

```bash
cd web
pnpm dev
```

3. 在第二个窗口运行主程序：

```bash
cd src
python main.py --debug
```

### 生产模式

运行以下命令打包并运行生产版本：

```bash
# 打包前端代码
cd web
pnpm build

# 复制dist
cp -r dist/ ../src/dist/

# 运行后端服务
cd src
python main.py
```

## 打包

打包为可执行文件（EXE）：

```bash
# 不带 Qt 和 GTK 的版本(Linux将无法运行)
python build.py

# 带 Qt 版本
uv sync --extra qt
python build.py qt

# 带 GTK 版本
uv sync --extra gtk
python build.py gtk
```

---

# 特别感谢

感谢以下项目和组织对 HoYoCenter 的支持：

- [UIGF Organization](https://uigf.org)：为原神数据交换提供标准化支持，以及 API 逆向。

- [GitHub](https://github.com)：提供代码托管和 CI/CD 支持。

- [Enka Network](https://enka.network)：提供原神角色数据查询接口。

- [DGP-Studio](https://github.com/DGP-Studio): 数据支持

---

使用的技术栈

HoYoCenter 使用了以下技术栈，确保高效、稳定和易用性：

- [FastAPI](https://github.com/tiangolo/fastapi)：高性能的 Python Web 框架，用于构建 RPC 服务。

- [JSON-RPC](https://www.jsonrpc.org/)：用于前后端通信的轻量级 RPC 协议。

- [PyInstaller](https://github.com/pyinstaller/pyinstaller)：将 Python 应用打包为可执行文件。

- [Vue.js](https://vuejs.org/)：渐进式 JavaScript 框架，用于构建用户界面。

- [Element Plus](https://element-plus.org/)：基于 Vue 3 的 UI 组件库，提供丰富的组件支持。

- [TypeScript](https://www.typescriptlang.org/)：提供静态类型检查，增强代码的可维护性。

- [Vite](https://vitejs.dev/)：下一代前端构建工具，提供快速的开发体验。

- [PyWebView](https://github.com/r0x0r/pywebview)：用于在桌面环境中显示 Web 页面。

---

# 贡献指南

欢迎贡献代码或提出改进建议！在提交 PR 或 Issue 之前，请阅读[贡献指南](CONTRIBUTING.md)。

---

# 许可证

HoYoCenter 采用[类 MIT 许可证](LICENSE)，请在使用和分发时遵守相关条款。

---

# 联系我们

如果有任何问题或建议，请通过以下方式联系我们：

- GitHub Issues：在[GitHub 仓库](https://github.com/moyanj/HoYoCenter/issues)提交问题。

- Email：moyan@moyanjdc.top
