from PIL import Image, ImageTk
import tkinter as tk
import glob
import cv2
import os
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher

import tkinter.font as tkFont

w_box = 240
h_box = 180
i = 0
tk_image = []
tk_image_path = []
cd = ColorDescriptor((8, 12, 3))
tk_im = []
button_list = []
# 功能 -》 选择数据集之后得到csv文件！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
class ImgProcess2(object):
    def __init__(self, master=None):  #, w_box=240, h_box=180):
        self.root = master
        # root = tk.Tk()  # 创建窗口，必须在ImageTk.PhotoImage()之前！
        # self.root.geometry('1280x900')
        self.root.geometry('1380x900')

        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_columnconfigure(0, weight=0)

        # self.root.w_box = 240
        # self.root.h_box = 180

        self.createimagepage()

    # 对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
    def resize(self, w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.size  # 获取图像的原始大小
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)

    def call_back(self, imagepath):
        print(imagepath)
        e = tk.StringVar()
        out = tk.Label(self.canvas2, textvariable=e)
        # self.canvas.create_window(300, 200, window=out)
        # self.canvas.grid(row=0, column=0)

        global i

        e.set(imagepath)

        # command like :  python search.py --index index.csv --query queries/108100.png --result-path dataset

        imageID = imagepath[imagepath.rfind("\\") + 1:]
        querypath = "queries/" + imageID

        # load the query image and describe it
        query = cv2.imread(querypath)
        features = cd.describe(query)

        # perform the search
        searcher = Searcher("index.csv")
        results = searcher.search(features)

        j = 0
        k = 0

        # destroy all of button or label here:
        global button_list
        for a in button_list:
            print(a)
            a.destroy()
        button_list = []

        # tk_im_path = []
        # loop over the results
        for (score, resultID) in results:
            # load the result image and display it

            path2 = self.root.datafolder + "\\" + resultID
            print(path2)

            pil_image2 = Image.open(path2)

            pil_image_resized2 = self.resize(w_box, h_box, pil_image2)
            # tk_im.append(ImageTk.PhotoImage(pil_image_resized2))

            # imageOutput = tk.Button(root, image=tk_im[j], width=w_box, height=h_box)
            a = ImageTk.PhotoImage(pil_image_resized2)
            imageOutput = tk.Button(self.canvas2, image=a, width=w_box, height=h_box)

            button_list.append(imageOutput)

            # button_list[j].image = tk_im[j]
            button_list[j].image = a
            self.canvas2.create_window(150+250*(int(j % 6)), 100 + 250 * k, window=button_list[j])
            # self.canvas2.create_window(350 + 250 * k, 100*(int(j % 6)), window=button_list[j])
            # button_list[j].grid(row=int(9 + (k * 8)), column=int(j % 6), rowspan=6)

            j = j + 1
            k = int(j / 6)

        for a in button_list:
            print(a)

    def createimagepage(self):

        status = tk.IntVar()
        global i
        i = 0

        # initialize the image descriptor
        global cd
        cd = ColorDescriptor((8, 12, 3))

        # use tk_im as a global list to store described image and avoid garbage collection
        global tk_im
        tk_im = []

        # use this to store button and destroy them
        global button_list
        button_list = []


        if self.root.queryfolder == '':
            path = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\queries"
        else:
            path = self.root.queryfolder

        if self.root.datafolder == '':
            datapath = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset"
        else:
            datapath = self.root.datafolder

        self.textframe = tk.Frame(self.root, width=1380, height=200)
        self.textframe.grid(row=0, column=0, columnspan=10)
        ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
        text = tk.Label(self.textframe,
                        text="This is a CBIR app, Please click the following image to search others,hahahahaha",font=ft)
        text.grid(row=0, column=0, columnspan=5, sticky='e')
        self.textframe.grid_rowconfigure(0, weight=1)

        self.frame = tk.Frame(self.root, width=1580, height=400)
        self.frame.grid(row=1, column=0)
        self.canvas = tk.Canvas(self.frame, bg='red', width=1500, height=300, scrollregion=(0, 0, 1600, 1000))
        self.canvas.create_line(0, 0, 200, 100)

        global tk_image
        tk_image = []
        global tk_image_path
        tk_image_path = []
        for imagepath in glob.glob(path + "/*.png"):
            pil_image = Image.open(imagepath)

            tk_image_path.append(imagepath)
            print(tk_image_path[i])

            # pil_image_resized = self.resize(self.root.w_box, self.root.h_box, pil_image)
            pil_image_resized = self.resize(w_box, h_box, pil_image)
            tk_image.append(ImageTk.PhotoImage(pil_image_resized))

            cb = (lambda p: lambda: self.call_back(p))(imagepath)
            button = tk.Button(self.frame, image=tk_image[i], width=w_box, height=h_box, command=cb)

            # global i
            i += 1
            print(i)
            self.canvas.create_window(150+250*(i-1), 100, window=button)
            # button.grid(row=1, column=i - 2, rowspan=6, sticky='w')

        hbar = tk.Scrollbar(self.frame, orient='horizontal')
        hbar.grid(row=1, column=0, sticky='we')
        hbar.config(command=self.canvas.xview)
        vbar = tk.Scrollbar(self.frame, orient="vertical")
        vbar.grid(row=0, column=1, sticky='ns')
        vbar.config(command=self.canvas.yview)

        self.canvas.config(width=1500, height=300)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.grid(row=0, column=0)

        # self.canvas.create_window(0, 0, window=self.frame)



        self.frame2 = tk.Frame(self.root, width=1580, height=400)
        self.frame2.grid(row=2, column=0)
        self.canvas2 = tk.Canvas(self.frame2, bg='green', width=1500, height=400, scrollregion=(0, 0, 1600, 1000))

        hbar2 = tk.Scrollbar(self.frame2, orient='horizontal')
        hbar2.grid(row=1, column=0, sticky='we')
        hbar2.config(command=self.canvas2.xview)
        vbar2 = tk.Scrollbar(self.frame2, orient="vertical")
        vbar2.grid(row=0, column=1, sticky='ns')
        vbar2.config(command=self.canvas2.yview)

        self.canvas2.config(width=1500, height=400)
        self.canvas2.config(xscrollcommand=hbar2.set, yscrollcommand=vbar2.set)
        self.canvas2.grid(row=0, column=0)


