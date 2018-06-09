#----------------------------------------#
#......Channels Splitting And Merging....#
#--------AUTHOR- Ritesh Aggarwal---------#
#-----Language->Python3 AND OpenCv-------#
#-----------Github:->imkiller32----------#
#----------------Appendix----------------#
# The Path has to be change on another Pc#
#-Change images Accodring To You & Enjoy-#

#code Below

import cv2
import matplotlib.pyplot as plt

path = "C:\\Users\\imkiller\\Desktop\\Python\\Dataset\\"

def main():
    img1path = path + "4.2.03.tiff"
    img1 = cv2.imread(img1path)
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

    r, g ,b = cv2.split(img1)

    titles = ['OriginalOne', 'Reds', 'Greens', 'Blues']
    images = [cv2.merge((r, g, b)), r, g, b]

    plt.subplot(2,2,1)
    plt.imshow(images[0])
    plt.title(titles[0])
    plt.xticks([])
    plt.yticks([])

    for i in range(2,5):
        plt.subplot(2,2,i)
        plt.imshow(images[i-1],cmap=str(titles[i-1]))
        plt.title(titles[i-1])
        plt.xticks([])
        plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()
