import numpy as np
import cv2
import matplotlib.pyplot as plt

#Thresholding 기법과 blur 필터를 활용하여 이미지 노이즈 제거에 효율적으로 적용하기!
def thresholding():
    img = cv2.imread('openCV/images/sana.jpg', cv2.IMREAD_GRAYSCALE)

    #전역 thresholding 적용
    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    #Otsu 바이너리제이션
    ret, thr2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #Otsu 플래그 값을 thresholding 플래그에 더하고 문턱값으로 0을 전달해주면 된다.
    #리턴한 ret, thr2는 각각 알고리즘으로 계산된 문턱값과 이 문턱값을 적용한 결과 이미지

    #가우시안 블록 적용 후 Otsu 바이너리제이션
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret, thr3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    titles = ['original noisy', 'Histogram', 'G-Thresholding',
              'original noisy', 'Histogram', 'Otsu Thresholding',
              'Gaussian-filtered', 'Histogram', 'Otsu Thresholding']

    images = [img, 0, thr1, img, 0, thr2, blur, 0, thr3]

    for i in range(3):
        plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])

        plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])

        plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

    plt.show()

thresholding()
