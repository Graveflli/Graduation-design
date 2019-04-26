from PIL import Image, ImageTk
import tkinter as tk
import glob
import cv2
import os
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher

import tkinter.font as tkFont

# 对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例

def resize(w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
    w, h = pil_image.size  # 获取图像的原始大小
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


root = tk.Tk()  # 创建窗口，必须在ImageTk.PhotoImage()之前！
root.geometry('1280x900')

# resize函数使用过程：
# ==================================================================
w_box = 240  # 期望图像显示的大小（窗口大小）
h_box = 180

path = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\queries"
datapath = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset"

ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)

text = tk.Label(root, text="This is a CBIR app, Please click the following image to search others", font=ft)
text.grid(row=0, column=0, columnspan=5, sticky='e')

status = tk.IntVar()


i = 1

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# use tk_im as a global list to store described image and avoid garbage collection
tk_im = []

# use this to store button and destroy them
button_list = []

def call_back(imagepath):
    print(imagepath)
    e = tk.StringVar()
    out = tk.Label(root, textvariable=e)
    out.grid(row=8, columnspan=5)

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

    #destroy all of button or label here:
    global button_list
    for a in button_list:
        print(a)
        a.destroy()
    button_list = []

    # tk_im_path = []
    # loop over the results
    for (score, resultID) in results:
        # load the result image and display it

        path2 = datapath + "\\" + resultID
        print(path2)

        pil_image2 = Image.open(path2)

        pil_image_resized2 = resize(w_box, h_box, pil_image2)
        # tk_im.append(ImageTk.PhotoImage(pil_image_resized2))

        # imageOutput = tk.Button(root, image=tk_im[j], width=w_box, height=h_box)
        a = ImageTk.PhotoImage(pil_image_resized2)
        imageOutput = tk.Button(root, image=a, width=w_box, height=h_box)

        button_list.append(imageOutput)

        # button_list[j].image = tk_im[j]
        button_list[j].image = a
        button_list[j].grid(row=int(9 + (k * 8)), column=int(j % 6), rowspan=6)

        j = j + 1
        k = int(j / 6)

    for a in button_list:
        print(a)


tk_image = []
tk_image_path = []
for imagepath in glob.glob(path + "/*.png"):
    pil_image = Image.open(imagepath)

    tk_image_path.append(imagepath)
    print(tk_image_path[i - 1])

    pil_image_resized = resize(w_box,h_box,pil_image)
    tk_image.append(ImageTk.PhotoImage(pil_image_resized))

    cb = (lambda p: lambda: call_back(p))(imagepath)
    button = tk.Button(root, image=tk_image[i - 1], width=w_box, height=h_box, command=cb)

    # global i
    i += 1
    print(i)
    button.grid(row=1, column=i - 2, rowspan=6, sticky='w')


root.mainloop()
