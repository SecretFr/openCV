import numpy as np
import cv2

#Contour Area(둘러싸인 부분의 면적)와 Contour Perimeter(호의 길이)를 구하는 방법
#키값이 m00인 값이 contourArea의 값이다.
#arcLength()는 2개의 인자를 가짐, 두 번째 인자에서 True이면 폐곡선, False이면 열려있는 호를 나타냄

def contour():
    img = cv2.imread('images/sana.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[164]
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)

    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)

    print('contour 면적:', area)
    print('contour 길이:', perimeter)

    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()
