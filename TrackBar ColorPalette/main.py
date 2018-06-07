#----------------------------------------#
# COLOR TRACKER USING PYTHON3 AND OPENCV #
#--------AUTHOR- Ritesh Aggarwal---------#
#-----------Language->Python3------------#
#-----------Github:->imkiller32----------#
#----------------Appendix----------------#
#uint8 = unsigned integer of 8 bit(0-255)#
#np.zeros(p1, p2)..p1 = tuple & p2 = type#


#................NOTE....................#
#The Output Window will close on pressing Esc Button#

import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    #print("ok")
    img1 = np.zeros((512, 512, 3), np.uint8)
    windowName = 'Open CV Color Palette'
    cv2.namedWindow(windowName)

    cv2.createTrackbar('B', windowName, 0, 255,emptyFunction)
    cv2.createTrackbar('G', windowName, 0, 255,emptyFunction)
    cv2.createTrackbar('R', windowName, 0, 255,emptyFunction)

    while True:
        cv2.imshow(windowName, img1)

#The Output Window will close on pressing Esc Button#
        if(cv2.waitKey(1)==27):
            break
        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)

        img1[:] = [blue, green, red]
        print(blue, green, red)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    
