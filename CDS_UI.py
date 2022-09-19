from tkinter import *
from PIL import Image,ImageTk
import os


def fun1():
    os.system("py CDS_DatasetCollector.py")


def fun2():
    os.system("py CDS_Trainer.py")


def fun3():
    os.system("py CDS_Detector.py")


def fun4():
    root.destroy()


root = Tk()

root.configure(background = "gray")

root.title("CRIMINAL DETECTION SYSTEM")

img = Image.open('tech.jpg')
size = width,height = img.size

name=Label(root, text="CRIMINAL  DETECTION  SYSTEM",font=("times new roman",20),fg="red",bg="black",height=3)
canvas = Canvas(width=800, height=100, bg='white')

#photo = ImageTk.PhotoImage(file='tech.jpg')
#canvas.create_image(0,0, image=photo, anchor=NW)

b1 = Button(root,text="Create Dataset",padx=15,font=("times new roman",20),bg="black",fg='green',command=fun1)
b2 = Button(root,text="Training",padx=40,font=("times new roman",20),bg="black",fg='green',command=fun2)
b3 = Button(root,text="Detector",padx=38,font=("times new roman",20),bg="black",fg='green',command=fun3)
b4 = Button(root,text="Exit",font=("times new roman",20),bg="black",fg='green',command=fun4)

name.grid(row=0,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
canvas.grid(row=1,columnspan=3)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1,padx=5,pady=10)
b3.grid(row=1,column=2)
b4.grid(row=2,columnspan=3,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
