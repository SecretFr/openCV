import numpy as np
import cv2

#이미지의 서로 다른 작은 영역에 적용되는 문턱값을 계산하고 이를 이미지에 적용함으로써 보다 나은
#결과를 도출하는데 사용되는 방법
#cv2.adaptiveThreshold(img, value, adaptiveMethod, thresholdType, blocksize, C)
#value = adaptiveMethod에 의해 계산된 문턱값과 thresholdType에 의해 픽셀에 적용될 최대값
#adaptiveMethod = 사용할 알고리즘
#cv2.ADAPTIVE_THRESH_MEAN_C = 적용할 픽셀 (x,y)를 중심으로 하는 blocksize x blocksize 안에 있는
#픽셀값의 평균에서 C를 뺀 값을 문턱값으로 함
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C = 적용할 픽셀(x,y)를 중심으로 하는 blocksize x blocksize 안에 있는
#Gaussan 윈도우 기반 가중치들의 합에서 C를 뺀 값을 문턱값으로 함
#thresholdType = type
#blocksize = 픽셀에 적용할 문턱값을 계산하기 위한 블럭 크기, 적용될 픽셀이 블럭의 중심이 됨. 따라서 홀수 여야함
#C = 보정 상수, 양수이면 계산된 adaptive 문턱값에서 빼고, 음수면 더해준다. 0이면 그대로

def thresholding():
    img = cv2.imread('openCV/images/sana.jpg', cv2.IMREAD_GRAYSCALE)

    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    thr3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    titles = ['original', 'Global Thresholding(v=127)', 'Adaptive MEAN', 'Adaptive GAUSSIAN']
    images = [img, thr1, thr2, thr3]

    for i in range(4):
        cv2.imshow(titles[i], images[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

thresholding()
