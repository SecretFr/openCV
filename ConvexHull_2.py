import numpy as np
import cv2

def convex():
    img = cv2.imread('images/lightning.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[4]

    x, y, w, h = cv2.boundingRect(cnt)
    #꼭지점 좌표 (x,y)와 가로 세로 폭을 리턴
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)
    #이렇게 얻은 좌표를 이용해 원본 이미지에 빨간색으로 사각형을 그린다.

    rect = cv2.minAreaRect(cnt)
    #인자인 cnt에 외접하면서 면적이 가장 작은 직사각형을 구하는데 활용
    #리턴값 : 좌상단 꼭지점 좌표(x,y), 가로,세로 폭과 이 사각형이 기울어진 각도
    box = cv2.boxPoints(rect)
    #얻은 직사각형의 꼭지점 4개의 좌표를 얻기 위해 사용
    box = np.int0(box)
    #좌표는 float형으로 리턴되므로 정수형 값으로 전환

    cv2.drawContours(img, [box], 0, (0, 255, 0), 3)

    cv2.imshow('rectangle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

convex()
