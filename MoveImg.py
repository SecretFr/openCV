import numpy as np
import cv2

#cv2.warpAffine()

def transform():
    img = cv2.imread('openCV/images/model_copy.jpg')
    h, w = img.shape[:2]

    M = np.float32([[1, 0, 100], [0, 1, 50]])
    #x 방향으로 100, y 방향으로 50 픽셀만큼 이동 변환은 나타내는 2x3 매크릭스를 생성

    img2 = cv2.warpAffine(img, M, (w, h))
    #(이미지, 2x3 변환 매트릭스, 출력될 이미지 사이즈)
    
    cv2.imshow('Shift image', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

transform()
