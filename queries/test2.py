import tkinter as tk
from PIL import Image, ImageTk
import glob

root = tk.Tk()
root.geometry('1280x900')
path = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset\100000.png"
path2 = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset\101200.png"
path3 = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\queries"
path = r"C:\Users\DYL18\Pictures\1444873934051.jpg"
path4 = r"C:\Users\DYL18\Pictures\Bing Images"

'''
def call(e = ""):
    print("ya")
    image2 = ImageTk.PhotoImage(Image.open(path2))
    print(image2)
    b = tk.Button(root, image=image2)
    b.image = image2
    a.destroy()
    b.grid(row=100, column=0)

'''
button_list = []
flag = 0

def call(e = ""):

    global button_list
    for i in button_list:
        i.destroy()
    button_list = []

    print("ya")

    global flag
    if flag == 0:
        j = 0
        for imagepath in glob.glob(path3 + "\*.png"):
            image2 = ImageTk.PhotoImage(Image.open(imagepath))
            print(image2)
            b = tk.Button(root, image=image2)
            button_list.append(b)
            button_list[j].image = image2
            # a.destroy()
            button_list[j].grid(row=int(j * 1), column=1)
            j = j + 1
        flag = 1
    else:
        j = 0
        for imagepath in glob.glob(path4 + "\*.jpg"):
            image2 = ImageTk.PhotoImage(Image.open(imagepath))
            print(image2)
            b = tk.Button(root, image=image2)
            button_list.append(b)
            button_list[j].image = image2
            # a.destroy()
            button_list[j].grid(row=int(j * 1), column=1)
            j = j + 1
        flag = 0




image1 = ImageTk.PhotoImage(Image.open(path))

# cb = (lambda p: lambda: call(p))("haha")
cb = lambda: call()
a = tk.Button(root, image=image1, command=cb)
# a.image = image1
a.grid(column=0, row=0)
print("wa")

# root.bind("<Button-1>", call)
root.mainloop()
