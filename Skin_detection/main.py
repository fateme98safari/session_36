import cv2
import numpy as np

lower_HSV = np.array([0, 60, 155], dtype = "uint8")
higer_HSV = np.array([30, 255, 255], dtype = "uint8")
image = cv2.imread("Skin_detection\input\IMG_4714.JPG")
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
skin_detect = cv2.inRange(imageHSV, lower_HSV, higer_HSV)

skinHSV = cv2.bitwise_and(image, image, mask = skin_detect)
cv2.imwrite("Skin_detection/output/result.jpg",skinHSV)
cv2.waitKey()