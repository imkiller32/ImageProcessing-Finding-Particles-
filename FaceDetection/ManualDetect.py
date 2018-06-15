#This uses a video loaded from some directory ..You can specify your own path


#----------------------------------------#
#FACE DETECTION USING PYTHON3 AND OPENCV #
#--------AUTHOR- Ritesh Aggarwal---------#
#-----------Language->Python3------------#
#-----------Github:->imkiller32----------#
#---------Enjoy Your DETECTION-----------#


#importing useful library
import cv2
#import numpy as np


def main():
    path = "C:\\Users\\imkiller\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\"
    ClassifierPath= path + "haarcascade_frontalface_default.xml"
    facedetect=cv2.CascadeClassifier(ClassifierPath)

    #resolution
    w=800
    h=600

    #select a video path
    cap=cv2.VideoCapture("E:\FILES\motivational\ABC.mp4")

    #setting width and height
    cap.set(3,w)
    cap.set(4,h)

    while cap.isOpened():
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            #debug
            print('ok')
            #Red color box over Face
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            
        cv2.imshow('DETECTION',frame)
        if cv2.waitKey(1)==27:  #exit on ESC
            break

    #releasing camera
    cap.release()
    #destroy window created
    cv2.destroyAllWindows()
    print('Bye...')

if __name__ == "__main__":
    print('Starting software...')
    main()
    
