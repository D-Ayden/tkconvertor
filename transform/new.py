import tkinter
import tkinter.font
from tkinter import ttk

from transform.utils import centerDlg


class tk2ttk:
    def __init__(self, root, isTKRoot=True):

        self.root = root

        if isTKRoot == True:
            root.title("tk2ttk")
            centerDlg(self.root, 640, 200)
            root["background"] = "#efefef"
        Form_1 = tkinter.Canvas(root, width=10, height=4)
        Form_1.place(x=0, y=0, width=640, height=200)
        Form_1.configure(bg="#efefef")
        Form_1.configure(highlightthickness=0)

        # Create the elements of root
        textLabel = ttk.Label(text="文件转换")
        LabelFrame_2 = ttk.Labelframe(
            Form_1, labelwidget=textLabel, takefocus=True, width=10
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
        Label_4 = ttk.Label(LabelFrame_2, text="文件路径", width=10)

        Label_4.place(x=12, y=22, width=66, height=28)
        Label_4.configure(relief="flat")

        Entry_5 = ttk.Entry(
            LabelFrame_2,
        )

        Entry_5.place(x=94, y=22, width=372, height=28)

        Button_6 = ttk.Button(LabelFrame_2, text="选择", width=10)

        Button_6.place(x=477, y=22, width=66, height=28)

        Button_3 = ttk.Button(Form_1, text="确定", width=10)

        Button_3.place(x=524, y=146, width=76, height=33)

        # Inital all element's Data

        # Add Some Logic Code Here: (Keep This Line of comments)


# Create the root of Kinter
if __name__ == "__main__":
    root = tkinter.Tk()
    MyDlg = tk2ttk(root)
    root.mainloop()
