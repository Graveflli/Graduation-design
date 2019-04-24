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

ft = tkFont.Font(family = 'Fixdsys',size = 20,weight = tkFont.BOLD)

text = tk.Label(root,text = "This is a CBIR app, Please click the following image to search others",font = ft)
text.grid(row = 0,column = 0,columnspan = 5,sticky = 'e')

status = tk.IntVar()


i = 1

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))


tk_im = []
imageOutput = tk.Button(root, width=w_box, height=h_box)
def call_back(imagepath):
    print(imagepath)
    # if status.get() == 1:
    e = tk.StringVar()
    out = tk.Label(root, textvariable=e)
    out.grid(row=8, columnspan=5)

    global i
    # i += 1
    e.set(imagepath)

    # nowtime = os.popen('date')
    # print(nowtime.read())

    # command like :  python search.py --index index.csv --query queries/108100.png --result-path dataset

    imageID = imagepath[imagepath.rfind("\\") + 1:]
    querypath = "queries/" + imageID

    # load the query image and describe it
    query = cv2.imread(querypath)
    features = cd.describe(query)

    # perform the search
    searcher = Searcher("index.csv")
    results = searcher.search(features)

    # display the query
    # cv2.imshow("Query", query)

    # testpath = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset\103500.png"
    '''
    a = Image.open(testpath)
    b = resize(w_box, h_box, a)
    d = ImageTk.PhotoImage(image=b)
    # imageOutput = tk.Button(root,text = "haha")
    imageOutput = tk.Button(root, image=d, width=w_box, height=h_box)
    imageOutput.grid(row=12, column=0, rowspan=6)
    print("hahaha")

    '''
    j = 0
    k = 0

    # tk_im_path = []
    # loop over the results
    for (score, resultID) in results:
        # load the result image and display it

        # path2 = "dataset" + "\\" + resultID
        path2 = datapath + "\\" + resultID
        print(path2)

        pil_image2 = Image.open(path2)
        # tk_im_path.append(pil_image2)

        pil_image_resized2 = resize(w_box, h_box, pil_image2)
        # photograph = ImageTk.PhotoImage(pil_image_resized2)
        tk_im.append(ImageTk.PhotoImage(pil_image_resized2))

        # imageOutput = tk.Label(root, image=tk_im[j], width=w_box, height=h_box)
        imageOutput.configure(image=tk_im[j])
        imageOutput.grid(row=int(9 + (k * 8)), column=int(j % 6), rowspan=6)

        j = j + 1
        k = int(j / 6)

    '''
        result = cv2.imread(path)
        cv2.imshow("Result", result)
        cv2.waitKey(0)
        '''


tk_image = []
tk_image_path = []
for imagepath in glob.glob(path + "/*.png"):
    pil_image = Image.open(imagepath)
    # print(imagepath)
    tk_image_path.append(imagepath)
    print(tk_image_path[i - 1])
    # tk_image_path[i - 1] = imagepath

    # image = cv2.imread(imagepath)
    # cv2.imshow("image",image)
    # cv2.waitKey(0)

    pil_image_resized = resize(w_box,h_box,pil_image)
    tk_image.append(ImageTk.PhotoImage(pil_image_resized))

    '''
    cb = (lambda p: lambda: call_back(p))(imagepath)
    button = tk.Button(root, image=tk_image[i - 1], width=w_box, height=h_box, command=cb)
    '''
    # c = imagepath
    # button = tk.Button(root, image=tk_image[i - 1], width=w_box, height=h_box, command=lambda : call_back(c))
    # python BUG:imagepath 循环一圈，我调用command callback的时候传入此作为参数，结果是最后的image的path 但在一般人眼里imagepath作为局部变量
    # 但从结果来看并非如此，郭氏便先用c作为变量等于imagepath 在赋值过去，依然不行，使出大招：俩lambda，结果对了，我也无语了。。wtfpython
    cb = (lambda p: lambda: call_back(p))(imagepath)
    button = tk.Button(root, image=tk_image[i - 1], width=w_box, height=h_box, command=cb)

    # global i
    i += 1
    print(i)
    # button.pack()
    button.grid(row=1, column=i - 2, rowspan=6, sticky='w')


root.mainloop()
