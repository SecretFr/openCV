import numpy as np
import cv2

def transform():
    img = cv2.imread('openCV/images/model.png')
    h, w = img.shape[:2]

    img2 = cv2.resize(img, None, fx=0.5, fy=1, interpolation=cv2.INTER_AREA)
    img3 = cv2.resize(img, None, fx=1, fy=0.5, interpolation=cv2.INTER_AREA)
    img4 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #cv2.resize(이미지원본, dsize를 나타내는 튜플 값으로(가로,세로방향 픽셀 수) 나타냄,
    #fx,fy=각각 가로, 세로 방향 배율 인자 크기 조절, 리사이징을 할때 interpolation방법)
    #_LINEAR : bilinear interpolation(default)
    #_NEAREST : nearest-neighbor interpolation
    #_AREA : 픽셀 영역 관계를 이용한 resampling 방법으로 이미지 축소에 있어 선호되는방법
    #이미지를 확대하는 경우에는 _NEAREST와 비슷한 효과를 보임
    #_CUBIC : 4x4픽셀에 적용되는 bicubic interpolation
    #_LANCZOS4 : 8x8 픽셀에 적용되는 Lanczos interpolation
    cv2.imshow('original', img)
    cv2.imshow('fx=0.5', img2)
    cv2.imshow('fx=1', img3)
    cv2.imshow('fx=0.5, fy=0.5', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

transform()
