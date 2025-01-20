import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import font
import tkinter.ttk as ttk
import traceback
import sys

proc = []


class MainWindow(tk.Tk):
    def __init__(self, exc_type, exc_value, exc_traceback):
        super().__init__()
        self.exc_type = exc_type
        self.exc_value = exc_value
        self.exc_traceback = exc_traceback
        self.title("错误报告")
        self.init_ui()

    def init_ui(self):
        # 使用 Frame 将界面分为上下两部分
        top_frame = ttk.Frame(self)
        top_frame.pack(fill=tk.X, padx=10, pady=10)
        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 顶部显示错误信息
        ttk.Label(top_frame, text="发生了一个错误：", font=font.Font(size=12, weight="bold")).pack(anchor=tk.W)
        ttk.Label(top_frame, text=f"错误类型：{self.exc_type.__name__}", font=font.Font(size=10)).pack(anchor=tk.W)
        ttk.Label(top_frame, text=f"错误信息：{str(self.exc_value)}", font=font.Font(size=10)).pack(anchor=tk.W)
        ttk.Label(top_frame, text="错误追踪信息：", font=font.Font(size=10)).pack(anchor=tk.W)

        # 底部显示详细的错误追踪信息
        self.error_text = scrolledtext.ScrolledText(bottom_frame, wrap=tk.WORD)
        self.error_text.pack(fill=tk.BOTH, expand=True)
        self.error_text.insert(tk.END, "".join(traceback.format_exception(self.exc_type, self.exc_value, self.exc_traceback)))
        self.error_text.config(state=tk.DISABLED)  # 设置为不可编辑

        # 按钮区域
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        ttk.Button(button_frame, text="复制错误信息", command=self.copy_error).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="关闭", command=self.close_window).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="退出程序", command=self.close_window).pack(side=tk.LEFT, padx=5)

    def copy_error(self):
        """将错误信息复制到剪贴板"""
        self.clipboard_clear()
        error_text = self.error_text.get("1.0", tk.END)
        self.clipboard_append(error_text)
        messagebox.showinfo("提示", "错误信息已复制到剪贴板！")

    def close_window(self):
        """关闭窗口"""
        self.destroy()

    def quit_program(self):
        """退出程序"""
        self.destroy()
        sys.exit(1)


def error_handler(exc_type, exc_value, exc_traceback):
    window = MainWindow(exc_type, exc_value, exc_traceback)
    window.mainloop()
    for t in proc:
        t.terminate()
        t.join()
    sys.exit(1)
