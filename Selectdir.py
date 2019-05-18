import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
# from Main import *
from ImgProcess2 import *
import tkinter.font as tkFont
import os
# from search import *

class Selectdir(object):
    def __init__(self, master=None):
        self.root = master

        # make the canvas expandable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.root.geometry("1280x600")

        # use these two folderpath to save the path of dataset and queryset (default under this line)
        self.root.queryfolder = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\queries"
        self.root.datafolder = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset"
        # path to save index.csv
        self.root.indexcsvpath = self.root.queryfolder + "\\"
        # "C:/Users/DYL18/Desktop/Graduation_design/vacation-image-search-engine/queries/"

        self.createpage()

    def createpage(self):
        self.frame = tk.Frame(self.root, width=1400, height=400)
        self.frame.grid(row=0, column=0)

        ft = tkFont.Font(family='Fixdsys', size=30, weight=tkFont.BOLD)
        text = tk.Label(self.frame, heigh=5, text="欢迎使用图像检索程序", font=ft)
        text.grid(row=0, column=0, columnspan=5, sticky='n')
        ft2 = tkFont.Font(family='Fixdsys', size=20)
        text2 = tk.Label(self.frame,
                         text="点以下按钮选数据集为检索的图像集合", font=ft2)
        text2.grid(row=1, column=0,  columnspan=10, sticky='n')
        text3 = tk.Label(self.frame,
                         text="选择查询数据集作为要查询的图像集合", font=ft2)
        text3.grid(row=2, column=0, columnspan=10, sticky='n')

        databutton = tk.Button(self.frame, text="选择数据集", width=30, height=8, command=lambda: choosedatadir())
        databutton.grid(row=5, column=0, sticky='e')

        querybutton = tk.Button(self.frame, text="选择查询集", width=30, height=8, command=lambda: choosequerydir())
        querybutton.grid(row=5, column=1, sticky='w')

        enterbutton = tk.Button(self.frame, text="进入检索界面", width=60, height=5, command=lambda: enter())
        enterbutton.grid(row=6, column=0, columnspan=2)


        def choosedatadir():
            self.root.datafolder = filedialog.askdirectory(parent=self.frame, initialdir=os.getcwd(), title="请选择数据集")
            print(self.root.datafolder)

            querypath = "C:/Users/DYL18/Desktop/Graduation_design/vacation-image-search-engine/queries/"
            path = "C:/Users/DYL18/Desktop/Graduation_design/vacation-image-search-engine/"

            # use index.py to make index.csv (if self.root.datafolder doesn't give then use default)
            # but U need to click to call this command so..
            cmd = "python " + path + "index.py --dataset " + self.root.datafolder + " --index " + querypath + "index.csv"
            print(cmd)
            # cmd = "python index.py --dataset dataset --index index.csv"
            os.system(cmd)

        def choosequerydir():
            self.root.queryfolder = filedialog.askdirectory(parent=self.frame, initialdir=os.getcwd(), title="请选择查询集")
            print("*****")
            print(self.root.queryfolder)

            cmd = "python --version"
            returned_value = os.system(cmd)  # returns the exit code in unix
            print('returned value:', returned_value)


        def enter():
            self.frame.destroy()
            # MainPage(self.root)
            ImgProcess2(self.root)
