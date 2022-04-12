# coding=utf-8
# import libs
import sys
import tk2ttk_cmd
import tk2ttk_sty
import Fun
import os
import tkinter
from tkinter import *
import tkinter.ttk
import tkinter.font

# Add your Varial Here: (Keep This Line of comments)
# Define UI Class
class tk2ttk:
    def __init__(self, root, isTKroot=True):
        uiName = self.__class__.__name__
        Fun.Register(uiName, "UIClass", self)
        self.root = root
        Fun.Register(uiName, "root", root)
        style = tk2ttk_sty.SetupStyle()
        if isTKroot == True:
            root.title("tt2ttk")
            Fun.CenterDlg(uiName, root, 640, 200)
            root["background"] = "#efefef"
        Form_1 = tkinter.Canvas(root, width=10, height=4)
        Form_1.place(x=0, y=0, width=640, height=200)
        Form_1.configure(bg="#efefef")
        Form_1.configure(highlightthickness=0)
        Fun.Register(uiName, "Form_1", Form_1)
        # Create the elements of root
        LabelFrame_2 = tkinter.LabelFrame(
            Form_1, text="文件转换", takefocus=True, width=10, height=4
        )
        Fun.Register(uiName, "LabelFrame_2", LabelFrame_2)
        Fun.SetControlPlace(uiName, "LabelFrame_2", 40, 14, 560, 124)  # lock
        LabelFrame_2.configure(relief="groove")
        LabelFrame_2_Ft = tkinter.font.Font(
            family="Cascadia Mono",
            size=15,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0,
        )
        LabelFrame_2.configure(font=LabelFrame_2_Ft)
        Label_4 = tkinter.Label(LabelFrame_2, text="文件路径", width=10, height=4)
        Fun.Register(uiName, "Label_4", Label_4)
        Fun.SetControlPlace(uiName, "Label_4", 12, 22, 66, 28)  # lock
        Label_4.configure(relief="flat")
        Label_4_Ft = tkinter.font.Font(
            family="Cascadia Mono",
            size=12,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0,
        )
        Label_4.configure(font=Label_4_Ft)
        Entry_5_Variable = Fun.AddTKVariable(uiName, "Entry_5", "")
        Entry_5 = tkinter.Entry(LabelFrame_2, textvariable=Entry_5_Variable)
        Fun.Register(uiName, "Entry_5", Entry_5)
        Fun.SetControlPlace(uiName, "Entry_5", 94, 22, 372, 28)  # lock
        Entry_5.configure(relief="sunken")
        Button_6 = tkinter.Button(LabelFrame_2, text="选择", width=10, height=4)
        Fun.Register(uiName, "Button_6", Button_6)
        Fun.SetControlPlace(uiName, "Button_6", 478, 22, 66, 28)  # lock
        Button_6.configure(relief="ridge")
        Button_6_Ft = tkinter.font.Font(
            family="Cascadia Mono",
            size=12,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0,
        )
        Button_6.configure(font=Button_6_Ft)
        Button_6.bind(
            "<Button-1>",
            Fun.EventFunction_Adaptor(
                tk2ttk_cmd.Button_6_onButton1, uiName=uiName, widgetName="Button_6"
            ),
        )
        Button_3 = tkinter.Button(Form_1, text="确定", width=10, height=4)
        Fun.Register(uiName, "Button_3", Button_3)
        Fun.SetControlPlace(uiName, "Button_3", 524, 148, 76, 33)  # lock
        Button_3.configure(relief="ridge")
        Button_3_Ft = tkinter.font.Font(
            family="Cascadia Mono",
            size=15,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0,
        )
        Button_3.configure(font=Button_3_Ft)
        # Inital all element's Data
        Fun.InitElementData(uiName)
        # Add Some Logic Code Here: (Keep This Line of comments)


# Create the root of Kinter
if __name__ == "__main__":
    root = tkinter.Tk()
    MyDlg = tk2ttk(root)
    root.mainloop()
