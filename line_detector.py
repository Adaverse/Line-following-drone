import cv2
import numpy as np
def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if (x1 - x2) == 0:
        return 0
    else:
        return ((x1 - x2))

cap = cv2.VideoCapture("blackline.mp4")

while(1):
#frame operations to canny edges
    _, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    row, col = frame.shape  
    img1 = cv2.resize(frame, ((int)(col/6),(int)(row/6)), interpolation = cv2.INTER_AREA)
    kernel = 9
    gray1 = cv2.GaussianBlur(img1,(kernel, kernel),0)
    _, gray1 = cv2.threshold(gray1, 110 ,200,cv2.THRESH_BINARY)
    kernel1 = np.ones((5,5),np.uint8)
    img_dilated = cv2.morphologyEx(gray1, cv2.MORPH_OPEN, kernel1)
    img_canny = cv2.Canny(img_dilated, 100, 200)
    ############################################
    row, col = img_canny.shape
    x_center = []
    y_center = []
    for j in range(row):
        for i in range(col):
            if (img_canny[j, i] == 255):
                first = i
                i = i + 10
                for k in range(i, col):
                    if (img_canny[j, k] == 255):
                        center = (first + k) / 2
                        x_center.append(center)
                        y_center.append(j)
                        break
                break

    ########################slices###############
    if (len(x_center)==0):
        continue
    n = 3 #parameter
    s_img_list = []
    row_s = (int)(row / n)
    for i in range(n):
        img_s = img_canny[(i*row_s):((i+1)*row_s), :]
    j = 1
    s_img_list = []
    r_img_list = []
    row, col = img_canny.shape
    row_s = (int)(row / n)
    for i in range(n):
        img_s = img_canny[(i*row_s):((i+1)*row_s), :]
        img_r = gray1[(i*row_s):((i+1)*row_s), :]
        s_img_list.append(img_s)
        r_img_list.append(img_r)
    img_ = s_img_list[j-1]
    img_r = r_img_list[j-1]
    if ((index - 1)>=len(x_center)):
        continue
    index = (int)((row/n)* (j-0.5))i = i + 10
    center = (int)(x_center[index-1])
    p1 = [center, row_s/2]
    p2 = [col/2, row_s/2]
    distance = dist(p1, p2)
    img_t = cv2.line(img_r,(center, int(row_s/2)),((int)(col/2), (int)(row_s/2)), (255,255,0),1 )
    #plt.imshow(img_t)
    #plt.scatter(center, row_s/2)
    #plt.scatter(col/2, row_s/2)
    print (distance)
    cv2.imshow('frame',img_t)
    if cv2.waitKey(1) & 0xFF ==  ord('q'):
        break
    for i in range(8):
        _, frame = cap.read()
cap.release()
cv2.destroyAllWindows()
