import cv2

image=cv2.imread("materwelon_HSV/input/4acd2d1b192405fd3d44e64f73cd9f75.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
H,S,V=cv2.split(image)
H_new=H.copy()
for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if 30<H[i,j]<80:   #green
            H_new[i,j]-=30
        if H_new[i,j]<0:
            H_new[i,j]+=180
        if H[i,j]<15 or H[i,j]>165:  #red
            H_new[i,j] +=60

result=cv2.merge((H_new, S, V))
result=cv2.cvtColor(result,cv2.COLOR_HSV2RGB)
result=cv2.cvtColor(result,cv2.COLOR_RGB2BGR)

cv2.imwrite("materwelon_HSV/output/result.jpg",result)
cv2.waitKey()