import numpy as np
import cv2

#Opening : erosion 수행을 한 후 바로 dialation 수행을 하여 본래 이미지 크기로 돌려 놓는 것
#Closing : dilation 수행을 한 후 바로 erosion 수행을 하여 본래 이미지 크기로 돌려 놓는 것

def morph():
    img1 = cv2.imread('images/opening.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/closing.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5,5), np.uint8)

    opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
    #cv2.morphologyEx(src, operation, kernel)
    #_GRADIENT : dilation 이미지와 erosion 이미지의 차이를 나타냄
    #_TOPHAT : 원본 이미지와 opening한 이미지의 차이를 나타냄
    #_BLACKHAT : closing한 이미지와 원본 이미지의 차이를 나타냄

    #cv2.imshow('original', img1)
    #cv2.imshow('original2', img2)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

morph()
