import numpy as np
import cv2

def histogram():
    img = cv2.imread('images/hist.jpg', cv2.IMREAD_GRAYSCALE)

    equ = cv2.equalizeHist(img)
    #cv2.equalizeHist()함수는 grayscale 이미지만 인자로 받고
    #리턴값도 grayscale 이미지 이다.
    res = np.hstack((img, equ))
    #img와 equ를 수평으로 붙이는 함수
    cv2.imshow('equalizer', res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

histogram()
