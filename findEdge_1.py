import numpy as np
import cv2
import matplotlib.pyplot as plt

#cv2.Sobel(src, ddepth, dx, dy, ksize)
#ddepth : 결과 이미지 데이터 타입
#CV_8U : 이미지 픽셀값을 uint8로 설정
#CV_16U : 이미지 픽셀값을 uint16로 설정
#CV_32F : 이미지 픽셀값을 float32로 설정
#CV_64F : 이미지 픽셀값을 float64로 설정
#dx, dy : 각각 x방향, y방향으로 미분 차수(ex) 1, 0이면, x방향으로 1차 미분 수행, y방향으로 그대로 두라는 의미)
#ksize : 확장 Sobel 커널의 크기. 1, 3, 5, 7 중 하나의 값으로 설정. -1로 설정되면
#3x3 Sobel 필터 대신 3x3 Scharr 필터를 적용하게 됨.

#Sobel, Scharr, Laplacian 이 세가지 타입의 Gradient 필터(High-pass filters;HPF)를 제공

def grad():
    img = cv2.imread('images/keyboard.jpg', cv2.IMREAD_GRAYSCALE)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    #x, y 방향 편미분 결과를 더한 형태가 결과가 되는것
    #원본 이미지의 가로선과 세로선이 모두 나타나는 것을 확인
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    #세로선이 두드러지게 나타남
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    #가로선이 두드러지게 나타남

    plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
    plt.title('original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2,2,2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

    plt.subplot(2,2,3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

    plt.subplot(2,2,4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()

grad()
