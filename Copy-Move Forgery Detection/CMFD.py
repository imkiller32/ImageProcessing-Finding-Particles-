#..Program To Find a copy-move forgery in a image
#..Implementation of a research paper
#..Author : Ritesh Aggarwal
#..Concept : RadixSort Optimization
#..Complexity : O(klogk)  where, k = (N-b+1)^2
#   image of size = N x N
#   block size = b x b
#..Used : Python3,OpenCv(Just to read Image ),numpy,matplotlib
#..User Interactive : Yes
#..Written From Scratch
#..Github : www.github.com/imkiller32

import cv2
import numpy
import math
import matplotlib.pyplot as plt

path="C:\\Users\\rites\\Desktop\\"
imgpath=path+"image.png"

img=cv2.imread(imgpath,0)
#img = numpy.random.randint(0,256, size=(32,32))
#print(img)
img_r,img_c=img.shape
print(img_r,img_c)
window_r,window_c=16,16
T1 = 100
T2 = 10

titles=['Original','Thresholded']

plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title(titles[0])
plt.xticks([])
plt.yticks([])

modified = img        

block=0
window=[]
row=[]
col=[]

for r in range(0,img_r-window_r+1):
    for c in range(0,img_c-window_c+1):
        window.append(img[r:r+window_r,c:c+window_c])
        row.append(r)
        col.append(c)
        block=block+1
        
##print(block)
res=False
array_fv=[]
x=0
for curr in range(0,block):

    array_sv=[]
    totalElements=0
    intensity=[]
    avgI=[]
    for r in range(0,window_r-8+1,8):
        for c in range(0,window_c-8+1,8):
            
            sub_block=window[curr][r:r+8,c:c+8]
            sub_vector=[]
            Sum=0
            
            for element in sub_block:
                for e in element:
                    
                    Sum += e
                    totalElements += 1
                    sub_vector.append(e)
            
            array_sv.append(sub_vector)
            intensity.append(Sum)
    
    feature_vector=[]

    avg_intensity = (intensity[0]+intensity[1]+intensity[2]+intensity[3])/(totalElements)
    
    feature_vector.append(avg_intensity)
    
    for i in range(0,4):
        intensity[i]=intensity[i]/64

    feature_vector.append(math.floor(255*(intensity[0]/(4*feature_vector[0]))))
    feature_vector.append(math.floor(255*(intensity[1]/(4*feature_vector[0]))))
    feature_vector.append(math.floor(255*(intensity[2]/(4*feature_vector[0]))))
    feature_vector.append(math.floor(255*(intensity[3]/(4*feature_vector[0]))))

    feature_vector.append(intensity[0]-feature_vector[0])
    feature_vector.append(intensity[1]-feature_vector[0])
    feature_vector.append(intensity[2]-feature_vector[0])
    feature_vector.append(intensity[3]-feature_vector[0])

    m1 = -10000000000
    m2 = 10000000000
    for i in range(5,9):
        if(feature_vector[i] > m1):
            m1=feature_vector[i]
        if(feature_vector[i] < m2):
            m2=feature_vector[i]

    feature_vector[0] = math.floor(feature_vector[0])

    for i in range(5,9):
        feature_vector[i] = math.floor(255*((feature_vector[i]-m2)/(m1-m2)))

    Tuple=(feature_vector,x)
    array_fv.append(Tuple)
    #print(array_fv[x])
    x+=1


def takeFirst(element):
    return(element[0])

array_fv.sort(key=takeFirst)
##print(x)
##print("",end='\n')
##for i in range(0,x):
##    print(array_fv[i])

for i in range(0,x-1):
    shift_vector = []
    j=0
    val=0
    for element in array_fv[i+1][0]:
        shift_vector.append(element-array_fv[i][0][j])
        val = val*10 + shift_vector[j]
        j+=1
    #print(shift_vector)
    if(val > T1):
        img[row[array_fv[i+1][1]]][col[array_fv[i+1][1]]] = 0
        img[row[array_fv[i][1]]][col[array_fv[i][1]]] = 0
    
img = cv2.medianBlur(img, 3)
print(img)

if(res==True):
    print("CMFD Detected.")
else:
    print("CMFD not detected")

plt.subplot(1,2,2)
plt.imshow(modified,cmap='gray')
plt.title(titles[1])
plt.xticks([])
plt.yticks([])
plt.show()
