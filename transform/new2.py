import tkinter
import tkinter.font
from pathlib import Path
from tkinter import filedialog
from typing import Iterable

import ttkbootstrap as ttk

from transform.tk2ttkbootstrap import tk2ttkbootstrap
from transform.utils import centerDlg


class tk2ttk:
    def __init__(self, root, isTKRoot=True):

        self.root = root
        self.path_var = ttk.StringVar(value='')

        if isTKRoot:
            root.title("tk2ttkbootstrap")
            centerDlg(self.root, 640, 200)
            root["background"] = "#efefef"
        Form_1 = tkinter.Canvas(root, width=10, height=4)
        Form_1.place(x=0, y=0, width=640, height=200)
        Form_1.configure(bg="#efefef")
        Form_1.configure(highlightthickness=0)

        # Create the elements of root
        textLabel = ttk.Label(text="文件转换")
        LabelFrame_2 = ttk.Labelframe(
            Form_1, labelwidget=textLabel, takefocus=True, width=10, bootstyle="info"
        )

        LabelFrame_2.place(x=40, y=14, width=560, height=124)  # lock
        LabelFrame_2.configure(relief="groove")
        LabelFrame_2_Ft = tkinter.font.Font(
            family="Cascadia Mono",
            size=15,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0,
        )
        textLabel.configure(font=LabelFrame_2_Ft)
        Label_4 = ttk.Label(LabelFrame_2, text="文件路径", width=10, bootstyle="info")

        Label_4.place(x=12, y=22, width=66, height=28)
        Label_4.configure(relief="flat")

        Entry_5 = ttk.Entry(LabelFrame_2, textvariable=self.path_var)

        Entry_5.place(x=94, y=22, width=372, height=28)

        Button_6 = ttk.Button(LabelFrame_2, text="选择", width=10, bootstyle="warning")
        Button_6.configure(command=self.openFileDialog)

        Button_6.place(x=477, y=22, width=66, height=28)

        Button_3 = ttk.Button(Form_1, text="确定", width=10, bootstyle="success")
        Button_3.configure(command=self.on_convert)

        Button_3.place(x=524, y=146, width=76, height=33)

        # Initial all element's Data

        # Add Some Logic Code Here: (Keep This Line of comments)

    def on_convert(self: 'tk2ttk'):
        tk2ttkbootstrap(self.path_var.get())

    # *TODO Rename
    def openFileDialog(
        self: 'tk2ttk',
        route: str = '.',
        title: str | None = 'Open Python File',
        filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]]
        | None = None,
    ):
        if filetypes is None:
            filetypes = [('Python File', '*.py')]
        if path := filedialog.askopenfilename(
            initialdir=Path(route).resolve(), title=title, filetypes=filetypes
        ):
            self.path_var.set(path)


# Create the root of Kinter
if __name__ == "__main__":
    root = tkinter.Tk()
    MyDlg = tk2ttk(root)
    root.mainloop()
