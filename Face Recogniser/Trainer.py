import os
import cv2
import numpy as np
from PIL import Image

def getImagesWithID(path):
    imagePaths=[f for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        PATH=os.path.join(path,imagePath)
        faceImg=cv2.imread(PATH,0)
        #faceImg=Image.open(PATH)
        faceNp=np.array(faceImg,'uint8')
        ID=str(os.path.split(PATH)[-1].split(".")[1])
        print(ID)
        faces.append(faceNp)
        IDs.append(int(ID))
        cv2.imshow('Training',faceImg)
        cv2.waitKey(10)

    return IDs,faces

def main():    
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    path="C:\\Users\\imkiller\\Desktop\\Python\\Face Recogniser\\"
    IDs,faces = getImagesWithID(path+"DataSet")
    recognizer.train(faces,np.array(IDs))
    recognizer.save(path+"Recognizer\\trainingData.yml")
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print('Starting software...')
    main()
    
