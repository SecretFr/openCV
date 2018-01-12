import numpy as np
import cv2

#이미지 블랜딩: 가중치를 두어 합치는 방법
#1번 이미지에서 2번 이미지로 전환될때, 1번에서 2번으로 서서히 변해가도록 하는 기법

#g(x) = (1-a)f0(x) + af1(x)
def onMouse(x):
    pass

def imgBlending(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.namedWindow('ImgPane')
    cv2.createTrackbar('MIXING', 'ImgPane', 0, 100, onMouse)
    #mix = cv2.getTrackbarPos('MIXING', 'ImgPane')
    #TrackBar의 현재 위치값을 mix에 담는다.
    while True:
        mix = cv2.getTrackbarPos('MIXING', 'ImgPane')
        img = cv2.addWeighted(img1, float(100-mix)/100, img2, float(mix)/100, 0)
        #g(x) = (1-a)f0(x) + af1(x)
        cv2.imshow('ImgPane', img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        #mix = cv2.getTrackbarPos('MIXING', 'ImgPane')
    cv2.destroyAllWindows()

imgBlending('images/model_copy.jpg', 'images/sana.jpg')
