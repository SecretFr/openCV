import numpy as np
import cv2

#경우에 따라서 원, 타원 모양의 커널을 만들어 적용해야할 필요가 있다.

def makeKernel():
    M1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    M2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    M3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

    print(M1)
    print(M2)
    print(M3)

makeKernel()
