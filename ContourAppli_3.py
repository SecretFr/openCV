import numpy as np
import cv2

#Contour Approxmation

def contour():
    img = cv2.imread('images/bbox.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)

    epsilon1 = 0.01*cv2.arcLength(cnt, True)
    #둘레 길이의 1%를 할당
    epsilon2 = 0.1*cv2.arcLength(cnt, True)
    #둘레 길이의 10%를 할당
    #epsilon값이 작으면 오리지널 contour와 비슷한 결과가 도출
    #값이 크면 오리지널 contour와 차이가 있는 결과가 나오게 된다.

    approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
    approx2 = cv2.approxPolyDP(cnt, epsilon2, True)
    #cnt : Numpy Array 형식의 곡선 또는 다각형
    #epsilon : 근사 정확도를 위한 값, 이 값은 오리지널 커브와 근사 커브간 거리의 최대값으로 사용
    #True : 세 번째 인자가 True이면 폐곡선, False이면 양끝이 열려있는 곡선임을 의미

    img1 = cv2.drawContours(img, [approx1], 0, (0, 255, 0), 3)
    img2 = cv2.drawContours(img, [approx2], 0, (0, 255, 0), 3)

    cv2.imshow('contour', img)
    cv2.imshow('Approx1', img1)
    cv2.imshow('Approx2', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()
