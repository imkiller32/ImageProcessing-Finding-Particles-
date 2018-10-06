#..Program To Convert a colored image to BlackAndWhite image
#..Author : Ritesh Aggarwal
#..Concept : Thresholding
#..Complexity : O(r*c)
#..Used : Python3,OpenCv,Tkinter(GUI)
#..User Interactive : Yes
#..Github : www.github.com/imkiller32

import cv2
import PIL.Image, PIL.ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import ImageTk,Image

path = "C:\\Users\\imkiller\\Desktop\\"
imgpath = ""

root = Tk()
root.title('Convert Color To Black and White')
root.state('zoomed')
root.resizable(False,False)

text = ttk.Label(root,text = '\nChoose a image to convert to \'Black and White Image\'\n')
text.config(justify = CENTER, font = ('Courier', 20, 'bold') )
text.pack()    

panedwindow = ttk.Panedwindow(root,orient = HORIZONTAL)
panedwindow.config(width=800,height=500)
panedwindow.pack(expand = FALSE)

frame1 = ttk.LabelFrame(panedwindow,text='Original',relief=SUNKEN)
frame1.config(width=200,height=400)    

frame2 = ttk.LabelFrame(panedwindow,text='Converted',relief=SUNKEN)
frame2.config(width=200,height=400)

panedwindow.add(frame1,weight=1)
panedwindow.add(frame2,weight=1)

original = ttk.Label(frame1, text = 'Image Not Available')
original.pack(padx=5,pady=5)

converted = ttk.Label(frame2, text = 'Try Convert image to view the result')
converted.config(justify = CENTER,wrap=100)
converted.pack(padx=5,pady=5)


def OPEN():
    global imgpath
    imgpath = (fd.askopenfile().name)
    img = ImageTk.PhotoImage(Image.open(imgpath))
    original.config(image = img)
    original.img=img

def CONVERT():
    if(imgpath == ""):
        messagebox.showinfo(title = 'Error', message = 'Please Choose an Image First')
        return
    cimg = cv2.imread(imgpath,0)
    r,c = cimg.shape
    
    for i in range(r):
        for j in range(c):
            if(cimg[i][j]>128):
                cimg[i][j]=255
            else:
                cimg[i][j]=0
    nimg = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(cimg))
    converted.config(image = nimg)
    converted.img=nimg

choose_button = ttk.Button(root, text = 'Open')
choose_button.pack(padx = 5, pady = 5)
choose_button.config(command = OPEN)

convert = ttk.Button(root,text = 'Convert')
convert.pack(padx = 5, pady = 5)
convert.config(command = CONVERT)

root.mainloop()


