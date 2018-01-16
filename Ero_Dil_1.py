import numpy as np
import cv2

def morph():
    img = cv2.imread('images/alp.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3,3), np.uint8)
    #이미지에 가해지는 변형을 결정하는 구조화된 요소로 불리는 커널
    #3x3 크기의 1로 채워진 매트릭스를 생성
    erosion = cv2.erode(img, kernel, iterations=1)
    #전경이 되는 이미지의 경계부분을 침식시켜 배경 이미지로 전환
    #iterations : Erosion 반복 횟수
    dilation = cv2.dilate(img, kernel, iterations=1)
    #erosin의 반대 이미지의 경계부분을 팽창시켜 전경 이미지로 전환

    cv2.imshow('original', img)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

morph()
