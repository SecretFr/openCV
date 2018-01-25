import numpy as np
import cv2

def histogram():
    img = cv2.imread('images/hist.jpg')

    hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    cdf = hist.cumsum()
    #numpy 배열을 1차원 배열로 변경한 후 , 각 멤버값을 누적하여
    #더한 값을 멤버로 하는 numpy 1차원 배열을 생성한다.

    cdf_m = np.ma.masked_equal(cdf, 0)
    #값이 0인 부분을 모두 mask처리하는 함수
    cdf_m = (cdf_m-cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    #이미지 히스토그램 균일화 방적식을 코드로 나타낸 것
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    #mask 처리된 부분을 0으로 채운 후 numpy 1차원 배열로 리턴

    img2 = cdf[img]

    cv2.imshow('Histogram Equalization', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

histogram()
