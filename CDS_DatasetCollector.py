import cv2
import sqlite3
from tkinter import *
from tkinter import messagebox

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def submit():
    Id = entry1.get()
    Name = entry2.get()
    Age = entry3.get()
    Gender = entry4.get()
    CR = entry5.get()
    DBCreator(Id,Name,Age,Gender,CR)
    
    

def DBCreator(Id,Name,Age,Gender,CR):
    conn = sqlite3.connect("CDS.db")
    cmd = "select * from PeopleDB where Id="+str(Id)
    cursor = conn.execute(cmd)
    flag=0
    for row in cursor:
        flag=1
    if(flag==1):
        messagebox.showerror("ID exists","Enter new ID")
    else:
        messagebox.showwarning("Image","Press OK to start capturing images")
    
    cmd = "insert into PeopleDB(ID,Name,Age,Gender,CR) Values("+str(Id)+","+str(Name)+","+str(Age)+","+str(Gender)+","+str(CR)+")"
    conn.execute(cmd)

    conn.commit()
    conn.close()

    sample=0

    while(True):
        try:
            ret, img = cam.read()
            #cv2.imshow('o/p for frame',img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                #incrementing sample number 
                sample+=1
                #saving the captured face in the dataset folder
                gray = gray[y:y+h,x:x+w]
                cv2.imwrite("dataSet/User."+Id +'.'+ str(sample) + ".png", gray)
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('frame',img)
            #wait for 2 miliseconds 
            if cv2.waitKey(2) == 13:
                break
            # break if the sample number is morethan 20
            elif sample>20:
                cam.release()
                cv2.destroyAllWindows()
                break
        except:
            print("Print Error Please Check ")



root = Tk()

root.title("Database Creator")

Id = Label(root, text="ID")
Name = Label(root, text="Name")
Age = Label(root, text="Age")
Gender = Label(root, text="Gender")
CR = Label(root, text="Criminal Record")

entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry4=Entry(root)
entry5=Entry(root)

Id.grid(row=0)
entry1.grid(row=0,column=1)

Name.grid(row=1)
entry2.grid(row=1,column=1)

Age.grid(row=2)
entry3.grid(row=2,column=1)

Gender.grid(row=3)
entry4.grid(row=3,column=1)

CR.grid(row=4)
entry5.grid(row=4,column=1)


b = Button(root, text="Submit", command=submit).grid(row=5,columnspan=2)

root.mainloop()
