#################       For opencv version '3.3.1-dev'       #################
import cv2
import numpy as np
#import matplotlib.pyplot as plt

def show(arr, name):
    cv2.imshow(name,arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('line2.jpg')
# show(img, "Raw Image")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show(gray, "Gray Image")
gray = cv2.GaussianBlur(gray, (9, 9), 0)
# show(gray, "Blurred Image")
#thresholding
ret,thresholded = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
# print(thresholded)
# show(thresholded, "Threshold Image")
#reversing the image
thresholded = 255 - thresholded
# show(thresholded, "Reversed")
#making kernel and applying erosion to avoid noise
kernel = np.ones((10,10),np.uint8)
erosion = cv2.erode(thresholded,kernel,iterations = 1)
show(erosion, "Eroded Image")

####### For checking noises : Dilate the image!  ############
# kernel = np.ones((30,30),np.uint8)
# erosion = cv2.dilate(erosion,kernel,iterations = 1)
# show(erosion, "Dilated Image")

#finding the mid points of the lines
mid_points = []
for i in range(0,erosion.shape[0],50):
    d = np.argwhere(erosion[i] == 255)
    if len(d) >0 :
        avg = (d[0] + d[-1])/2
        mid_points.append((i, int(avg)))

cv2.line(img,mid_points[-1][::-1],mid_points[0][::-1],(0,255,255),2)
#cv2.imwrite('New_code.jpg',img)
show(img, "Final Image")
