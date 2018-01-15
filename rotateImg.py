import numpy as np
import cv2

def transform():
    img = cv2.imread('openCV/images/model_copy.jpg')
    h, w = img.shape[:2]

    M1 = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)
    M2 = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)
    M3 = cv2.getRotationMatrix2D((w/2, h/2), 135, 1)
    #원본 이미지 무게중심을 회전 중심으로 하고 45, 90, 135도, scale=1인 회전 변환 매트릭스

    img2 = cv2.warpAffine(img, M1, (w, h))
    img3 = cv2.warpAffine(img, M2, (w, h))
    img4 = cv2.warpAffine(img, M3, (w, h))
    #구한 매트릭스를 통해서 변환된 이미지를 출력

    cv2.imshow('45-Rotated', img2)
    cv2.imshow('90-Rotated', img3)
    cv2.imshow('135-Rotated', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

transform()
