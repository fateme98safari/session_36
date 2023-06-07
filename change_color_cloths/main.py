import cv2
import numpy as np

image=cv2.imread("change_color_cloths/input/9dbd1097-e619-4486-b936-cf9d50c2328d.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)

H,S,V=cv2.split(image)
H_new=H.copy()

for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if  10<H[i,j]<85  and S[i,j]>15 and V[i,j]<=100:        
            H_new[i,j]+=90
      
         
    
         
         
result=cv2.merge((H_new,S,V))
result=cv2.cvtColor(result,cv2.COLOR_HSV2BGR)
# image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

# result=cv2.cvtColor(result,cv2.COLOR_RGB2BGR)
cv2.imwrite("change_color_cloths/output/result.jpg", result)
cv2.waitKey()