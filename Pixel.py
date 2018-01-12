import numpy as np
import cv2

img = cv2.imread('images/model.png')
cv2.imshow('original', img)

subimg = img[200:300, 200:400]
cv2.imshow('cutting', subimg)
#200~300 행과 200~400열을 ROI로 잡는다.
img[100:200, 100:300] = subimg
#잘라낸 subimg를 해당 좌표에 집어 넣는다.
print(img.shape)
print(subimg.shape)

cv2.imshow('modified', img)
#수정된 이미지를 보여준다
cv2.waitKey(0)
cv2.destroyAllWindows()
