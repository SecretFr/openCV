import numpy as np
import cv2

def transform():
    img = cv2.imread('openCV/images/model_copy.jpg')
    h, w = img.shape[:2]

    pts1 = np.float32([[0,0], [300, 0], [0, 300], [300, 300]])
    pts2 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    #변환되기전 4개의 좌표, 변환된 후 4개의 좌표

    M = cv2.getPerspectiveTransform(pts1, pts2)
    #변환 시키기 위한 매트릭스

    img2 = cv2.warpPerspective(img, M, (w, h))
    #cv2.warpAffine 함수와 인자는 같지만, M은 3x3 매트릭스여야 한다.

    cv2.imshow('original', img)
    cv2.imshow('Perspective-Transform', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

transform()
