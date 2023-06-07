import cv2
import numpy as np

image=cv2.imread("Spiderman\input\spiderman.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# result=cv2.cvtColor(result,cv2.COLOR_RGB2HSV)
H,S,V=cv2.split(image)
H_new=H.copy()

for i in range(H.shape[0]):
    for j in range(H.shape[1]):
      if  90<H[i,j]<135 and S[i,j]>96 :         #blue
         H_new[i,j]-=40
      if  H[i,j]<15  and S[i,j]>90  or H[i,j]>165 and S[i,j]>90 :        #red
          H_new[i,j]+=30
         
         
result=cv2.merge((H_new,S,V))
result=cv2.cvtColor(result,cv2.COLOR_HSV2BGR)
# result=cv2.cvtColor(result,cv2.COLOR_RGB2BGR)
cv2.imwrite("Spiderman/output/result.jpg", result)
cv2.waitKey()