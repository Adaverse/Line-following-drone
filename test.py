import cv2
import numpy as np
import matplotlib.pyplot as plt

def slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    return m

img = cv2.imread('sample.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 0)
thresholded = cv2.threshold(gray,
                                100,
                                255,
                                cv2.THRESH_BINARY)[1]
edges = cv2.Canny(thresholded,100,255,apertureSize = 3)
thresholded = 255 - thresholded 

kernel = np.ones((10,10),np.uint8)
erosion = cv2.erode(thresholded,kernel,iterations = 1)
mid_points = []
for i in range(0,erosion.shape[0],100):
    d = np.argwhere(erosion[i] == 255)
    avg = (d[0] + d[-1])/2
    mid_points.append((i, int(avg)))
plt.imshow(erosion)
cv2.line(img,mid_points[-1][::-1],mid_points[0][::-1],(0,255,255),2)
cv2.imwrite('houghlines5.jpg',img)





