import cv2
import numpy as np

cap = cv2.VideoCapture('line_latest.mp4')
while(1):
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9, 9), 0)
    _,thresholded = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    thresholded = 255 - thresholded
    kernel = np.ones((10,10),np.uint8)
    erosion = cv2.erode(thresholded,kernel,iterations = 1)
    mid_points = []
    for i in range(0,erosion.shape[0],100):
        d = np.argwhere(erosion[i] == 255)
        avg = (d[0] + d[-1])/2
        mid_points.append((i, int(avg)))

    cv2.line(img,mid_points[-1][::-1],mid_points[0][::-1],(0,255,255),2)
    cv2.imshow('frame',img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
