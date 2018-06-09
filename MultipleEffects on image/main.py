#----------------------------------------#
#IMAGE ROTATION USING PYTHON3 AND OPENCV #
#--------AUTHOR- Ritesh Aggarwal---------#
#-----------Language->Python3------------#
#-----------Github:->imkiller32----------#
#----------------Appendix----------------#
# The Path has to be change on another Pc#
#-Change images Accodring To You & Enjoy-#


#................NOTE....................#
#The Output Window will close on pressing Esc Button#

#code Below

import cv2
import numpy
import time

def main():
    path = "C:\\Users\\imkiller\\Desktop\\Python\\Dataset\\"
    img1path = path + "4.1.06.tiff"
    img1 = cv2.imread(img1path)
    img1 = cv2.resize(img1,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
    rows,columns,channels = img1.shape

    angle = 0
    scale = 0
    
    while True:
        R = cv2.getRotationMatrix2D((columns,rows/2),angle,scale)
        output = cv2.warpAffine(img1,R,(columns,rows))
        cv2.imshow('See the magic',output)
        angle +=1
        scale +=0.1
        if angle == 360:
            angle = 0
        if scale>=2:
            scale = 0
        time.sleep(0.01)
        if cv2.waitKey(1) ==27:
            break
    
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()
