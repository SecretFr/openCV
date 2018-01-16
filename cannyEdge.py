import numpy as np
import cv2
import matplotlib.pyplot as plt

#Canny Edge Detection
#1단계 : 5x5 가우시안 필터를 이용해 이미지의 노이즈를 줄여준다.
#2단계 : Sobel kernel을 수평방향, 수직방향으로 적용하여 각 방향의 gradient를 획득
#3단계 : 최대값이 아닌 픽셀의 값을 0으로 만들기
#4단계 : 3단계를 거친 것들이 실제 edge인지 아닌지 판단하는 단계

def canny():
    img = cv2.imread('images/sana.jpg', cv2.IMREAD_GRAYSCALE)

    #cv2.Canny(src, min threshold value, max threshold value)
    edge1 = cv2.Canny(img, 50, 200)
    edge2 = cv2.Canny(img, 100, 200)
    edge3 = cv2.Canny(img, 170, 200)

    cv2.imshow('original', img)
    cv2.imshow('Can Edge1', edge1)
    cv2.imshow('Can Edge2', edge2)
    cv2.imshow('Can Edge3', edge3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()
