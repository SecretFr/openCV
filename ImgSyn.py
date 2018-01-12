import numpy as np
import cv2

def addImage(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    add_img1 = img1 + img2
    add_img2 = cv2.add(img1, img2)

    cv2.imshow('img1+img2', add_img1)
    #동일한 크기의 동일한 데이터 타입으로 되어 있어야 한다. 또는 img2가 하나의 단일한 값을 가져도 된다.
    #각 픽셀들을 더한 값이 255보다 크면 그 값을 256으로 나눈 나머지가 픽셀값이 된다.
    #ex) 257일 경우, 256으로 나눈 나머지가 1이므로, 픽셀값은 1이 된다.
    cv2.imshow('add()', add_img2)
    #Numpy array 연산과 다르게 더한 값이 500 보다 크면 500으로 값이 정해짐
    cv2.waitKey(0)
    cv2.destroyAllWindows()

addImage('images/model_copy.jpg', 'images/sana.jpg')
img = cv2.imread('images/sana.jpg')
img2 = cv2.imread('images/model_copy.jpg')
print(img.dtype)
print(img2.dtype)
print(img.size)
print(img2.size)
print(img.shape)
print(img2.shape)
