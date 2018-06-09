#----------------------------------------#
#IMAGE BLENDING USING PYTHON3 AND OPENCV #
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
import time
import numpy as np
path = "C:\\Users\\imkiller\\Desktop\\Python\\Dataset\\"

def emptyFunction():
    pass

def main():
    img1path = path + "4.1.01.tiff"
    img2path = path + "4.1.03.tiff"

    img1 = cv2.imread(img1path)
    img2 = cv2.imread(img2path)

    windowName = 'Image Blending'
    cv2.namedWindow(windowName)

    for i in np.linspace(0,1,100):
        alpha=i
        beta=1-i
        output = cv2.addWeighted(img1,alpha,img2,beta,0)
        output = cv2.resize(output,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
        cv2.imshow(windowName, output)
        if(cv2.waitKey(1)==27):
            break
        time.sleep(0.01)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

