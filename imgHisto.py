import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram():
    img1 = cv2.imread('images/landscape.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/landscape.jpg')

    #OpenCV 함수를 이용해 히스토그램 구하기
    hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    #calcHist(img, channel, mask, histSize, range), 이미지 히스토그램을 찾아서 numpy 배열로 리턴
    #img : 히스토그램을 찾을 이미지, 인자는 []로 둘러싸야 함
    #channel : grayscale 이미지 [0], B,G,R 각각 [0],[1],[2]
    #mask : 이미지 전체에 대한 히스토그램을 구할 경우 None, 이미지의 특정 영역에 대한 히스토그램을 구할 경우 이 영역에 해당하는 mask값을 입력
    #histSize : BIN개수, 인자는 []
    #range : 픽셀값의 범위. 보통 [0, 256]


    #numpy를 이용해 히스토그램 구하기
    hist2, bins = np.histogram(img1.ravel(), 256, [0, 256])

    #1-D 히스토그램의 경우, numpy가 빠름
    hist3 = np.bincount(img1.ravel(), minlength=256)
    #grayscale 이미지의 경우 numpy.bincount()함수를 이용하여 히스토그램을 구하면 numpy.histogram() 함수에 비해 10배정도 빠른 속도로 결과를 내준다.
    #numpy.ravel()함수는 numpy 배열을 1차원으로 바꿔주는 함수

    #matplotlib로 히스토그램 그리기
    plt.hist(img1.ravel(), 256, [0, 256])

    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        #plt.plot은 화면에 그려주는 함수
        plt.xlim([0, 256])
        #x축을 0~256까지로 제한

    plt.show()

histogram()
