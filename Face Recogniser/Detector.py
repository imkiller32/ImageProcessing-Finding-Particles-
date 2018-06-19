import cv2
#import numpy as np

def main():
    path = "C:\\Users\\imkiller\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\"
    ClassifierPath= path + "haarcascade_frontalface_default.xml"
    facedetect=cv2.CascadeClassifier(ClassifierPath)

    #Resolution if available
    w=800
    h=600

    #Capturing LiveFeed
    cap=cv2.VideoCapture(1)

    #setting Width and Height
    cap.set(3,w)
    cap.set(4,h)

    rec=cv2.face.LBPHFaceRecognizer_create()
    rec.read("C:\\Users\\imkiller\\Desktop\\Python\\Face Recogniser\\Recognizer\\trainingData.yml")
    id=0
    #Checking Whether Cam is open or Not
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret=False
    
    ret, frame = cap.read()

    while ret:
        #Reading webcam
        ret, frame = cap.read()
        grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('gray',grayFrame) For Debug
        #Their can be more than one face.....parameters are set to get a good result
        faces = facedetect.detectMultiScale(grayFrame,1.3,5)

        for (x,y,w,h) in faces:
            #for Debug
            print('Ok')
            #Draw a red Rectangle Over image if their is a face
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            id,conf=rec.predict(grayFrame[y:y+h,x:x+w])
            if(id==1):
                id='name1'
            elif(id==2):
                id='name2'
            elif(id==3):
                id='name3'
            elif(id==4):
                id='name4'
            elif(id==5):
                id='name5'
            else:
                id='Unknown'
            cv2.putText(frame,str(id),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))
        cv2.imshow('FaceDetection Soft',frame)

        if cv2.waitKey(1) == 27: #exit on ESC
            break

    #Releasing Camera
    cap.release()
    #destroying All windows Created
    cv2.destroyAllWindows()
    print('Thanks For checking...visit again')

if __name__ == "__main__":
    print('Starting software...')
    main()
    
