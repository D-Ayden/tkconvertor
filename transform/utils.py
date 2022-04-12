import re
import random
from ttkbootstrap.style import Keywords
from typing import Dict
from pathlib import Path
from tkinter import filedialog
from typing import Iterable

COLORS = Keywords.COLORS
TYPES = ["outline", "link"]

regulars = {
    "place": r'Fun.SetControlPlace\(uiName, "(.*)", (.*), (.*), (.*), (.*)\)',
    "tkMethod": r"(\S*) = tkinter\.(.*)\(([\s\S]*?)\)",
    "entryRelief": r"Entry_\d*\.configure\(relief=\".*?\"\)",
    "fun": r"[^\n].*Fun.*\)",
    "labelFrameFont": r"LabelFrame_\d*?\.configure\(font=(.*)\)",
}


UNUSED_CODE = """uiName = self.__class__.__name__
# coding=utf-8
# import libs
import sys
import Fun
import os
from tkinter import *
import tkinter.ttk
# Add your Varial Here: (Keep This Line of comments)
# Define UI Class"""


def sub(pattern: str, repl, content: str):
    """自定义正则替换函数

    Args:
        pattern (str): 正则表达式
        repl (_type_): 替换内容
        content (str): 原始内容

    Returns:
        _type_:
    """
    return re.sub(pattern, repl, content, 0)


def setPlace(target) -> str:
    """设置root控件位置

    Args:
        target (_type_): 正则匹配的结果

    Returns:
        str: 设置的位置
    """
    name = target.group(1)
    x = int(target.group(2))
    y = int(target.group(3))
    width = int(target.group(4))
    height = int(target.group(5))
    return f"{name}.place({x=}, {y=}, {width=}, {height=})"


def splitArgs(strArgs: str) -> Dict[str, str]:
    """分割函数参数

    Args:
        strArgs (str): 函数参数字符串

    Returns:
        Dict[str, str]: 分割后的参数映射
    """
    args = strArgs.replace(" ", "").split(",")
    argsMapping = {}
    for strArg in args:
        try:
            key, value = strArg.split("=")
        except ValueError:
            canvas = strArg
            argsMapping["canvas"] = canvas
        else:
            argsMapping[key] = value
    return argsMapping


def centerDlg(popupDlg, dw: int = None, dh: int = None):
    """设置窗口居中

    Args:
        popupDlg (_type_): 窗口对象
        dw (int, optional): 窗口宽度. Defaults to None.
        dh (int, optional): 窗口高度. Defaults to None.
    """

    dw = dw or popupDlg.winfo_width()
    dh = dh or popupDlg.winfo_height()

    root = popupDlg
    while 1:
        master = popupDlg.master
        if master is None:
            break
        root = master

    if root and popupDlg != root:
        rw = root.winfo_width()
        rh = root.winfo_height()
        x = (rw - dw) / 2 + root.winfo_x()
        y = (rh - dh) / 2 + root.winfo_y()

    else:
        import ctypes

        user32 = ctypes.windll.user32
        rw = user32.GetSystemMetrics(0)
        rh = user32.GetSystemMetrics(1)
        x = (rw - dw) / 2
        y = (rh - dh) / 4

    popupDlg.geometry(f'{int(dw)}x{int(dh)}+{int(x)}+{int(y)}')


def randomColor() -> str:
    return random.choice(COLORS)


def randomType() -> str:
    return random.choice(TYPES)


# *TODO Maybe don't use this function
def openFileDialog(
    route: str = ".",
    title: str = 'Open Python File',
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = None,
):
    if filetypes is None:
        filetypes = [('Python File', '*.py'), ('All files', '*')]
    filedialog.askopenfilename(
        initialdir=Path(route).resolve(),
        title=title,
        filetypes=filetypes,
    )
