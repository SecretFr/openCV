import numpy as np
import cv2
from random import shuffle
#무작위 색상값
import math

mode, drawing = True, False
ix, iy = -1, -1
B = [i for i in range(256)]
G = [i for i in range(256)]
R = [i for i in range(256)]

def onMouse(event, x, y, flags, param):#setMouseCallback 함수의 인자로 전달
    global ix, iy, drawing, mode, B, G, R
    if event == cv2.EVENT_LBUTTONDOWN:#마우스 왼쪽 더블클릭시 작동
        drawing = True
        ix, iy = x, y
        shuffle(B), shuffle(G), shuffle(R)
        print('excute')

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(param, (ix, iy), (x,y), (B[0], G[0], R[0]), -1)
            else:
                r = (ix-x)**2 + (iy-y)**2
                r1 = int(math.sqrt(r))
                print(r1)
                cv2.circle(param, (ix, iy), r1, (B[0], G[0], R[0]), -1)
                #param에 img가 전달된다
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(param, (ix, iy), (x,y), (B[0], G[0], R[0]), -1)
            print('excute3')
        else:
            r = (ix-x)**2 + (iy-y)**2
            r1 = int(math.sqrt(r))
            print(r1)
            cv2.circle(param, (ix,iy), r1, (B[0], G[0], R[0]), -1)

def mouseBrush():
    global mode
    img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param=img)
    #콜백함수 onMouse(), 전달할 사용자 데이터 = img

    while True:
        cv2.imshow('paint', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break
        elif k == ord('m'):
            print('excute2')
            mode = not mode
    cv2.destroyAllWindows()

mouseBrush()
