import cv2
import sqlite3

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Recognizer/trainer.yml')

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def getInfo(id):
    conn = sqlite3.connect("CDS.db")
    cmd = "select * from PeopleDB where ID="+str(id)
    row = conn.execute(cmd)
    for i in row:
        profile = i
    conn.close()
    return profile

cap = cv2.VideoCapture(0)
while True:
    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        face=[]
    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,255),2)
        face = image[y:y+h, x:x+w]
        face = cv2.resize(face, (200,200))
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = recognizer.predict(face)
        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            print(confidence)
            display_string = str(confidence)+'% is a criminal'
        if confidence > 75:
            profile = getInfo(result[0])
            cv2.putText(image, str(display_string), (x,y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(image, str(profile[0]), (x,y+h+40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(image, str(profile[1]), (x,y+h+60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(image, str(profile[2]), (x,y+h+80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(image, str(profile[3]), (x,y+h+100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(image, str(profile[4]), (x,y+h+120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
            cv2.imshow('Face Cropper', image)

        else:
            cv2.putText(image, "No record found", (x,y+h+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Cropper', image)


    except:
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Cropper', image)
        pass

    if cv2.waitKey(1)==13:
        break


cap.release()
cv2.destroyAllWindows()

