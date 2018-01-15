import numpy as np
import cv2

#문턱값(Thresholding Value) = 이 값을 기준으로 상황이 급격하게 변한다는 것을 의미

img = cv2.imread('openCV/images/sana.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.threshold(Grayscale 이미지, threshold_value 픽셀 문턱값,
#value 픽셀 문턱값보다 클때 적용되는 최대값 또는 적용되는 플래그에 따라 픽셀 문턱값보다 작을 때 사용되는 최대값)
#,flag 문턱값 적용 방법 또는 스타일)
ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#픽셀값이 threshold_value보다 크면 value, 작으면 0
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#픽셀값이 threshold_value보다 크면 0, 작으면 value
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
#픽셀값이 threshold_value보다 크면 threshold_value, 작으면 픽셀값 그대로
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
#픽셀값이 threshold_value보다 크면 픽셀값 그대로, 작으면 0
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
#픽셀값이 threshold_value보다 크면 0, 작으면 픽셀값 그대로

cv2.imshow('original', img)
cv2.imshow('Binary', thr1)
cv2.imshow('Binary_INV', thr2)
cv2.imshow('Trunc', thr3)
cv2.imshow('TOZERO', thr4)
cv2.imshow('TOZERO_INV', thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()
