#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import cv2
import numpy as np

#################       For opencv version '3.3.1-dev'       #################
kernel = np.ones((10,10),np.uint8)
cap = cv2.VideoCapture("line_latest.mp4")

def line_publisher():
    pub = rospy.Publisher('Line_value',Int32 , queue_size=10)
    rospy.init_node('Line_pub', anonymous=True)
    rate = rospy.Rate(50)
    print("working")
    while(cap.isOpened() and (not rospy.is_shutdown())):
        _, img = cap.read()
        avg = 0
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (9, 9), 0)
        _,thresholded = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
        thresholded = 255 - thresholded
        erosion = cv2.erode(thresholded,kernel,iterations = 1)
        row, column = erosion.shape
        d = np.argwhere(erosion[int(row/2)] == 255)
        if len(d) >0 :
            avg = int((d[0] + d[-1])/2)
            avg = avg - int(column/2)
            #if line is on right : positive avg
        pub.publish(avg)
        # rate.sleep()
        # cv2.imshow('frame',erosion)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
            # break
    cap.release()
    # cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        line_publisher()
    except rospy.ROSInterruptException:
        pass
