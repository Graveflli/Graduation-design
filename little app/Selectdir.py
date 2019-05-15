import tkinter as tk
from tkinter.messagebox import *
from PIL import ImageTk,Image
import cv2

class Selectdir(object):
    def __init__(self, master=None):
        self.root = master

        # make the canvas expandable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # self.frame = tk.Frame(self.root, width=1200, height=400)
        # self.frame.grid(row=0, column=0)
        # self.canvas = tk.Canvas(self.frame, bg='red', width=1000, height=300, scrollregion=(0, 0, 1300, 1000))
        # self.canvas.create_line(0, 0, 200, 100)
        #
        # hbar = tk.Scrollbar(self.frame, orient='horizontal')
        # # hbar.pack(side="bottom", fill="x")
        # hbar.grid(row=1, column=0, sticky='we')
        # hbar.config(command=self.canvas.xview)
        # vbar = tk.Scrollbar(self.frame, orient="vertical")
        # # vbar.pack(side="right", fill="y")
        # vbar.grid(row=0, column=1, sticky='ns')
        # vbar.config(command=self.canvas.yview)
        # self.canvas.config(width=1000, height=300)
        # self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        # # self.canvas.pack(side="left", expand=True, fill="both")
        # self.canvas.grid(row=0, column=0)
        #
        # # self.canvas.create_window(0, 0, window=self.frame)



        self.frame2 = tk.Frame(self.root, width=1200, height=300)
        self.frame2.grid(row=2, column=0)
        self.canvas2 = tk.Canvas(self.frame2, bg='green', width=1200, height=300, scrollregion=(0, 0, 4000, 10000))

        path2 = r"C:\Users\DYL18\Pictures\images (3).jpg"
        path = r"C:\Users\DYL18\Pictures\images (1).jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        button1 = tk.Button(self.canvas2, image=img)
        button1.image = img
        button2 = tk.Button(self.canvas2, image=img)
        button2.image = img
        # button1.grid(row=0, column=0)
        #  button1.place(0, 0)
        # button2.grid(row=0, column=1)
        self.canvas2.create_window(200, 100, window=button1)
        self.canvas2.create_window(400, 200, window=button2)
        # i = 2
        # while(i != 4):
        #     button = tk.Button(self.canvas2, image=img)
        #     img = ImageTk.PhotoImage(Image.open(path2))
        #     button.image = img
        #     button.grid(row=0, column=i)
        #     i = i + 1
        # i = 0
        # while (i != 5):
        #     button = tk.Button(self.canvas2, image=img)
        #     img = ImageTk.PhotoImage(Image.open(path2))
        #     button.image = img
        #     # self.canvas.create_image(50 * i, 50 * i, image=img)
        #     button.grid(row=1, column=i)
        #     i = i + 1
        self.canvas2.create_line(1600, 0, 0, 1000)
        hbar2 = tk.Scrollbar(self.frame2, orient='horizontal')
        hbar2.grid(row=3, column=0, sticky='we')
        hbar2.config(command=self.canvas2.xview)
        vbar2 = tk.Scrollbar(self.frame2, orient="vertical")
        vbar2.grid(row=2, column=1, sticky='ns')
        vbar2.config(command=self.canvas2.yview)

        # self.canvas2.create_window(0, 0, window=self.frame2)

        self.canvas2.config(width=1200, height=300)
        self.canvas2.config(xscrollcommand=hbar2.set, yscrollcommand=vbar2.set)
        self.canvas2.grid(row=2, column=0)
        # self.frame2.grid(row=2, column=0)

        # self.canvas2.create_window((4,4), window=self.frame2, anchor="nw", tags="self.frame")

        # self.canvas2.create_window(0, 0, window=self.frame2)
        # self.canvas2.create_window(0, 0)
        # self.frame.update_idletasks()
        # self.canvas2.config(scrollregion=self.canvas2.bbox("all"))


# class Selectdir(object):
#     def __init__(self, master=None):
#         self.root = master
#
#         self.root.geometry("800x600")
#
#         self.createPage()
#
#     def createPage(self):
#         label1 = tk.Label(text="wa")
#         label1.grid(row=0, column=0)

        # self.page = tk.Frame(self.root, bg='green', width=500, height=320)
        #
        # self.page.grid(row=0, column=0)
        #
        # self.canvas = tk.Canvas(self.page, width=400, height=220)
        #
        # tk.Button(self.page, text="test").grid(row=1, stick='w', pady=10)
        #
        # vbar = tk.Scrollbar(self.canvas, orient="vertical")
        # vbar.grid(row=0, column=100)
        # self.canvas.config(yscrollcommand=vbar.set)
        # self.canvas.create_window((90, 240), window=self.page)



        # hbar.config(command=canvas.xview)

        # self.page.vsb = tk.Scrollbar(self.page, orient="vertical", command=self.page.canvas.yview)
        # self.page.canvas.configure(yscrollcommand=self.page.vsb.set)

        # self.page.vsb.pack(side="right", fill="y")
        # self.canvas.pack(side="left", fill="both", expand=True)
        # self.canvas.create_window((4,4), window=self.page, anchor="nw", tags="self.frame")



