import numpy as np
import cv2
from random import shuffle
#무작위 색상값 추출

r = [i for i in range(256)]
g = [i for i in range(256)]
b = [i for i in range(256)]

def onMouse(event, x, y, flags, param):#setMouseCallback 함수의 인자로 전달
    if event == cv2.EVENT_LBUTTONDBLCLK:#마우스 왼쪽 더블클릭시 작동
        shuffle(b), shuffle(r), shuffle(g)
        cv2.circle(param, (x,y), 50, (b[0], g[0], r[0]), -1)
        #param에 img가 전달된다

def mouseBrush():
    img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param=img)
    #콜백함수 onMouse(), 전달할 사용자 데이터 = img

    while True:
        cv2.imshow('paint', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break
        elif k == ord('c'):
            cv2.imwrite('images/mouse.jpg', img)
            cv2.destroyAllWindows()
    cv2.destroyAllWindows()

mouseBrush()
