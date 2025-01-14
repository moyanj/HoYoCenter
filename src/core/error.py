import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
import tkinter.ttk as ttk
import traceback

proc = []


class MainWindow(tk.Tk):
    def __init__(self, exc_type, exc_value, exc_traceback):
        super().__init__()
        self.exc_type = exc_type
        self.exc_value = exc_value
        self.exc_traceback = exc_traceback
        self.title("Error")

        self.init_ui()

    def init_ui(self):
        ttk.Label(self, text="发生了一个错误：", font=font.Font(size=12)).pack()
        ttk.Label(self, text="错误类型：" + self.exc_type.__name__).pack()
        ttk.Label(self, text="错误信息：" + str(self.exc_value)).pack()
        ttk.Label(self, text="错误追踪信息：").pack()
        # 使用 scrolledtext 组件显示异常信息，支持滚动
        self.error_text = scrolledtext.ScrolledText(self)
        self.error_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # 将异常信息格式化后插入到 scrolledtext 组件中
        traceback_info = "".join(traceback.format_tb(self.exc_traceback))
        self.error_text.insert(
            tk.END, f"{self.exc_type.__name__}:{self.exc_value}\n" + traceback_info
        )
        self.error_text.config(state=tk.DISABLED)  # 设置为不可编辑
        ttk.Button(self, text="关闭", command=self.close_window).pack(pady=10)
        # 关闭按钮
        close_button = ttk.Button(self, text="退出", command=self.close_window)

        close_button.pack(pady=10)

    def close_window(self):
        self.destroy()  # 关闭窗口

    def make_info(self):
        pass


def error_handler(exc_type, exc_value, exc_traceback):
    window = MainWindow(exc_type, exc_value, exc_traceback)
    window.mainloop()
    for t in proc:
        t.terminate()
        t.join()
    exit(1)
