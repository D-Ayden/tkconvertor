import os
from pathlib import Path
from typing import Mapping

from transform.utils import UNUSED_CODE, setPlace, splitArgs, sub

centerDlg_regular = r"Fun\.CenterDlg\(uiName, (\w*?), (\d*?), (\d*?)\)"
place_regular = r'Fun.SetControlPlace\(uiName, "(\w*)", (\d*), (\d*), (\d*), (\d*)\)'
tkMethod_regular = r"(\w*) = tkinter\.([a-zA-Z]*?)\(([\s\S]*?)\)"
relief_regular = r"([a-zA-Z]*?)_\d*\.configure\(relief=\"[a-z]*?\"\)"
fun_regular = r"[^\n].*Fun.*\)"
font_regular = r"([a-zA-Z]*?)_\d*?_Ft = tkinter.font.Font\([\s\S]*?\)"
fontConfigure_regular = r"([a-zA-Z]*?)_\d*?\.configure\(font=(\w*?)\)"


file = "./init/tk2ttk.py"
os.system(f"black {file}")
fileName = Path(file).stem
unused = UNUSED_CODE.split("\n")
unused.extend(
    (
        f"import {fileName}_cmd",
        f"import {fileName}_sty",
        f"style = {fileName}_sty.SetupStyle()",
    )
)


def convert(target) -> str:
    name, method, args = target.group(1), target.group(2), target.group(3)
    argsMapping = splitArgs(args)
    match method:
        case "Label":
            result = convertLabel(name, argsMapping)
        case "Button":
            result = convertButton(name, argsMapping)
        case "Entry":
            result = convertEntry(name, argsMapping)
        case "LabelFrame":
            result = convertLabelFrame(name, argsMapping)
        case _:
            result = target.group()

    return result


def convertCenterDlg(target):
    """转换控件居中代码

    Args:
        target (_type_): 正则匹配的结果

    Returns:
        _type_: 替换后的控件居中代码
    """
    widget = target.group(1)
    if widget == "root":
        widget = "self.root"
    dw, dh = target.group(2), target.group(3)

    return f"centerDlg({widget}, {dw}, {dh})"


def convertLabel(name: str, argsMapping: Mapping[str, str]) -> str:
    """转换 Label 控件

    Args:
        name (str): 控件名称
        argsMapping (Mapping[str, str]): 控件参数映射

    Returns:
        str: 替换后的 Label 控件
    """
    form = argsMapping.pop("canvas") if argsMapping.get("canvas") else ""
    if argsMapping.get("height"):
        del argsMapping["height"]

    args = ",".join(f"{item[0]}={item[1]}" for item in argsMapping.items())

    return f"{name} = ttk.Label({form},{args})"


def convertButton(name: str, argsMapping: Mapping[str, str]) -> str:
    """转换 Button 控件

    Args:
        name (str): 控件名称
        argsMapping (Mapping[str, str]): 控件参数映射

    Returns:
        str: 替换后的 Button 控件
    """
    form = argsMapping.pop("canvas") if argsMapping.get("canvas") else ""
    if argsMapping.get("height"):
        del argsMapping["height"]

    args = ",".join(f"{item[0]}={item[1]}" for item in argsMapping.items())

    return f"{name} = ttk.Button({form},{args})"


def convertEntry(name: str, argsMapping: Mapping[str, str]) -> str:
    """转换 Entry 控件

    Args:
        name (str): 控件名称
        argsMapping (Mapping[str, str]): 控件参数映射

    Returns:
        str: 替换后的 Entry 控件
    """
    form = argsMapping.pop("canvas") if argsMapping.get("canvas") else ""
    if argsMapping.get("textvariable"):
        del argsMapping["textvariable"]

    args = ",".join(f"{item[0]}={item[1]}" for item in argsMapping.items())

    return f"{name} = ttk.Entry({form},{args})"


def convertLabelFrame(name: str, argsMapping: Mapping[str, str]) -> str:
    """转换 LabelFrame 控件

    Args:
        name (str): 控件名称
        argsMapping (Mapping[str, str]): 控件参数映射

    Returns:
        str: 替换后的 LabelFrame 控件

    """
    form = argsMapping.pop("canvas") if argsMapping.get("canvas") else ""
    text = argsMapping.pop("text") if argsMapping.get("text") else ""
    labelStr = f'textLabel = ttk.Label(text={text})'

    if argsMapping.get("height"):
        del argsMapping["height"]

    args = ",".join(f"{item[0]}={item[1]}" for item in argsMapping.items())

    newLabelFrameStr = f"""{name} = ttk.Labelframe(
        {form},
        labelwidget=textLabel,
        {args}
    )"""
    return f"{labelStr}\n        {newLabelFrameStr}"


def convertConfigureFont(target) -> str:
    """转换字体设置代码

    Args:
        target (_type_): 正则匹配的结果

    Returns:
        str: 替换后的字体设置代码
    """
    name = target.group(1)
    ft = target.group(2)

    if name == "LabelFrame":
        return f"textLabel.configure(font={ft})"
    return ""


def convertRelief(target) -> str:
    """转换控件的 relief 属性设置代码

    Args:
        target (_type_): 正则匹配的结果

    Returns:
        str: 替换后的控件的 relief 属性设置代码
    """
    method = target.group(1)
    if method in ["Entry", "Button"]:
        return ""
    return target.group()


def convertFont(target) -> str:
    """转换控件的 font 属性设置代码

    Args:
        target (_type_): 正则匹配的结果

    Returns:
        str: 替换后的控件的 font 属性设置代码
    """
    name = target.group(1)
    if name != "LabelFrame":
        return ""
    return target.group()


def trans(content: str) -> str:
    for each in unused:
        content = content.replace(each, '')

    content = sub(centerDlg_regular, convertCenterDlg, content)
    content = sub(place_regular, setPlace, content)  # 设置组件位置
    content = sub(tkMethod_regular, convert, content)  # 更换组件
    content = sub(font_regular, convertFont, content)
    content = sub(fontConfigure_regular, convertConfigureFont, content)
    content = sub(relief_regular, convertRelief, content)
    content = sub(fun_regular, '', content)  # 去除第三方方法
    content = content.replace("isTKroot", "isTKRoot")

    return content


with open(file, "r+", encoding="utf-8") as rf, open(
    "./new.py", "x", encoding="utf-8"
) as wf:
    content = rf.read()
    content = trans(content)
    wf.write("from tkinter import ttk\n")
    wf.write("from transform.utils import centerDlg")

    wf.write(content)


os.system("black new.py")
