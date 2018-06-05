from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

example=glob.glob(r"C:\Users\imkiller\Desktop\wint_sky.gif")[0]
im=imread(example,as_gray=True)
plt.imshow(im,cmap=plt.get_cmap('gray'))
plt.title('Close To View Next')
plt.show()


blobs_log = blob_log(im,max_sigma=30,num_sigma=10,threshold=.1)
blobs_log[:,2]=blobs_log[:,2]*sqrt(2)
numrows=len(blobs_log)
print("Number of Start Counted : ",numrows)

fig,ax=plt.subplots(1,1)
plt.imshow(im,cmap=plt.get_cmap('gray'))
for blob in blobs_log:
    y,x,r=blob
    c=plt.Circle((x,y),r+5,color='lime',linewidth=2,fill=True)
    ax.add_patch(c)
plt.title('Check Your Interpreter For get count of STARS')
plt.show()
