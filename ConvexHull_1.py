import numpy as np
import cv2

def convex():
    img = cv2.imread('images/convexhull.png')
    img1 = img.copy()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[1]
    #1인 이유는 도형바깥쪽을 감싸는 cnt이기 때문이다.
    cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

    check = cv2.isContourConvex(cnt)
    #cnt가 ConvexHull 인지 체크, 맞으면 True, 틀리면 False 리턴
    #convexhull.png는 Convex Hull이 아니므로 False를 리턴한다

    if not check:#cnt가 ConvexHull이 아니라면
        hull = cv2.convexHull(cnt)
        #원본 이미지 contours[1]에 대한 Convex Hull을 구한다.
        cv2.drawContours(img1, [hull], 0, (0, 255, 0), 3)
        cv2.imshow('convexhull', img1)

    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

convex()
