#This Project Works Well if Your camera(WEBCAM) is working ..if Not then Check my another project where the video is loaded manually (From directory)


#----------------------------------------#
#DATASET CREATER USING PYTHON AND OPENCV #
#--------AUTHOR- Ritesh Aggarwal---------#
#-----------Language->Python3------------#
#-----------Github:->imkiller32----------#
#----------------Appendix----------------#
# Select Camera According to your Laptop.#
#for more camera hint ...comment below
#---------Enjoy Your Live Feed----------#


#importing useful library
import cv2
#import numpy as np

def main():
    path = "C:\\Users\\imkiller\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\"
    writePath="C:\\Users\\imkiller\\Desktop\\Python\\Face Recogniser\\DataSet\\"
    ClassifierPath= path + "haarcascade_frontalface_default.xml"
    facedetect=cv2.CascadeClassifier(ClassifierPath)
    id=input('Enter User id:')
    #Resolution if available
    w=800
    h=600

    #variables
    sample=0
    
    
    #Capturing LiveFeed
    cap=cv2.VideoCapture(1)

    #setting Width and Height
    cap.set(3,w)
    cap.set(4,h)

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
            sample+=1
            #for Debug
            print('Ok')
            cv2.imwrite(writePath+"/User."+str(id)+"."+str(sample)+".jpg",grayFrame[y:y+h,x:x+w])
            #Draw a red Rectangle Over image if their is a face
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.waitKey(100)   
        cv2.imshow('FaceDetection Soft',frame)
        cv2.waitKey(1)
        if sample>50:
            break

    #Releasing Camera
    cap.release()
    #destroying All windows Created
    cv2.destroyAllWindows()
    print('Thanks For checking...visit again')

if __name__ == "__main__":
    print('Starting software...')
    main()
    
