import numpy as np
import cv2
#low-pass filter(LPF)를 이용한 이미지 블러(blur)
def bluring():
    img = cv2.imread('openCV/images/model_copy.jpg')

    kernel = np.ones((5,5), np.float32)/25
    blur = cv2.filter2D(img, -1, kernel)
    #픽셀을 중심으로 5x5 영역을 만듬
    #이 영역의 모든 픽셀 값을 더함
    #더한 값을 25로 나누고 이 값을 중심 픽셀 값으로 취함

    cv2.imshow('original', img)
    cv2.imshow('blur', blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

bluring()
