import cv2
import numpy as np

image=cv2.imread("Balloons_detection/input/b.jpg")
image_HSV=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_hue = np.array([15,40,50]) 
upper_hue = np.array([24,255,255])
mask = cv2.inRange(image_HSV, lower_hue, upper_hue)
result=cv2.bitwise_and(image,image,mask=mask)

cv2.imwrite("Balloons_detection/output/result2.jpg",result)
cv2.waitKey()