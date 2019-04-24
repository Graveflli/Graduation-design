
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()

path = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset\100000.png"
path2 = r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset\101200.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    img2 = ImageTk.PhotoImage(Image.open(path2))
    panel.configure(image=img2)
    panel.image = img2

root.bind("<Return>", callback)
root.mainloop()



# import cv2
# img = cv2.imread("C://Users//DYL18//Pictures//DaLong Wang.PNG")
# img = cv2.imread("C:\\Users\\DYL18\\Pictures\\DaLong Wang2.PNG")
# img = cv2.imread("C:/Users/DYL18/Pictures/DaLong Wang.PNG")
# img = cv2.imread(r"C:\Users\DYL18\Desktop\Graduation_design\vacation-image-search-engine\dataset\100000.png")
# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


